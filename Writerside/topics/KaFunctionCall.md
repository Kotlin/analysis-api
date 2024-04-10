# KaFunctionCall

`KaFunctionCall` represents a call to a function within Kotlin code. This includes calls to regular functions,
constructors, constructors of super classes, and annotations.

## Hierarchy

Inherits [KaCallableMemberCall](KaCallableMemberCall.md).

## Members

`val argumentMapping: Map<KtExpression, KaVariableSignature<KaValueParameterSymbol>>`
: A map associating argument expressions with the corresponding parameter signatures.