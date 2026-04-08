# Migrating from the Former Type-Building API

If you are still using former type creation endpoints available directly inside the `analyze` block
and starting with `build`:

- `buildClassType`
- `buildArrayType`
- `buildVarargArrayType`
- `buildTypeParameterType`
- `buildStarTypeProjection`

then please migrate to the new API that's available through `typeCreator` (see [](Types.md#building-katypes)).
The former one is obsolete and will be deprecated soon.

For most endpoints, the migration is straightforward and doesn't require any additional workload:
- `buildArrayType` can be safely replaced with `typeCreator.arrayType` (see [](Types.md#building-array-types)).
- `buildVarargArrayType` can be safely replaced with `typeCreator.varargArrayType` (see [](Types.md#building-array-types)).
- `buildTypeParameterType` can be safely replaced with `typeCreator.typeParameterType` (see [](Types.md#building-type-parameter-types)).
- `buildStarTypeProjection` can be safely replaced with `typeCreator.starTypeProjection` (see [](Types.md#building-star-projections)).

The only functional difference between them is that the new type-building API
[allows putting annotations](Types.md#building-annotated-types) on the constructed types.

## Migrating from `buildClassType`

Usages of `buildClassType` require special attention.
The main difference between `buildClassType` and `typeCreator.classType` is the way they handle type arguments.
If the constructed type requires type arguments and none are provided in the builder,
`buildClassType` doesn't fill these missing arguments and constructs an invalid type.
`typeCreator.classType`, on the other hand, fills these missing arguments with `KaStarTypeProjection` (`*`).

Take a look at the following example:
```kotlin
analyze(ktFile) {
    val pairClassId = ClassId.fromString("kotlin/Pair")
    val formerApi = buildClassType(pairClassId)
    val newApi = typeCreator.classType(pairClassId)
}
```

Here we are trying to contruct a class type for `kotlin.Pair<A, B>`.
It requires two type arguments; however, we haven't provided any.
`buildClassType(pairClassId)` constructs an incorrect type `Pair` that has no type arguments.
Note that this type is valid from the Analysis API perspective, i.e., it's not `KaErrorType`, however,
it still lacks essential type arguments.

`typeCreator.classType(pairClassId)` constructs `Pair<*, *>` instead, so all type arguments are taken into account.

Note that excessive type arguments are discarded in both cases:
```kotlin
analyze(ktFile) {
    val pairClassId = ClassId.fromString("kotlin/Pair")
    val formerApi = buildClassType(pairClassId) {
        repeat(3) {
            argument(buildStarTypeProjection())
        }
    }
    val newApi = typeCreator.classType(pairClassId) {
        repeat(3) {
            typeArgument(starTypeProjection())
        }
    }
}
```
Both API calls from the example above produce the exact same type `kotlin.Pair<*, *>`.

The migration approach here depends on the desired behavior:
- If you'd like to construct a type with default type arguments from a class symbol, then you can use `KaClassifierSymbol.defaultType`.
  E.g., for `kotlin.Pair` it produces `kotlin.Pair<A, B>`. The nullability can be adjusted with `KaType.withNullability`.
  With a `ClassId`, the easiest way is to use `findClassLike(classId).defaultType`.
  However, if you need to only partially preserve original type parameters, then you can use `typeCreator.classType` and fill the arguments manually:
  ```kotlin
  analyze(ktFile) {
      val symbol: KaClassLikeSymbol = ...
      typeCreator.classType(symbol) {
          // Just the first two default type arguments
          symbol.typeParameters.take(2).forEach { typeParameter ->
              invariantTypeArgument(typeParameter.defaultType)
          }
  
          invariantTypeArgument {
              ...
          }
      }
  }
  ```
- If you'd like to construct a type with star projections used as type arguments, call `KaClassifierSymbol.defaultTypeWithStarProjections`.
  If you only have a `ClassId`, then the easiest way is to just call `typeCreator.classType(classId)` without registering any type arguments.
  When some selected type arguments need custom types, use `typeCreator.classType` and only register arguments that you need:
  ```kotlin
  analyze(ktFile) {
      val symbol: KaClassLikeSymbol = ...
      typeCreator.classType(symbol) {
          typeArgument(starTypeProjection())
          // Providing a custom type just for the second type argument
          invariantTypeArgument { 
              ...
          }
          // The rest is filled with `*`
      }
  }
  ```

## Migrating from Workarounds
Type creation facilities offered within `typeCreator` also provide endpoints for new types that weren't supported by the former API.

For example, this includes `typeCreator.functionType` that allows constructing [](KaFunctionType.md).
Previously, a common workaround was to build it through `buildClassType` as `KaFunctionType` is a `KaClassType`.
However, it's unsafe and inconvenient. Such calls should be transformed to `typeCreator.functionType`, see [](Types.md#building-function-types).

Some other workarounds include creating a `KtTypeCodeFragment` with some code producing the desired type and then
getting the `KaType` of the corresponding expression.
New type building endpoints support the construction of all possible `KaType`s.
All such workarounds became redundant and should be replaced with proper calls to `typeCreator`.