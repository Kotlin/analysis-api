---
tags:
 - jvm
title: "getOrPut"
---

# getOrPut

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="get-or-put.html">K</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span><a href="get-or-put.html">V</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">> </span>Cache<span class="o"><</span><a href="get-or-put.html">K</a><span class="p">, </span><a href="get-or-put.html">V</a><span class="o">></span><span class="p">.</span><a href="get-or-put.html"><span class="nf">getOrPut</span></a><span class="p">(</span>key<span class="o">: </span><a href="get-or-put.html">K</a><span class="p">, </span>compute<span class="o">: </span><span class="p">(</span><a href="get-or-put.html">K</a><span class="p">)</span><span class="o"> -> </span><a href="get-or-put.html">V</a><span class="p">)</span><span class="o">: </span><a href="get-or-put.html">V</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the value for the given [`key`](get-or-put.md) if it's contained in the cache, or computes the value with [`compute`](get-or-put.md) outside the cache's computation lock and adds it to the cache.


</div>

</div>
