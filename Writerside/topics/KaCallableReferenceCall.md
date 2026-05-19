# KaCallableReferenceCall

`KaCallableReferenceCall<S, C>` represents a resolved [callable reference](https://kotlinlang.org/docs/reflection.html#function-references)
to a function, property, or constructor.

```Kotlin
class A { fun foo() {} }

val unbound = A::foo         // unbound member function reference
val bound = A()::foo         // bound, with a dispatch receiver
fun topLevel() {}
val topLevelRef = ::topLevel // top-level function reference
val ctor = ::A               // constructor reference
```

A callable reference does **not** actually invoke the callable, so the result is leaner than other call types &mdash;
no value-argument mapping, no read/write access kind. Only the signature, bound receivers, and type-argument mapping.

`KaCallableReferenceCall` is the cleanest example of the new resolution shape. Unlike most other call types, it
extends [](KaSingleCall.md) only &mdash; there is no [legacy](Legacy-Resolution-API.md) `KaCallableMemberCall`
ancestor on this interface.

## Hierarchy

Inherits [](KaSingleCall.md).

## Members

`KaCallableReferenceCall` does not add new members beyond `KaSingleCall`. The relevant accessors are:

`val signature: C`
: The substituted signature of the referenced callable.

`val symbol: S`
: Helper extension &mdash; the referenced callable symbol.

`val dispatchReceiver: KaReceiverValue?`
: The bound dispatch receiver, if any (e.g. `A()::foo`).

`val extensionReceiver: KaReceiverValue?`
: The bound extension receiver, if any.

`val contextArguments: List<KaReceiverValue>`
: The bound context arguments, if any.

`val typeArgumentsMapping: Map<KaTypeParameterSymbol, KaType>`
: The type arguments of the reference.

## When to use it

`KtCallableReferenceExpression.resolveCall()` returns `KaCallableReferenceCall<*, *>?` directly. If you only need the
referenced declaration, `KtCallableReferenceExpression.resolveSymbol()` returns `KaCallableSymbol?` &mdash; the
shorter path.
