---
tags:
 - jvm
title: "KaDeprecation"
---

# KaDeprecation

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaDeprecation</a>
</span></code></pre></div>Represents the deprecation status of a symbol.

#### See also


 - [`deprecation`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#deprecation)



</div>

## Properties
### isPropagatedToOverrides

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#ispropagatedtooverrides">isPropagatedToOverrides</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether this deprecation propagates to overriding members.


</div>

</div>
### level

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#level">level</a><span class="o">: </span><a href="../-ka-deprecation-level/index.html">KaDeprecationLevel</a>
</span></code></pre></div>
</div>


<div markdown>

The deprecation level.


</div>

</div>
