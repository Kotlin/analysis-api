# Analysis API

Analysis API is a powerful library for analyzing code in Kotlin. Made on top of the Kotlin PSI syntax tree, it provides
access to various semantic information, including reference targets, expression types, declaration scopes, diagnostics
and more.

While Analysis API uses the Kotlin compiler internally, the API layer itself does not expose any compiler internals.
The library offers both source and binary backward compatibility for its stable parts.

Analysis API encapsulates all challenging parts needed for efficient Kotlin code analysis, including lazy resolution and
cache invalidation, so you can focus on the actual code handling logic.

## Quick example

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

`builtinTypes` is also a part of Analysis API available inside the analysis block. It provides access to basic
Kotlin types, including number types, `Any`, `Nothing`, and `String`.

The type of `builtinTypes.string` is a `KaType`. `Ka` is a common prefix for all Analysis API components and
abstractions; it means "Kotlin Analysis API". Instances of classes with the `Ka` prefix often require special handling.
Check the [KaLifetimeOwner](Fundamentals.md#kalifetimeowner) section for more information.

## Using in IntelliJ IDEA

Analysis API is not just some external API. It serves as the foundation for many features within the Kotlin plugin for
IntelliJ IDEA, including code completion, navigation across declarations, refactorings, inspections, debugger, and
many more. By using Analysis API, you get the same tools as the developers of the Kotlin plugin itself.

Analysis API mainly targets the K2 Kotlin compiler, but there is also limited support for the legacy 1.0 compiler.
So the same piece of logic, if implemented on top of Analysis API, can work both in the K1 and K2 Kotlin modes.

## Using in command-line tools

Analysis API can also be used in command-line tools that perform Kotlin code analysis, including linters, documentation
generators, and code generating utilities.

<note>
    Currently, the only officially supported use-case is IntelliJ IDEA plugin development.
    While Analysis API provides the Standalone mode for command-line tool developers, it is currently in development
    and subject to incompatible changes.
</note>