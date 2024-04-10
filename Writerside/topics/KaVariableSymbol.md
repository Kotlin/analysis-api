# KaVariableSymbol

Represents a variable-like declaration, including properties, local variables, and value parameters.

## Hierarchy

A sealed class.  
Inherits from [KaCallableSymbol](KaCallableSymbol.md).

Notable inheritors: [KaPropertySymbol](KaPropertySymbol.md), [KaValueParameterSymbol](KaValueParameterSymbol.md).

## Members

`val name: Name`
: The declaration name.

`val isVal: Boolean`
: `true` if the declaration is read-only (is not marked with `var`).