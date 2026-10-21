---
tags:
 - jvm
title: "SublistMerger"
---

# SublistMerger

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">SublistMerger</a><span class="o"><</span><a href="index.html">A</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">(</span>initialElements<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">A</a><span class="o">></span><span class="p">, </span><span class="kd">val </span>destination<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-list/index.html">MutableList</a><span class="o"><</span><a href="index.html">A</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>With each call to [`merge`](index.md#merge), [`SublistMerger`](index.md) can merge all elements of a specific (reified) type into a single element using a supplied constructor and then add it to [`destination`](index.md#destination). Unmerged elements are added to [`destination`](index.md#destination) using [`finish`](index.md#finish).

The purpose of [`SublistMerger`](index.md) is to merge multiple different types of elements from a single origin list without the need for intermediate list management and partitionIsInstance boilerplate.


</div>

## Constructors
### SublistMerger

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>initialElements<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">A</a><span class="o">></span><span class="p">, </span>destination<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-list/index.html">MutableList</a><span class="o"><</span><a href="index.html">A</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### destination

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#destination">destination</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-list/index.html">MutableList</a><span class="o"><</span><a href="index.html">A</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### remainingElements

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">var </span><a href="index.html#remainingelements">remainingElements</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">A</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
## Functions
### finish

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#finish"><span class="nf">finish</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### merge

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="index.html#merge">R</a><span class="o"> : </span><a href="index.html">A</a><span class="o">> </span><a href="index.html#merge"><span class="nf">merge</span></a><span class="p">(</span>create<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html#merge">R</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span><a href="index.html">A</a><span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
