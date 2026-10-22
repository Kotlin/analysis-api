---
tags:
 - jvm
title: "KtReference"
---

# KtReference

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.psi/-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KtReference</a> : PsiPolyVariantReference
</span></code></pre></div>
</div>

## Properties
### [`absoluteRange`](index.md#absoluterange)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">val </span><a href="index.html#absoluterange">absoluteRange</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> TextRange
</span></code></pre></div>
</div>

</div>
### [`canonicalText`](index.md#canonicaltext)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="se">@get:</span><span class="se">NlsSafe</span>
<span class="kd">abstract </span><span class="kd">val </span><a href="index.html#canonicaltext">canonicalText</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <span class="se">@</span><span class="se">NlsSafe</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### element

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#element">element</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>

</div>
### [`isSoft`](index.md#issoft)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#issoft">isSoft</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`rangeInElement`](index.md#rangeinelement)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">abstract </span><span class="kd">val </span><a href="index.html#rangeinelement">rangeInElement</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> TextRange
</span></code></pre></div>
</div>

</div>
### resolver

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#resolver">resolver</a><span class="o">: </span>ResolveCache.PolyVariantResolver<span class="o"><</span><a href="index.html">KtReference</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### resolvesByNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#resolvesbynames">resolvesByNames</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Exhaustive collection of names that this reference may resolve to, or an empty collection if it cannot be predicted.

**Exceptional cases**

Note that there might be cases where the resolved element won't have a name from this [`resolvesByNames`](index.md#resolvesbynames) collection, so the client should handle it accordingly.

Here is a list of known cases:

 - Import aliases


 -  - E.g., a function might be imported with a different name (and called via it), so the result name won't be the same



 - Implicit companion object usages


 -  - If you have a companion object, and you use it implicitly via the class (e.g., [`String`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) as an expression will be resolved to [`String.Companion`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/-companion/index.html))



 - Constructor references


 -  - Constructors don't have a name by their nature, but [`resolvesByNames`](index.md#resolvesbynames) has the class name instead



**Unpredictable cases**

 - `this`/`super` usages


 -  - [`KtNameReferenceExpression`](../../org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md) from [`KtInstanceExpressionWithLabel`](../../org.jetbrains.kotlin.psi/-kt-instance-expression-with-label/index.md) or KDocReference is context-sensitive and might be resolved to anonymous elements,     so the result cannot be fully expressed in the terms of this API



 - Labels


 -  - [`KtLabelReferenceExpression`](../../org.jetbrains.kotlin.psi/-kt-label-reference-expression/index.md) is context-sensitive and might be resolved to anonymous elements,     so the result cannot be fully expressed in the terms of this API



 - KtConstructorDelegationReference


 -  - It resolves into constructors, but the result class name cannot be predicted properly since it might be generated by compiler plugins



**Return**

an exhaustive collection of names that this reference may resolve to, or an empty collection if it cannot be predicted


</div>

</div>
### [`variants`](index.md#variants)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="index.html#variants">variants</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>
## Functions
### [`bindToElement`](index.md#bindtoelement)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#bindtoelement"><span class="nf">bindToElement</span></a><span class="p">(</span>p0<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### getElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getelement"><span class="nf">getElement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>

</div>
### [`handleElementRename`](index.md#handleelementrename)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#handleelementrename"><span class="nf">handleElementRename</span></a><span class="p">(</span>p0<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`isReferenceTo`](index.md#isreferenceto)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#isreferenceto"><span class="nf">isReferenceTo</span></a><span class="p">(</span>p0<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`multiResolve`](index.md#multiresolve)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#multiresolve"><span class="nf">multiResolve</span></a><span class="p">(</span>p0<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span>ResolveResult<span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`resolve`](index.md#resolve)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolve"><span class="nf">resolve</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
