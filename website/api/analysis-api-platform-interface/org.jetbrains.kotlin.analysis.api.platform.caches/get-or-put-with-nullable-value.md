---
tags:
 - jvm
title: "getOrPutWithNullableValue"
---

# getOrPutWithNullableValue

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="get-or-put-with-nullable-value.html">K</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span><a href="get-or-put-with-nullable-value.html">R</a><span class="o">> </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentMap.html">ConcurrentMap</a><span class="o"><</span><a href="get-or-put-with-nullable-value.html">K</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">.</span><a href="get-or-put-with-nullable-value.html"><span class="nf">getOrPutWithNullableValue</span></a><span class="p">(</span>key<span class="o">: </span><a href="get-or-put-with-nullable-value.html">K</a><span class="p">, </span><span class="kd">crossinline </span>compute<span class="o">: </span><span class="p">(</span><a href="get-or-put-with-nullable-value.html">K</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="get-or-put-with-nullable-value.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

Implements [`ConcurrentMap.getOrPut`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/index.html) with [`NullValue`](-null-value/index.md) conversion.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="get-or-put-with-nullable-value.html">K</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span><a href="get-or-put-with-nullable-value.html">R</a><span class="o">> </span>Cache<span class="o"><</span><a href="get-or-put-with-nullable-value.html">K</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">.</span><a href="get-or-put-with-nullable-value.html"><span class="nf">getOrPutWithNullableValue</span></a><span class="p">(</span>key<span class="o">: </span><a href="get-or-put-with-nullable-value.html">K</a><span class="p">, </span><span class="kd">crossinline </span>compute<span class="o">: </span><span class="p">(</span><a href="get-or-put-with-nullable-value.html">K</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="get-or-put-with-nullable-value.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

Implements [`Cache.getOrPut`](get-or-put.md) with [`NullValue`](-null-value/index.md) conversion.


</div>

</div>
