# Migrating from the Legacy Resolution API

The Analysis API resolution surface was redesigned as part of [KT-66039](https://youtrack.jetbrains.com/issue/KT-66039). This guide maps the
old API to the new one. If you are not yet familiar with the new shape, read
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
2. **Discoverability suffered.** The `.mainReference` hop was easy to miss and gave no type-level hint that resolution
   was happening at all.
3. **Result types were under-specified.** `resolveToSymbol()` returned `KaSymbol?` everywhere; `resolveToCall()`
   returned a `KaCallInfo?` over a generic `KaCall`. Callers had to `as?`-cast to anything specific.
4. **`KaPartiallyAppliedSymbol` was a useless wrapper.** Receivers, signature, and type-argument mapping had to be
   unwrapped through an extra layer. The new `KaSingleCall` exposes all of this inline; the new compound calls
   expose named sub-call accessors (`variableCall`, `getterCall`, `setterCall`, `operationCall`).
5. **`KtElement.resolveToCall` accepted any `KtElement`.** Nothing in the type told you whether resolution would
   succeed or what it would return. `KtReference` filled the gap for everything `resolveToCall` could not handle &mdash;
   so plugins had to maintain two parallel resolution mechanisms.

The new API replaces both `KtReference`-based resolution and `KtElement.resolveToCall` with a single, type-driven
surface: specialized `resolveSymbol` / `resolveCall` methods on concrete PSI types, plus the marker interfaces
`KtResolvable` and `KtResolvableCall` for the generic case.

## Migration rules

Two rules cover almost all sites:

1. **Use the specialized method on the concrete PSI type whenever possible.** If you know the element is a
   `KtCallElement`, write `callElement.resolveCall()` &mdash; you get back a `KaFunctionCall<*>?` directly. Each
   specialization narrows the return type, so type checks and casts you used to write disappear.
2. **When the PSI type is genuinely unknown, narrow with a safe `as?` cast.** To check whether the element implements
   `KtResolvable` or `KtResolvableCall`.

```Kotlin
// Specialized form (preferred)
val call: KaFunctionCall<*>? = callElement.resolveCall()

// Generic form (only when the element type is unknown)
val call: KaSingleOrMultiCall? =
    (element as? KtResolvableCall)?.resolveCall()
```

## Old &rarr; new matrix

### Symbol resolution

| Old call                                       | New equivalent                                                                                                                                                                         |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `expr.mainReference.resolveToSymbol()`         | Specialized form on the concrete PSI type (e.g. `simpleName.resolveSymbol()`, `annotationEntry.resolveSymbol()`).<br/>Generic fallback: `(element as? KtResolvable)?.resolveSymbol()`. |
| `expr.mainReference.resolveToSymbols()`        | Specialized form on the concrete PSI type, or `(element as? KtResolvable)?.resolveSymbols().orEmpty()`.                                                                                |
| `KtReference.isImplicitReferenceToCompanion()` | `(element as? KtSimpleNameExpression)?.isImplicitReferenceToCompanion == true`                                                                                                         |
| `KtReference.usesContextSensitiveResolution`   | `(element as? KtSimpleNameExpression)?.usesContextSensitiveResolution == true` ([KEEP-0379](https://github.com/Kotlin/KEEP/issues/379))                                                |

### Call resolution

| Old call                                                                | New equivalent                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `expr.resolveToCall(): KaCallInfo?`                                     | Specialized form on the concrete PSI type (`callElement.resolveCall()`, `arrayAccess.resolveCall()`, ...).<br/>Generic fallback: `(element as? KtResolvableCall)?.resolveCall()`.                                                                  |
| `KaCallInfo.successfulFunctionCallOrNull()`                             | Specialized: `callElement.resolveCall()` already returns `KaFunctionCall<*>?`.<br/>Generic fallback: `(element as? KtResolvableCall)?.resolveCall() as? KaFunctionCall<*>`.                                                                        |
| `KaCallInfo.successfulVariableAccessCall()`                             | `callElement.resolveCall() as? KaVariableAccessCall` (or use the specialized form on the concrete PSI element).                                                                                                                                    |
| `KaCallInfo.successfulConstructorCallOrNull()`                          | Specialized: `constructorCallee.resolveCall()` returns `KaFunctionCall<KaConstructorSymbol>?` directly.<br/>Generic fallback: `((element as? KtResolvableCall)?.resolveCall() as? KaFunctionCall<*>)?.takeIf { it.symbol is KaConstructorSymbol}`. |
| `KaCallInfo.singleCallOrNull<T>()` / `singleFunctionCallOrNull()` / ... | From `tryResolveCall()`: `attempt.calls.singleOrNull { it is T }`. From an error path: `(attempt as? KaCallResolutionError)?.candidateCalls`.                                                                                                      |
| `KaCallInfo.calls`                                                      | `tryResolveCall()?.calls` for the unified set of resolved/candidate calls.                                                                                                                                                                         |
| `KtElement.resolveToCallCandidates(): List<KaCallCandidateInfo>`        | `callElement.collectCallCandidates(): List<KaCallCandidate>`.                                                                                                                                                                                      |

### Inline access on a `KaSingleCall`

Every `*PartiallyAppliedSymbol` access becomes a direct field on the call.

| Old call (legacy member on `KaCallableMemberCall`)                    | New equivalent (inline on `KaSingleCall`)                                                                            |
|-----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| `call.partiallyAppliedSymbol.signature`                               | `call.signature`                                                                                                     |
| `call.partiallyAppliedSymbol.symbol`                                  | `call.symbol`                                                                                                        |
| `call.partiallyAppliedSymbol.dispatchReceiver`                        | `call.dispatchReceiver`                                                                                              |
| `call.partiallyAppliedSymbol.extensionReceiver`                       | `call.extensionReceiver`                                                                                             |
| `call.partiallyAppliedSymbol.contextArguments`                        | `call.contextArguments`                                                                                              |
| `(call as KaCallableMemberCall<*, *>).typeArgumentsMapping`           | `call.typeArgumentsMapping`                                                                                          |
| `KaFunctionCall.argumentMapping`                                      | `KaFunctionCall.valueArgumentMapping` (or `combinedArgumentMapping` if you also need context arguments).             |

### Subtypes you may have used

| Legacy type / member                                                                        | Replacement                                                                                                       |
|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| `KaSimpleFunctionCall`                                                                      | `KaFunctionCall<*>`                                                                                               |
| `KaSimpleFunctionCall.isImplicitInvoke`                                                     | `call is KaImplicitInvokeCall`                                                                                    |
| `KaSimpleVariableAccessCall`                                                                | `KaVariableAccessCall`                                                                                            |
| `KaSimpleVariableAccess` / `KaSimpleVariableAccess.Read` / `.Write`                         | `KaVariableAccessCall.Kind` / `KaVariableAccessCall.Kind.Read` / `KaVariableAccessCall.Kind.Write`                |
| `KaCallCandidateInfo` / `KaApplicableCallCandidateInfo` / `KaInapplicableCallCandidateInfo` | `KaCallCandidate` / `KaApplicableCallCandidate` / `KaInapplicableCallCandidate` (works on `KaSingleOrMultiCall`). |

### Compound calls (`+=`, `++`, `--`, `a[i] += v`, `by`, `for`)

| Old call                                                      | New equivalent                                                                                                          |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| `KaCompoundVariableAccessCall.variablePartiallyAppliedSymbol` | `variableCall: KaVariableAccessCall`                                                                                    |
| `KaCompoundArrayAccessCall.getPartiallyAppliedSymbol`         | `getterCall: KaFunctionCall<KaNamedFunctionSymbol>`                                                                     |
| `KaCompoundArrayAccessCall.setPartiallyAppliedSymbol`         | `setterCall: KaFunctionCall<KaNamedFunctionSymbol>`                                                                     |
| `KaCompoundOperation.operationPartiallyAppliedSymbol`         | `operationCall: KaFunctionCall<KaNamedFunctionSymbol>` (also exposed directly on `KaCompoundAccessCall.operationCall`). |

For-loops and delegated properties did not have a separate API in the old world; they were either resolved indirectly
or required custom code. The new API exposes them as first-class multi-calls:
[](KaForLoopCall.md) and [](KaDelegatedPropertyCall.md), with matching attempt
types `KaForLoopCallResolutionAttempt` and `KaDelegatedPropertyCallResolutionAttempt`.

## Emulating `mainReference.resolveToSymbols()`

For navigation, find-usages, and similar features, the old `mainReference.resolveToSymbols()` returned every symbol the
compiler considered &mdash; a kitchen-sink that included results from both call resolution (precise targets) and
plain symbol resolution. The new API does not bundle these two into a single call, but the recipe is short:

```Kotlin
@OptIn(KaExperimentalApi::class, KtExperimentalApi::class)
context(_: KaSession)
fun resolveToSymbols(element: KtElement): Collection<KaSymbol> {
    // 1. Prefer symbols extracted from a resolved call.
    //    Call resolution is more precise: a constructor call,
    //    for instance, points at the constructor, not the class.
    val callSymbols = (element as? KtResolvableCall)
        ?.tryResolveCall()
        ?.calls
        ?.flatMap(KaSingleOrMultiCall::symbols)
        ?.takeUnless(List<KaSymbol>::isEmpty)

    if (callSymbols != null) return callSymbols

    // 2. Fall back to plain symbol resolution.
    return (element as? KtResolvable)
        ?.tryResolveSymbols()
        ?.symbols
        .orEmpty()
}
```

This pattern is the canonical way to migrate a `mainReference.resolveToSymbols()` call site that needs the broadest
possible result.

## What about `KtReference`?

`KtReference` is **not** a `KtResolvable`. It is owned by the IntelliJ reference contract, not the Analysis API.

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
    element.resolveCall()
}
```

When a snippet names the `KtResolvable` / `KtResolvableCall` marker interfaces directly (the generic fallback form), add
the second opt-in &mdash; the markers themselves are annotated `@KtExperimentalApi`:

```Kotlin
@OptIn(KaExperimentalApi::class, KtExperimentalApi::class)
fun myUsage(element: KtElement) = analyze(element) {
    (element as? KtResolvableCall)?.resolveCall()
}
```

This is the only deliberate friction during migration: the rest of the surface is designed to require no manual cast,
no wrapper unwrapping, and no parallel `KtReference` fallback.
