# Diagnostics

Analysis API allows you to access and analyze compiler diagnostics (errors and warnings) associated with entire files
or specific elements.

## Diagnostics in a `KtFile`

To collect diagnostics for an entire file, use `collectDiagnostics()`:

```kotlin
analyze(ktFile) {
    val diagnostics = ktFile
        .collectDiagnostics(KaDiagnosticCheckerFilter.ONLY_COMMON_CHECKERS)
        .filterIsInstance<KaFirDiagnostic.WrongAnnotationTarget>()
}
```

The `KaDiagnosticCheckerFilter` enum allows you to control which kinds of diagnostics are included:

* `ONLY_COMMON_CHECKERS`: Includes diagnostics only from the compiler checkers.
* `ONLY_EXTENDED_CHECKERS`: Includes diagnostics from extended checkers (that typically run only in the IDE).
* `EXTENDED_AND_COMMON_CHECKERS`: Includes diagnostics from both common and extended checkers.

## Diagnostics on an element

<note>Experimental API. Subject to changes.</note>

To get diagnostics for a specific element, use `diagnostics`:

```kotlin
analyze(ktElement) {
    val diagnostics = ktElement
        .diagnostics(KaDiagnosticCheckerFilter.ONLY_COMMON_CHECKERS)
}
```

Note that the returned list of diagnostics does not include diagnostics for nested `KtElement`s.

## `KtDiagnosticWithPsi`

`collectDiagnostics` and `diagnostics` return a collection of `KtDiagnosticWithPsi` instances.
This interface provides access to information about the diagnostic.



| Member           | Description                                                                   |
|------------------|-------------------------------------------------------------------------------|
| `severity`       | The severity of the diagnostic (e.g., `ERROR`, `WARNING`).                    |
| `factoryName`    | The name of the diagnostic factory that produced the diagnostic.              |
| `defaultMessage` | The default message associated with the diagnostic.                           |
| `psi`            | The `PsiElement` to which the diagnostic is attached.                         |
| `textRanges`     | The text ranges within the `psi` element that are relevant to the diagnostic. |