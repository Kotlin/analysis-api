# KaFunctionCall

`KaFunctionCall` represents a call to a function within Kotlin code. This includes calls to regular functions,
constructors, constructors of super classes, and annotations.

## Hierarchy

Inherits [KaCallableMemberCall](KaCallableMemberCall.md).

## Members

`valueArgumentMapping: Map<KtExpression, KaVariableSignature<KaValueParameterSymbol>>`
: A mapping from the call's argument expressions to their associated parameter symbols in a stable order. 
In case of `vararg`parameters, multiple arguments may be mapped to the same `KaValueParameterSymbol`

`contextArgumentMapping: Map<KtExpression, KaVariableSignature<KaContextParameterSymbol>>`
: A mapping from the call's [explicit context argument](https://github.com/Kotlin/KEEP/blob/main/proposals/KEEP-0448-explicit-context-arguments.md)
expressions to their associated context parameter symbols in a stable order.

`combinedArgumentMapping: Map<KtExpression, KaVariableSignature<KaParameterSymbol>>`
: A combined mapping from the call's argument expressions to their associated parameter symbols in a stable order. 
This includes both `valueArgumentMapping` and `contextArgumentMapping`.
In case of `vararg` parameters, multiple arguments may be mapped to the same `KaValueParameterSymbol`.