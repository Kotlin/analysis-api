---
tags:
 - jvm
title: "commonSupertype"
---

# commonSupertype

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/index.html">Iterable</a><span class="o"><</span><a href="-ka-type/index.html">KaType</a><span class="o">></span><span class="p">.</span><a href="common-supertype.html">commonSupertype</a><span class="o">: </span><a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The common supertype of the given [`KaType`](-ka-type/index.md)s.

#### Throws


[`IllegalArgumentException`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html)

:   If the collection of types is empty.





</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="-ka-type/index.html">KaType</a><span class="o">></span><span class="p">.</span><a href="common-supertype.html">commonSupertype</a><span class="o">: </span><a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The common supertype of the given [`KaType`](-ka-type/index.md)s.

#### Throws


[`IllegalArgumentException`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html)

:   If the array of types is empty.





</div>

</div>
