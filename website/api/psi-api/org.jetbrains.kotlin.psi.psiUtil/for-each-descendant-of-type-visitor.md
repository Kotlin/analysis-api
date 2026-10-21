---
tags:
 - jvm
title: "forEachDescendantOfTypeVisitor"
---

# forEachDescendantOfTypeVisitor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="for-each-descendant-of-type-visitor.html">T</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="o">> </span><a href="for-each-descendant-of-type-visitor.html"><span class="nf">forEachDescendantOfTypeVisitor</span></a><span class="p">(</span><span class="kd">noinline </span>block<span class="o">: </span><span class="p">(</span><a href="for-each-descendant-of-type-visitor.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-visitor-void/index.html">KtVisitorVoid</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a recursive visitor that calls [`block`](for-each-descendant-of-type-visitor.md) on each visited element of type [`T`](for-each-descendant-of-type-visitor.md), including the element passed to `accept`. Calls happen in DFS-exit order, so deeper nodes are visited before their ancestors.


</div>

</div>
