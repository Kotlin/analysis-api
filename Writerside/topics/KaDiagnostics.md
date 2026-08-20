# KaDiagnostics

`KaDiagnostics` is the description of a diagnostic query. It is returned by
[`diagnostics()`](Diagnostics.md#the-entry-point) and yields the requested [](KaDiagnosticWithPsi.md) instances on
iteration.

For the high-level view, see [](Diagnostics.md).

<warning>
<code>KaDiagnostics</code> is annotated <code>@KaExperimentalApi</code>, and so is the <code>diagnostics()</code> entry
point which produces it. The API is not stable yet, so its contract may change between versions.
</warning>

## Hierarchy

```Kotlin
@KaExperimentalApi
interface KaDiagnostics :
    KaLifetimeOwner,
    Sequence<KaDiagnosticWithPsi<*>>
```

As a [KaLifetimeOwner](Fundamentals.md#kalifetimeowner), a query is valid only within the `analyze {}` block that
created it. It must not be stored in a field or iterated after the block has finished.

## Query semantics

A query is **immutable**. Every modifier returns a new `KaDiagnostics` and leaves the receiver untouched, so a single
base query can be adjusted for several use sites:

```Kotlin
val query = file.diagnostics()

val errors = query.filter { it.severity == KaSeverity.ERROR }
val withExtended = query.withCheckers(
    KaDiagnosticCheckerKind.COMMON,
    KaDiagnosticCheckerKind.EXTENDED,
)
```

Modifiers **replace** rather than accumulate. Applying the same modifier twice keeps the value from the last call.

A query is also **lazy**. Creating it and chaining modifiers performs no analysis; the analysis runs during the
iteration, and only as far as the iteration goes. Iterating does not consume the query, so the same instance may be
iterated again. See [](Diagnostics.md#laziness) for what that means in practice.

## Modifiers

### `withCheckers`

```Kotlin
fun withCheckers(
    kinds: Set<KaDiagnosticCheckerKind>,
): KaDiagnostics

fun withCheckers(
    vararg kinds: KaDiagnosticCheckerKind,
): KaDiagnostics
```

Returns a query which yields the diagnostics of the given checker [kinds](KaDiagnosticCheckerKind.md). The default is
`KaDiagnosticCheckerKind.COMMON` alone, matching what the compiler reports.

The kinds **replace** the currently requested ones instead of being added to them, so both of the following queries run
common *and* extended checkers, and the second one does not additionally keep any previously requested kind:

```Kotlin
element.diagnostics().withCheckers(
    KaDiagnosticCheckerKind.COMMON,
    KaDiagnosticCheckerKind.EXTENDED,
)

element.diagnostics()
    .withCheckers(KaDiagnosticCheckerKind.EXPERIMENTAL)
    .withCheckers(
        KaDiagnosticCheckerKind.COMMON,
        KaDiagnosticCheckerKind.EXTENDED,
    )
```

An empty set of kinds yields no diagnostics, and no checkers are run in that case:

```Kotlin
// Yields nothing, and analyzes nothing
element.diagnostics().withCheckers(emptySet())
```

Each requested kind runs its own checkers, so requesting more kinds means more work.

### `ignoreSuppressed`

```Kotlin
fun ignoreSuppressed(ignore: Boolean): KaDiagnostics
```

Controls whether [suppressed](KaDiagnostic.md) diagnostics are filtered out. The default is `true` &mdash; suppressed
diagnostics are not yielded, mirroring the compiler, which does not report them.

`ignoreSuppressed(false)` yields them in addition to the regular ones, so the result is a superset of the default one.
Suppressed diagnostics carry `isSuppressed == true`, which is how they can be told apart:

```Kotlin
val onlySuppressed = element.diagnostics()
    .ignoreSuppressed(false)
    .filter { it.isSuppressed }
```

Suppressed diagnostics should not be presented to the user as reported problems. They exist for tooling which reasons
about suppressions themselves, such as an inspection which detects a redundant `@Suppress` annotation. Collecting them
requires no additional analysis.

### `directOnly`

```Kotlin
fun directOnly(direct: Boolean): KaDiagnostics
```

Controls whether the query covers the element's subtree. The default is `false` &mdash; the query yields every
diagnostic reported on the element itself and on any element below it.

With `directOnly(true)`, only the diagnostics attached to the exact element are yielded.

<warning>
The direct result is <b>not</b> the complete set of diagnostics which concern an element: a problem with the element may
well be reported on one of its children or on a containing element. Keep the default <code>false</code> unless the
diagnostics of that exact PSI element are what you need &mdash; for example, when checking whether the element itself is
reported on, ignoring whatever its nested code contains.
</warning>

```Kotlin
// Every diagnostic inside the function, including its body
function.diagnostics()

// Only the diagnostics attached to the KtNamedFunction itself
function.diagnostics().directOnly(true)
```

## Recipes

Check whether an element contains errors, stopping at the first one:

```Kotlin
val hasErrors = element.diagnostics()
    .any { it.severity == KaSeverity.ERROR }
```

Render the messages of a file the way the compiler would:

```Kotlin
val messages = file.diagnostics()
    .map { it.getDefaultMessageWithFactoryName() }
    .toList()
```

Include the additional checkers on top of the common ones:

```Kotlin
val ideDiagnostics = file.diagnostics()
    .withCheckers(
        KaDiagnosticCheckerKind.COMMON,
        KaDiagnosticCheckerKind.EXTENDED,
    )
    .toList()
```

Group the diagnostics of a declaration by severity:

```Kotlin
val bySeverity = declaration.diagnostics()
    .groupBy { it.severity }
```

Find the first error and its position in the file:

```Kotlin
val firstError = file.diagnostics()
    .firstOrNull { it.severity == KaSeverity.ERROR }

val offset = firstError?.textRanges?.firstOrNull()?.startOffset
```

Handle the diagnostics of a whole file per element. Collect them once and group them by their PSI instead of querying
every element separately &mdash; a query per element repeats the traversal for each of them:

```Kotlin
val byElement = file.diagnostics().groupBy { it.psi }
```
