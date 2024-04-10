# KaPropertySymbol

Represents a property declaration.

## Hierarchy

Inherits from [KaVariableSymbol](KaVariableSymbol.md).

## Members

`val typeParameters: List<KaTypeParameterSymbol>`
: A list of declared type parameters.

`val initializer: KaInitializerValue?`
: The property initializer.

`val hasGetter: Boolean`
: `true` if the property has a getter.

`val getter: KaPropertyGetterSymbol?`
: The property getter.

`val hasSetter: Boolean`
: `true` if the property has a setter.

`val setter: KaPropertySetterSymbol?`
: The property setter.

`val hasBackingField: Boolean`
: `true` if the property has a backing field.

`val backingFieldSymbol: KaBackingFieldSymbol?`
: The backing field symbol.

`val isDelegatedProperty: Boolean`
: `true` if the property has a delegate.

`val isFromPrimaryConstructor: Boolean`
: `true` if the property is defined in a class primary constructor.

`val isOverride: Boolean`
: `true` if the property is an override.

`val isStatic: Boolean`
: `true` if the property is static.

## Utilities

`val KaPropertySymbol.getterDeprecationStatus: DeprecationInfo?`
: Deprecation status for the property getter, or `nil` if the getter is not deprecated.
: **Experimental API**.

`val KaPropertySymbol.setterDeprecationStatus: DeprecationInfo?`
: Deprecation status for the property setter, or `nil` if the getter is not deprecated.
: **Experimental API**.