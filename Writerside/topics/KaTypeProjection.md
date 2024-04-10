# KaTypeProjection

`KaTypeProjection` represents a type argument used in the context of a class or function type. It provides information
about the type and its variance.

## Members

`val type: KaType?`
: The projected type, or `null` for the star projection.

## Subclasses

### `KtStarTypeProjection`

Represents a [star projection](https://kotlinlang.org/docs/generics.html#star-projections) (`*`) used in type arguments.
It indicates that the specific type is not important or unknown.

### `KaTypeArgumentWithVariance`

Represents a type argument with an explicit type and
[variance](https://kotlinlang.org/docs/generics.html#use-site-variance-type-projections).

`val type: KaType`
: The projected type.

`val variance: Variance`
: The `Variance` of the type argument. It can be:
* `OUT_VARIANCE`: The type argument is used as a "covariant", `out` type parameter.
* `IN_VARIANCE`: The type argument is used as a "contravariant", `in` type parameter.
* `INVARIANT`: The type argument is used as an "invariant" type parameter.