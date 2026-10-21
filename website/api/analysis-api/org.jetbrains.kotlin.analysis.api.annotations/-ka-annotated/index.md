---
tags:
 - jvm
title: "KaAnnotated"
---

# KaAnnotated

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaAnnotated</a>
</span></code></pre></div>[`KaAnnotated`](index.md) represents an entity which may have annotations applied to it. All [`types`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)s and almost all [`symbols`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) can have annotations.

#### Inheritors


 - [`KaAnnotatedSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-annotated-symbol/index.md)
 - [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)



</div>

## Properties
### annotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.html#annotations">annotations</a><span class="o">: </span><a href="../-ka-annotation-list/index.html">KaAnnotationList</a>
</span></code></pre></div>
</div>


<div markdown>

A list of annotations applied to the annotated entity.


</div>

</div>
