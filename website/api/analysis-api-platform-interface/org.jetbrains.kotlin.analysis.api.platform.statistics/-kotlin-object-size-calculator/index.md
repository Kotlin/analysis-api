---
tags:
 - jvm
title: "KotlinObjectSizeCalculator"
---

# KotlinObjectSizeCalculator

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinObjectSizeCalculator</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>Provides endpoints for calculating the runtime size of objects.

This interface is not intended to be used in production. It should only be used for statistics purposes.


</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Functions
### shallowSize

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#shallowsize"><span class="nf">shallowSize</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>
</span></code></pre></div>
</div>


<div markdown>

Calculates the shallow runtime size of the given [`value`](index.md#shallowsize) in bytes.

This function is not intended to be used in production. It should only be used for statistics purposes.


</div>

</div>
