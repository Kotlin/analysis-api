# Resolving Symbols

**Symbol resolution** answers *"what declaration does this PSI element refer to?"*. The result is the literal target
of the element &mdash; a class, function, property, type parameter, package, or any other declaration. Read
[](Resolution-Fundamentals.md) first if you have not.

> Snippets on this page assume an `analyze { }` block (or `context(_: KaSession)`) is in scope and that
> `@OptIn(KaExperimentalApi::class)` is applied somewhere up the call chain. Snippets that name the
> `KtResolvable` marker interface additionally require `@OptIn(KtExperimentalApi::class)`.

## Entry points

For a given resolvable PSI element, prefer the **specialized** form &mdash; an extension on the concrete PSI type with a
precisely typed return value:

```Kotlin
val constructor: KaConstructorSymbol? = annotationEntry.resolveSymbol()
val function: KaFunctionSymbol? = callElement.resolveSymbol()
val classifier: KaClassifierSymbol? = typeReference.resolveSymbol()
```

When the PSI type is unknown, fall back to the generic form on `KtResolvable` via a safe cast:

```Kotlin
val symbol: KaSymbol? =
    (element as? KtResolvable)?.resolveSymbol()
val symbols: Collection<KaSymbol> =
    (element as? KtResolvable)?.resolveSymbols().orEmpty()
```

`resolveSymbol()` returns the single resolved symbol, or `null` if resolution failed or produced more than one
candidate. `resolveSymbols()` returns every resolved symbol &mdash; useful when ambiguity is acceptable.
For the richest form (success / error / diagnostic / candidate symbols), use `tryResolveSymbols()` and the
[](KaSymbolResolutionAttempt.md) hierarchy.

## Specialized methods

Each row below is an extension defined on the listed PSI type. The return type is precisely the kind of symbol that
the element can refer to.

### Symbols of callables and constructors

| PSI element                                      | Returns                       |
|--------------------------------------------------|-------------------------------|
| `KtAnnotationEntry`                              | `KaConstructorSymbol?`        |
| `KtSuperTypeCallEntry`                           | `KaConstructorSymbol?`        |
| `KtConstructorDelegationCall`                    | `KaConstructorSymbol?`        |
| `KtConstructorDelegationReferenceExpression`     | `KaConstructorSymbol?`        |
| `KtConstructorCalleeExpression`                  | `KaConstructorSymbol?`        |
| `KtCallElement`                                  | `KaFunctionSymbol?`           |
| `KtReturnExpression`                             | `KaFunctionSymbol?`           |
| `KtCallableReferenceExpression`                  | `KaCallableSymbol?`           |
| `KtQualifiedExpression`                          | `KaCallableSymbol?`           |
| `KtDestructuringDeclarationEntry`                | `KaCallableSymbol?`           |
| `KtArrayAccessExpression`                        | `KaNamedFunctionSymbol?`      |
| `KtCollectionLiteralExpression`                  | `KaNamedFunctionSymbol?`      |
| `KtWhenConditionInRange`                         | `KaNamedFunctionSymbol?`      |

### Symbols of classifiers and labels

| PSI element                                      | Returns                       |
|--------------------------------------------------|-------------------------------|
| `KtTypeReference`                                | `KaClassifierSymbol?`         |
| `KtNullableType`                                 | `KaClassifierSymbol?`         |
| `KtFunctionType`                                 | `KaClassSymbol?`              |
| `KtClassLiteralExpression`                       | `KaClassifierSymbol?`         |
| `KtSuperTypeEntry`                               | `KaClassifierSymbol?`         |
| `KtDelegatedSuperTypeEntry`                      | `KaClassifierSymbol?`         |
| `KtEnumEntrySuperclassReferenceExpression`       | `KaNamedClassSymbol?`         |
| `KtLabelReferenceExpression`                     | `KaDeclarationSymbol?`        |
| `KtInstanceExpressionWithLabel`                  | `KaDeclarationSymbol?`        |

