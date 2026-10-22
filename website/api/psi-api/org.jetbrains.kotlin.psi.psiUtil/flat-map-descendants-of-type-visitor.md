---
tags:
 - jvm
title: "flatMapDescendantsOfTypeVisitor"
---

# flatMapDescendantsOfTypeVisitor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="flat-map-descendants-of-type-visitor.html">T</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">, </span><a href="flat-map-descendants-of-type-visitor.html">R</a><span class="o">> </span><a href="flat-map-descendants-of-type-visitor.html"><span class="nf">flatMapDescendantsOfTypeVisitor</span></a><span class="p">(</span>accumulator<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-collection/index.html">MutableCollection</a><span class="o"><</span><a href="flat-map-descendants-of-type-visitor.html">R</a><span class="o">></span><span class="p">, </span><span class="kd">noinline </span>map<span class="o">: </span><span class="p">(</span><a href="flat-map-descendants-of-type-visitor.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="flat-map-descendants-of-type-visitor.html">R</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-visitor-void/index.html">KtVisitorVoid</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a recursive visitor that maps each visited element of type [`T`](flat-map-descendants-of-type-visitor.md), including the element passed to `accept`, and adds all results to [`accumulator`](flat-map-descendants-of-type-visitor.md) in DFS-exit order.


</div>

</div>
