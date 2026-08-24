# KaSimpleOrMultiCall

`KaSimpleOrMultiCall` is the sealed return type of `resolveSuccessfulCall()`. The type system splits resolved calls into
two shapes:

* [](KaSimpleCall.md) &mdash; a simple call: a single resolved callable applied at this site. Most everyday call sites
  (function invocations, property accesses, callable references, annotation entries, supertype calls) return this.
* [](KaMultiCall.md) &mdash; a compound or desugared expression that resolves to several sub-calls. This is
  what `for` loops, delegated properties, compound assignments (`+=`, `++`, `--`), and compound array access
  (`a[i] += v`) return.

## Hierarchy

<code-block lang="mermaid">
graph TB
  KaSimpleOrMultiCall
  KaSimpleOrMultiCall --> KaSimpleCall
  KaSimpleOrMultiCall --> KaMultiCall
</code-block>

## Helper extensions

Two extension properties give a uniform view across both branches:

`val KaSimpleOrMultiCall.calls: List<KaSimpleCall<*, *>>`
: The flattened list of simple calls. Returns `listOf(this)` for a `KaSimpleCall`; returns `KaMultiCall.calls` for a
`KaMultiCall`.

`val KaSimpleOrMultiCall.symbols: List<KaSymbol>`
: The flattened list of symbols across every contained `KaSimpleCall`. Convenient when you only care about *who* was
called and not about the call structure.

## Narrowing to a concrete call

Four more extension properties narrow a call to the shape you are interested in and return `null` when it has a
different one. They replace the `as?` casts that reading a result used to require:

`val KaSimpleOrMultiCall.simple: KaSimpleCall<*, *>?`
: The call as a [](KaSimpleCall.md), or `null` for a `KaMultiCall`.

`val KaSimpleOrMultiCall.function: KaFunctionCall<*>?`
: The call as a [](KaFunctionCall.md), or `null` if it is not a call to a function.

`val KaSimpleOrMultiCall.variable: KaVariableAccessCall?`
: The call as a [](KaVariableAccessCall.md), or `null` if it is not an access to a variable.

`val KaSimpleOrMultiCall.constructor: KaFunctionCall<KaConstructorSymbol>?`
: The call as a constructor call, or `null` if it is not one. Unlike `function`, this cannot be a plain type check:
constructor calls are spread over `KaAnnotationCall`, `KaDelegatedConstructorCall`, and plain `KaFunctionCall`s whose
type argument is erased, so the resolved symbol is inspected instead.

They compose with the attempt-level `single` / `successful` properties, which is how the API is meant to be read:

```Kotlin
// the resolved function call, or null if resolution failed
val resolved = expression.resolveSuccessfulCall()?.function

// also the sole candidate of a failed call
val candidate = expression.tryResolveCall()?.single?.function

// the called symbol, whatever kind of simple call this is
val symbol = expression.resolveSuccessfulCall()?.simple?.symbol
```

## When the type system narrows the result

Many specialized `resolveSuccessfulCall(...)` methods commit to one branch in their return type:

* `KtForExpression.resolveSuccessfulCall(): KaForLoopCall?` &mdash; always a `KaMultiCall`.
* `KtPropertyDelegate.resolveSuccessfulCall(): KaDelegatedPropertyCall?` &mdash; always a `KaMultiCall`.
* `KtCallElement.resolveSuccessfulCall(): KaFunctionCall<*>?` &mdash; always a `KaSimpleCall`.
* `KtAnnotationEntry.resolveSuccessfulCall(): KaAnnotationCall?` &mdash; always a `KaSimpleCall`.

The generic `KtResolvableCall.resolveSuccessfulCall(): KaSimpleOrMultiCall?` is the broadest return type, useful when
the PSI type is unknown.
