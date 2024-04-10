# KaBackingFieldSymbol

Represents a [backing field](https://kotlinlang.org/docs/properties.html#backing-fields) declaration.

## Hierarchy

Inherits from [KaVariableSymbol](KaVariableSymbol.md).

## Members

`val owningProperty: KaKotlinPropertySymbol`
: The owning property declaration.

## Default values

| Member              | Value                                   |
|---------------------|-----------------------------------------|
| `callableId`        | `null`                                  |
| `contextReceivers`  | `emptyList()`                           |
| `isExtension`       | `false`                                 |
| `isVal`             | `true`                                  |
| `name`              | `"field"`                               |
| `location`          | `KaSymbolLocation.PROPERTY`             |
| `receiverParameter` | `null`                                  |
| `origin`            | `KaSymbolOrigin.PROPERTY_BACKING_FIELD` |