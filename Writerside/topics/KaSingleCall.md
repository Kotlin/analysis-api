# KaSingleCall

`KaSingleCall<S, C>` represents a single resolved callable applied at a call site. It is one branch of
[](KaSingleOrMultiCall.md); the other branch, [](KaMultiCall.md), describes compound and
desugared expressions.

`KaSingleCall` replaces the legacy `KaCallableMemberCall` as the conceptual base for "one resolved callable at this
site". All accessors are inline &mdash; there is no `partiallyAppliedSymbol` wrapper to drill through.

## Hierarchy

<code-block lang="mermaid">
graph TB
  KaSingleOrMultiCall
  KaSingleOrMultiCall --> KaSingleCall
  KaSingleCall --> KaFunctionCall
  KaSingleCall --> KaVariableAccessCall
  KaSingleCall --> KaCallableReferenceCall
  KaFunctionCall --> KaImplicitInvokeCall
  KaFunctionCall --> KaAnnotationCall
  KaFunctionCall --> KaDelegatedConstructorCall
</code-block>

## Members

`val signature: C`
: The substituted callable signature &mdash; parameter types for functions, return type for functions and properties.

`val dispatchReceiver: KaReceiverValue?`
: The dispatch receiver for this symbol access. Present when the callable is declared inside a class or object.
See [](Receivers.md).

`val extensionReceiver: KaReceiverValue?`
: The extension receiver. Present when the callable is declared with an extension receiver.

`val contextArguments: List<KaReceiverValue>`
: The [context parameters](https://github.com/Kotlin/KEEP/issues/367) for this symbol access.

`val typeArgumentsMapping: Map<KaTypeParameterSymbol, KaType>`
: Inferred and explicit type arguments. Keys are the signature's type parameters. May be empty on a resolution or
inference error.

### Helper extension

`val <S : KaCallableSymbol, C : KaCallableSignature<S>> KaSingleCall<S, C>.symbol: S`
: Short-cut for `signature.symbol` &mdash; the resolved callable symbol.

## Concrete subtypes

The concrete return types of the specialized `resolveCall(...)` methods all implement `KaSingleCall`:

* [](KaFunctionCall.md) and its subtypes ([](KaImplicitInvokeCall.md),
  [](KaAnnotationCall.md), [](KaDelegatedConstructorCall.md)).
* [](KaVariableAccessCall.md) for property and variable accesses.
* [](KaCallableReferenceCall.md) for callable references &mdash; the cleanest example of the
  new shape, extending `KaSingleCall<S, C>` only.

> The transitional subtypes `KaFunctionCall`, `KaVariableAccessCall`, `KaAnnotationCall`, and
> `KaDelegatedConstructorCall` still inherit `KaCallableMemberCall` from the [legacy hierarchy](Legacy-Resolution-API.md)
> &mdash; their `partiallyAppliedSymbol` and `argumentMapping` members are deprecated. New code should use the inline
> accessors documented here.
