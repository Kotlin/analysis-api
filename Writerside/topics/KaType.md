# KaType

Represents a Kotlin type. It serves as the base interface for various specific type.

## Hierarchy

Inherits from [KaAnnotated](Annotations.md#kaannotated).

## Members

`val abbreviation: KaUsualClassType?`
: The abbreviated type for the given expanded type, or `null` if this type has not been expanded, or the
abbreviated type cannot be resolved.
: An abbreviated type is an expanded type alias application. For example, if we have a type
alias `typealias MyString = String` and its application `MyString`, `String` would be the type alias expansion and `MyString` its
abbreviated type.

`val nullability: KaTypeNullability`
: The type nullability: `NULLABLE`, `NON_NULLABLE`, `UNKNOWN` (for flexible types).

## Subtypes

The `KtType` interface has several subtypes that represent different kinds of types in Kotlin:

* **KtClassType**: Represents a Kotlin class type, encompassing classes, interfaces, objects, and enum classes.
* **KtFunctionalType**: Represents Kotlin function types, including regular functions, suspend functions, and those with
  receivers.
* **KtTypeParameterType**: Represents a type parameter type, such as `T` in the
  declaration `class Box<T>(val element: T)`.
* **KtDefinitelyNotNullType**: Represents a type that is known to be non-nullable at a particular point in the program.
* **KtCapturedType**: Represents a type that is captured during type inference, often occurring when working with
  generics and variance.
* **KtFlexibleType**: Represents a type with flexibility in its bounds, commonly used for platform types or types with
  uncertain nullability.
* **KtIntersectionType**: Represents a type formed by the intersection of multiple types.
* **KtDynamicType**: Represents the dynamic type in Kotlin, used for interoperability with dynamically-typed languages
  or platforms.

## Transformation utilities

`val Iterable<KaType>.commonSupertype: KaType`
: The common super type of the given collection of [KaType]. The collection must not be empty.

`fun KaType.withNullability(newNullability: KaTypeNullability): KaType`
: Returns the given type with the modified nullability.

## Nullability utilities

`val KaType.canBeNull: Boolean`
: `true` if a public value of the given type can potentially be `null`.
: This means this type is not a subtype of [Any]. However, it does not mean one can assign `null` to a variable of this
type because it may be unknown if this type can accept `null`.

`val KaType.isMarkedNullable: Boolean`
: `true` if the given type is explicitly marked as nullable. This means it is safe to assign `null` to a variable with this type.

`val KaType.hasFlexibleNullability: Boolean`
: `true` if the given type is a flexible
([platform](https://kotlinlang.org/docs/java-interop.html#null-safety-and-platform-types)) type, can both safe and
ordinary calls are valid on it.

`fun KaType.upperBoundIfFlexible(): KaType`
: Returns the upper bound if the given type is a flexible type, and `null` otherwise.

`fun KaType.lowerBoundIfFlexible(): KaType`
: Returns the lower bound if the given type is a flexible type, and `null` otherwise.

## Type relation utilities

`fun KaType.semanticallyEquals(other: KaType, errorTypePolicy: KaSubtypingErrorTypePolicy = KaSubtypingErrorTypePolicy.STRICT): Boolean`
: Check semantic type equality. Returns `true` if the given type can be used instead of `other`.

`fun KaType.isSubtypeOf(supertype: KaType, errorTypePolicy: KaSubtypingErrorTypePolicy = KaSubtypingErrorTypePolicy.STRICT): Boolean`
: Check if the given type is a subtype of the `supertype`.

`fun KaType.isClassType(classId: ClassId): Boolean`
: `true` if the given type is a class type with the given `ClassId`, or its nullable version.

`fun KaType.hasCommonSubtypeWith(that: KaType): Boolean`
: Check whether the given type is compatible with the other type. Compatibility means the types can have a common subtype.

`val KaType.directSupertypes: Sequence<KaType>`
: Direct super types of the given type. For example, for `MutableList<String>` it will be `List<String>` and
`MutableCollection<String>`.

`val KaType.allSupertypes: Sequence<KaType>`
: All supertypes of the given type.

`val KaType.isArrayOrPrimitiveArray: Boolean`
: `true` if the given type is an array or a primitive array type.

`val KaType.isNestedArray: Boolean`
: `true` if the given type is an array or a primitive array type, and if its element is also an array type.

`val KaType.isPrimitive: Boolean`
: `true` if the given [KaType] is one of these types: `Byte`, `Short`, `Int`, `Long`, `Float`, `Double`, `Char`,
`Boolean`, or a nullable version of them.

`val KaType.isAnyType`<br/>
`val KaType.isNothingType`<br/>
`val KaType.isUnitType`<br/>
`val KaType.isByteType`<br/>
`val KaType.isUByteType`<br/>
`val KaType.isShortType`<br/>
`val KaType.isUShortType`<br/>
`val KaType.isIntType`<br/>
`val KaType.isUIntType`<br/>
`val KaType.isLongType`<br/>
`val KaType.isULongType`<br/>
`val KaType.isFloatType`<br/>
`val KaType.isDoubleType`<br/>
`val KaType.isCharType`<br/>
`val KaType.isBooleanType`<br/>
`val KaType.isCharSequenceType`<br/>
`val KaType.isStringType`
: `true` if the given type is the specified Kotlin type or its nullable version.

`val KaType.isFunctionalInterface: Boolean`
: `true` if the given type is a functional interface type (SAM type), e.g., `Runnable`.

`val KaType.isFunctionType: Boolean`
: `true` if this type is a `kotlin.Function` type.

`val KaType.isKFunctionType: Boolean`
: `true` if this type is a `kotlin.reflect.KFunction` type.

`val KaType.isSuspendFunctionType: Boolean`
: `true` if this type is a `kotlin.coroutines.SuspendFunction` type.

`val KaType.isKSuspendFunctionType: Boolean`
: `true` if this type is a `kotlin.reflect.KSuspendFunction` type.

`val KaType.functionTypeKind: FunctionTypeKind?`
: The `FunctionTypeKind` of the given type, or `null` if the type is not a function type.
: **Experimental API**.

## Scope utilities

`val KaType.scope: KaTypeScope?`
: Return a `KaTypeScope` for a given type. The type scope includes all members which are declared and callable on a given type.
: Comparing to a `KaScope`, in the `KaTypeScope` all use-site type parameters are substituted.
: **Experimental API**.

`val KaType.syntheticJavaPropertiesScope: KaTypeScope?`
: A `KaTypeScope` with synthetic Java properties created for a given type.

## Other utilities

`val builtinTypes: KaBuiltinTypes`
: An instance providing access to all built-in Kotlin types, including number types, `Any`, `Nothing`, `String`
and others.

`val KaType.arrayElementType: KaType?`
: The array element type for a primitive type array or `Array`, `null` otherwise.

`val KaType.expandedSymbol: KaClassSymbol?`
: The class symbol backing the given type, or `null` if the type has no expansion.

`val KaType.fullyExpandedType: KaType`
: The type with type aliases recursively expanded.

`val KaType.isDenotable: Boolean`
: `true` if this type is denotable. In other words, it can be written in Kotlin by a developer. Flexible type is an
example of a non-denotable type.

`val KaType.enhancedType: KaType?`
: The warning-level enhanced type for the given type, or `null` if it is absent.
: **Experimental API**.

`val KaType.enhancedTypeOrSelf: KaType?`
: The warning-level enhanced type for the given type, or the given type itself if it is absent.
: **Experimental API**.

`fun KaType.render(renderer: KaTypeRenderer = KaTypeRendererForSource.WITH_QUALIFIED_NAMES, position: Variance): String`
: Render the given type to a `String`. The particular rendering strategy is defined by the `renderer`.
: **Experimental API**.