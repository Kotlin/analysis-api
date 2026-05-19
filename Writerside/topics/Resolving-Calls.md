# Resolving Calls

**Call resolution** answers *"how is this expression executed at this site &mdash; which callable, applied to which
receivers, type arguments, and value arguments?"*. Read [](Resolution-Fundamentals.md) first if
you have not.

> Snippets on this page assume an `analyze { }` block (or `context(_: KaSession)`) is in scope and that
> `@OptIn(KaExperimentalApi::class)` is applied somewhere up the call chain. Snippets that name the
> `KtResolvableCall` marker interface additionally require `@OptIn(KtExperimentalApi::class)`.

## Entry points

For a given resolvable PSI element, prefer the **specialized** form &mdash; an extension on the concrete PSI type with
a precisely typed return value:

```Kotlin
val callForFunction: KaFunctionCall<*>? =
    callElement.resolveCall()

val callForAnnotation: KaAnnotationCall? =
    annotationEntry.resolveCall()

val callForArray: KaFunctionCall<KaNamedFunctionSymbol>? =
    arrayAccess.resolveCall()

val callForRef: KaCallableReferenceCall<*, *>? =
    callableReference.resolveCall()

val loop: KaForLoopCall? = forExpression.resolveCall()

val delegate: KaDelegatedPropertyCall? =
    propertyDelegate.resolveCall()
```

When the PSI type is unknown, fall back to the generic form on `KtResolvableCall` via a safe cast:

```Kotlin
val call: KaSingleOrMultiCall? =
    (element as? KtResolvableCall)?.resolveCall()
```

For the rich form, use `tryResolveCall()` and the [](KaCallResolutionAttempt.md) hierarchy.

## Specialized methods

| PSI element                                      | Returns                                          |
|--------------------------------------------------|--------------------------------------------------|
| `KtCallElement`                                  | `KaFunctionCall<*>?`                             |
| `KtAnnotationEntry`                              | `KaAnnotationCall?`                              |
| `KtSuperTypeCallEntry`                           | `KaFunctionCall<KaConstructorSymbol>?`           |
| `KtConstructorDelegationCall`                    | `KaDelegatedConstructorCall?`                    |
| `KtConstructorDelegationReferenceExpression`     | `KaDelegatedConstructorCall?`                    |
| `KtConstructorCalleeExpression`                  | `KaFunctionCall<KaConstructorSymbol>?`           |
| `KtEnumEntrySuperclassReferenceExpression`       | `KaDelegatedConstructorCall?`                    |
| `KtCallableReferenceExpression`                  | `KaCallableReferenceCall<*, *>?`                 |
| `KtArrayAccessExpression`                        | `KaFunctionCall<KaNamedFunctionSymbol>?`         |
| `KtCollectionLiteralExpression`                  | `KaFunctionCall<KaNamedFunctionSymbol>?`         |
| `KtWhenConditionInRange`                         | `KaFunctionCall<KaNamedFunctionSymbol>?`         |
| `KtNameReferenceExpression`                      | `KaSingleCall<*, *>?`                            |
| `KtQualifiedExpression`                          | `KaSingleCall<*, *>?`                            |
| `KtDestructuringDeclarationEntry`                | `KaSingleCall<*, *>?`                            |
| `KtForExpression`                                | `KaForLoopCall?`                                 |
| `KtPropertyDelegate`                             | `KaDelegatedPropertyCall?`                       |

## What `resolveCall()` returns

The result is a `KaSingleOrMultiCall?` &mdash; sealed into two branches:

* [](KaSingleCall.md) describes a single resolved callable applied at this site. This is what you get for
  ordinary function calls, property accesses, callable references, annotation entries, supertype calls, and so on.
* [](KaMultiCall.md) describes a compound or desugared call that involves several sub-calls. This is what
  you get for `for` loops, delegated properties, compound assignments (`+=`, `++`, `--`), and compound array access
  (`a[i] += v`).

The type system tells you which branch you are on. Many specializations narrow the return further &mdash; for instance
`KtForExpression.resolveCall(): KaForLoopCall?` already commits to the multi-call branch.

> `KaCall` and `KaCallableMemberCall` are the *legacy* base types of the resolution API. New code should rely on
> `KaSingleOrMultiCall` / `KaSingleCall` / `KaMultiCall`. See [](Legacy-Resolution-API.md).

