# KaFunctionCall

`KaFunctionCall<S>` represents a call to a function within Kotlin code &mdash; regular functions, constructors,
superclass constructors, and annotations.

## Hierarchy

Inherits [](KaSingleCall.md). (For historical reasons it also inherits the
[legacy](Legacy-Resolution-API.md) `KaCallableMemberCall`; new code should treat `KaFunctionCall` as a `KaSingleCall`
and use the inline accessors documented there.)

The following subtypes commit to a specific kind of function call:

* [](KaImplicitInvokeCall.md) &mdash; an implicit `invoke` call.
* [](KaAnnotationCall.md) &mdash; a call to an annotation constructor.
* [](KaDelegatedConstructorCall.md) &mdash; a `this(...)` or `super(...)` delegation.

## Members

In addition to the [](KaSingleCall.md) members (`signature`, `dispatchReceiver`, `extensionReceiver`,
`contextArguments`, `typeArgumentsMapping`), `KaFunctionCall` adds argument mappings.

`val valueArgumentMapping: Map<KtExpression, KaVariableSignature<KaValueParameterSymbol>>`
: A mapping from the call's argument expressions to their associated parameter symbols in a stable order. In case of
`vararg` parameters, multiple arguments may be mapped to the same `KaValueParameterSymbol`.

`val contextArgumentMapping: Map<KtExpression, KaVariableSignature<KaContextParameterSymbol>>`
: A mapping from the call's [explicit context argument](https://github.com/Kotlin/KEEP/blob/main/proposals/KEEP-0448-explicit-context-arguments.md)
expressions to their associated context parameter symbols in a stable order.

`val combinedArgumentMapping: Map<KtExpression, KaVariableSignature<KaParameterSymbol>>`
: A combined mapping from the call's argument expressions to their associated parameter symbols in a stable order.
Includes both `valueArgumentMapping` and `contextArgumentMapping`. In case of `vararg` parameters, multiple arguments
may be mapped to the same `KaValueParameterSymbol`.

`val argumentMapping: Map<KtExpression, KaVariableSignature<KaValueParameterSymbol>>` &mdash; **deprecated**
: Use `valueArgumentMapping` (only value arguments) or `combinedArgumentMapping` (value + context arguments).
