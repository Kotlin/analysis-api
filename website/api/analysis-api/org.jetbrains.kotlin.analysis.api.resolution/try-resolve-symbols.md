---
tags:
 - jvm
title: "tryResolveSymbols"
---

# tryResolveSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">.</span><a href="try-resolve-symbols.html"><span class="nf">tryResolveSymbols</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve a symbol for the given [`KtResolvable`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md).

### Usage Example:
```kotlin
context(session: KaSession)
fun findSymbol(reference: KtNameReferenceExpression): KaSymbol? {
  val attempt = reference.tryResolveSymbols() ?: return null
  return attempt.fold(
    onSuccess = { symbols -> symbols.singleOrNull() },
    onFailure = { errors ->
      val name = reference.getReferencedName()
      errors.forEach { println("Cannot resolve '$name': ${it.diagnostic.defaultMessage}") }
      null
    },
  )
}
```

Returns a [`KaSymbolResolutionAttempt`](-ka-symbol-resolution-attempt/index.md) that describes either success ([`KaSimpleSymbolResolutionSuccess`](-ka-simple-symbol-resolution-success/index.md)) or failure ([`KaSimpleSymbolResolutionError`](-ka-simple-symbol-resolution-error/index.md), or [`KaCompoundSymbolResolutionError`](-ka-compound-symbol-resolution-error/index.md) for a compound call), or `null` when there is nothing to resolve: the element carries no resolvable reference, such as a type reference to a dynamic or intersection type, or the engine has no result for it, which broken code can cause.

A non-null result describes the outcome of an actual resolution. Check it with [`errors`](-ka-compound-symbol-resolution-error/index.md#errors) or [`isSuccessful`](-ka-compound-symbol-resolution-error/index.md#issuccessful) rather than with a type check, which only covers simple attempts. A reported error may carry an empty [`candidateSymbols`](-ka-simple-symbol-resolution-error/index.md#candidatesymbols) list.

In contract to [`tryResolveCall`](try-resolve-call.md), it could represent any [`KaSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md), not only [`KaCallableSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md).

In most cases, a not-null result of [`tryResolveCall`](try-resolve-call.md) will represent the same symbol. The only exceptions are:

 - [`KtNameReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md)


 - [`KtOperationReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-operation-reference-expression/index.md)


 - [`KtEnumEntrySuperclassReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md)


For which the behavior could be different depending on the context.

The main idea is that [`tryResolveSymbols`](try-resolve-symbols.md) could represent more cases, so it prefers exactly the referenced symbol and not the parent call. For more details, see the mentioned elements.

See [References and Calls](https://kotlin.github.io/analysis-api/references-and-calls.html) for a top-level overview.

#### See also


 - [`KaSimpleSymbolResolutionSuccess`](-ka-simple-symbol-resolution-success/index.md)
 - [`KaSimpleSymbolResolutionError`](-ka-simple-symbol-resolution-error/index.md)



</div>

</div>
