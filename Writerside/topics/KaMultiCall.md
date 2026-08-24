# KaMultiCall

`KaMultiCall` represents a compound or desugared expression that resolves to multiple sub-calls. It is one branch of
[](KaSimpleOrMultiCall.md); the other branch, [](KaSimpleCall.md), describes a single
resolved callable.

A `KaMultiCall` is returned for the four desugared constructs Kotlin lowers into several operator calls:

* `for` loops &rarr; [](KaForLoopCall.md) (`iterator()`, `hasNext()`, `next()`).
* `by`-delegated properties &rarr; [](KaDelegatedPropertyCall.md)
  (`getValue()`, optionally `setValue()`, optionally `provideDelegate()`).
* Compound variable assignment and unary increment/decrement (`i += 1`, `i++`, `i--`) &rarr;
  [](KaCompoundVariableAccessCall.md) (the variable access plus the operator).
* Compound array access (`a[i] += v`) &rarr; [](KaCompoundArrayAccessCall.md)
  (`get()`, `set()`, plus the operator).

## Hierarchy

<code-block lang="mermaid">
graph TB
  KaSimpleOrMultiCall
  KaSimpleOrMultiCall --> KaMultiCall
  KaMultiCall --> KaForLoopCall
  KaMultiCall --> KaDelegatedPropertyCall
  KaMultiCall --> KaCompoundVariableAccessCall
  KaMultiCall --> KaCompoundArrayAccessCall
</code-block>

## Members

`val calls: List<KaSimpleCall<*, *>>`
: The non-empty list of [](KaSimpleCall.md)s discovered during resolution &mdash; the flat view of every
sub-call.

Each concrete subtype additionally exposes **named** sub-call accessors that describe each sub-call's role
(`iteratorCall`, `valueGetterCall`, `getterCall`, `setterCall`, `operationCall`, and so on). See the individual subtype
pages for the full list.

## Working with attempts

When you need to know *which* sub-calls resolved and *which* did not, use `tryResolveCall()` on the originating PSI
element. The resulting [](KaCallResolutionAttempt.md) is a
`KaMultiCallResolutionAttempt` (or one of its concrete subtypes) and exposes each sub-call attempt independently. The
assembled `KaMultiCall` is only available when every sub-attempt succeeded.

> Compound calls cover a "bunch of unrelated compound calls", so the client typically is not expected to handle every
> possible subtype. Prefer the specialized `resolveSuccessfulCall(...)` on the originating PSI element (e.g.
> `KtForExpression.resolveSuccessfulCall(): KaForLoopCall?`) when you know exactly which compound case you are dealing
> with.
