# KaNamedClassSymbol

Represents a named class, object, or interface declaration.
Basically, covers all class-like declarations, excluding anonymous objects.

## Use Cases

* **Checking for specific class features.** Use properties like `isData`, `isInner`, and `isCompanion` to determine if
  the class has specific characteristics.

Also see use cases for the [KaClassSymbol](KaClassSymbol.md#use-cases) supertype.

## Hierarchy

Inherits from [KaClassSymbol](KaClassSymbol.md).

## Members

`val name: Name`
: The simple declaration name, e.g., `String` for `kotlin.String`.

`val companionObject: KaNamedClassSymbol?`
: The nested companion object, or `null` if there is no companion object.

`val contextReceivers: List<KaContextReceiver>`
: A list of context receivers.
: **Experimental API**.

`val isExternal: Boolean`
: `true` if the declaration has the `external` modifier.

`val isData: Boolean`
: `true` if the declaration is a `data class`.

`val isInline: Boolean`
: `true` if the declaration is an `inline class`.

`val isFun: Boolean`
: `true` if the declaration is a `fun interface`.

`val isInner: Boolean`
: `true` if the declaration is an inner class.

`val typeParameters: List<KaTypeParameterSymbol>`
: A list of declared type parameters.

## Type utilities

`val KaNamedClassSymbol.defaultType: KaType`
: A class type where type parameters are substituted with matching type parameter types, e.g., `List<T>` for the `List`
class.

## Relation utilities

`val KaNamedClassSymbol.sealedClassInheritors: List<KaNamedClassSymbol>`
: Inheritors of the given sealed class.