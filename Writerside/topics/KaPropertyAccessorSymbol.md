# KaPropertyAccessorSymbol

Represents a property [getter or setter](https://kotlinlang.org/docs/properties.html#getters-and-setters) declaration.

## Hierarchy

Inherits from [KaFunctionSymbol](KaFunctionSymbol.md).

Inheritors: `KaPropertyGetterSymbol` (for getters), `KaPropertySetterSymbol` (for setters).

## Members

`val isDefault: Boolean`
: `true` if the accessor is implicitly generated.

`val isInline: Boolean`
: `true` if the property is an inline property.

`val isOverride: Boolean`
: `true` if the property accessor is an override.

`val hasBody: Boolean`
: `true` if the property accessor has body. Such as, the following property has an explicit getter without a body:
: ```Kotlin
val name: String = "Foo"
    @Throws(RuntimeException::class) get
```

`val containingClassId: ClassId?`
: The fully-qualified name of a containing class, or `null` if the class is local.

## Default values

| Member              | Value                       |
|---------------------|-----------------------------|
| `contextReceivers`  | `emptyList()`               |
| `isExtension`       | `false`                     |
| `location`          | `KaSymbolLocation.PROPERTY` |
| `receiverParameter` | `null`                      |