# KaIntersectionType

Represents an [intersection type](https://kotlinlang.org/spec/type-system.html#intersection-types).

Can be constructed using [typeCreator.intersectionType](Types.md#building-intersection-types).

## Hierarchy

Inherits from [KaType](KaType.md).

## Members

`val conjuncts: List<KaType>`
: A list of individual types participating in the intersection.