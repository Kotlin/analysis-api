# KaValueParameterSymbol

Represents a value parameter of a function, constructor, and a property setter.

In Kotlin, we generally use the phrase "value parameter", as function have both value and 
[type parameters](KaTypeParameterSymbol.md).

## Hierarchy

Inherits from [KaVariableSymbol](KaVariableSymbol.md).

## Members

`val name: Name`
: The value parameter name.

`val isNoinline: Boolean`
: `true` if the value parameter has the
[`noinline`](https://kotlinlang.org/docs/inline-functions.html#noinline) modifier.

`val isCrossinline: Boolean`
: `true` if the value parameter has the
[`crossinline`](https://kotlinlang.org/docs/inline-functions.html#non-local-returns) modifier.

`val hasDefaultValue: Boolean`
: `true` if the parameter has the default value.

`val isVararg: Boolean`
: `true` if the parameter has the `vararg` modifier.

`val isImplicitLambdaParameter: Boolean`
: `true` if the parameter is the implicitly generated `it` lambda parameter.

## Default values

| Member              | Value                    |
|---------------------|--------------------------|
| `callableId`        | `null`                   |
| `contextReceivers`  | `emptyList()`            |
| `isExtension`       | `false`                  |
| `isVal`             | `true`                   |
| `location`          | `KaSymbolLocation.LOCAL` |
| `receiverParameter` | `null`                   |