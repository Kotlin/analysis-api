---
tags:
 - jvm
title: "NullableConcurrentCache"
---

# NullableConcurrentCache

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-inline/index.html"><span class="se">JvmInline</span></a>
<span class="kd">value </span><span class="kd">class </span><a href="index.html">NullableConcurrentCache</a><span class="o"><</span><a href="index.html">K</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span><a href="index.html">V</a><span class="o">></span><span class="p">(</span><span class="kd">val </span>map<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentMap.html">ConcurrentMap</a><span class="o"><</span><a href="index.html">K</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="o"> = </span>ConcurrentHashMap()<span class="p">)</span>
</span></code></pre></div>A wrapper around a [`ConcurrentMap`](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentMap.html) which stores `null` values returned by the computation in the form of explicit objects.


</div>

## Constructors
### NullableConcurrentCache

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>map<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentMap.html">ConcurrentMap</a><span class="o"><</span><a href="index.html">K</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="o"> = </span>ConcurrentHashMap()<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### map

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#map">map</a><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentMap.html">ConcurrentMap</a><span class="o"><</span><a href="index.html">K</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
## Functions
### getOrPut

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="index.html#getorput"><span class="nf">getOrPut</span></a><span class="p">(</span>key<span class="o">: </span><a href="index.html">K</a><span class="p">, </span><span class="kd">crossinline </span>compute<span class="o">: </span><span class="p">(</span><a href="index.html">K</a><span class="p">)</span><span class="o"> -> </span><a href="index.html">V</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="index.html">V</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the value for the given [`key`](index.md#getorput) if it's contained in the cache, or computes the value with [`compute`](index.md#getorput) outside the cache's computation lock and adds it to the cache.


</div>

</div>
