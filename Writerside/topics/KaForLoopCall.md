# KaForLoopCall

`KaForLoopCall` represents a resolved `for` loop. A `for` loop desugars into three operator calls on the iterable
expression and its iterator:

```Kotlin
for (item in list) {
    println(item)
}
```

Desugared form:

```Kotlin
val iterator = list.iterator()
while (iterator.hasNext()) {
    val item = iterator.next()
    println(item)
}
```

`KaForLoopCall` is the assembled multi-call obtained from `KtForExpression.resolveCall(): KaForLoopCall?`. For
per-sub-call inspection (including partial failure handling), use the matching attempt type
`KaForLoopCallResolutionAttempt` documented under [](KaCallResolutionAttempt.md).

## Hierarchy

Inherits [](KaMultiCall.md).

## Members

`val iteratorCall: KaFunctionCall<KaNamedFunctionSymbol>`
: The `iterator()` call invoked on the loop range expression.

`val hasNextCall: KaFunctionCall<KaNamedFunctionSymbol>`
: The `hasNext()` call invoked on the iterator.

`val nextCall: KaFunctionCall<KaNamedFunctionSymbol>`
: The `next()` call invoked on the iterator.

All three sub-calls are full [](KaFunctionCall.md) instances and expose the usual call-site context
(`signature`, `dispatchReceiver`, `extensionReceiver`, type arguments, value-argument mapping). Through
[KaMultiCall.calls](KaMultiCall.md) you can also access the flat list of sub-calls.
