# In-memory file analysis

<note>Experimental API. Subject to changes.</note>

Parsing a Kotlin file does not require any knowledge about the project it belongs to. On the other hand, for *semantic
code analysis*, understanding dependencies and compilation options of a file is crucial.

In most cases, source files — whether written by a user or auto-generated — are stored on disk and belong to a specific module.
The build system understands the project layout and instructs the compiler or the IDE to use appropriate dependencies for
all files in that module. For script files, such as `build.gradle.kts`, the situation is more complex since
scripts technically do not belong to any module. However, in such cases, the build system also provides the necessary
context. For example, Gradle build scripts include the Gradle API and all libraries Gradle depends on in their classpath.

In certain cases, it might be useful to analyze a file without storing it in the file system. For example, an IDE
inspection may use in-memory files to verify whether code will remain valid after applying a proposed change.
Specifically, the inspection might create a copy of the `KtFile`, apply the change to the copy, and check for new
compilation errors. In such scenarios, the inspection needs to supply the correct analysis context for the in-memory
`KtFile`.

The Analysis API provides multiple approaches for analyzing in-memory files and attaching context to them.
Below, we explore these options and their differences.

## Stand-alone file analysis

Let's begin with the most generic case: creating an in-memory file with arbitrary content and analyzing it.

To create a file, we use the `KtPsiFactory` class:

```kotlin
val text = 
    """
    package test
    
    fun foo() {
        println("Hello, world!")
    }
    """.trimIndent()

val factory = KtPsiFactory(project)
val file = factory.createFile(text)
```

`KtPsiFactory` offers many utilities for creating chunks of Kotlin code. In our case, we are primarily interested in
creating entire Kotlin files.

If we analyze the file we created using `analyze {}`, we notice that the `println` reference is reported as unresolved:

```kotlin
analyze(file) {
    val diagnostics = file.collectDiagnostics(KaDiagnosticCheckerFilter.ONLY_COMMON_CHECKERS)
    // ["Unresolved reference 'println'."]
    val messages = diagnostics.map { it.defaultMessage }
}
```

This happens because the `KtFile` we created lacks any attached context, making the Kotlin Standard Library unavailable.
However, code in the file still *can* access a few basic Kotlin types, such as `Int` or `String`, and can resolve
references to declarations from the same file.

Now, let's assume we have a `contextFile` that belongs to a module and want to analyze our in-memory file as it was
in that module. First, we retrieve the containing module of the `contextFile`.

```kotlin
val contextModule = KaModuleProvider.getModule(project, contextFile, useSiteModule = null)
```

Now that we have the module, we attach it to our file:

```kotlin
@OptIn(KaExperimentalApi::class)
file.contextModule = contextModule
```

If the context module includes a dependency to the Kotlin Standard library, the analysis will no longer produce errors.

The created file can reference declarations from the context module, including `internal` ones.
However, no matter the content of our newly created file, it will not affect resolution of our context file.
Such as, if we declare a function in the `file`, it will not be visible from the `contextFile`.

Here is the complete code of our example:

```kotlin
val text = 
    """
    package test
    
    fun foo() {
        println("Hello, world!")
    }
    """.trimIndent()

val factory = KtPsiFactory(project)
val file = factory.createFile(text)

val contextModule = KaModuleProvider.getModule(project, contextFile, useSiteModule = null)

@OptIn(KaExperimentalApi::class)
file.contextModule = contextModule

analyze(file) {
    val diagnostics = file.collectDiagnostics(KaDiagnosticCheckerFilter.ONLY_COMMON_CHECKERS)
    // An empty list
    val messages = diagnostics.map { it.defaultMessage }
}
```


## Context modules

In the previous example, we used the `KaModuleProvider.getModule()` function to retrieve the module containing the
`contextFile`. The returned value is of type `KaModule` which is an Analysis API abstraction over `Module`, `Library`,
and `Sdk` concepts from IntelliJ IDEA. Specifically, a `KaSourceModule` represents a source module, and libraries and
SDKs are represented by `KaLibraryModule`s. Every `KaSymbol` in the Analysis API is associated with some `KaModule`.

If you already have a reference to a `Module`, you can convert it to a `KaModule` using one of the Kotlin plugin helper
functions:

```kotlin
fun Module.toKaSourceModule(kind: KaSourceModuleKind): KaSourceModule?
fun Module.toKaSourceModuleForProduction(): KaSourceModule?
fun Module.toKaSourceModuleForTest(): KaSourceModule?
```

