# Types

`KaType` is a fundamental concept in the Analysis API, representing types of Kotlin expressions and declarations. It
provides information about the type structure, nullability, and annotations.

## KaType Hierarchy

The `KaType` interface serves as the base for specific type kinds:

* [`KaClassType`](KaClassType.md): Represents types of classes, objects, and interfaces. This includes both named class
  types (e.g., `String`, `Int`) and types of anonymous objects. For function types like `(Int) -> String`, there is
  a [`KaFunctionType`](KaFunctionType.md) subtype.
* [`KaTypeParameterType`](KaTypeParameterType.md): Represents type parameter types, such as `T` in `class Box<T>()`.
* [`KaCapturedType`](KaCapturedType.md): Represents [captured types](https://kotlinlang.org/spec/type-system.html#type-capturing).
* [`KaDefinitelyNotNullType`](KaDefinitelyNotNullType.md): Represents a `T & Any` type.
* [`KaFlexibleType`](KaFlexibleType.md): Represents types with both a lower and upper bound, such as `String?`
  or `(Mutable)List<Int>`.
* [`KaIntersectionType`](KaIntersectionType.md): Represents types that are intersections of other types.
* [`KaDynamicType`](KaDynamicType.md): Represents dynamic types, used for interoperability with dynamically typed
  languages (e.g., JavaScript).
* [`KaErrorType`](KaErrorType.md): Represents unresolved types, providing information about the error.

## Example

The following example demonstrates how to obtain the `KaType` of a `KtExpression` and render its type:

```Kotlin
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
The Analysis API distinguishes between an expression's type and its expected type, which represent different aspects of
the Kotlin type system.

The <em>expression type</em> represents the actual type of an expression after it has been resolved. It reflects the
result of type inference, smart casts, and implicit conversions.

The <em>expected type</em> represents the type that is expected for an expression at a specific location in the code.
This is determined by the context in which the expression appears, such as a variable type for its initializer, or a
parameter type for a function call.
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

Comparing to `type1 == type2`, which only considers simple structural equivalence, `semanticallyEquals()` ensures
that `type1` can be substituted with `type2`.

### Subtyping check

To determine if one type is a subtype of another, use `isSubtypeOf`:

```kotlin
val subtype: KaType = ...
val supertype: KaType = ...

val isSubtype = subtype.isSubtypeOf(supertype)
```

## Building `KaType`s

The Analysis API provides facilities for constructing `KaType` instances, representing various Kotlin types.
The entry point for the type building DSL is `typeCreator` accessible directly inside the `analyze` block.

<warning> 
Type creation endpoints available directly inside the <code>analyze</code> block and starting with 'build' are obsolete and will be deprecated soon.
This includes:
 
- `buildClassType`
- `buildArrayType`
- `buildVarargArrayType`
- `buildTypeParameterType`
- `buildStarTypeProjection`

If you are still using them, migrate to the new type creation DSL. The former API lacks a wide set of features and containts some long-standing bugs.
</warning>

Here's how you can build different types:

### Building Class Types

To build a [](KaClassType.md), use the `typeCreator.classType` function. 
You can specify the target class either by its `ClassId` or using a [](KaClassLikeSymbol.md):

#### By a class ID:

```kotlin
analyze(ktFile) {
    val intType = typeCreator.classType(KaStandardTypeClassIds.INT)
}
```

<note>
If the provided <code>ClassId</code> doesn't resolve to a valid symbol, the <code>typeCreator.classType</code> function will
return an error type.
</note>

#### By a class symbol:

```kotlin
analyze(ktFile) {
    val listSymbol: KaClassLikeSymbol = ...
    val listOfStringType = typeCreator.classType(listSymbol) {
        invariantTypeArgument(builtinTypes.string)
    }
}
```

#### Specifying Type Arguments:

Within the `classType` block, you can specify type arguments using the `typeArgument` function. This function accepts
either a `KaTypeProjection` or a `KaType` and optionally its variance:

```kotlin
analyze(ktFile) {
    val mapType = typeCreator.classType(KaStandardTypeClassIds.MAP) { 
        typeArgument(Variance.IN_VARIANCE) { 
            builtinTypes.int
        }
        typeArgument(Variance.OUT_VARIANCE, builtinTypes.string)
    }
}
```

There is also `invariantTypeArgument` that allows adding a type argument with `Variance.INVARIANT`.
If the type expects more type arguments than provided, the remaining ones are filled with `KaStarTypeProjection` (`*`).
Excessive type arguments are discarded.

<note>
If you'd like to construct a type with default type arguments, use <code>KaClassifierSymbol.defaultType</code>.
You can also use <code>KaClassifierSymbol.defaultTypeWithStarProjections</code> as a shortcut for constructing a type with
all type arguments filled with <code>KaStarTypeProjection</code>.
</note>

#### Nullability:

You can also set the nullability of the constructed type by modifying the `isMarkedNullable` property within the builder:

```kotlin
analyze(ktFile) {
    val nullableStringType = typeCreator.classType(KaStandardTypeClassIds.STRING) {
        isMarkedNullable = true
    }
}
```

### Building Array Types

If you'd like to build an array type, you can still use `typeCreator.classType` with the desired array `ClassId`.
However, there is a more safe and convenient way to do it using `typeCreator.arrayType`:

```kotlin
analyze(ktFile) {
    val elementType: KaType = builtinTypes.int
    val nullableIntArrayWithOutVariance = typeCreator.arrayType(elementType) { 
        variance = Variance.OUT_VARIANCE
        isMarkedNullable = true
    }
}
```

By default, the builder constructs primitive array types when possible.
E.g., for the `Int` element type, `IntArray` is constructed instead of `Array<Int>`.
You can override this behavior by setting the `shouldPreferPrimitiveTypes` property within the builder to `false`.

**Note:** There is also a shortcut for constructing `vararg` array types, i.e.,
the underlying type of `vararg` function parameters with the given type.
You can use `typeCreator.varargArrayType` for that:
```kotlin
analyze(ktFile) {
    val elementType: KaType = builtinTypes.string
    val stringBoxedArrayType = typeCreator.varargArrayType(elementType)
}
```

### Building Function Types

[](KaFunctionType.md) can be constructed with `typeCreator.functionType`:

```kotlin
analyze(ktFile) { 
    val reflectFuctionType = typeCreator.functionType { 
        isReflectType = true
        valueParameter(Name.identifier("first")) {
            builtinTypes.int
        }
        returnType = builtinTypes.string 
    }
}
```

<note>
<code>KaFunctionType</code> is a <code>KaClassType</code> and can be constructed through <code>typeCreator.classType</code>.
However, not only is it inconvenient, but it's also unsafe.
That's because it requires manually providing a function type <code>ClassId</code> which can be affected by
various aspects like <code>suspend</code> / <code>reflect</code> flags and the number of parameters.
Additionally, some compiler plugins can register their own function <code>ClassId</code>s for some function annotations 
(e.g., <code>@Composable</code>). <code>typeCreator.functionType</code> handles all of these cases 
and constructs a refined <code>ClassId</code> for you.
</note>

#### Specifying Return Type

The return type is defined by `returnType`. By default, it's set to `Unit`.

```kotlin
analyze(ktFile) { 
    val functionReturningAny = typeCreator.functionType {
        returnType = builtinTypes.any 
    }

    val functionReturningUnit = typeCreator.functionType()
}
```

#### Specifying Parameters

The receiver type parameter can be set using `receiverType`. 
By default, it's set to `null` which indicates that the function is not an extension one.

```kotlin
analyze(ktFile) { 
    val extensionFunctionOnInt = typeCreator.functionType { 
        receiverType = builtinTypes.int
    }
}
```

Value parameters can be constructed using `valueParameter`.
The API accepts an optional name and a type for the produced parameter:

```kotlin
analyze(ktFile) { 
    val myFunction = typeCreator.functionType { 
        valueParameter(Name.identifier("first")) {
            classType(...) {
                ...
            }
        }
        valueParameter(null, builtinTypes.nullableAny)
    }
}
```

The builder supports experimental [context parameters](https://kotlinlang.org/docs/context-parameters.html) as well.
They can be added via `contextParameter` which accepts just a type:

```kotlin
analyze(ktFile) { 
    val myFunctionWithContextParameters = typeCreator.functionType {
        contextParameter {
            classType(...) {
                ...
            }
        }
        contextParameter(builtinTypes.int)
    }
}
```

**Note:** Kotlin prohibits context parameters in reflection types.
All context parameters passed to the builder are discarded when `isReflectType` is set to `true`.

#### Creating Suspending and Reflection Function Types

`typeCreator.functionType` allows specifying whether the produces `KaFunctionType` is a 
[suspending function type](https://kotlinlang.org/spec/asynchronous-programming-with-coroutines.html#suspending-functions)
or a [reflection function type](https://kotlinlang.org/docs/reflection.html#function-references).
This is controlled by `isSuspend` and `isReflectType` respectively, the defaults are set to `false`.

```kotlin
analyze(ktFile) { 
    val reflectFunctionType = typeCreator.functionType { 
        isReflectType = true
    }

    val suspendingFunctionType = typeCreator.functionType { 
        isSuspend = true
    }
}
```

**Note:** Kotlin prohibits context parameters in reflection types.
All context parameters passed to the builder are discarded when `isReflectType` is set to `true`.


### Building Type Parameter Types

To build a [](KaTypeParameterType.md), use the `typeCreator.typeParameterType` function. You need to provide the
corresponding [](KaTypeParameterSymbol.md):

```kotlin
analyze(ktFile) {
    val typeParameterSymbol: KaTypeParameterSymbol = ...
    val type = typeCreator.typeParameterType(typeParameterSymbol)
}
```

**Note:** Similar to class types, you can adjust the nullability of the type parameter type
by using `isMarkedNullable` within the builder.

### Building Definitely Not Null Types
[](KaDefinitelyNotNullType.md) can be constructed using `typeCreator.definitelyNotNullType`
by providing either a `KaCapturedType` or a `KaTypeParameterType`.

**Note:** If the original type was not nullable, `typeCreator.definitelyNotNullType` returns the original type
as no additional wrapping is required.

#### By a captured type {id="def-not-null-type-by-a-captured-type"}:
```kotlin
analyze(ktFile) {
    val capturedType: KaCapturedType = ...
    val definitelyNotNullParameterType = typeCreator.definitelyNotNullType(capturedType)
}
```

#### By a type parameter type:
```kotlin
analyze(ktFile) {
  val typeParameterType: KaTypeParameterType = ...
  val definitelyNotNullParameterType = typeCreator.definitelyNotNullType(typeParameterType)
}
```

### Building Intersection Types
[](KaIntersectionType.md) can be constructed using `typeCreator.intersectionType`
by building a list of conjuncts via `conjunct` and `conjuncts`:
```kotlin
analyze(ktFile) {
  val intersectionType = typeCreator.intersectionType {
    conjunct(builtinTypes.throwable)
    conjuncts(listOf(builtinTypes.int, builtinTypes.any))
    conjunct {
      arrayType(builtinTypes.char)
    }
    conjunct {
      dynamicType()
    }
  }
}
```

**Note:** The result of `typeCreator.intersectionType` is normalized, so it's not always a `KaIntersectionType`.
However, the resulting type is guaranteed to represent a subtype of all the passed conjuncts.

### Building Captured Types
[](KaCapturedType.md) can be constructed using `typeCreator.capturedType`
by providing either a [](KaTypeProjection.md) or another [](KaCapturedType.md):

#### By a captured type: {id="captured-type-by-a-captured-type"}
```kotlin
analyze(ktFile) {
    val capturedType: KaCapturedType = ...
    val capturedType = typeCreator.capturedType(capturedType) {
        isMarkedNullable = true
    }
}
```

#### By a type projection
```kotlin
analyze(ktFile) {
    val typeProjection: KaTypeProjection = ...
    val capturedType = typeCreator.capturedType(typeProjection)
}
```

**Note:** If the passed `KaTypeProjection` is a `KaTypeArgumentWithVariance`, its variance cannot be `Variance.INVARIANT`.
That's because captured types are intended to capture non-invariant projections.
Otherwise, an exception is thrown.

### Building Flexible Types
[](KaFlexibleType.md) can be constructed using `typeCreator.flexibleType` using three different ways.

If one of the provided bounds is a `KaFlexibleType`, the corresponding bound of this type is taken instead.
E.g., if the upper bound is a flexible type itself, then its upper bound is taken instead.

If the lower bound is not a subtype of the upper bound, `null` is returned.

If bounds are equal, then it's unnecessary to create a flexible type for them, so this bound type is returned instead.

#### By another flexible type
```kotlin
analyze(ktFile) {
    val anotherFlexibleType: KaFlexibleType = ...
    val flexibleType = typeCreator.flexibleType(anotherFlexibleType) {
        lowerBound = builtinTypes.int
    }
}
```

#### By providing bounds manually
```kotlin
analyze(ktFile) {
    val flexibleType = typeCreator.flexibleType(builtinTypes.int, builtinTypes.any)
}
```

#### By providing bounds in the builder
```kotlin
analyze(ktFile) {
    val flexibleType = typeCreator.flexibleType {
        lowerBound = arrayType(builtinTypes.int) {
            shouldPreferPrimitiveTypes = false
            isMarkedNullable = true
        }
        upperBound = builtinTypes.any
    }
}
```

### Building Dynamic Types
[](KaDynamicType.md) can be constructed using `typeCreator.dynamicType`:

```kotlin
analyze(ktFile) {
    val dynamicType = typeCreator.dynamicType()
}
```

### Building Annotated Types
Each type except for [](KaIntersectionType.md) can be constructed with additional annotations.
To add annotations to your type, call `annotation` or `annotations` with desired annotation `ClassId`s within the builder.
```kotlin
analyze(ktFile) {
    val myAnnotation: ClassId = ...
    val myAdditionalAnnotations: Iterable<ClassId> = ... 
    val dynamicType = typeCreator.dynamicType {
        annotation(myAnnotation)
        annotations(myAdditionalAnnotations)
    }
}
```

**Note:** At the moment, only annotations without value arguments are supported.
All annotations requiring arguments are discarded.