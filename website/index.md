---
icon: lucide/rocket
hide:
  - navigation
---
<h1 style="text-align: center;"><img alt="</> logotype" src="images/kotlin-logo.png" width="100" height="100" style="vertical-align: middle;"> Kotlin Analysis API</h1>

## Introduction

The **Kotlin Analysis API** is a library for analyzing Kotlin code at the semantic level. It provides a structured way to query information
about Kotlin code, including symbols, types, and semantic relationships between them. Built on top of Kotlin's
[PSI](https://plugins.jetbrains.com/docs/intellij/psi.html) syntax trees, the API offers a clean abstraction over the compiler's internal
representations, making it accessible both for IDE plugin makers and command-line tool developers.

While the Analysis API uses the Kotlin compiler internally, the API layer itself does not expose any compiler internals.
The library offers both source and binary backward compatibility for its stable parts.

The Analysis API encapsulates all challenging parts needed for efficient Kotlin code analysis, including lazy resolution
and cache invalidation, so you can focus on the actual code handling logic.

### Quick Example

The `hasStringType()` function below checks if the given expression has a non-null `kotlin.String` type.

```Kotlin
@RequiresReadLock
fun KtExpression.hasStringType(): Boolean {
    analyze(this) {
        return expressionType == builtinTypes.string
    }
}
```

Most of the Analysis API surface can be accessed from inside `analyze {}` blocks. Such is the `expressionType` extension
property – for the given `KtExpression`, it returns the resolved type.

`builtinTypes` is also a part of the Analysis API available inside the analysis block. It provides access to basic
Kotlin types, including number types, `Any`, `Nothing`, and `String`.

The type of `builtinTypes.string` is a `KaType`. `Ka` is a common prefix for all Analysis API components and
abstractions which stands for "Kotlin Analysis".

## Where to Use

The Analysis API works both inside IntelliJ IDEA and as a separate library.  
The API for analyzing code is the same in both of them.

### In IntelliJ IDEA Plugins

The Analysis API is not just some external API. It serves as the foundation for many features within the Kotlin plugin
for IntelliJ IDEA, including code completion, navigation across declarations, refactorings, inspections, the debugger,
and many more. By using the Analysis API, you get the same tools as the developers of the Kotlin plugin itself.

The Analysis API is a part of the Kotlin plugin, so your plugin only needs to depend on it.

[Using in IntelliJ Plugins](topics/IntelliJ-Plugins.md){ .md-button }

### In Command-Line Tools

The Analysis API can also be used outside the IDE, in any JVM application. This is called the **Standalone mode**.
It is a good fit for linters, documentation generators, code-generating utilities, and other tools that run from the
command line or as a part of the build.

In the Standalone mode, there is no IDE that knows the project layout. The tool describes the sources and libraries
to analyze by itself, and then uses the same `analyze {}` function.

[Standalone Mode](topics/Standalone.md){ .md-button }
[Quickstart Project](https://github.com/Kotlin/analysis-api-quickstart){ .md-button }

!!! note
    While the core Analysis API is stable in both environments, the API for describing project structure in the
    Standalone mode is experimental and will change in future releases.

## Read about Analysis API

- [The Story Behind K2 Mode and How It Works - JetBrains Blog](https://blog.jetbrains.com/idea/2025/04/the-story-behind-k2-mode-and-how-it-works/)

## Projects using Analysis API

* [Kotlin IntelliJ Plugin](https://plugins.jetbrains.com/plugin/6954-kotlin) - official Kotlin plugin for **IntelliJ IDEA**
* [Kotlin LSP](https://github.com/Kotlin/kotlin-lsp) - official Kotlin language server and **Visual Studio Code** extension
* [Kotlin Dokka](https://github.com/Kotlin/dokka) - Kotlin documentation generator
* [Kotlin Swift Export](https://kotlinlang.org/docs/native-swift-export.html) - Swift generator for Kotlin/Native code
* [Android Lint](https://developer.android.com/studio/write/lint) - Lint for Android projects by **Google**
* [Metalava](https://android.googlesource.com/platform/tools/metalava/) - Metadata generator by **Google**
* [KSP](https://github.com/google/ksp) - Kotlin Symbol Processing API by **Google**
* [Detekt](https://github.com/detekt/detekt) - Static code analysis for Kotlin
* And more

Have a project using **Analysis API**? Contact us to be listed here!

## Report an Issue

**Kotlin Analysis API** works with [**JetBrains YouTrack**](https://youtrack.jetbrains.com/issues/KT) task management system.
To report an issue you've encountered, please select **KT** project as well as a suitable
**Analysis API** subsystem when creating a ticket.
