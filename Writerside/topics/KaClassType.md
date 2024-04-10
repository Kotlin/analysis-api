# KaClassType

Represents a Kotlin generic class type, such as `String`, `List<Int>`, or a function type (like `(String) -> Int`). 

Can be created using [buildClassType](Types.md#building-class-types).

## Hierarchy

Inherits from [KaType](KaType.md).

Notable subtypes: [KaUsualClassType](KaUsualClassType.md) for non-function types and [KaFunctionType](KaFunctionType.md)
for function types.

## Members

`val symbol: KaClassLikeSymbol`
: The class for which the given type is built.

`val classId: ClassId`
: The qualified name of the class.

`val typeArguments: List<KaTypeProjection>`
: A list of type arguments.