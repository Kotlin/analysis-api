# KaTypeParameterSymbol

Represents a type parameter of a class, function, property, or a type alias.

## Hierarchy

Inherits from [KaClassifierSymbol](KaClassifierSymbol.md).

## Members

`val name: Name`
: The declaration name.

`val upperBounds: List<KaType>`
: A list of upper bound types.

`val variance: Variance`
: The [declaration-site variance](https://kotlinlang.org/docs/generics.html#declaration-site-variance)
(invariant, covariant `out`, contravariant `in`).

`val isReified: Boolean`
: `true` if the type parameter has the `reified` modifier (applicable only to callable type parameters).