---
tags:
 - jvm
title: "resolveSuccessfulSymbols"
---

# resolveSuccessfulSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">.</span><a href="resolve-successful-symbols.html"><span class="nf">resolveSuccessfulSymbols</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Resolves symbols for the given [`KtResolvable`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md).

Returns all resolved [`KaSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md)s if successful; otherwise, an empty list. Might contain multiple symbols for a compound case

In contract to [`resolveSuccessfulCall`](resolve-successful-call.md), it could represent any [`KaSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md), not only [`KaCallableSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md).

In most cases, a not-null result of [`resolveSuccessfulCall`](resolve-successful-call.md) will represent the same symbol. The only exceptions are:

 - [`KtNameReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md)


 - [`KtOperationReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-operation-reference-expression/index.md)


 - [`KtEnumEntrySuperclassReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md)


For which the behavior could be different depending on the context.

The main idea is that [`resolveSuccessfulSymbols`](resolve-successful-symbols.md) could represent more cases, so it prefers exactly the referenced symbol and not the parent call. For more details, see the mentioned elements.

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`resolveSuccessfulSymbol`](resolve-successful-symbol.md)
 - [`KaSimpleSymbolResolutionSuccess`](-ka-simple-symbol-resolution-success/index.md)



</div>

</div>
