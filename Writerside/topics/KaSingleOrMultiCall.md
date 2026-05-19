# KaSingleOrMultiCall

`KaSingleOrMultiCall` is the sealed return type of `resolveCall()`. The type system splits resolved calls into two
shapes:

* [](KaSingleCall.md) &mdash; a single resolved callable applied at this site. Most everyday call sites
  (function invocations, property accesses, callable references, annotation entries, supertype calls) return this.
* [](KaMultiCall.md) &mdash; a compound or desugared expression that resolves to several sub-calls. This is
  what `for` loops, delegated properties, compound assignments (`+=`, `++`, `--`), and compound array access
  (`a[i] += v`) return.

## Hierarchy

<code-block lang="mermaid">
graph TB
  KaSingleOrMultiCall
  KaSingleOrMultiCall --> KaSingleCall
  KaSingleOrMultiCall --> KaMultiCall
</code-block>

## Helper extensions

Two extension properties give a uniform view across both branches:

`val KaSingleOrMultiCall.calls: List<KaSingleCall<*, *>>`
: The flattened list of single calls. Returns `listOf(this)` for a `KaSingleCall`; returns `KaMultiCall.calls` for a
`KaMultiCall`.

`val KaSingleOrMultiCall.symbols: List<KaSymbol>`
: The flattened list of symbols across every contained `KaSingleCall`. Convenient when you only care about *who* was
called and not about the call structure.

## When the type system narrows the result

Many specialized `resolveCall(...)` methods commit to one branch in their return type:

* `KtForExpression.resolveCall(): KaForLoopCall?` &mdash; always a `KaMultiCall`.
* `KtPropertyDelegate.resolveCall(): KaDelegatedPropertyCall?` &mdash; always a `KaMultiCall`.
* `KtCallElement.resolveCall(): KaFunctionCall<*>?` &mdash; always a `KaSingleCall`.
* `KtAnnotationEntry.resolveCall(): KaAnnotationCall?` &mdash; always a `KaSingleCall`.

The generic `KtResolvableCall.resolveCall(): KaSingleOrMultiCall?` is the broadest return type, useful when the PSI
type is unknown.
