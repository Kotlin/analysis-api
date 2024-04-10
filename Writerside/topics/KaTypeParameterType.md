# KaTypeParameterType

Represents a type parameter type, such as `T` in the declaration `class Box<T>(val element: T)`.

Can be created using [buildTypeParameterType](Types.md#building-type-parameter-types).

## Hierarchy

Inherits from [KaType](KaType.md).

## Members

`val name: Name`
: The type parameter name.

`val symbol: KaTypeParameterSymbol`
: The type parameter symbol.