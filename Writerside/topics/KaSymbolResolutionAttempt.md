# KaSymbolResolutionAttempt

`KaSymbolResolutionAttempt` is the rich result type of `tryResolveSymbols()`. Unlike the plain
`resolveSuccessfulSymbol()` / `resolveSuccessfulSymbols()` &mdash; which collapse failures to `null` &mdash; an attempt
always carries everything the compiler considered: either the resolved symbols, or a diagnostic together with candidate
symbols, or a mix of both for compound calls.

This page documents the sealed hierarchy and the helper extensions. For the high-level "how do I use this?" view, see
[](Resolving-Symbols.md).

## Hierarchy

<code-block lang="mermaid">
graph TB
  KaSymbolResolutionAttempt
  KaSymbolResolutionAttempt --> KaSimpleSymbolResolutionAttempt
  KaSimpleSymbolResolutionAttempt --> KaSimpleSymbolResolutionSuccess
  KaSimpleSymbolResolutionAttempt --> KaSimpleSymbolResolutionError
  KaSymbolResolutionAttempt --> KaCompoundSymbolResolutionError
</code-block>

## Members

### `KaSymbolResolutionAttempt`

The sealed root. Two branches: `KaSimpleSymbolResolutionAttempt` and `KaCompoundSymbolResolutionError`.

> Unlike the call API, the symbol API does **not** model "successful compound resolution" with its own type. When all
> sub-symbol resolutions in a compound case succeed, the result is just `KaSimpleSymbolResolutionSuccess` carrying the
> merged list of symbols.

### `KaSimpleSymbolResolutionAttempt`

A resolution attempt for a simple &mdash; non-compound &mdash; target. One of:

`KaSimpleSymbolResolutionSuccess`
: Resolution succeeded. Exposes `symbols: List<KaSymbol>` &mdash; one entry for unambiguous resolution, several for
ambiguity. The list is always non-empty.

`KaSimpleSymbolResolutionError`
: Resolution failed. Exposes `diagnostic: KaDiagnostic` describing the reason and `candidateSymbols: List<KaSymbol>`
&mdash; the symbols the compiler considered before giving up (e.g. an `INVISIBLE_REFERENCE` error still names the
invisible declaration as a candidate). The list may be empty.

### `KaCompoundSymbolResolutionError`

Returned only when a compound resolution produced a **mix** of successful and failed sub-attempts (or all sub-attempts
failed). Exposes `simpleAttempts: List<KaSimpleSymbolResolutionAttempt>` &mdash; at most one
`KaSimpleSymbolResolutionSuccess` (merging symbols from all successful sub-calls) and at least one
`KaSimpleSymbolResolutionError`, totaling at least two entries. When every sub-attempt succeeds, the result is
`KaSimpleSymbolResolutionSuccess` instead.

> A non-compound failure surfaces as `KaSimpleSymbolResolutionError` directly &mdash;
> `KaCompoundSymbolResolutionError` only appears when the call is genuinely compound and at least two sub-attempts are
> involved (a mix of success and failure, or all failures). For a simple-call failure, expect
> `KaSimpleSymbolResolutionError`.

## Helper extensions

The sealed hierarchy is exhaustive, but most callers do not need to pattern-match on it. Five extension properties cover
the common cases:

`val KaSymbolResolutionAttempt.symbols: List<KaSymbol>`
: Every symbol the compiler considered, regardless of success or failure. On success returns the resolved symbols; on
error returns the candidate symbols; on a compound error returns the combined symbols from all sub-attempts. Use this
for "best effort" navigation that wants to highlight anything reachable.

`val KaSymbolResolutionAttempt.successfulSymbols: List<KaSymbol>`
: The resolved symbols if resolution succeeded; empty otherwise. A successful resolution always has at least one
symbol, so an empty list always means a failure. Use this when you want to silently drop failed resolutions.

`val KaSymbolResolutionAttempt.isSuccessful: Boolean`
: Whether the resolution succeeded. Prefer this over a `this is KaSimpleSymbolResolutionSuccess` check, which only
covers simple attempts and silently treats every `KaCompoundSymbolResolutionError` as a success.

`val KaSymbolResolutionAttempt.errors: List<KaSimpleSymbolResolutionError>`
: The errors of the attempt, for every attempt kind: empty on success, a one-element list for a simple error, and the
failed sub-attempts of a compound error. The list is empty if and only if `isSuccessful` is `true`.

`val KaSymbolResolutionAttempt.simpleAttempts: List<KaSimpleSymbolResolutionAttempt>`
: The flattened sub-attempts: the attempt itself for a simple one, and `KaCompoundSymbolResolutionError.simpleAttempts`
for a compound one. Use it when the **successful** sub-attempt of a partially failed compound matters, since `errors`
drops it.

For full control, use the `fold` extension:

```Kotlin
fun <T> KaSymbolResolutionAttempt.fold(
    onSuccess: (List<KaSymbol>) -> T,
    onFailure: (List<KaSimpleSymbolResolutionError>) -> T,
): T
```

`onSuccess` is invoked once with the resolved symbols when all sub-attempts succeeded; `onFailure` is invoked with the
`errors` otherwise &mdash; including the single error case (a one-element list) and the compound mixed case. A
successful sub-attempt of a compound error is not passed to `onFailure`; reach it through `simpleAttempts`.

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
            "Failed (${errors.size} errors)"
        },
    )
}
```
