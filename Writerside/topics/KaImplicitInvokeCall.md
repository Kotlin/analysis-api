# KaImplicitInvokeCall

`KaImplicitInvokeCall` represents an [implicit `invoke` operator call](https://kotlinlang.org/docs/operator-overloading.html#invoke-operator)
&mdash; a call on a value whose type has an `invoke` member function.

```Kotlin
interface Foo {
    operator fun <T> invoke(t: T)
}

fun test(f: Foo) {
    f("str")
//  ^^^^^^^^
}
```

`f("str")` is the implicit form of `f.invoke("str")` and resolves to a `KaImplicitInvokeCall`.

## Hierarchy

Inherits [](KaFunctionCall.md) (`KaImplicitInvokeCall : KaFunctionCall<KaNamedFunctionSymbol>`).

## Detecting an implicit invoke

`KaImplicitInvokeCall` does not add new members beyond `KaFunctionCall`. The intended use is a type check:

```Kotlin
val call: KaFunctionCall<*>? = callElement.resolveCall()
if (call is KaImplicitInvokeCall) {
    handleImplicitInvoke(call)
}
```

This replaces the deprecated `KaSimpleFunctionCall.isImplicitInvoke` boolean from the
[legacy API](Legacy-Resolution-API.md).
