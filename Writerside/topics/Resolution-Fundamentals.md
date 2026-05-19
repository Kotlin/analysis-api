# Resolution Fundamentals

This page introduces the **resolution API** of the Analysis API: the entry points used to ask, given a piece of Kotlin
PSI, *what* it refers to or *how* it is called at that exact site. Read this before the more detailed how-to pages, as
it establishes the mental model and the rules that the rest of the documentation builds on.

<warning>
The resolution API described here is annotated <code>@KaExperimentalApi</code>. Every entry point requires opting in,
either through <code>@OptIn(KaExperimentalApi::class)</code> at the call site or a propagated opt-in.
The <code>KtResolvable</code> / <code>KtResolvableCall</code> marker interfaces are annotated
<code>@KtExperimentalApi</code>, so snippets that name them require an additional
<code>@OptIn(KtExperimentalApi::class)</code>.
The API is intended to stabilize soon, but until then the contract may change between versions.
</warning>

## Two questions, two APIs

Resolution in the Analysis API answers two **independent** questions about a piece of Kotlin PSI.

**Symbol resolution** answers *"what declaration does this PSI element refer to?"* &mdash; the literal target of the
element. For the name reference `MyClass` in `val c = MyClass()`, symbol resolution returns the **class**
`MyClass` &mdash; that is what the name literally points to. Symbol resolution applies to almost every
resolvable element, including those that are not calls (type references, package qualifiers, labels, supertypes,
class literals, and so on).

**Call resolution** answers *"how is this expression executed at this site &mdash; which callable, applied to which
receivers, type arguments, and value arguments?"*. For the same `MyClass()` expression, call resolution returns a
**constructor call** &mdash; because the class itself cannot be invoked (it is a type), it is the constructor that is
called. Call resolution only applies to expressions and elements that actually represent an executed callable.

The two views are deliberately separate. Use the one that matches your task:

* You want navigation, find-usages, or a textual rename target &rarr; symbol resolution.
* You want to inspect the call site itself &mdash; selected overload, arguments, receivers, type arguments,
  smart-casts &rarr; call resolution.

Not every PSI element has a call. `KtTypeReference`, `KtUserType`, `KtNullableType`,
`KtLabelReferenceExpression`, and similar expose only symbol resolution. Compound expressions
(for-loops, delegated properties, compound assignments, compound array access) expose multiple sub-calls
through the call API.

## Resolvable PSI elements

Resolvable PSI elements are marked by two interfaces in `org.jetbrains.kotlin.resolution`:

```Kotlin
@KtExperimentalApi interface KtResolvable
@KtExperimentalApi interface KtResolvableCall : KtResolvable
```

`KtResolvable` marks an element that can be resolved to a symbol; `KtResolvableCall` marks an element that can additionally
be resolved to a call. For example, `KtReferenceExpression : KtResolvable`, and call-bearing elements like `KtCallElement`
implement `KtResolvableCall` (and therefore `KtResolvable`).

In practice you rarely use these names directly &mdash; you reach for the *specialized* form on the concrete PSI type.

## How to call the resolution API

The resolution API is available inside a `KaSession` &mdash; that is, inside an `analyze { ... }` block, or inside a
function with a `context(_: KaSession)` declaration. The resolution functions are exposed both as member-extensions on
`KaSession` and as top-level extension functions that can be imported and used wherever a `KaSession` is in scope.

The canonical entry point is the **specialized form on the concrete PSI type**:

```Kotlin
@OptIn(KaExperimentalApi::class)
fun perform(expression: KtSimpleNameExpression) {
    analyze(expression) {
        val symbol: KaSymbol? = expression.resolveSymbol()
        println(symbol?.name)
    }
}
```

Each specialized method returns a precisely typed result &mdash; for instance, `KtAnnotationEntry.resolveSymbol()`
returns `KaConstructorSymbol?`, and `KtCallElement.resolveCall()` returns `KaFunctionCall<*>?`. Prefer this form whenever
the PSI type is known: it is shorter, type-safe, and discoverable through IDE completion on the element.

### Working with a generic `PsiElement`

When the element type is genuinely unknown (for instance, you only have a `PsiElement` from a reference traversal), use a
**safe** cast to the marker interface and then call the generic entry point. Never use an unchecked `as` cast.

```Kotlin
@OptIn(KaExperimentalApi::class, KtExperimentalApi::class)
fun perform(element: KtElement) = analyze(element) {
    val symbol = (element as? KtResolvable)?.resolveSymbol()
    val call = (element as? KtResolvableCall)?.resolveCall()
}
```

### Plain form vs try form

Every resolution flavor exists in two forms:

* The **plain** form (`resolveSymbol`, `resolveSymbols`, `resolveCall`) returns the happy-path result &mdash; a symbol or
  a `KaSingleOrMultiCall`, or `null` if resolution did not succeed. Use it when you only care about a valid result
  and want failed/ambiguous resolutions to be silently dropped (typical for inspections that must not produce
  false positives).
* The **try** form (`tryResolveSymbols`, `tryResolveCall`) returns a richer **attempt** &mdash; either a
  **success** with the result, or an **error** carrying a diagnostic and candidate symbols/calls.
  Use it when you want every piece of information the compiler considered, including failed attempts and partial
  results (typical for navigation, find-usages, and any tooling that wants to do a best-effort match on red code).

See [](KaSymbolResolutionAttempt.md) and [](KaCallResolutionAttempt.md) for the full attempt hierarchy.

## A complete example

The following is a complete, runnable example using the resolution API on a `KtSimpleNameExpression`.

```Kotlin
import org.jetbrains.kotlin.analysis.api.KaExperimentalApi
import org.jetbrains.kotlin.analysis.api.analyze
import org.jetbrains.kotlin.analysis.api.resolution.successfulCall
import org.jetbrains.kotlin.analysis.api.resolution.symbols
import org.jetbrains.kotlin.psi.KtSimpleNameExpression

@OptIn(KaExperimentalApi::class)
fun describe(
  expression: KtSimpleNameExpression, 
): String? = analyze(expression) {
    // 1. What does the expression refer to?
    val target = expression.resolveSymbol() ?: return@analyze null

    // 2. Was this expression also used as a call site?
    val call = expression.resolveCall()

    buildString {
        append("Target: ")
        append(target.javaClass.simpleName)
        if (call != null) {
            append(", call: ")
            append(call.javaClass.simpleName)
        }
    }
}
```

Subsequent pages keep snippets compact: they assume an `analyze { }` block is in scope and
`@OptIn(KaExperimentalApi::class)` is applied somewhere up the call chain.

## Where to go next

* [](Resolving-Symbols.md) &mdash; symbol resolution in detail, with the table of specialized methods
  and the `KaSymbolResolutionAttempt` flow.
* [](Resolving-Calls.md) &mdash; call resolution, the `KaSingleOrMultiCall` hierarchy, and compound calls.
* [](Resolution-Candidates.md) &mdash; collecting overload candidates regardless of resolution outcome.
* [](Migrating-Resolution-API.md) &mdash; mapping from the old
  `mainReference` / `resolveToCall` / `KaCallInfo` API to the new one.
