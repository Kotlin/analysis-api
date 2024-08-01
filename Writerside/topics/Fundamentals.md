# Fundamentals

This page covers a few fundamental concepts and rules of the Analysis API. Please read it thoroughly.

## Kotlin PSI

The Kotlin compiler exposes a Kotlin abstract syntax tree, built on top of
the [PSI](https://plugins.jetbrains.com/docs/intellij/psi.html) API, a part of IntelliJ IDEA. For some languages, such
as Java, the PSI acts both as a syntax tree and as a source of semantic information. In Kotlin, though, these concepts
are clearly separated.

Below is a simplified tree of the Kotlin PSI hierarchy.

<code-block lang="mermaid">
graph TD
  KtElement
  KtElement --> KtFile
  KtElement --> KtTypeElement
  KtElement --> KtExpression
  KtExpression --> KtDeclaration
  KtDeclaration --> KtClassOrObject
  KtDeclaration --> KtFunction
  KtDeclaration --> KtVariableDeclaration
  KtExpression --> KtOperationExpression
  KtOperationExpression --> KtUnaryExpression
  KtOperationExpression --> KtBinaryExpression
  KtExpression --> KtCallExpression
  KtExpression --> KtBlockExpression
</code-block>

`KtElement` is the root type of the hierarchy. `KtDeclaration` and `KtExpression` are two notable subtypes of
it. `KtDeclaration` itself is an expression, which makes it possible to have local classes and functions.

The Kotlin PSI does not have a strict separation between statements and expressions. There is, however,
a `KtStatementExpression` marker interface that annotates statement-like constructs.

The Analysis API is implemented on top of the Kotlin PSI, mostly as a set of extension functions and properties,
providing access to semantic information. For example, to get an expression type, there is
a `ktExpression.expressionType` extension property. Or, to get resolved call information, one should
use `ktCallExpression.resolveToCall()`.

## KaSession

`KaSession` is the entry point for interacting with the Analysis API. It provides access to various components and
utilities needed for analyzing code in Kotlin.

Each `KaSession` is associated with a specific module and provides analysis results from the perspective of that module.
In other words, a `KaSession` only sees declarations from the owning (use-site) module and from all its dependencies,
both direct and transitive.

To get a `KaSession`, use the `analyze {}` function, passing a `KtModule` or some `KtElement` from that module:

```Kotlin
@RequiresReadLock
fun perform(element: KtElement) {
    analyze(element) {
        // Use the 'KaSession' within this block
    }
}
```

The `KaSession` is available as an extension receiver within the lambda block. The session is valid only within this
block, and it **should not** be stored or accessed outside of it.

The `analyze {}` call is only available
inside [read actions](https://plugins.jetbrains.com/docs/intellij/general-threading-rules.html#read-access). You can use
the `@RequiresReadLock` annotation to specify that the method must be called from a read action. In later parts of the
documentation, the annotation is not added for clarity.

## KaLifetimeOwner

`KaSession` and most entities retrieved from it (symbols, types, etc.) are valid only within the same read action and
the `analyze` block in which they were created. All such entities have the `KaLifetimeOwner` supertype.

It is crucial to avoid caching `KaLifetimeOwner`s for an arbitrary time, including storing them in properties of
long-living classes or in a static context. Doing so will likely lead to severe memory leaks as these entities hold the
whole underlying resolution session. Always retrieve and use them within the `analyze` block or pass them as parameters
to functions that require them.

If you need to extract parts of the resolution logic to a separate function, prefer passing the `KaSession` as an
extension or ordinary parameter, instead of keeping it in some shared context class.

```Kotlin
fun perform(element: KtElement) {
    analyze(element) {
        if (check(element)) {
            modify(element)
        }
    }
}

// Here we pass the session as a receiver parameter
fun KaSession.check(element: KtElement) { ... }

fun modify(element: KtElement) { ... }
```

Inside the `analyze {}` block, `KaSession` is also available as a `useSiteSession` property:

```Kotlin
fun perform(element: KtElement) {
    analyze(element) {
        check(useSiteSession, element)
    }
}

// Here we pass the session as an ordinary parameter
fun check(useSiteSession: KaSession, element: KtElement) { ... }
```

If you need to pass a `KaSymbol` to a different analysis session, use `KaSymbolPointer`s. Unlike symbols, pointers do
not capture the analysis session, so they can be freely passed around or cached:

```Kotlin
fun perform(ktCall: KtCallExpression) {
    val pointer = resolveCall(ktCall) ?: return
    processCallTarget(ktCall, pointer)
}

fun resolveCall(ktCall: KtCallExpression): KaSymbolPointer<KaCallableSymbol>? {
    analyze(ktCall) {
        val symbol = ktCall.mainReference.resolveToSymbol() as? KaCallableSymbol
        return symbol?.createPointer() // Create the pointer
    }
}

fun processCallTarget(ktContext: KtElement, pointer: KaSymbolPointer<KaCallableSymbol>) {
    analyze(ktContext) {
        val symbol = pointer.restoreSymbol() ?: return
        symbol.callableId // Use the restored symbol
    }
}
```

<note>
    In IntelliJ IDEA 2024.3, pointers will become available also for `KaType`s.
</note>