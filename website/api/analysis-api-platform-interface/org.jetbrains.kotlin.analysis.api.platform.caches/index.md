---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.platform.caches"
---

# org.jetbrains.kotlin.analysis.api.platform.caches
## Types
### [`NullableCaffeineCache`](-nullable-caffeine-cache/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-inline/index.html"><span class="se">JvmInline</span></a>
<span class="kd">value </span><span class="kd">class </span><a href="-nullable-caffeine-cache/index.html">NullableCaffeineCache</a><span class="o"><</span><a href="-nullable-caffeine-cache/index.html">K</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span><a href="-nullable-caffeine-cache/index.html">V</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">(</span><span class="kd">val </span>cache<span class="o">: </span>Cache<span class="o"><</span><a href="-nullable-caffeine-cache/index.html">K</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

A wrapper around a Caffeine Cache which stores `null` values returned by the computation in the form of explicit objects. On a conceptual level, this allows the cache to store failures so that future accesses to the same key don't recompute the same failure.


</div>

</div>
### [`NullableConcurrentCache`](-nullable-concurrent-cache/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-inline/index.html"><span class="se">JvmInline</span></a>
<span class="kd">value </span><span class="kd">class </span><a href="-nullable-concurrent-cache/index.html">NullableConcurrentCache</a><span class="o"><</span><a href="-nullable-concurrent-cache/index.html">K</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span><a href="-nullable-concurrent-cache/index.html">V</a><span class="o">></span><span class="p">(</span><span class="kd">val </span>map<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentMap.html">ConcurrentMap</a><span class="o"><</span><a href="-nullable-concurrent-cache/index.html">K</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="o"> = </span>ConcurrentHashMap()<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

A wrapper around a [`ConcurrentMap`](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentMap.html) which stores `null` values returned by the computation in the form of explicit objects.


</div>

</div>
### [`NullValue`](-null-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-null-value/index.html">NullValue</a>
</span></code></pre></div>
</div>


<div markdown>

An object used as a representative for `null` in collections which prohibit `null` values.


</div>

</div>
## Functions
### [`getOrPut`](get-or-put.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="get-or-put.html">K</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span><a href="get-or-put.html">V</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">> </span>Cache<span class="o"><</span><a href="get-or-put.html">K</a><span class="p">, </span><a href="get-or-put.html">V</a><span class="o">></span><span class="p">.</span><a href="get-or-put.html"><span class="nf">getOrPut</span></a><span class="p">(</span>key<span class="o">: </span><a href="get-or-put.html">K</a><span class="p">, </span>compute<span class="o">: </span><span class="p">(</span><a href="get-or-put.html">K</a><span class="p">)</span><span class="o"> -> </span><a href="get-or-put.html">V</a><span class="p">)</span><span class="o">: </span><a href="get-or-put.html">V</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the value for the given [`key`](get-or-put.md) if it's contained in the cache, or computes the value with [`compute`](get-or-put.md) outside the cache's computation lock and adds it to the cache.


</div>

</div>
### [`getOrPutWithNullableValue`](get-or-put-with-nullable-value.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="get-or-put-with-nullable-value.html">K</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span><a href="get-or-put-with-nullable-value.html">R</a><span class="o">> </span>Cache<span class="o"><</span><a href="get-or-put-with-nullable-value.html">K</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">.</span><a href="get-or-put-with-nullable-value.html"><span class="nf">getOrPutWithNullableValue</span></a><span class="p">(</span>key<span class="o">: </span><a href="get-or-put-with-nullable-value.html">K</a><span class="p">, </span><span class="kd">crossinline </span>compute<span class="o">: </span><span class="p">(</span><a href="get-or-put-with-nullable-value.html">K</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="get-or-put-with-nullable-value.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

Implements [`Cache.getOrPut`](get-or-put.md) with [`NullValue`](-null-value/index.md) conversion.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="get-or-put-with-nullable-value.html">K</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span><a href="get-or-put-with-nullable-value.html">R</a><span class="o">> </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentMap.html">ConcurrentMap</a><span class="o"><</span><a href="get-or-put-with-nullable-value.html">K</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">.</span><a href="get-or-put-with-nullable-value.html"><span class="nf">getOrPutWithNullableValue</span></a><span class="p">(</span>key<span class="o">: </span><a href="get-or-put-with-nullable-value.html">K</a><span class="p">, </span><span class="kd">crossinline </span>compute<span class="o">: </span><span class="p">(</span><a href="get-or-put-with-nullable-value.html">K</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="get-or-put-with-nullable-value.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

Implements [`ConcurrentMap.getOrPut`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/index.html) with [`NullValue`](-null-value/index.md) conversion.


</div>

</div>
### [`nullValueToNull`](null-value-to-null.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="null-value-to-null.html">V</a><span class="o">> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">.</span><a href="null-value-to-null.html"><span class="nf">nullValueToNull</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="null-value-to-null.html">V</a>
</span></code></pre></div>
</div>


<div markdown>

Converts [`NullValue`](-null-value/index.md) to `null`, and all other instances of [`this`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html) to [`V`](null-value-to-null.md).


</div>

</div>
### [`withStatsCounter`](with-stats-counter.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="with-stats-counter.html">K</a><span class="p">, </span><a href="with-stats-counter.html">V</a><span class="o">> </span>Caffeine<span class="o"><</span><a href="with-stats-counter.html">K</a><span class="p">, </span><a href="with-stats-counter.html">V</a><span class="o">></span><span class="p">.</span><a href="with-stats-counter.html"><span class="nf">withStatsCounter</span></a><span class="p">(</span>statsCounter<span class="o">: </span>StatsCounter<span class="o">?</span><span class="p">)</span><span class="o">: </span>Caffeine<span class="o"><</span><a href="with-stats-counter.html">K</a><span class="p">, </span><a href="with-stats-counter.html">V</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Applies the StatsCounter to the Caffeine cache builder if it's non-null, or otherwise doesn't register it.


</div>

</div>
