# Legacy Diagnostics API

<warning>
This page documents the <b>legacy</b> diagnostics API based on <code>KtFile.collectDiagnostics()</code>,
<code>KtElement.diagnostics(filter)</code>, and the <code>KaDiagnosticCheckerFilter</code> enum. The whole surface is
obsolete, and most of it is already deprecated. See <a href="Diagnostics.md"/> for the replacement.
</warning>

The legacy surface consisted of five endpoints. Their semantics were not aligned with each other:
`KtElement.diagnostics()` covered a single element while `KtFile.diagnostics()` was recursive; `collectDiagnostics()`
was eager and `diagnostics()` was lazy; suppressed diagnostics were reachable for files only, through
`diagnosticsIgnoringSuppression()`. Each endpoint also took a `KaDiagnosticCheckerFilter`, a closed enum which named
four of the eight combinations of the three checker kinds.

The [](KaDiagnostics.md) query replaces all of them with a single entry point and composable modifiers.

## Endpoints

| Legacy endpoint                                        | Replacement                                                    |
|--------------------------------------------------------|----------------------------------------------------------------|
| `KtElement.diagnostics(filter): Collection<...>`       | `element.diagnostics().withCheckers(...).directOnly(true)`     |
| `KtElement.directDiagnostics(filter): Collection<...>` | `element.diagnostics().withCheckers(...).directOnly(true)`     |
| `KtFile.collectDiagnostics(filter): Collection<...>`   | `file.diagnostics().withCheckers(...).toList()`                |
| `KtFile.diagnostics(filter): Sequence<...>`            | `file.diagnostics().withCheckers(...)`                         |
| `KtFile.diagnosticsIgnoringSuppression(filter)`        | `file.diagnostics().withCheckers(...).ignoreSuppressed(false)` |

## Checker filters

`KaDiagnosticCheckerFilter` becomes a set of [](KaDiagnosticCheckerKind.md) values passed to
[`withCheckers()`](KaDiagnostics.md#withcheckers). Unlike the enum, the set covers every combination of kinds:

| `KaDiagnosticCheckerFilter`    | `withCheckers()` argument                                          |
|--------------------------------|--------------------------------------------------------------------|
| `ONLY_COMMON_CHECKERS`         | `KaDiagnosticCheckerKind.COMMON`, which is also the default        |
| `ONLY_EXTENDED_CHECKERS`       | `KaDiagnosticCheckerKind.EXTENDED`                                 |
| `ONLY_EXPERIMENTAL_CHECKERS`   | `KaDiagnosticCheckerKind.EXPERIMENTAL`                             |
| `EXTENDED_AND_COMMON_CHECKERS` | `KaDiagnosticCheckerKind.COMMON, KaDiagnosticCheckerKind.EXTENDED` |

Because `ONLY_COMMON_CHECKERS` is what a query requests by default, a `withCheckers()` call can be dropped entirely when
migrating from it.

## Watch out for the scope

The legacy `KtElement.diagnostics(filter)` and `KtElement.directDiagnostics(filter)` both returned the diagnostics of
the element **alone**, while `KtFile.collectDiagnostics(filter)` was recursive. In the new API, the scope is a modifier
instead of being encoded in the endpoint name, and the default is the recursive one, which is the correct choice in most
cases:

```Kotlin
// Legacy: the element alone
element.diagnostics(KaDiagnosticCheckerFilter.ONLY_COMMON_CHECKERS)

// Same behavior
element.diagnostics().directOnly(true)

// Everything reported inside the element, which the
// legacy element endpoints could not express
element.diagnostics()
```

Dropping `directOnly(true)` while migrating is often the actual fix: a diagnostic which concerns an element may be
reported on one of its children, so the direct result was rarely the complete answer. See
[`directOnly`](KaDiagnostics.md#directonly).

## Migration examples

### Collecting file diagnostics

```Kotlin
// Legacy
analyze(file) {
    val diagnostics = file.collectDiagnostics(
        KaDiagnosticCheckerFilter.ONLY_COMMON_CHECKERS,
    )
    val messages = diagnostics.map { it.defaultMessage }
}

// New
analyze(file) {
    val messages = file.diagnostics()
        .map { it.defaultMessage }
        .toList()
}
```

The query is lazy, so the `toList()` call is what materializes the result. Where the legacy collection was only iterated
over, `toList()` can be dropped, and the analysis then stops as soon as the iteration does.

### Extended checkers

```Kotlin
// Legacy
file.diagnostics(
    KaDiagnosticCheckerFilter.EXTENDED_AND_COMMON_CHECKERS,
)

// New
file.diagnostics().withCheckers(
    KaDiagnosticCheckerKind.COMMON,
    KaDiagnosticCheckerKind.EXTENDED,
)
```

### Suppressed diagnostics

```Kotlin
// Legacy
file.diagnosticsIgnoringSuppression(
    KaDiagnosticCheckerFilter.ONLY_COMMON_CHECKERS,
)

// New
file.diagnostics().ignoreSuppressed(false)
```

Suppression is per-diagnostic data now rather than a collection mode: the query yields suppressed diagnostics together
with the regular ones, and each of them is marked with [`isSuppressed`](KaDiagnostic.md). The endpoint also works for
any element, not only for a file.

## Stability

`collectDiagnostics()` is the only stable endpoint here: it is neither experimental nor deprecated, even though its
semantics are superseded. The other legacy endpoints are experimental and deprecated.

The replacement is annotated `@KaExperimentalApi`, so migrating from `collectDiagnostics()` does trade a stable endpoint
for one whose contract may still change between versions. It is, however, the only surface which can express element
scopes, suppressed diagnostics, and arbitrary combinations of checker kinds.
