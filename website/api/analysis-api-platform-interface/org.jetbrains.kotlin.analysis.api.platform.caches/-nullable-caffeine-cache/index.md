---
tags:
 - jvm
title: "NullableCaffeineCache"
---

# NullableCaffeineCache

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-inline/index.html"><span class="se">JvmInline</span></a>
<span class="kd">value </span><span class="kd">class </span><a href="index.html">NullableCaffeineCache</a><span class="o"><</span><a href="index.html">K</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span><a href="index.html">V</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">(</span><span class="kd">val </span>cache<span class="o">: </span>Cache<span class="o"><</span><a href="index.html">K</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>A wrapper around a Caffeine Cache which stores `null` values returned by the computation in the form of explicit objects. On a conceptual level, this allows the cache to store failures so that future accesses to the same key don't recompute the same failure.


</div>

## Constructors
### NullableCaffeineCache

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>cache<span class="o">: </span>Cache<span class="o"><</span><a href="index.html">K</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>configure<span class="o">: </span><span class="p">(</span>Caffeine<span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span>Caffeine<span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a new [`NullableCaffeineCache`](index.md) by configuring a Caffeine builder with [`configure`](../../../analysis-api-platform-interface/org.jetbrains.kotlin.analysis.api.platform.caches/-nullable-caffeine-cache/--root--.md).


</div>

</div>
## Properties
### cache

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#cache">cache</a><span class="o">: </span>Cache<span class="o"><</span><a href="index.html">K</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### estimatedSize

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#estimatedsize">estimatedSize</a><span class="o">: </span><span class="se">@</span><span class="se">NonNegative</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the approximate number of entries in the cache.


</div>

</div>
## Functions
### get

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="index.html#get"><span class="nf">get</span></a><span class="p">(</span>key<span class="o">: </span><a href="index.html">K</a><span class="p">, </span><span class="kd">crossinline </span>compute<span class="o">: </span><span class="p">(</span><a href="index.html">K</a><span class="p">)</span><span class="o"> -> </span><a href="index.html">V</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="index.html">V</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the value for the given [`key`](index.md#get) if it's contained in the cache, or computes the value with [`compute`](index.md#get) and adds it to the cache.


</div>

</div>
### getOrPut

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="index.html#getorput"><span class="nf">getOrPut</span></a><span class="p">(</span>key<span class="o">: </span><a href="index.html">K</a><span class="p">, </span><span class="kd">crossinline </span>compute<span class="o">: </span><span class="p">(</span><a href="index.html">K</a><span class="p">)</span><span class="o"> -> </span><a href="index.html">V</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="index.html">V</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the value for the given [`key`](index.md#getorput) if it's contained in the cache, or computes the value with [`compute`](index.md#getorput) outside the cache's computation lock and adds it to the cache.


</div>

</div>
