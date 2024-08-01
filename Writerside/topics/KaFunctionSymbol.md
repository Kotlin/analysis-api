# KaFunctionSymbol

Represents a function-like declaration, including named and anonymous functions, constructors, and property accessors.

## Hierarchy

A sealed class.  
Inherits from [KaCallableSymbol](KaCallableSymbol.md).

Notable inheritors: [KaNamedFunctionSymbol](KaNamedFunctionSymbol.md), [KaConstructorSymbol](KaConstructorSymbol.md),
[KaPropertyAccessorSymbol](KaPropertyAccessorSymbol.md).

## Members

`val valueParameters: List<KaValueParameterSymbol>`
: A list of declared value parameters.

`val hasStableParameterNames: Boolean`
: `true` if the declaration has stable parameter names, so they can be used in a named parameter call syntax
(e.g., `User(name = "Joe")` instead of `User("Joe")`). Parameter names are always stable for Kotlin declarations, and
usually unstable for all other declaration sources.