# KaCompoundArrayAccessCall

`KaCompoundArrayAccessCall` represents a compound array-like access convention involving calls to both `get()` and
`set()`, e.g. `a[1] += "foo"`.

```Kotlin
fun test(m: MutableMap<String, String>) {
    m["a"] += "b"
}
```

The above desugars into `m.get("a").plus("b")` followed by `m.set("a", ...)`. The compound call captures all three
operator calls plus the index arguments.

> If the collection has an `<op>Assign` operator function (for example `MutableList.plusAssign`), the call is
> represented as a plain [](KaFunctionCall.md) instead.

## Hierarchy

Inherits [](KaMultiCall.md). (It also inherits the [legacy](Legacy-Resolution-API.md) `KaCall` for historical
reasons.)

## Members

`val getterCall: KaFunctionCall<KaNamedFunctionSymbol>`
: The `get` function call invoked when reading values corresponding to the given `indexArguments`.

`val setterCall: KaFunctionCall<KaNamedFunctionSymbol>`
: The `set` function call invoked when writing the computed value corresponding to the given `indexArguments`.

`val indexArguments: List<KtExpression>`
: The arguments representing the indices in the
[index access operator](https://kotlinlang.org/docs/operator-overloading.html#indexed-access-operator).

```Kotlin
m1["a"] += "b"   // a single index argument: "a"
m2[1, 5] += 12   // two index arguments: 1 and 5
```

`val compoundOperation: KaCompoundOperation`
: The compound operation kind. See [](KaCompoundOperation.md). `compoundOperation.operationCall`
gives the resolved operator function call (e.g. `String.plus` for `+=`); the operation call is also available directly
on the inherited `KaCompoundAccessCall.operationCall`.

`val getPartiallyAppliedSymbol: KaPartiallyAppliedFunctionSymbol<KaNamedFunctionSymbol>` &mdash; **deprecated**
: Legacy wrapper around the `get` function. Replaced by `getterCall`.

`val setPartiallyAppliedSymbol: KaPartiallyAppliedFunctionSymbol<KaNamedFunctionSymbol>` &mdash; **deprecated**
: Legacy wrapper around the `set` function. Replaced by `setterCall`.
