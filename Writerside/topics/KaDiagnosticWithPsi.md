# KaDiagnosticWithPsi

A [](KaDiagnostic.md) reported on a `PsiElement` of type `PSI`.

This is the element type of a [](KaDiagnostics.md) query, so every diagnostic obtained from
[diagnostic collection](Diagnostics.md) knows the PSI it is attached to.

## Hierarchy

Inherits from [KaDiagnostic](KaDiagnostic.md).

```Kotlin
interface KaDiagnosticWithPsi<out PSI : PsiElement> :
    KaDiagnostic
```

The generated `KaFirDiagnostic<PSI>` interface inherits from `KaDiagnosticWithPsi<PSI>` and has a subinterface per
diagnostic kind, with the parameters of that diagnostic exposed as typed properties:

```Kotlin
val wrongTargets = file.diagnostics()
    .filterIsInstance<KaFirDiagnostic.WrongAnnotationTarget>()
```

Those interfaces are annotated `@KaUnstableDiagnosticApi` and have no compatibility guarantees. See
[Selecting diagnostics by kind](Diagnostics.md#selecting-diagnostics-by-kind) for the trade-off against
[`factoryName`](KaDiagnostic.md).

## Members

`val psi: PSI`
: The PSI element the diagnostic is reported on. For a diagnostic from a query with the default
[`directOnly(false)`](KaDiagnostics.md#directonly), this is the queried element itself or any element below it.

`val textRanges: Collection<TextRange>`
: The text ranges where the diagnostic occurs, in the offsets of the containing file, and contained within the range of
the `psi` element. A diagnostic is not necessarily reported on the whole element &mdash; the ranges are what an editor
would underline.

`val diagnosticClass: KClass<out KaDiagnosticWithPsi<PSI>>`
: The class of the diagnostic, narrowed from [`KaDiagnostic.diagnosticClass`](KaDiagnostic.md).
