# Overview

Diagnostics are the errors, warnings, and informational messages that compiler checkers report on Kotlin code. The
Analysis API exposes them through a single entry point, `diagnostics()`, which returns a [`KaDiagnostics`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostics/index.md) &mdash; a
*query* over the diagnostics of a `KtElement`.

!!! warning
    The `diagnostics()` entry point, the `KaDiagnostics` query, and
    `KaDiagnosticCheckerKind` are annotated `@KaExperimentalApi`. The API is not stable yet, so its
    contract may change between versions.

!!! tip
    Snippets on this page assume an `analyze { }` block (or a `context(_: KaSession)` declaration) is in scope.

## The entry point

`diagnostics()` is a top-level extension function on `KtElement` declared in the
`org.jetbrains.kotlin.analysis.api.diagnostics` package with a `KaSession` context parameter. Import it and use it
wherever a session is available:

```Kotlin
import org.jetbrains.kotlin.analysis.api.diagnostics.diagnostics

context(_: KaSession)
fun report(file: KtFile) {
    for (diagnostic in file.diagnostics()) {
        handle(diagnostic)
    }
}
```

The query covers the element together with its subtree, so its scope is chosen by the element it is asked about:

```Kotlin
// Diagnostics of the whole file
file.diagnostics()

// Diagnostics of the function, including its body
function.diagnostics()
```

## Defaults

By default, `element.diagnostics()` yields **exactly the diagnostics the compiler reports** for the element and its
subtree. Each aspect of the query has a modifier which overrides that default:

| Aspect                 | Default                                                     | Modifier                                                  |
|------------------------|-------------------------------------------------------------|-----------------------------------------------------------|
| Checker kinds          | Only [common](../api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic-checker-kind/index.md) compiler checkers | [`withCheckers()`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostics/index.md#withcheckers)         |
| Suppressed diagnostics | Not yielded                                                 | [`ignoreSuppressed()`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostics/index.md#ignoresuppressed) |
| Scope                  | The element together with its subtree                       | [`directOnly()`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostics/index.md#directonly)             |

Modifiers are chained before the iteration begins:

```Kotlin
element.diagnostics()
    .withCheckers(
        KaDiagnosticCheckerKind.COMMON,
        KaDiagnosticCheckerKind.EXTENDED,
    )
    .ignoreSuppressed(false)
    .directOnly(true)
    .forEach { handle(it) }
```

The query is immutable: each modifier returns a new `KaDiagnostics` instead of mutating the receiver, so a query can be
kept around and adjusted for several use sites. Modifiers do not accumulate &mdash; applying the same modifier twice
keeps the last value, and `withCheckers()` *replaces* the requested kinds rather than adding to them.

See [`KaDiagnostics`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostics/index.md) for the exact semantics of every modifier.

## Laziness

`diagnostics()` and its modifiers only build a description of the query. The analysis runs during the iteration, and
only as far as the iteration goes, so the cost of a query is proportional to how much of it is consumed.

A query which stops early analyzes only what it had to. The following code stops at the first error, however many
diagnostics the element has:

```Kotlin
val hasErrors = element.diagnostics()
    .any { it.severity == KaSeverity.ERROR }
```

`toList()`, on the other hand, always analyzes the whole scope. The same holds for anything that has to see every
diagnostic, such as `count()` or `groupBy {}`.

Iterating a query does not consume it: the same instance may be iterated again, and adjusted with modifiers in between.

!!! warning
    A `KaDiagnostics` query is a [KaLifetimeOwner](Fundamentals.md#kalifetimeowner), and so are the
    diagnostics it yields. Neither the query nor its elements may be stored or iterated outside of the
    `analyze {}` block they were created in. If diagnostic data has to outlive the session, extract the plain
    values, such as `defaultMessage` or `textRanges`, inside the block.

## Handling a diagnostic

The query yields [`KaDiagnosticWithPsi`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic-with-psi/index.md) instances, which expose the reported message, its severity, and the PSI it
is attached to:

```Kotlin
file.diagnostics()
    .filter { it.severity == KaSeverity.ERROR }
    .forEach { diagnostic ->
        val range = diagnostic.textRanges.firstOrNull()
        println("$range: ${diagnostic.defaultMessage}")
    }
```

### Selecting diagnostics by kind

The generated `KaFirDiagnostic` hierarchy has an interface per diagnostic kind, which exposes the parameters of that
diagnostic as typed properties:

```Kotlin
val wrongTargets = file.diagnostics()
    .filterIsInstance<KaFirDiagnostic.WrongAnnotationTarget>()
    .map { it.actualTarget to it.allowedTargets }
```

This is usually the form to prefer, but it comes with no compatibility guarantees: `KaFirDiagnostic` and every
diagnostic in it are annotated `@KaUnstableDiagnosticApi`. Diagnostics mirror the ones reported by the compiler, and the
Analysis API does not control that set &mdash; a diagnostic may be renamed, split, merged, gain or lose parameters, or
be removed, without a deprecation cycle.

Where the code has to keep working across Analysis API versions, compare the [`factoryName`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic/index.md) instead:

```Kotlin
val unresolved = element.diagnostics()
    .filter { it.factoryName == "UNRESOLVED_REFERENCE" }
```

The two differ in how they fail. A renamed or removed diagnostic breaks the typed form at compile time, which is loud
but has to be migrated; the `factoryName` comparison keeps compiling and silently stops matching anything.

## Suppressed diagnostics

A diagnostic which is suppressed at its use site, for example by a `@Suppress` annotation, is not reported by the
compiler. Such diagnostics are filtered out by default, and `ignoreSuppressed(false)` yields them as well, each marked
with [`isSuppressed`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic/index.md#issuppressed):

```Kotlin
val suppressed = declaration.diagnostics()
    .ignoreSuppressed(false)
    .filter { it.isSuppressed }
```

Suppressed diagnostics should not be presented to the user as if the compiler reported them. They are meant for tooling
which analyzes the suppressions themselves &mdash; an inspection reporting a redundant `@Suppress` annotation, for
instance. Collecting them requires no additional analysis.

## Performance

* Every requested checker kind runs its checkers, so requesting more kinds means more work. Prefer listing the kinds
  you need over [`KaDiagnosticCheckerKind.ALL`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic-checker-kind/-companion/index.md#all).
* Ask about the narrowest element that covers your interest. A subtree query only computes the file structure needed for
  that subtree, so it is cheaper than collecting the diagnostics of the whole file and filtering them by PSI afterwards.
* Prefer short-circuiting sequence operations over materializing the query with `toList()`.

## Where to go next

* [`KaDiagnostics`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostics/index.md) &mdash; the query interface and the precise semantics of its modifiers.
* [`KaDiagnosticCheckerKind`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic-checker-kind/index.md) &mdash; the available checker kinds and what each of them reports.
* [`KaDiagnostic`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic/index.md) and [`KaDiagnosticWithPsi`](../api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic-with-psi/index.md) &mdash; the diagnostic itself.
* [Legacy Diagnostics API](Legacy-Diagnostics-API.md) &mdash; mapping from the former `collectDiagnostics` /
  `KaDiagnosticCheckerFilter` API to the query.
