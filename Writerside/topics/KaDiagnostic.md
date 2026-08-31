# KaDiagnostic

A diagnostic message reported by a compiler checker.

Diagnostics come either from [diagnostic collection](Diagnostics.md), which yields the more specific
[](KaDiagnosticWithPsi.md), or from other parts of the Analysis API which expose the reason of a failure, such as
`KaSimpleCallResolutionError.diagnostic` in [](KaCallResolutionAttempt.md).

## Members

`val factoryName: String`
: A technical name identifying the diagnostic, such as `UNRESOLVED_REFERENCE`. This is the same name as reported by the
compiler when the `-Xrender-internal-diagnostic-names` compiler flag is enabled. Prefer it over the rendered message
when a diagnostic has to be recognized programmatically.

`val severity: KaSeverity`
: The severity of the diagnostic (e.g., `ERROR` or `WARNING`), determined from the compiler's classification of the
diagnostic.

`val defaultMessage: String`
: The human-readable message rendered by the compiler to describe the error, warning, or info.

`val isSuppressed: Boolean`
: Whether the diagnostic is suppressed at its use site, for example by a `@Suppress` annotation. Suppressed diagnostics
are not reported by the compiler, so they should not be presented to the user as is. Diagnostic collection filters them
out by default, and [`ignoreSuppressed(false)`](KaDiagnostics.md#ignoresuppressed) yields them as well. The property is
only meaningful for diagnostics obtained from diagnostic collection; for a diagnostic obtained in another way, such as
the diagnostic of an unresolved call, it is always `false`.
: **Experimental API**.

`val diagnosticClass: KClass<*>`
: The class of the diagnostic. For a diagnostic of the `KaFirDiagnostic` hierarchy, this is the interface which
corresponds to the diagnostic kind, such as `KaFirDiagnostic.WrongAnnotationTarget`.

## Utilities

`fun KaDiagnostic.getDefaultMessageWithFactoryName(): String`
: The `defaultMessage` prefixed with the `factoryName`, formatted as `[FACTORY_NAME] message`. Handy for logs and test
data, where the rendered message alone is ambiguous.

## `KaSeverity`

The `severity` property indicates how the compiler classifies the diagnostic.

| Member    | Description                                                            |
|-----------|------------------------------------------------------------------------|
| `ERROR`   | The code is invalid and will not compile.                              |
| `WARNING` | The code compiles, but the checker reports a problem with it.          |
| `INFO`    | An informational message which reports neither an error nor a problem. |

## Example

```Kotlin
context(_: KaSession)
fun describe(diagnostic: KaDiagnostic): String = buildString {
    append(diagnostic.severity)
    append(": ")
    append(diagnostic.getDefaultMessageWithFactoryName())
}
```
