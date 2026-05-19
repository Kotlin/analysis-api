# KaDelegatedPropertyCall

`KaDelegatedPropertyCall` represents a resolved `by`-delegated property. The Kotlin compiler desugars a delegated
property into up to three operator calls:

```Kotlin
val name: String by lazy { "John" }
```

Desugared form (conceptually):

```text
val name$delegate = lazy { "John" }
val name: String get() = name$delegate.getValue(thisRef, property)
```

For a `var` property a `setValue()` call is also generated. If the delegate expression provides a `provideDelegate()`
operator, it is called first.

`KaDelegatedPropertyCall` is the assembled multi-call returned from
`KtPropertyDelegate.resolveCall(): KaDelegatedPropertyCall?`. For per-sub-call inspection (and partial-failure
handling), use `KaDelegatedPropertyCallResolutionAttempt` documented under
[](KaCallResolutionAttempt.md).

## Hierarchy

Inherits [](KaMultiCall.md).

## Members

`val valueGetterCall: KaFunctionCall<KaNamedFunctionSymbol>`
: The `getValue()` operator call on the delegate object.

`val valueSetterCall: KaFunctionCall<KaNamedFunctionSymbol>?`
: The `setValue()` operator call. `null` for `val` properties.

`val provideDelegateCall: KaFunctionCall<KaNamedFunctionSymbol>?`
: The `provideDelegate()` operator call. `null` when the delegate does not provide that operator.

Each non-null sub-call is a full [](KaFunctionCall.md) and exposes the call-site context as usual.
[KaMultiCall.calls](KaMultiCall.md) gives a flat list of all present sub-calls.
