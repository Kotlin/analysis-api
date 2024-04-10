# KaConstructorSymbol

Represents a class [constructor](https://kotlinlang.org/docs/classes.html#constructors) declaration.

## Hierarchy

Inherits from [KaFunctionSymbol](KaFunctionSymbol.md).

## Members

`val isPrimary: Boolean`
: `true` if the constructor is a primary constructor.

`val containingClassId: ClassId?`
: The fully-qualified name of a containing class, or `null` if the class is local.

## Default values

| Member              | Value                    |
|---------------------|--------------------------|
| `callableId`        | `null`                   |
| `contextReceivers`  | `emptyList()`            |
| `isExtension`       | `false`                  |
| `location`          | `KaSymbolLocation.CLASS` |
| `receiverParameter` | `null`                   |
