# KaTypeAliasSymbol

Represents a type alias declaration.

## Hierarchy

Inherits from [KaClassLikeSymbol](KaClassLikeSymbol.md).

## Members

`val name: Name`
: The simple type alias declaration name.

`val expandedType: KaType`
: The type from right-hand site of the type alias. If the given type alias has type parameters,
those type parameters will be present in the result type.

`val typeParameters: List<KaTypeParameterSymbol>`
: A list of declared type parameters.