## Working with a `KaSingleCall`

Every `KaSingleCall<S, C>` exposes the call-site context inline &mdash; no `partiallyAppliedSymbol` wrapper to drill
through:

```Kotlin
val call: KaSingleCall<*, *> = TODO()
val signature = call.signature             // callable signature
val symbol    = call.symbol                // signature.symbol
val dispatch  = call.dispatchReceiver      // member receiver
val extension = call.extensionReceiver     // extension receiver
val contexts  = call.contextArguments      // KEEP-367 ctx params
val typeArgs  = call.typeArgumentsMapping  // inferred + explicit
```

Concrete subtypes add their own fields. `KaFunctionCall<S>` adds the argument mappings:

```Kotlin
val call: KaFunctionCall<*> = callElement.resolveCall() ?: return
val valueArgs   = call.valueArgumentMapping    // value arguments
val contextArgs = call.contextArgumentMapping  // KEEP-0448 ctx args
val combined    = call.combinedArgumentMapping // values + ctx
```

`KaVariableAccessCall` adds the access kind: `call.kind` is a `KaVariableAccessCall.Kind.Read` or
`KaVariableAccessCall.Kind.Write` &mdash; the latter exposes `value: KtExpression?`, the right-hand side of the
assignment. The boolean `call.isContextSensitive` indicates whether
[context-sensitive resolution](https://github.com/Kotlin/KEEP/issues/379) was used.

[](KaCallableReferenceCall.md) is the cleanest example of the new shape: it extends
`KaSingleCall<S, C>` only &mdash; no legacy base. A callable reference does not invoke the callable, so there is no
`valueArgumentMapping` and no read/write kind &mdash; only the signature, bound receivers, and type arguments.

Use `call is KaImplicitInvokeCall` to detect implicit `f("...")` invocations on values with a functional type. The
legacy `KaSimpleFunctionCall.isImplicitInvoke` boolean is deprecated.

### `KtNameReferenceExpression` on a constructor reference

The call counterpart of a name reference can return a *different* symbol from the symbol counterpart. For
`MyClass()` the name `MyClass` literally points to the class (`resolveSymbol()` returns the `KaClassLikeSymbol`), but
the call wraps the constructor that is actually invoked:

```Kotlin
class MyClass
val c = MyClass()
//      ^^^^^^^  resolveCall()   -> KaFunctionCall<...>
//      ^^^^^^^  resolveSymbol() -> class `MyClass`
```

Pick the one that matches your question: *who is invoked here* &rarr; `resolveCall()`; *what does the name literally
mean* &rarr; `resolveSymbol()`.

## Compound and desugared calls

Some Kotlin constructs desugar into several operator calls. The Analysis API exposes the assembled multi-call and the
individual sub-calls through dedicated `KaMultiCall` subtypes. The names of the sub-calls match what the language spec
calls them.

### `for` loops

```Kotlin
for (item in list) {
    println(item)
}
```

A `for` loop desugars into `iterator()`, `hasNext()`, and `next()`. The call is a [](KaForLoopCall.md):

```Kotlin
val loop = forExpression.resolveCall() ?: return
val iter:    KaFunctionCall<KaNamedFunctionSymbol> = loop.iteratorCall
val hasNext: KaFunctionCall<KaNamedFunctionSymbol> = loop.hasNextCall
val next:    KaFunctionCall<KaNamedFunctionSymbol> = loop.nextCall
```

The richer form is `KtForExpression.tryResolveCall(): KaForLoopCallResolutionAttempt?`, which exposes each sub-call
attempt separately &mdash; if one of `iterator()` / `hasNext()` / `next()` fails to resolve, the others remain
available.

### Delegated properties

```Kotlin
val name: String by lazy { "John" }
```

A delegated property desugars into `getValue()`, optionally `setValue()` (for `var`), and optionally `provideDelegate()`.
The call is a [](KaDelegatedPropertyCall.md):

```Kotlin
val delegate = propertyDelegate.resolveCall() ?: return
// KaFunctionCall<KaNamedFunctionSymbol>
val getter  = delegate.valueGetterCall
// null for `val`
val setter  = delegate.valueSetterCall
// null if not applicable
val provide = delegate.provideDelegateCall
```

The matching attempt type is `KaDelegatedPropertyCallResolutionAttempt`.

### Compound variable access (`+=`, `++`, `--`)

```Kotlin
var i = 0
i += 1
i++
```

A compound assignment or unary increment on a variable resolves to a `KaCompoundVariableAccessCall`:

```Kotlin
val call: KaCompoundVariableAccessCall = TODO()
// the variable read/write
val variable: KaVariableAccessCall = call.variableCall
// the `plus` / `inc` / ...
val operator: KaFunctionCall<KaNamedFunctionSymbol> =
    call.operationCall

when (val op = call.compoundOperation) {
    is KaCompoundAssignOperation -> {
        // PLUS_ASSIGN, MINUS_ASSIGN, TIMES_ASSIGN,
        // DIV_ASSIGN, REM_ASSIGN
        op.kind
        op.operand    // right-hand-side expression
    }
    is KaCompoundUnaryOperation -> {
        op.kind          // INC or DEC
        op.precedence    // PREFIX or POSTFIX
    }
}
```

> An `<op>Assign` operator like `MutableList.plusAssign` is represented as a plain `KaFunctionCall`, not a
> `KaCompoundVariableAccessCall`. Only the three-step read-modify-write form (the `plus` + write path) is a compound
> call.

### Compound array access (`a[i] += v`)

```Kotlin
m["a"] += "b"
```

The most elaborate compound is the array form, represented by `KaCompoundArrayAccessCall`. It involves both `get` and
`set`, plus the operator function:

```Kotlin
val call: KaCompoundArrayAccessCall = TODO()

val getter: KaFunctionCall<KaNamedFunctionSymbol> =
    call.getterCall

val setter: KaFunctionCall<KaNamedFunctionSymbol> =
    call.setterCall

val operator: KaFunctionCall<KaNamedFunctionSymbol> =
    call.operationCall

val indices: List<KtExpression> = call.indexArguments
```

The matching attempt is `KaCompoundArrayAccessCallResolutionAttempt` with `getterCallAttempt`, `operationCallAttempt`,
and `setterCallAttempt`.

> The `KtOperationReferenceExpression` for `+=` follows a deliberate convention, documented as an
> *Analysis API Resolver Note* on `KtOperationReferenceExpression`:
>
> > The resolver targets symbols contributed by the operation reference itself.
> >
> > For compound cases, this includes the symbols corresponding to the resulting update, but not the symbols used only
> > for intermediate reads.
> >
> > For instance, in compound array assignments this includes the operator symbol (e.g., `plus`) and the writing accessor
> > (`set`), but not the reading accessor (`get`).
> >
> > If the reading symbol is also needed, the API should be called on the parent expression (e.g., `KtBinaryExpression`
> > or `KtUnaryExpression`).
>
> The new compound call types expose `getterCall` / `setterCall` / `operationCall` directly, so you usually do not need
> to call `resolveSymbol()` on the operation reference at all. Reach for the parent expression only when you specifically
> want both reading and writing symbols.

### A flat view of the sub-calls

Every `KaMultiCall` also exposes `calls: List<KaSingleCall<*, *>>`. If you do not care which sub-call is which, this is
the simplest accessor:

```Kotlin
val flat: List<KaSingleCall<*, *>> = (call as KaMultiCall).calls
```

## Plain form vs try form

Use `resolveCall()` when you only need a valid result; resolution failure becomes `null`. Use `tryResolveCall()` when
you want the diagnostic and the candidate calls the compiler considered. The richer form returns a
`KaCallResolutionAttempt` &mdash; see [](KaCallResolutionAttempt.md) for the full hierarchy and
helpers.

```Kotlin
val attempt = callElement.tryResolveCall() ?: return
// single resolved call, or null
val resolved = attempt.successfulCall
// success: one call; error: candidate calls
val everything = attempt.calls
```

For compound expressions, the multi-attempt types (`KaForLoopCallResolutionAttempt`,
`KaDelegatedPropertyCallResolutionAttempt`, `KaCompoundVariableAccessCallResolutionAttempt`,
`KaCompoundArrayAccessCallResolutionAttempt`) keep each sub-call attempt addressable, so you can still inspect the
sub-calls that did resolve when another sub-call failed.