For more related APIs, refer to the Kotlin plugin's
[source code](https://github.com/JetBrains/intellij-community/blob/master/plugins/kotlin/base/project-structure/src/org/jetbrains/kotlin/idea/base/projectStructure/api.kt).
There are also overloads that accept `ModuleId` and `ModuleEntity` from the newer project model API.

In the `KaModuleProvider.getModule` function call, we passed `useSiteModule = null`. For advanced scenarios,
you might want to analyze files from other modules in the context of a synthetic module. In such cases, that synthetic
module can be passed as a `useSiteModule`. For typical use cases, it is safe to pass `null`.


## Physical and non-physical files

In the previous example, we used the `KtPsiFactory` to create a non-physical file. From IntelliJ IDEA's perspective,
"non-physical" differs from whether the file is stored on disk. We can create both physical and non-physical `KtFile`s
that are not written to the disk.

So what is the difference? Non-physical files are typically created for one-shot analysis. Creating them has a lower
cost, but IntelliJ IDEA does not track changes in them. A physical file, on the other hand, is handled by the PSI
modification machinery, allowing the Analysis API to track changes and update analysis results accordingly.

If you need a long-lived file that will be modified and analyzed multiple times, you should create a physical file by
using a `KtPsiFactory` with `eventSystemEnabled = true`:

```kotlin
val factory = KtPsiFactory(project, eventSystemEnabled = true)
val file = factory.createFile(text)
```


## File copies

In some cases, you might want to create a complete copy of an existing file, modify it in some way, and analyze
the result.

To create a copy of a file, you can use the `copy` function:

```kotlin
val fileCopy = file.copy() as KtFile
```

The `copy()` function sets a reference to the original file in the produced copy. As a result, the `getOriginalFile()`
of the newly created file points back to the original file. This allows the Analysis API to automatically use the
context of the original file. In other words, there is no need to manually set the `contextModule` for a copied file.

The `copy()` function creates non-physical files. For this setup (a non-physical file with a `getOriginalFile()` set),
the Analysis API uses a different analysis strategy by default.

This behavior is optimized for efficiency. Since the original file might be large, analyzing it from scratch could be
unnecessarily resource-intensive. In most cases, file copies primarily differ in declaration bodies, so the Analysis API
leverages existing analysis results from the original file.

If you make changes to the declaration signatures in the copied file, you should analyze it independently of the
original file. To do so, use the `PREFER_SELF` resolution mode with the `analyzeCopy()` function:

```kotlin
analyzeCopy(fileCopy, KaDanglingFileResolutionMode.PREFER_SELF) {
    // Analysis code, just as in `analyze()`
}
```

On the other side, if you manually create a physical file copy, you can still request more efficient analysis by passing
the `KaDanglingFileResolutionMode.IGNORE_SELF` option:

```kotlin
val factory = KtPsiFactory(file.project, eventSystemEnabled = true)
val fileCopy = factory.createFile("text.kt", originalFile.text)
fileCopy.originalFile = file

analyzeCopy(fileCopy, KaDanglingFileResolutionMode.IGNORE_SELF) {
    // Analysis code, just as in `analyze()`
}
```

The `analyzeCopy()` function works exclusively for file copies. Unless you need to configure the resolution mode
explicitly, use the usual `analyze()` instead.

<note>In the future, the Analysis API may be able to track changes in file copies and decide on an appropriate
resolution mode automatically.</note>


## Code fragments

If you only need to analyze a single expression or reference within the context of surrounding code, creating a full
file copy is often unnecessary. For these use cases, the Analysis API provides the concept of *code fragments*.

A code fragment is a small piece of code that can be analyzed within the context of some other code.
There are three types of code fragments:

- `KtExpressionCodeFragment` for analyzing a single expression;
- `KtBlockCodeFragment` for analyzing a block of statements;
- `KtTypeCodeFragment` for analyzing a single type reference.

All three types of code fragments extend the `KtCodeFragment` class, which itself extends `KtFile`.

Code fragments differ from typical `KtFile`s in several important ways:

- **No package directive**: A code fragment cannot have a `package` directive; its package is inherently the same as
  the package of the context file.
- **Import handling**: Imports are submitted externally, and no import aliases are permitted.
- **Local-only content**: All content within a code fragment is considered local.

To create a code fragment, you need two inputs: the source text of the fragment and a context element from the
surrounding code. For example, consider the following code snippet where `print(name)` is a context element:

```kotlin
fun test() {
    val name = "poem.txt"
    print(name)
}
```

Now, let's create a code fragment that references `name` to read from a file:

```kotlin
val fragment = KtExpressionCodeFragment(
    project,
    name = "fragment.kt",
    text = "File(name).readText()",
    context = contextElement,
    imports = listOf("java.io.File")
)
```

A code fragment can reference any declaration visible from its context element, including local declarations.
For the above example, the code fragment accesses the local variable `name`.

If we pass the `val name = "poem.txt"` declaration as a context element, the code fragment analysis will result in an
error, as variables are not yet available on the line of their declaration.

Since code fragments extend `KtFile`, you can analyze them in the same way as you analyze files:

```kotlin
analyze(fragment) {
    // Analysis code
}
```

Code fragments can have a context element from another code fragment, or from an in-memory file.