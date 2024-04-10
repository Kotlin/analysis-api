# KaEnumEntrySymbol

Represents an [enum entry](https://kotlinlang.org/docs/enum-classes.html) declaration.

<note>
In the Kotlin PSI, a <code>KtEnumEntry</code> is a <code>KtClass</code>, as it was so In the old compiler. 
In Analysis API, though, similarly to the K2 compiler, it is a <code>KaVariableSymbol</code>.
</note>

## Hierarchy

Inherits from [KaVariableSymbol](KaVariableSymbol.md).

## Members

`val enumEntryInitializer: KaEnumEntryInitializerSymbol?`
: The enum entry initializer, or `null` if the entry does not have a body.

## Default values

| Member              | Value                    |
|---------------------|--------------------------|
| `callableId`        | `null`                   |
| `contextReceivers`  | `emptyList()`            |
| `isExtension`       | `false`                  |
| `isVal`             | `true`                   |
| `location`          | `KaSymbolLocation.CLASS` |
| `receiverParameter` | `null`                   |