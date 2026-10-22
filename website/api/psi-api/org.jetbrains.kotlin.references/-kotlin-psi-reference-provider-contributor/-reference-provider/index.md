---
tags:
 - jvm
title: "ReferenceProvider"
---

# ReferenceProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="kd">interface </span><a href="index.html">ReferenceProvider</a><span class="o"><</span><span class="kd">in </span><a href="index.html">T</a><span class="o"> : </span><a href="../../../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="o">></span> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-function1/index.html">Function1</a><span class="o"><</span><a href="index.html">T</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>PsiReference<span class="o">></span><span class="o">> </span>
</span></code></pre></div>Functional interface used to create references for a specific PSI element of type [`T`](index.md). The function must be pure and must return a (possibly empty) list of PsiReferences. Returning an empty list is preferred to doing unnecessary work when the element is not applicable.


</div>

## Functions
### [`invoke`](index.md#invoke)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">operator </span><span class="kd">fun </span><a href="index.html#invoke"><span class="nf">invoke</span></a><span class="p">(</span>p1<span class="o">: </span><a href="index.html">T</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>PsiReference<span class="o">></span>
</span></code></pre></div>
</div>

</div>
