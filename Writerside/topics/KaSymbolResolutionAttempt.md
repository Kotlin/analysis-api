# KaSymbolResolutionAttempt

`KaSymbolResolutionAttempt` is the rich result type of `tryResolveSymbols()`. Unlike the plain `resolveSymbol()` /
`resolveSymbols()` &mdash; which collapse failures to `null` &mdash; an attempt always carries everything the compiler
considered: either the resolved symbols, or a diagnostic together with candidate symbols, or a mix of both for
compound calls.

This page documents the sealed hierarchy and the helper extensions. For the high-level "how do I use this?" view, see
[](Resolving-Symbols.md).

## Hierarchy

<code-block lang="mermaid">
graph TB
  KaSymbolResolutionAttempt
  KaSymbolResolutionAttempt --> KaSingleSymbolResolutionAttempt
  KaSingleSymbolResolutionAttempt --> KaSymbolResolutionSuccess
  KaSingleSymbolResolutionAttempt --> KaSymbolResolutionError
  KaSymbolResolutionAttempt --> KaCompoundSymbolResolutionError
</code-block>

## Members

### `KaSymbolResolutionAttempt`

The sealed root. Two branches: `KaSingleSymbolResolutionAttempt` and `KaCompoundSymbolResolutionError`.

> Unlike the call API, the symbol API does **not** model "successful compound resolution" with its own type. When all
> sub-symbol resolutions in a compound case succeed, the result is just `KaSymbolResolutionSuccess` carrying the merged
> list of symbols.

### `KaSingleSymbolResolutionAttempt`

A resolution attempt for a single conceptual target. One of:

`KaSymbolResolutionSuccess`
: Resolution succeeded. Exposes `symbols: List<KaSymbol>` &mdash; one entry for unambiguous resolution, several for
ambiguity. The list is always non-empty.

`KaSymbolResolutionError`
: Resolution failed. Exposes `diagnostic: KaDiagnostic` describing the reason and `candidateSymbols: List<KaSymbol>`
&mdash; the symbols the compiler considered before giving up (e.g. an `INVISIBLE_REFERENCE` error still names the
invisible declaration as a candidate). The list may be empty.

### `KaCompoundSymbolResolutionError`

Returned only when a compound resolution produced a **mix** of successful and failed sub-attempts (or all sub-attempts
failed). Exposes `attempts: List<KaSingleSymbolResolutionAttempt>` &mdash; at most one `KaSymbolResolutionSuccess`
(merging symbols from all successful sub-calls) and at least one `KaSymbolResolutionError`, totaling at least two
entries. When every sub-attempt succeeds, the result is `KaSymbolResolutionSuccess` instead.

> A non-compound failure surfaces as `KaSymbolResolutionError` directly &mdash; `KaCompoundSymbolResolutionError` only
> appears when the call is genuinely compound and at least two sub-attempts are involved (a mix of success and failure,
> or all failures). For a plain single-call failure, expect `KaSymbolResolutionError`.

## Helper extensions

The sealed hierarchy is exhaustive, but most callers do not need to pattern-match on it. Two extension properties cover
the common cases:

`val KaSymbolResolutionAttempt.symbols: List<KaSymbol>`
: Every symbol the compiler considered, regardless of success or failure. On success returns the resolved symbols; on
error returns the candidate symbols; on a compound error returns the combined symbols from all sub-attempts. Use this
for "best effort" navigation that wants to highlight anything reachable.

`val KaSymbolResolutionAttempt.successfulSymbols: List<KaSymbol>`
: The resolved symbols if resolution succeeded; empty otherwise. Use this when you want to silently drop failed
resolutions.

For full control, use the `fold` extension:

```Kotlin
fun <T> KaSymbolResolutionAttempt.fold(
    onSuccess: (List<KaSymbol>) -> T,
    onFailure: (List<KaSingleSymbolResolutionAttempt>) -> T,
): T
```

`onSuccess` is invoked once with the resolved symbols when all sub-attempts succeeded; `onFailure` is invoked with the
list of individual `KaSingleSymbolResolutionAttempt`s otherwise &mdash; including the single error case (a one-element
list) and the compound mixed case.

## Example

```Kotlin
@OptIn(KaExperimentalApi::class, KtExperimentalApi::class)
fun describe(element: KtElement): String? = analyze(element) {
    val attempt = (element as? KtResolvable)?.tryResolveSymbols()
        ?: return@analyze null

    attempt.fold(
        onSuccess = { symbols ->
            val names = symbols.joinToString {
                it.name?.asString() ?: "?"
            }
            
            "Resolved: $names"
        },
        onFailure = { errors ->
            "Failed (${errors.size} sub-attempts)"
        },
    )
}
```
