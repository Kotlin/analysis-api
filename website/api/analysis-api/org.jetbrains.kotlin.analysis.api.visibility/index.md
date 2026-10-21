---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.visibility"
---

# org.jetbrains.kotlin.analysis.api.visibility
## Types
### [`KaUseSiteVisibilityChecker`](-ka-use-site-visibility-checker/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-use-site-visibility-checker/index.html">KaUseSiteVisibilityChecker</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Allows checking if [`KaDeclarationSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) is visible from the current use-site.


</div>

</div>
## Properties
### [`isPublicApi`](is-public-api.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="is-public-api.html">isPublicApi</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the symbol is effectively public, including internal declarations with the [`PublishedApi`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-published-api/index.html) annotation.


</div>

</div>
## Functions
### [`createUseSiteVisibilityChecker`](create-use-site-visibility-checker.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="create-use-site-visibility-checker.html"><span class="nf">createUseSiteVisibilityChecker</span></a><span class="p">(</span>
    useSiteFile<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="p">, </span>
    receiverExpression<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span><span class="p">, </span>
    position<span class="o">: </span>PsiElement
<span class="p">)</span><span class="o">: </span><a href="-ka-use-site-visibility-checker/index.html">KaUseSiteVisibilityChecker</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a visibility checker for the given use-site position.


</div>

</div>
### [`isVisibleInClass`](is-visible-in-class.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="is-visible-in-class.html"><span class="nf">isVisibleInClass</span></a><span class="p">(</span>classSymbol<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether the given [`KaCallableSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) (possibly inherited from a superclass) is visible in the given [`classSymbol`](is-visible-in-class.md).


</div>

</div>
