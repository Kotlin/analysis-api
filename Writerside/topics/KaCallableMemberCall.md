# KaCallableMemberCall

## Hierarchy

Inherits [KaCall](KaCall.md).

## Members

`val partiallyAppliedSymbol: KaPartiallyAppliedSymbol<S, C>`
: A symbol wrapper, containing substituted declaration signature (parameter types for functions, return type for
functions and properties), and the actual dispatch receiver.

`val typeArgumentsMapping: Map<KaTypeParameterSymbol, KaType>`
: A map containing type arguments, including the inferred ones.