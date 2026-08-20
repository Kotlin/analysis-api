# KaDiagnosticCheckerKind

`KaDiagnosticCheckerKind` denotes a kind of compiler checkers which report [diagnostics](KaDiagnostic.md). A
[](KaDiagnostics.md) query runs the checkers of the kinds it was asked for, and only those, so a checker kind is both a
filter on the result and a knob on how much analysis is performed.

<warning>
<code>KaDiagnosticCheckerKind</code> is annotated <code>@KaExperimentalApi</code>. The API is not stable yet, so the
set of kinds and their meaning may change between versions.
</warning>

## Selecting the kinds

Kinds are passed to [`withCheckers()`](KaDiagnostics.md#withcheckers), either as a `vararg` or as a `Set`:

```Kotlin
element.diagnostics().withCheckers(
    KaDiagnosticCheckerKind.COMMON,
    KaDiagnosticCheckerKind.EXTENDED,
)
```

A query which was not given any kind explicitly runs the [`COMMON`](#common) checkers.

## Kinds

| Kind           | Reports                                                                            |
|----------------|------------------------------------------------------------------------------------|
| `COMMON`       | Exactly the diagnostics of a default compilation.                                  |
| `EXTENDED`     | Additional diagnostics which a default compilation does not report.                |
| `EXPERIMENTAL` | Additional diagnostics as well, but they may be slow and may have false positives. |

### `COMMON`

The compiler's common checkers, the ones which always run. Their diagnostics are exactly the ones reported by a default
compilation, which makes this kind the right choice for anything that has to agree with the compiler &mdash; error
highlighting, a linter, or a check that generated code compiles.

This is the default of a [](KaDiagnostics.md) query.

### `EXTENDED`

Additional checkers, which a default compilation does not run. They report diagnostics such as reports about redundant
code. Nothing about them is specific to an IDE &mdash; the compiler runs them too when they are explicitly enabled
&mdash; but in practice they are mostly requested by IDE features.

### `EXPERIMENTAL`

Additional checkers as well, with the same role as the `EXTENDED` ones, and with two differences:

* They might have false positives.
* They might be slow.

### `ALL`

A `Set<KaDiagnosticCheckerKind>` of all checker kinds supported by the current version of the Analysis API.

<warning>
The set may grow in future versions. By requesting <code>ALL</code>, a client opts in to the diagnostics and the
performance costs of checker kinds which do not exist yet. Prefer listing the required kinds explicitly.
</warning>

## Members

`val name: String`
: A technical name of the kind, such as `COMMON`. Also returned by `toString()`.
