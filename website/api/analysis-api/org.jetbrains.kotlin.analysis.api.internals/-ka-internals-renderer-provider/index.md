---
tags:
 - jvm
title: "KaInternalsRendererProvider"
---

# KaInternalsRendererProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaInternalsRendererProvider</a>
</span></code></pre></div>An implementation-agnostic facade for the default [`KaRenderer`](../../org.jetbrains.kotlin.analysis.api.rendering/-ka-renderer/index.md).


</div>

## Properties
### defaultRenderer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#defaultrenderer">defaultRenderer</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.rendering/-ka-renderer/index.html">KaRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### createStringRenderingOutput

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createstringrenderingoutput"><span class="nf">createStringRenderingOutput</span></a><span class="p">(</span>indentationUnit<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.rendering/-ka-rendering-output/index.html">KaRenderingOutput</a>
</span></code></pre></div>
</div>

</div>
