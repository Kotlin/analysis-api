# Using in IntelliJ Plugins

The Kotlin plugin for IntelliJ IDEA is built on top of the Analysis API: code completion, navigation, inspections,
refactorings, and the debugger all use it. A third-party plugin that works with Kotlin code gets exactly the same API.

The Analysis API ships inside the Kotlin plugin, so there is nothing to download or bundle. Your plugin only needs to
declare a dependency on the Kotlin plugin.

## Adding the dependency

The Kotlin plugin is bundled with IntelliJ IDEA and Android Studio. Its plugin ID is `org.jetbrains.kotlin`.

If you use the [IntelliJ Platform Gradle Plugin](https://plugins.jetbrains.com/docs/intellij/tools-intellij-platform-gradle-plugin.html),
add the Kotlin plugin as a
[bundled plugin dependency](https://plugins.jetbrains.com/docs/intellij/tools-intellij-platform-gradle-plugin-dependencies-extension.html#plugins)
in `build.gradle.kts`:

```kotlin
dependencies {
    intellijPlatform {
        bundledPlugin("org.jetbrains.kotlin")
    }
}
```

Then declare the dependency in `plugin.xml`, so the IDE loads the Kotlin plugin classes for your plugin:

```xml
<depends>org.jetbrains.kotlin</depends>
```

See [Plugin Dependencies](https://plugins.jetbrains.com/docs/intellij/plugin-dependencies.html) in the IntelliJ
Platform SDK documentation for details, including how to make the dependency optional.

!!! warning
    Do not add the `org.jetbrains.kotlin:kotlin-analysis-api` Maven artifact to an IDE plugin. That artifact is intended
    for [Standalone](Standalone.md) tools. In the IDE, the Analysis API classes come from the Kotlin plugin, and a second
    copy on the classpath leads to class loading conflicts.

## K2 mode

The Analysis API is powered by the K2 Kotlin compiler. In the IDE, it is available when the Kotlin plugin runs in the
*K2 mode*:

| IntelliJ IDEA version | K2 mode                                                     |
|-----------------------|-------------------------------------------------------------|
| 2024.2                | Available as an option. The Analysis API becomes usable.    |
| 2025.1                | Enabled by default.                                         |
| 2026.2 and later      | The only mode. All plugins are considered compatible.       |

You can read more about the K2 mode in
[The Story Behind K2 Mode and How It Works](https://blog.jetbrains.com/idea/2025/04/the-story-behind-k2-mode-and-how-it-works/).

## Calling the Analysis API

The entry point is the `analyze {}` function. It accepts a `KtElement` (or a `KaModule`) and provides
a [`KaSession`](Fundamentals.md#kasession) inside the block:

```kotlin
@RequiresReadLock
fun KtExpression.hasStringType(): Boolean {
    analyze(this) {
        return expressionType == builtinTypes.string
    }
}
```

There are a few rules specific to the IDE.

### Read actions

In the IDE, the user can change the code at any moment. To get consistent results, all code that reads PSI or uses the
Analysis API must run inside a
[read action](https://plugins.jetbrains.com/docs/intellij/general-threading-rules.html#read-access), which is a lock
that holds off code modifications.

Many IDE extension points, such as inspections and annotators, already call your code in a read action. In other
places, for example, in background tasks, you need to start one yourself:

```kotlin
val isString = readAction {
    expression.hasStringType()
}
```

Note that outside a read action, code may be changed arbitrary, and the results you got inside one may become invalid.

### No analysis on the UI thread

Analysis may take a noticeable amount of time. By default, calling `analyze {}` from the UI thread (the event dispatch
thread, or EDT) or from a write action throws an exception. Run the analysis in a background thread, and pass the
results to the UI.

For rare cases when this is not possible, the Analysis API provides the
[`allowAnalysisOnEdt`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.permissions/allow-analysis-on-edt.md) and
[`allowAnalysisFromWriteAction`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.permissions/allow-analysis-from-write-action.md)
functions. Both may freeze the UI, so treat them as a last resort.

### Lifetime of analysis results

Symbols, types, and other [`KaLifetimeOwner`](Fundamentals.md#kalifetimeowner)s are valid only inside the `analyze {}`
block and the read action in which they were created. After the code changes, they become invalid.

Do not store them in fields, caches, or UI models. To pass a symbol or a type to another analysis session, create a
pointer with `createPointer()` and restore it later.

## Project structure

Each `analyze {}` call resolves code from the point of view of one module. The Analysis API represents modules as
[`KaModule`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md)s:
a `KaSourceModule` for a set of sources, and a `KaLibraryModule` for a library or an SDK.

In the IDE, you do not create modules yourself. The Kotlin plugin derives them from the project model, which is
imported from the build system. In most cases, you only pass a PSI element to `analyze {}`, and the correct module is
found automatically.

If you need a module explicitly, use one of the following:

`fun PsiElement.kaModule(useSiteModule: KaModule?): KaModule`
: Returns the module that contains the element. Part of the Analysis API, available since IntelliJ IDEA 2026.2.
Pass `null` as the `useSiteModule` unless you already analyze the code from the point of view of a specific module.

`fun Module.toKaSourceModuleForProduction(): KaSourceModule?`<br>`fun Module.toKaSourceModuleForTest(): KaSourceModule?`
: Convert an IntelliJ `Module` to a `KaSourceModule`. Production and test sources of the same IntelliJ module are
separate `KaSourceModule`s. Part of the Kotlin plugin.

`fun Library.toKaLibraryModules(project: Project): List<KaLibraryModule>`<br>`fun Sdk.toKaLibraryModule(project: Project): KaLibraryModule`
: Convert an IntelliJ library or an SDK to a `KaLibraryModule`. Part of the Kotlin plugin.

For more helpers of this kind, refer to the Kotlin plugin's
[source code](https://github.com/JetBrains/intellij-community/blob/master/plugins/kotlin/base/project-structure/src/org/jetbrains/kotlin/idea/base/projectStructure/api.kt).

To analyze a file that is not a part of the project, such as a file you have just created in memory, see
[In-memory file analysis](In-memory-file-analysis.md).

## What to read next

- [Fundamentals](Fundamentals.md) describes the core rules of the Analysis API.
- [Symbols](Symbols.md), [Types](Types.md), and [References and Calls](References-And-Calls.md) cover the main parts of
  the API.
- The [Kotlin Plugin](https://plugins.jetbrains.com/docs/intellij/idea.html#kotlin-plugin) section of the IntelliJ
  Platform SDK documentation lists other resources for plugins that work with Kotlin code.
