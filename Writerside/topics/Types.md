# Types

`KaType` is a fundamental concept in the Analysis API, representing types of Kotlin expressions and declarations.
It provides information about the type structure, nullability and annotations.

## KaType Hierarchy

The `KaType` interface serves as the base for specific type kinds:

* [`KaClassType`](KaClassType.md): Represents types of classes, objects and interfaces. This includes both named class types
  (e.g., `String`, `Int`) and types of anonymous objects. For function types like `(Int) -> String`, there is a
  [`KaFunctionType`](KaFunctionType.md) subtype.
* [`KaTypeParameterType`](KaTypeParameterType.md): Represents type parameter types, such as `T` in `class Box<T>()`.
* [`KaCapturedType`](KaCapturedType.md): Represents captured types, which occur when a type parameter is used with an upper bound.
* [`KaDefinitelyNotNullType`](KaDefinitelyNotNullType.md): Represents a `T & Any` type.
* [`KaFlexibleType`](KaFlexibleType.md): Represents types with both a lower and upper bound, such as `String?` or `(Mutable)List<Int>`.
* [`KaIntersectionType`](KaIntersectionType.md): Represents types that are intersections of other types.
* [`KaDynamicType`](KaDynamicType.md): Represents dynamic types, used for interoperability with dynamically typed languages (e.g.,
  JavaScript).
* [`KaErrorType`](KaErrorType.md): Represents unresolved types, providing information about the error.

## Example

The following example demonstrates how to obtain the `KaType` of a `KtExpression` and renders its type:

```kotlin
val expression: KtExpression = ...

analyze(expression) {
    val type = expression.expressionType
    if (type is KaClassType) {
        // Analyze the class type
        val className = type.classId.asSingleFqName().asString()
        println(className)
    }
}
```

Avoid using `FqName`s or raw strings for type comparison. Use `ClassId`s instead:

```Kotlin
val MY_CLASS_ID = ClassId.fromString("my/app/MyClass")

fun check(expression: KtExpression): Boolean {
    analyze(expression) {
        val type = expression.expressionType
        return type is KaClassType && type.isClassType(MY_CLASS_ID)
    }
}
```

## Getting a `KaType`

You have already seen how to get the expression type. Here is the complete list of utilities that convert either PSI or
symbols to types:

`val KtTypeReference.type: KaType`
: A resolved reference type.

`val KtExpression.expressionType: KaType?`
: The expression type, or `null` if the given expression does not contribute a value.
: Particularly, the method returns:
* A not-null type for valued expressions (e.g., a variable, a function call, a lambda expression);
* `Unit` for statements (e.g., assignments, loops);
* `null` for `KtExpression`s that are not a part of the expression tree (e.g., expressions in import or package statements).

`val PsiElement.expectedType: KaType?`
: The expected type for the given element, or `null` if the element does not have an expected type.
: The expected type is the type that the expression is expected to have in the context where it appears.

<note>
Analysis API distinguishes between an expression's type and its expected type, which represent different aspects of
the Kotlin type system.

The <em>expression type</em> represents the actual type of an expression after it has been resolved. It reflects the result
of type inference, smart casts and implicit conversions.

The <em>expected type</em> represents the type that is expected for an expression at a specific location in the code. This is
determined by the context in which the expression appears, such as a variable type for its initializer, or a parameter
type for a function call.
</note>

`val KtDeclaration.returnType: KaType`
: The return type of the given `KtDeclaration`.
: Note: For `vararg foo: T` parameter returns full `Array<out T>` type
(unlike `KaValueParameterSymbol.returnType`, which returns `T`).

`val KtFunction.functionType: KaType`
: The functional type of the given `KtFunction`.
: Depending on the function's attributes, such as `suspend` or reflective access, different functional type, 
such as `SuspendFunction`, `KFunction`, or `KSuspendFunction`, will be constructed.

`val KaNamedClassSymbol.defaultType: KaType`
: A class type where type parameters are substituted with matching type parameter types,
e.g. `List<T>` for the `List` class.

`val KtDoubleColonExpression.receiverType: KaType?`
: Receiver type of the `foo::bar` expression, or `null` if the expression is unresolved, or if the resolved
callable reference is not of a reflection type.

## Comparing `KaType`s

### Equivalence check

To check if two types are equivalent, use `semanticallyEquals()`:

```kotlin
val type1: KaType = ...
val type2: KaType = ...

val areEqual = type1.semanticallyEquals(type2)
```

Comparing to `type1 == type2` which only considers simple structural equivalence, `semanticallyEquals()` ensures that
`type1` can be substituted with `type2`.

### Subtyping check

To determine if one type is a subtype of another, use `isSubtypeOf`:

```kotlin
val subtype: KaType = ...
val supertype: KaType = ...

val isSubtype = subtype.isSubtypeOf(supertype)
```

## Building `KaType`s

The Analysis API provides facilities for constructing `KaType` instances, representing various Kotlin types.
Here's how you can build different types:

### Building Class Types

To build a class type, use the `buildClassType` function. You can specify the class either by its `ClassId` or using
a `KaClassLikeSymbol`:

#### By a class name:

```kotlin
analyze(ktFile) {
    val intType = buildClassType(DefaultTypeClassIds.INT)
}
```

#### By a class symbol:

```kotlin
analyze(ktFile) {
    val listSymbol: KaClassLikeSymbol = ...
    val listOfStringType = buildClassType(listSymbol) {
        argument(builtinTypes.STRING)
    }
}
```

<note>
If the provided <code>ClassId</code> doesn't resolve to a valid symbol, the <code>buildClassType</code> function will
return an error type.
</note>

#### Specifying Type Arguments:

Within the `buildClassType` block, you can specify type arguments using the `argument` function. This function accepts
either a `KaTypeProjection` or a `KaType` and optionally its variance:

```kotlin
analyze(ktFile) {
    val mapType = buildClassType(DefaultTypeClassIds.MAP) {
        argument(builtinTypes.INT, Variance.IN_VARIANCE)
        argument(builtinTypes.STRING, Variance.OUT_VARIANCE)
    }
}
```

#### Nullability:

You can also set the nullability of the constructed type by modifying the `nullability` property within the builder:

```kotlin
analyze(ktFile) {
    val nullableStringType = buildClassType(DefaultTypeClassIds.STRING) {
        nullability = KaTypeNullability.NULLABLE
    }
}
```

### Building Type Parameter Types

To build a type parameter type, use the `buildTypeParameterType` function. You need to provide the
corresponding `KaTypeParameterSymbol`:

```kotlin
analyze(ktFile) {
    val typeParameterSymbol: KaTypeParameterSymbol = ...
    val type = buildTypeParameterType(typeParameterSymbol)
}
```

**Note:** Similar to class types, you can adjust the nullability of the type parameter type within the builder.