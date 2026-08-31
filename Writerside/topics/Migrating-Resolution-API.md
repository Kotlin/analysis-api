# Migrating from the Legacy Resolution API

The Analysis API resolution surface was redesigned as part of [KT-66039](https://youtrack.jetbrains.com/issue/KT-66039).
This guide maps the old API to the new one. If you are not yet familiar with the new shape, read
[](Resolution-Fundamentals.md) first &mdash; this guide assumes you know the old API.

> Snippets on this page assume an `analyze { }` block (or `context(_: KaSession)`) is in scope and that
> `@OptIn(KaExperimentalApi::class)` is applied somewhere up the call chain. Snippets that name the
> `KtResolvable` / `KtResolvableCall` marker interfaces additionally require `@OptIn(KtExperimentalApi::class)`,
> since those interfaces themselves are annotated `@KtExperimentalApi`.

## Why the API changed

Five user-facing pains motivated the redesign:

1. **`KtReference` was a PSI/IDE infrastructure leak.** It belongs to IntelliJ infrastructure, yet the Analysis API
   required reaching for `element.mainReference.resolveTo...()`, smuggling a syntax-layer concept into the semantic
   contract.
2. **Discoverability suffered.** To resolve via the Analysis API, you first had to know to call `.mainReference` on a
   `KtElement` and then invoke `resolveTo...()` on the resulting `KtReference`. Nothing about the API surface advertised
   this idiom, so callers who did not already know it fell back to the more familiar
   `PsiReference.resolve()` instead.
3. **Result types were under-specified.** `resolveToSymbol()` returned `KaSymbol?` everywhere; `resolveToCall()`
   returned a `KaCallInfo?` over a generic `KaCall`. Callers had to `as?`-cast to anything specific.
4. **`KaPartiallyAppliedSymbol` was a useless wrapper.** Receivers, signature, and type-argument mapping had to be
   unwrapped through an extra layer. The new `KaSimpleCall` exposes all of this inline; the new compound calls expose
   named sub-call accessors (`variableCall`, `getterCall`, `setterCall`, `operationCall`).
5. **`KtElement.resolveToCall` accepted any `KtElement`.** Nothing in the type told you whether resolution would succeed
   or what it would return. `KtReference` filled the gap for everything `resolveToCall` could not handle &mdash; so
   callers had to maintain two parallel resolution mechanisms.

The new API replaces both `KtReference`-based resolution and `KtElement.resolveToCall` with a single, type-driven
surface: specialized `resolveSuccessfulSymbol` / `resolveSuccessfulCall` methods on concrete PSI types, plus the marker
interfaces `KtResolvable` and `KtResolvableCall` for the generic case.

## Migration rules

Two rules cover almost all sites:

1. **Use the specialized method on the concrete PSI type whenever possible.** If you know the element is a
   `KtCallElement`, write `callElement.resolveSuccessfulCall()` &mdash; you get back a `KaFunctionCall<*>?`
   directly. Each specialization narrows the return type, so type checks and casts you used to write disappear.
2. **When the PSI type is genuinely unknown, narrow with a safe `as?` cast.** To check whether the element implements
   `KtResolvable` or `KtResolvableCall`.

```Kotlin
// Specialized form (preferred)
val call: KaFunctionCall<*>? = callElement.resolveSuccessfulCall()

// Generic form (only when the element type is unknown)
val call: KaSimpleOrMultiCall? =
    (element as? KtResolvableCall)?.resolveSuccessfulCall()
```

## Old &rarr; new matrix

### Result wrapper: `KaCallInfo` &rarr; `KaCallResolutionAttempt`

`resolveToCall()` returned a `KaCallInfo`; `tryResolveCall()` returns a `KaCallResolutionAttempt`. The hierarchies line
up one-to-one, but the new one carries `KaSimpleCall<*, *>` payloads instead of bare `KaCall`, and splits simple-call
attempts from multi-call ones (compound / `for` / delegated property).

| Old (`KaCallInfo`)                                               | New (`KaCallResolutionAttempt`)                                                                                                |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `KaCallInfo`                                                     | `KaCallResolutionAttempt` (`KaSimpleCallResolutionAttempt` / `KaMultiCallResolutionAttempt`)                                   |
| `KaSuccessCallInfo`                                              | `KaSimpleCallResolutionSuccess`                                                                                                      |
| `KaSuccessCallInfo.call: KaCall`                                 | `KaSimpleCallResolutionSuccess.call: KaSimpleCall<*, *>` (or the `attempt.successful: KaSimpleOrMultiCall?` extension)               |
| `KaErrorCallInfo`                                                | `KaSimpleCallResolutionError`                                                                                                        |
| `KaErrorCallInfo.candidateCalls: List<KaCall>`                   | `KaSimpleCallResolutionError.candidateCalls: List<KaSimpleCall<*, *>>`                                                               |
| `KaErrorCallInfo.diagnostic`                                     | `KaSimpleCallResolutionError.diagnostic`                                                                                             |
| `KaCallInfo.calls: List<KaCall>`                                 | `KaCallResolutionAttempt.calls: List<KaSimpleOrMultiCall>`                                                                     |
| `KaCallInfo.singleCallOrNull<T>()` / `successfulCallOrNull<T>()` | `attempt.single` / `attempt.successful`, narrowed with `.simple` / `.function` / `.variable` / `.constructor`                  |

Multi-call attempts (`KaForLoopCallResolutionAttempt`, `KaDelegatedPropertyCallResolutionAttempt`,
`KaCompound*CallResolutionAttempt`) expose `call: KaMultiCall?` plus per-step
`attempts: List<KaSimpleCallResolutionAttempt>`; the old `KaCallInfo` had no equivalent &mdash; these calls were
resolved indirectly.

### Call hierarchy: `KaCall` &rarr; `KaSimpleOrMultiCall`

A successful resolution used to hand back a `KaCall`; now it hands back a `KaSimpleOrMultiCall`. `KaFunctionCall` and
`KaVariableAccessCall` keep their names but are now `KaSimpleCall`s (so their data is inline &mdash; see below);
compound, `for`-loop, and delegated-property calls are `KaMultiCall`s.

| Old (`KaCall`)                                                  | New (`KaSimpleOrMultiCall`)                                                                    |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| `KaCall`                                                        | `KaSimpleOrMultiCall`                                                                          |
| `KaCallableMemberCall<S, C>`                                    | `KaSimpleCall<S, C>` (its `partiallyAppliedSymbol.*` members are now inline &mdash; see below) |
| `KaCompoundVariableAccessCall` / `KaCompoundArrayAccessCall`    | same names, now `KaMultiCall`s (`.calls: List<KaSimpleCall<*, *>>`)                            |
| *(no first-class type)* &mdash; `for`-loop / delegated property | `KaForLoopCall` / `KaDelegatedPropertyCall` (`KaMultiCall`s)                                   |
| *(no first-class type)* &mdash; callable references             | `KaCallableReferenceCall` (`KaSimpleCall`)                                                     |

### Candidate hierarchy: `KaCallCandidateInfo` &rarr; `KaCallCandidate`

`collectCallCandidates()` (was `resolveToCallCandidates()`) returns `KaCallCandidate`s instead of `KaCallCandidateInfo`
s. The hierarchy is identical; only the names change and `candidate` widens from `KaCall` to `KaSimpleOrMultiCall`.

| Old (`KaCallCandidateInfo`)                  | New (`KaCallCandidate`)                          |
|----------------------------------------------|--------------------------------------------------|
| `KaCallCandidateInfo`                        | `KaCallCandidate`                                |
| `KaCallCandidateInfo.candidate: KaCall`      | `KaCallCandidate.candidate: KaSimpleOrMultiCall` |
| `KaCallCandidateInfo.isInBestCandidates`     | `KaCallCandidate.isInBestCandidates` (unchanged) |
| `KaApplicableCallCandidateInfo`              | `KaApplicableCallCandidate`                      |
| `KaInapplicableCallCandidateInfo`            | `KaInapplicableCallCandidate`                    |
| `KaInapplicableCallCandidateInfo.diagnostic` | `KaInapplicableCallCandidate.diagnostic`         |

### Calls

| Old call                                                                                                     | New equivalent                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `KtElement.resolveToCall(): KaCallInfo?`                                                                     | `KtResolvableCall.tryResolveCall(): KaCallResolutionAttempt?`, but `resolveSuccessfulCall()` is preferred and more convenient in most cases.                                               |
| `KaCallInfo.{successfulFunctionCallOrNull, successfulVariableAccessCall, successfulConstructorCallOrNull}()` | `attempt.successful?.function` / `?.variable` / `?.constructor`, but in most cases `KaCallResolutionAttempt` is not needed. Call `resolveSuccessfulCall()` directly.                       |
| `KaCallInfo.singleCallOrNull<T>()` / `singleFunctionCallOrNull()` / ...                                      | `attempt.single`, narrowed with `.simple` / `.function` / `.variable` / `.constructor`.                                                                                                    |
| `KtElement.resolveToCallCandidates(): List<KaCallCandidateInfo>`                                             | `KtResolvableCall.collectCallCandidates(): List<KaCallCandidate>`.                                                                                                                         |

> **`resolveSuccessfulCall()` vs `tryResolveCall()` vs `collectCallCandidates()`.** `resolveSuccessfulCall()` returns
> only the successfully resolved (most-specific) call, or `null`. To inspect the candidate calls of an *unresolved or
> ambiguous* call (the old `KaCallInfo.calls`), use `tryResolveCall()?.calls`. To inspect *all* overload-resolution
> candidates (the old `resolveToCallCandidates()`), use `collectCallCandidates()`.

> The result of `tryResolveCall` and `resolveToCall` are equivalent in all cases (`tryResolveCall` may carry
> more detailed diagnostics on an error call).

### Inline access on a `KaSimpleCall`

Every `*PartiallyAppliedSymbol` access becomes a direct field on the call.

| Old call (legacy member on `KaCallableMemberCall`) | New equivalent (inline on `KaSimpleCall`) |
|----------------------------------------------------|-------------------------------------------|
| `call.partiallyAppliedSymbol.signature`            | `call.signature`                          |
| `call.partiallyAppliedSymbol.symbol`               | `call.symbol`                             |
| `call.partiallyAppliedSymbol.dispatchReceiver`     | `call.dispatchReceiver`                   |
| `call.partiallyAppliedSymbol.extensionReceiver`    | `call.extensionReceiver`                  |
| `call.partiallyAppliedSymbol.contextArguments`     | `call.contextArguments`                   |

### Subtypes you may have used

| Legacy type / member                                                | Replacement                                                                                        |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `KaSimpleFunctionCall`                                              | `KaFunctionCall<*>`                                                                                |
| `KaSimpleFunctionCall.isImplicitInvoke`                             | `call is KaImplicitInvokeCall`                                                                     |
| `KaSimpleVariableAccessCall`                                        | `KaVariableAccessCall`                                                                             |
| `KaSimpleVariableAccess` / `KaSimpleVariableAccess.Read` / `.Write` | `KaVariableAccessCall.Kind` / `KaVariableAccessCall.Kind.Read` / `KaVariableAccessCall.Kind.Write` |

### Compound calls (`+=`, `++`, `--`, `a[i] += v`, `by`, `for`)

| Old call                                                      | New equivalent                                                                                                          |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| `KaCompoundVariableAccessCall.variablePartiallyAppliedSymbol` | `variableCall: KaVariableAccessCall`                                                                                    |
| `KaCompoundArrayAccessCall.getPartiallyAppliedSymbol`         | `getterCall: KaFunctionCall<KaNamedFunctionSymbol>`                                                                     |
| `KaCompoundArrayAccessCall.setPartiallyAppliedSymbol`         | `setterCall: KaFunctionCall<KaNamedFunctionSymbol>`                                                                     |
| `KaCompoundOperation.operationPartiallyAppliedSymbol`         | `operationCall: KaFunctionCall<KaNamedFunctionSymbol>` (also exposed directly on `KaCompoundAccessCall.operationCall`). |

For-loops and delegated properties did not have a separate API in the old world; they were either resolved indirectly or
required custom code. The new API exposes them as first-class multi-calls:
[](KaForLoopCall.md) and [](KaDelegatedPropertyCall.md), with matching attempt types `KaForLoopCallResolutionAttempt`
and `KaDelegatedPropertyCallResolutionAttempt`.

### Symbol resolution

#### Emulating `mainReference.resolveToSymbols()`

For navigation, find-usages, and similar features, the old `mainReference.resolveToSymbols()` returned every symbol the
compiler considered &mdash; a kitchen-sink that included results from both call resolution (precise targets) and plain
symbol resolution. The new API does not bundle these two into a single call, but the recipe is short:

```Kotlin
@OptIn(KaExperimentalApi::class, KtExperimentalApi::class)
context(session: KaSession)
fun resolveToSymbols(element: KtElement): Collection<KaSymbol> {
    // 1. Prefer symbols extracted from a resolved call.
    //    Call resolution is more precise: a constructor call,
    //    for instance, points at the constructor, not the class.
    //
    //    `KtOperationReferenceExpression` is excluded on purpose. Its call resolution
    //    forwards to the parent expression and would also surface intermediate reads
    //    (e.g. the `get` of a compound `a[i] += v`), whereas the legacy
    //    `resolveToSymbols()` returned only the symbols the operator itself contributes
    //    (`plus`, `set`). Skipping the call step lets it fall through to
    //    `tryResolveSymbols()` below, which preserves that behavior.
    val callSymbols = (element as? KtResolvableCall)?.takeUnless { it is KtOperationReferenceExpression }
        ?.tryResolveCall()
        ?.calls
        ?.flatMap(KaSimpleOrMultiCall::symbols)
        ?.takeUnless(List<KaSymbol>::isEmpty)

    if (callSymbols != null) return callSymbols

    // 2. Fall back to plain symbol resolution.
    return (element as? KtResolvable)
        ?.tryResolveSymbols()
        ?.symbols
        .orEmpty()
}
```

This pattern is the formal way to migrate a `mainReference.resolveToSymbols()` call site that needs the broadest
possible result.

| Old call                                       | New equivalent                                                                                                                                                                                     |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `expr.mainReference.resolveToSymbol()`         | `expr.resolveSuccessfulSymbol()` – specialized form on the concrete PSI type. `KtResolvable.resolveSuccessfulSymbol(): KaSymbol?` – generic fallback.                                              |
| `expr.mainReference.resolveToSymbols()`        | `(expr as? KtResolvable)?.resolveSuccessfulSymbols()` – the generic `KtResolvable.resolveSuccessfulSymbols(): Collection<KaSymbol>` (there is no per-PSI-type specialization for the plural form). |
| `KtReference.isImplicitReferenceToCompanion()` | `(element as? KtSimpleNameExpression)?.isImplicitReferenceToCompanion == true`                                                                                                                     |
| `KtReference.usesContextSensitiveResolution`   | `(element as? KtSimpleNameExpression)?.usesContextSensitiveResolution == true`                                                                                                                     |

> **A resolved symbol is not always the call target.** For most elements the symbol from
> `resolveSuccessfulSymbol()` and the symbol behind `resolveSuccessfulCall()` coincide. They can diverge for
> `KtNameReferenceExpression`, `KtOperationReferenceExpression`, and `KtEnumEntrySuperclassReferenceExpression`:
> `resolveSuccessfulSymbol` / `resolveSuccessfulSymbols` prefer the *exact referenced symbol*, while
> `resolveSuccessfulCall` may describe the *enclosing call*. Choose the one that matches what you need (see
> **Common migration patterns** below).
>
> `resolveSuccessfulSymbol()` returns a non-`null` result only for a single, unambiguous, **successfully resolved**
> target, so on valid code it matches the old `resolveToSymbols().singleOrNull()`. Two warnings. The old
> `resolveToSymbols().firstOrNull()` silently picked one of several *ambiguous* results &mdash; for that breadth
> migrates to `resolveSuccessfulSymbols()`, not `resolveSuccessfulSymbol()`. And both `resolveSuccessfulSymbol()`
> and `resolveSuccessfulSymbols()` expose only `successfulSymbols`, whereas the legacy `resolveToSymbols()` also
> surfaced *candidate* symbols on red code; to keep that best-effort behavior, use `tryResolveSymbols()?.symbols`
> (the emulation recipe above).

## Common migration patterns

> **Pick the specialized overload first.** On a concrete PSI type (`KtCallElement`, `KtNameReferenceExpression`,
> `KtArrayAccessExpression`, ...) the `resolveSuccessfulCall` / `resolveSuccessfulSymbol` overload needs no cast and
> returns a narrower type. Only when your receiver is statically `KtElement` / `KtExpression` do cast to the marker
> interface (`as? KtResolvableCall` / `as? KtResolvable`) and use the generic form.

The recipes below assume the opt-ins from the note at the top of this page are in scope.

### `resolveToCall`

`resolveSuccessfulCall()` returns only the **successfully resolved** call &mdash; it is defined as
`tryResolveCall()?.successful`. It is therefore the faithful replacement for the `successful*` reductions, *not*
the `single*` ones: the `single*` helpers read `KaCallInfo.calls`, which for an *error* call is the candidate list, so
they also return the sole candidate of an unresolved call. Classify the old reduction before migrating:

| Old reduction over `KaCallInfo`                                                                   | On success      | On an **error** call                        | New equivalent                                                                    |
|---------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------|-----------------------------------------------------------------------------------|
| `successfulFunctionCallOrNull()` / `successfulVariableAccessCall()` / `successfulCallOrNull<T>()` | the call        | `null`                                      | `resolveSuccessfulCall()` (add `?.function` / `?.variable` on a generic receiver) |
| `singleFunctionCallOrNull()` / `singleVariableAccessCall()` / `singleCallOrNull<T>()`             | the call        | the sole candidate of type `T`, else `null` | `tryResolveCall()?.single?.function` (or `?.variable`)                            |
| `KaCallInfo.calls`                                                                                | a one-call list | the candidate calls                         | `tryResolveCall()?.calls`                                                         |

The common success-only case &mdash; a resolved single function call &mdash; collapses to one call, since
`resolveSuccessfulCall()` over a `KtCallElement` already returns `KaFunctionCall<*>?`:

```Kotlin
// Old (success-only)
val call = callExpression.resolveToCall()
    ?.successfulFunctionCallOrNull()
    ?: return

// New
val call = callExpression.resolveSuccessfulCall() ?: return
```

The candidate-tolerant `singleFunctionCallOrNull()` is **not** equivalent &mdash; `resolveSuccessfulCall()` drops the
sole candidate of a *failed* call that `singleFunctionCallOrNull()` would have returned. Preserve that behavior with
`tryResolveCall()`:

```Kotlin
// Old (candidate-tolerant)
val call = callExpression.resolveToCall()
    ?.singleFunctionCallOrNull()
    ?: return

// New
val call = callExpression.tryResolveCall()
    ?.single
    ?.function
    ?: return
```

> **Drop red code or match it?** Migrate to `resolveSuccessfulCall()` when an unresolved or ambiguous call should be
> silently dropped (typical for inspections that must not produce false positives); migrate to `tryResolveCall()` when
> you want a best-effort match on red code (typical for navigation and find-usages). This is the same distinction as the
> **iterating candidate calls** trap below.

If you only need the called symbol, skip the call entirely and use the specialized `resolveSuccessfulSymbol()`:

```Kotlin
// Old
val symbol = callExpression.resolveToCall()
    ?.successfulFunctionCallOrNull()
    ?.symbol
    ?: return

// New
val symbol = callExpression.resolveSuccessfulSymbol() ?: return
```

`KaPartiallyAppliedSymbol` is gone, so `partiallyAppliedSymbol.signature` / `.symbol` chains flatten:

```Kotlin
// Old
val id = callExpression.resolveToCall()
    ?.successfulFunctionCallOrNull()
    ?.partiallyAppliedSymbol?.signature?.callableId

// New
val id = callExpression.resolveSuccessfulCall()?.symbol?.callableId
// or:   callExpression.resolveSuccessfulSymbol()?.callableId
```

When the receiver is only statically a `KtExpression` / `KtElement`, cast to the marker interface and narrow the result:

```Kotlin
// Old
val call = expression.resolveToCall()?.successfulFunctionCallOrNull()

// New
val call = (expression as? KtResolvableCall)?.resolveSuccessfulCall()?.function
```

The same cast covers other call shapes. Variable access:

```Kotlin
// Old
val access = expression.resolveToCall()?.successfulVariableAccessCall()

// New
val access = (expression as? KtResolvableCall)?.resolveSuccessfulCall()?.variable
```

A member call resolved through `successfulCallOrNull<KaCallableMemberCall<*, *>>()`:

```Kotlin
// Old
val symbol = expression.resolveToCall()
    ?.successfulCallOrNull<KaCallableMemberCall<*, *>>()
    ?.partiallyAppliedSymbol?.symbol

// New
val symbol = (expression as? KtResolvableCall)?.resolveSuccessfulCall()?.simple?.symbol
```

**Trap &mdash; iterating candidate calls.** `resolveSuccessfulCall()` is `null` whenever resolution fails, which is
exactly the case a `.calls` loop wants to inspect. Migrate `.calls` to `tryResolveCall()?.calls`, *not*
`resolveSuccessfulCall()`:

```Kotlin
// Old
for (call in call.resolveToCall()?.calls.orEmpty()) {
    // ...
}

// New
for (call in call.tryResolveCall()?.calls.orEmpty()) {
    // ...
}
```

When a helper switched over a resolved `KaCall`, widen its parameter to `KaSimpleOrMultiCall` (the type
`resolveSuccessfulCall()` now returns) and drop the `successfulCallOrNull<KaCall>()` unwrapping at the call site.
Deprecated subtype casts also disappear: `as? KaSimpleFunctionCall` becomes the `function` property.

### `resolveToCallCandidates`

A rename plus a type rename: `resolveToCallCandidates()` &rarr; `collectCallCandidates()`, and the element type
`KaCallCandidateInfo` &rarr; `KaCallCandidate` (the `.candidate` and `.isInBestCandidates` members are unchanged):

```Kotlin
// Old
fun handle(candidates: List<KaCallCandidateInfo>) {
}

handle(callExpression.resolveToCallCandidates())

// New
fun handle(candidates: List<KaCallCandidate>) {
}

handle(callExpression.collectCallCandidates())
```

On a generic receiver, cast first:

```Kotlin
// Old
val first = expression.resolveToCallCandidates()
    .firstOrNull()
    ?.candidate as? KaFunctionCall<*>

// New
val candidates = (expression as? KtResolvableCall)?.collectCallCandidates()
val first = candidates?.firstOrNull()?.candidate as? KaFunctionCall<*>
```

`collectCallCandidates()` returns *all* overload-resolution candidates; `resolveSuccessfulCall()` returns only the
single most-specific result. Use candidates when you need to reason about ambiguity, the resolved call otherwise.

### `resolveToSymbol`

Resolve **on the element**, not on its `mainReference`. The specialized overload returns a narrower symbol type:

```Kotlin
// Old
val symbol = operationReference.mainReference.resolveToSymbol() as? KaFunctionSymbol
    ?: return

// New
val symbol = operationReference.resolveSuccessfulSymbol() as? KaFunctionSymbol
    ?: return
```

A `this` expression resolves directly &mdash; no `instanceReference.mainReference`:

```Kotlin
// Old
val symbol = thisExpression.instanceReference
    .mainReference
    .resolveToSymbol()

// New
val symbol = thisExpression.resolveSuccessfulSymbol()
```

When the static type is only `KtExpression`, narrow to `KtResolvable`:

```Kotlin
// Old
val symbol = expression.mainReference?.resolveToSymbol() as? KaValueParameterSymbol
    ?: return

// New
val symbol = (expression as? KtResolvable)?.resolveSuccessfulSymbol() as? KaValueParameterSymbol
    ?: return
```

> **Precision trap &mdash; the called declaration vs. the referenced symbol.** Old code often resolved the *callee name
> reference* of a call: `callExpression.calleeExpression?.mainReference?.resolveToSymbol()`. Resolving the **call
element**
> instead returns the *called* declaration &mdash; the constructor of a constructor call, the `invoke` of an implicit
> `invoke` call &mdash; whereas resolving the name reference returns the *referenced* symbol (the class, the property).
> These genuinely differ:
>
> ```Kotlin
> // Old: resolves the callee reference
> val symbol = callExpression.calleeExpression
>     ?.mainReference
>     ?.resolveToSymbol() as? KaConstructorSymbol
> 
> // New: resolves the call element -> the constructor itself
> val symbol = callExpression.resolveSuccessfulSymbol() as? KaConstructorSymbol
> ```
>
> Migrate to the call element when you want the *called* function; keep
> `(reference as? KtResolvable)?.resolveSuccessfulSymbol()` on the name reference when you want the exact *referenced*
> symbol.

### `resolveToSymbols`

`resolveToSymbols()` returned a collection. Both common reductions over it map to the single-result
`resolveSuccessfulSymbol()`, but with a warning:

```Kotlin
// Old (exact, single target)
val symbol = element.mainReference.resolveToSymbols().singleOrNull()

// New
val symbol = element.resolveSuccessfulSymbol()
// or:       (element as? KtResolvable)?.resolveSuccessfulSymbol()
```

```Kotlin
// Old (tolerated ambiguity, picked one)
val symbol = element.mainReference.resolveToSymbols().firstOrNull()
// New (returns null on more than one target!)
val symbol = element.resolveSuccessfulSymbol()
```

`resolveSuccessfulSymbol()` is an exact match for `.singleOrNull()` *on valid code* &mdash; both yield a result only for
a single, unambiguous target. It is *not* a faithful match for `.firstOrNull()`, which silently chose one of several
ambiguous symbols: `resolveSuccessfulSymbol()` returns `null` when there is more than one target. Note also that
`resolveSuccessfulSymbol()` and `resolveSuccessfulSymbols()` return only *successful* targets, whereas the old
`resolveToSymbols()` also exposed candidate symbols on invalid code. If a call site genuinely needs every candidate
&mdash; ambiguous or red &mdash; migrate to `resolveSuccessfulSymbols()` for ambiguity, or to the emulation recipe above
(`tryResolveCall()?.calls` / `tryResolveSymbols()?.symbols`) for the full best-effort set, not
`resolveSuccessfulSymbol()`.

## What about `KtReference`?

Kotlin references have become part of the IntelliJ IDEA Kotlin plugin. The Analysis API no longer uses them.

The extensions `KtReference.resolveToSymbols()` and `KtReference.resolveToSymbol()` remain available as a
backward-compatibility surface; they are not annotated `@Deprecated` outright, but the modern flow does not pass through
`KtReference` at all. Resolve directly on the `KtElement` instead, using the specialized method or a safe `as?`
narrowing to `KtResolvable`.

Two `KtReference` extensions **are** explicitly deprecated and have moved to `KtSimpleNameExpression`:

* `KtReference.isImplicitReferenceToCompanion()` &rarr;
  `(element as? KtSimpleNameExpression)?.isImplicitReferenceToCompanion == true`.
* `KtReference.usesContextSensitiveResolution` &rarr;
  `(element as? KtSimpleNameExpression)?.usesContextSensitiveResolution == true`.

## Opting in

All entry points described here are annotated `@KaExperimentalApi`. You must opt in at the call site:

```Kotlin
@OptIn(KaExperimentalApi::class)
fun myUsage(element: KtCallElement) = analyze(element) {
        element.resolveSuccessfulCall()
    }
```

When a snippet names the `KtResolvable` / `KtResolvableCall` marker interfaces directly (the generic fallback form), add
the second opt-in &mdash; the markers themselves are annotated `@KtExperimentalApi`:

```Kotlin
@OptIn(KaExperimentalApi::class, KtExperimentalApi::class)
fun myUsage(element: KtElement) = analyze(element) {
        (element as? KtResolvableCall)?.resolveSuccessfulCall()
    }
```

This is the only deliberate friction during migration: the rest of the surface is designed to require no manual cast, no
wrapper unwrapping, and no parallel `KtReference` fallback.
