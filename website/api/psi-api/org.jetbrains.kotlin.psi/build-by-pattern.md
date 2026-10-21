---
tags:
 - jvm
title: "buildByPattern"
---

# buildByPattern

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="build-by-pattern.html">TElement</a><span class="o">> </span><a href="build-by-pattern.html"><span class="nf">buildByPattern</span></a><span class="p">(</span>factory<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span><a href="build-by-pattern.html">TElement</a><span class="p">, </span>build<span class="o">: </span><a href="-builder-by-pattern/index.html">BuilderByPattern</a><span class="o"><</span><a href="build-by-pattern.html">TElement</a><span class="o">></span><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="build-by-pattern.html">TElement</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`BuilderByPattern`](-builder-by-pattern/index.md), runs [`build`](build-by-pattern.md) on it, and produces the element via [`factory`](build-by-pattern.md). Backs the `KtPsiFactory.build*` entry points.


</div>

</div>
