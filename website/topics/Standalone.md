# Standalone Mode

!!! note
    The API for setting up a Standalone session is currently experimental and will change in future releases.  
    See [Stability](#stability) for details.

The Analysis API was designed for the IDE, but it does not require one. The *Standalone mode* lets you use the same
API in an ordinary JVM application: a command-line tool, a build step, a test, or a server-side service.

Typical use cases are:

- Linters and static analyzers
- Documentation generators
- Code generators that need to understand existing code
- API dump and API compatibility tools
- Tools that export Kotlin declarations to other languages

Several well-known projects are built on the Standalone mode, including [Dokka](https://github.com/Kotlin/dokka),
[KSP](https://github.com/google/ksp), [Android Lint](https://developer.android.com/studio/write/lint), and
[Metalava](https://android.googlesource.com/platform/tools/metalava/).

## Quickstart project

The fastest way to start is the [Analysis API Quickstart](https://github.com/Kotlin/analysis-api-quickstart)
project. It is a small Gradle project you can copy and adapt. The project contains:

- A command-line tool that creates a Standalone session and analyzes a module.
- A Gradle plugin that collects source roots, the classpath, and compiler settings of a module, and runs the tool with
  them.
- A sandbox module to try the tool on.

The rest of this page explains what happens inside that project.

## How Standalone differs from the IDE

The `analyze {}` function, symbols, types, and all other parts of the Analysis API work in the same way in both
environments. The difference is in what surrounds them.

|                        | **IDE**                                          | **Standalone**                                          |
|------------------------|--------------------------------------------------|---------------------------------------------------------|
| **Project structure**  | Imported from the build system by the IDE        | Described by your tool                                  |
| **Code changes**       | Tracked. Analysis results are updated            | Not expected. The session is a snapshot of the project  |
| **Threading**          | `analyze {}` requires a read action              | `analyze {}` can be called from any thread              |

!!! tip
    Even though the Standalone mode does not enforce read actions, keep following the
    [lifetime rules](Fundamentals.md#kalifetimeowner): do not store symbols and types outside the `analyze {}` block.
    They hold the whole resolution session in memory.

## Why you need to describe the project

To parse a Kotlin file, the text of the file is enough. To *understand* it, much more is needed. Consider this code:

```kotlin
fun greet(user: User) = println(user.name.uppercase())
```

To resolve it, the Analysis API has to know:

- Where the `User` class is declared. It can be in another file of the same module, in another module, or in a library.
- Which libraries are available, and in which versions. `println` and `uppercase` come from the Kotlin standard
  library, which is an ordinary library from the Analysis API's point of view.
- Which JDK is used, since Kotlin types such as `String` map to Java classes on the JVM.
- For which platform the code is compiled. The same call may resolve to different declarations on JVM, JS, and Native.
- Which Kotlin language version and which language features are enabled.

Together, this information is called the *project structure*. A project consists of *modules*: sets of source files
compiled together, and libraries they depend on.

The Kotlin compiler receives the project structure from the build system as command-line arguments. The IDE imports it
from the build system when you open a project. A Standalone tool is launched outside of both, so nobody provides the
project structure for it. Your tool has to describe it explicitly when it creates a session.

If the description is incomplete, analysis does not fail. Instead, the missing parts are reported as unresolved,
similarly to what the compiler does when a library is missing in the classpath. For example, if you forget to add the
Kotlin standard library, the code above produces the `Unresolved reference 'println'` error, and only a few built-in
types such as `Int` and `String` are available.

## Getting started

### Add the dependency

The Analysis API is published to Maven Central as `org.jetbrains.kotlin:kotlin-analysis-api`.

```kotlin
repositories {
    mavenCentral()
}

dependencies {
    implementation("org.jetbrains.kotlin:kotlin-analysis-api:<version>")
}
```

The Analysis API is released together with the Kotlin compiler and has the same version. Each version of the Analysis
API can analyze code written for that Kotlin version and for the older language versions the compiler still supports.

The artifact includes the Analysis API, the Standalone session API, and their implementation. You do not need
to add the Kotlin compiler as a separate dependency.

### Create a session

A [`StandaloneAnalysisAPISession`](../api/analysis-api-standalone/org.jetbrains.kotlin.analysis.api.standalone/-standalone-analysis-a-p-i-session/index.md)
represents one project. To create it, call
[`buildStandaloneAnalysisAPISession`](../api/analysis-api-standalone/org.jetbrains.kotlin.analysis.api.standalone/build-standalone-analysis-a-p-i-session.md)
and describe the modules of the project inside `buildKtModuleProvider {}`.

The example below describes a typical JVM project with three modules: the JDK, the libraries from the classpath, and
the sources to analyze.

```kotlin
fun createSession(sourceRoot: Path, classpath: List<Path>): StandaloneAnalysisAPISession =
    buildStandaloneAnalysisAPISession {
        buildKtModuleProvider {
            val jvmPlatform = JvmPlatforms.defaultJvmPlatform
            platform = jvmPlatform

            // The JDK, taken from the JVM the tool runs on
            val jdk = buildKtSdkModule {
                libraryName = "JDK"
                platform = jvmPlatform
                addBinaryRootsFromJdkHome(Path(System.getProperty("java.home")), isJre = false)
            }

            // Libraries, including the Kotlin standard library
            val libraries = buildKtLibraryModule {
                libraryName = "classpath"
                platform = jvmPlatform
                addBinaryRoots(classpath)
            }

            // Sources to analyze
            val sources = buildKtSourceModule {
                moduleName = "main"
                platform = jvmPlatform
                addSourceRoot(sourceRoot)
                addRegularDependency(jdk)
                addRegularDependency(libraries)
            }

            addModule(jdk)
            addModule(libraries)
            addModule(sources)
        }
    }
```

A source root is a directory with `.kt` and `.java` files. The classpath is the list of JAR files and class
directories the module is compiled against. It must include the Kotlin standard library.

All available options are described in [Project Structure in Standalone](Standalone-Project-Structure.md).

### Analyze the code

The session provides the source files of each module in the `modulesWithFiles` property. Pass a file, or any element
inside it, to `analyze {}` just as you would do in the IDE.

The following function prints the signatures of all top-level declarations:

```kotlin
@OptIn(KaExperimentalApi::class)
fun printDeclarations(session: StandaloneAnalysisAPISession) {
    for ((module, files) in session.modulesWithFiles) {
        println("Module ${module.name}")

        analyze(module) {
            for (file in files.filterIsInstance<KtFile>()) {
                for (declaration in file.declarations) {
                    val symbol = declaration.symbol
                    println(KaRenderer.default.renderToString(symbol))
                }
            }
        }
    }
}
```

`modulesWithFiles` also contains Java files of the module, so the example filters the list to get `KtFile`s.

Everything you can do inside the `analyze {}` block is covered in the rest of the documentation. Start with
[Fundamentals](Fundamentals.md) and [Symbols](Symbols.md).

??? note "Imports for the examples above"
    ```kotlin
    import org.jetbrains.kotlin.analysis.api.KaExperimentalApi
    import org.jetbrains.kotlin.analysis.api.rendering.KaRenderer
    import org.jetbrains.kotlin.analysis.api.rendering.renderToString
    import org.jetbrains.kotlin.analysis.api.session.analyze
    import org.jetbrains.kotlin.analysis.api.standalone.StandaloneAnalysisAPISession
    import org.jetbrains.kotlin.analysis.api.standalone.buildStandaloneAnalysisAPISession
    import org.jetbrains.kotlin.analysis.api.symbols.symbol
    import org.jetbrains.kotlin.analysis.project.structure.builder.buildKtLibraryModule
    import org.jetbrains.kotlin.analysis.project.structure.builder.buildKtSdkModule
    import org.jetbrains.kotlin.analysis.project.structure.builder.buildKtSourceModule
    import org.jetbrains.kotlin.platform.jvm.JvmPlatforms
    import org.jetbrains.kotlin.psi.KtFile
    import java.nio.file.Path
    import kotlin.io.path.Path
    ```

## Session lifecycle

Building a Standalone session is relatively expensive: the Analysis API sets up its environment and indexes all source
files and libraries. Analysis results are cached inside the session, so reusing it for all files is much faster than
creating a new session for each file.

A session does not track changes in files on disk. If the sources or the dependencies change, you need to create a
new session.

By default, a session keeps all analysis results until it is disposed. If your tool analyzes a lot of modules in one
run, call `enableCacheCleaner()` in the session builder. It allows the Analysis API to drop caches when memory is low.

After you finished working with a session, dispose it using the `Disposer`:

```kotlin
val disposable = Disposer.newDisposable("My tool")
try {
    val session = buildStandaloneAnalysisAPISession(disposable) {
        // ...
    }
    // Use the session
} finally {
    Disposer.dispose(disposable)
}
```

Core IntelliJ components used by the Analysis API spawn background threads that may keep the JVM alive after the `main`
function returns ([KT-73127](https://youtrack.jetbrains.com/issue/KT-73127)). It is a known bug that will be fixed in
the future. Until that, you will need to with the process by calling `exitProcess()` explicitly.

## Running as a part of the build

A tool that analyzes a module needs the same inputs as the compiler: source roots, the classpath, and compiler options.
The build system already has them, so a common approach is to launch the tool from a build task.

When you do it, run the tool **in a separate JVM process**, not inside the build system's process. The Analysis API
artifact contains the Kotlin compiler and parts of the IntelliJ Platform. These classes may conflict with other
versions of the same classes already loaded by Gradle or its plugins.

The [Quickstart project](https://github.com/Kotlin/analysis-api-quickstart) shows this setup for Gradle. Its plugin
registers a `JavaExec` task, and passes the source directories, the compile classpath, and the language version of the
module as command-line arguments.

## Stability

The Standalone mode consists of two parts with different stability guarantees.

**The core Analysis API** is everything available through `analyze {}`. It is stable, and works in the same way as in
the IDE. Individual endpoints that are not stable yet are marked with `@KaExperimentalApi`.

**The session setup API** is currently experimental. It includes `buildStandaloneAnalysisAPISession` and the
`buildKt...Module` functions in the `org.jetbrains.kotlin.analysis.project.structure.builder` package. It may change
in an incompatible way in a future Kotlin release.

In practice, the setup code is a small, isolated part of a tool, as you can see in the example above. Keep it in one
place, and an update to a new version will only require changes there.
