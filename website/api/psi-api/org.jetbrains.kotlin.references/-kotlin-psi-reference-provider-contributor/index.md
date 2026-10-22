---
tags:
 - jvm
title: "KotlinPsiReferenceProviderContributor"
---

# KotlinPsiReferenceProviderContributor

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinPsiReferenceProviderContributor</a><span class="o"><</span><a href="index.html">T</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="o">></span>
</span></code></pre></div>Extension-point contributor for Kotlin PSI reference providers.

The EP allows registering custom reference contributors for [`KtElement`](../../org.jetbrains.kotlin.psi/-kt-element/index.md)s.

Contributors are supposed to be registered via the `org.jetbrains.kotlin.psiReferenceProvider` EP. Each contributor binds a particular PSI element type (represented by [`elementClass`](index.md#elementclass)) to a [`referenceProvider`](index.md#referenceprovider) function which may produce PsiReferences for a given element instance.

Implementation notes for contributors:

 - Keep [`referenceProvider`](index.md#referenceprovider) fast and side‑effect free; return an empty list when no references should be produced.


 - Perform inexpensive guards before any expensive analysis (e.g., quick kind checks, token/parent filters) to minimize overhead.



</div>

## Types
### [`ReferenceProvider`](-reference-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="kd">interface </span><a href="-reference-provider/index.html">ReferenceProvider</a><span class="o"><</span><span class="kd">in </span><a href="-reference-provider/index.html">T</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="o">></span> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-function1/index.html">Function1</a><span class="o"><</span><a href="-reference-provider/index.html">T</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>PsiReference<span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Functional interface used to create references for a specific PSI element of type [`T`](-reference-provider/index.md). The function must be pure and must return a (possibly empty) list of PsiReferences. Returning an empty list is preferred to doing unnecessary work when the element is not applicable.


</div>

</div>
## Properties
### elementClass

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#elementclass">elementClass</a><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><span class="kd">out </span><a href="index.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The base PSI class this contributor applies to. A contributor is considered applicable to an element if `elementClass.isAssignableFrom(element.javaClass)`


</div>

</div>
### referenceProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#referenceprovider">referenceProvider</a><span class="o">: </span><a href="-reference-provider/index.html">KotlinPsiReferenceProviderContributor.ReferenceProvider</a><span class="o"><</span><a href="index.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The function that produces references for elements of [`elementClass`](index.md#elementclass)


</div>

</div>
