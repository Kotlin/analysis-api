---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.symbols.pointers"
---

# org.jetbrains.kotlin.analysis.api.symbols.pointers
## Types
### [`KaSymbolPointer`](-ka-symbol-pointer/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-symbol-pointer/index.html">KaSymbolPointer</a><span class="o"><</span><span class="kd">out </span><a href="-ka-symbol-pointer/index.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

[`KaSymbolPointer`](-ka-symbol-pointer/index.md) allows to point to a [`KaSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) and later retrieve it in another [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md). A pointer is necessary because [`KaSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md)s cannot be shared past the boundaries of the [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) they were created in, as they are valid only there.


</div>

</div>
## Functions