`KtUserType` does not have a specialized `resolveSymbol()` extension. It implements `KtResolvable`, so the generic
form applies &mdash; with the broader return type `KaSymbol?`. See the [Type-side resolution](#type-side-resolution)
section below for the user-type subtleties (including resolution to a `KaPackageSymbol` for qualified-path prefixes).

A few of these also expose a call counterpart (for example `KtCallElement` &rarr; `resolveCall(): KaFunctionCall<*>?`).
See [](Resolving-Calls.md) for the call-side specializations.

## `resolveSymbol` shows the literal target

The defining principle of symbol resolution: **the symbol is what the element itself refers to**, not what is *invoked*
at that site. The clearest illustration is `KtNameReferenceExpression`.

```Kotlin
class MyClass
object MyObject

val c = MyClass()
//      ^^^^^^^  resolveSymbol() returns the class `MyClass`

val o = MyObject
//      ^^^^^^^^ resolveSymbol() returns the object `MyObject`
```

For `MyClass()`, the name reference `MyClass` literally points to the class, so `resolveSymbol()` returns a
`KaClassLikeSymbol` for `MyClass`. The constructor that is actually invoked only shows up in
[call resolution](Resolving-Calls.md), because invoking a class means calling its constructor.

> The constructor/class split is intentional and documented directly on `KtNameReferenceExpression` as an
> *Analysis API Resolver Note*:
>
> > Unlike other `KtResolvableCall` entry points that provide both `resolveCall` and `resolveSymbol` specializations,
> > `KtNameReferenceExpression.resolveCall` may return a different `KaSymbol`. For instance, this happens for
> > constructor references. While `resolveCall` returns a `KaConstructorSymbol`, this method returns the corresponding
> > `KaClassLikeSymbol`.

A `KtNameReferenceExpression` can also resolve to a type, not just a callable &mdash; this is why the generic
return type is `KaSymbol?` rather than `KaCallableSymbol?`.

## Type-side resolution

Symbol resolution is the only resolution flavor that applies to *types*. `KtTypeReference`, `KtUserType`,
`KtNullableType`, `KtFunctionType`, and `KtClassLiteralExpression` all support `resolveSymbol()` but no `resolveCall()`.
Of these, only `KtUserType` lacks a specialized return type &mdash; it reuses the generic `KtResolvable.resolveSymbol()`.

For a well-formed type the result is a `KaClassifierSymbol`. For a `KtFunctionType`, the result is the corresponding
`FunctionN` / `SuspendFunctionN` class &mdash; the return type is narrowed to `KaClassSymbol?`.

`KtUserType` delegates to its inner simple-name reference, so calling `resolveSymbol()` on a user type returns the
same symbol as resolving the inner expression. One subtlety, documented as an *Analysis API Resolver Note* on
`KtUserType` itself:

> A `KtUserType` may also resolve to a `KaPackageSymbol` when it appears as the package qualifier of a fully qualified
> nested type. In that case the user type is not a classifier reference itself but a package portion of one:
>
> ```Kotlin
> val foo: one.two.TopLevel = TODO()
> //       ^^^^^^^             package `one.two`
> //       ^^^                 package `one`
> //               ^^^^^^^^    class `one.two.TopLevel`
> ```

When walking type references, expect `KaPackageSymbol` and handle it explicitly.

## Plain form vs try form

Use `resolveSymbol()` / `resolveSymbols()` when you only care about a valid result and want failed/ambiguous resolutions
to be silently dropped. This is the right default for inspections that must not produce false positives.

Use `tryResolveSymbols()` when you want everything the compiler considered. The result is a
`KaSymbolResolutionAttempt` carrying success, error, or compound-error variants &mdash; with diagnostics and candidate
symbols. See [](KaSymbolResolutionAttempt.md) for the full breakdown.

```Kotlin
val attempt = element.tryResolveSymbols() ?: return
// every symbol the compiler considered
val allSymbols = attempt.symbols
// empty on error
val onlySuccessful = attempt.successfulSymbols
```

The two helpers `KaSymbolResolutionAttempt.symbols` and `KaSymbolResolutionAttempt.successfulSymbols` cover the most
common access patterns without forcing pattern matching on the sealed hierarchy.
