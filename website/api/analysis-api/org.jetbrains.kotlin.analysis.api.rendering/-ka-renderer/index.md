---
tags:
 - jvm
title: "KaRenderer"
---

# KaRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaRenderer</a>
</span></code></pre></div>Renders Analysis API entities such as [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md)s or [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)s into a [`KaRenderingOutput`](../-ka-rendering-output/index.md) as human-readable, Kotlin-like text.

A renderer is an immutable bundle of [`KaPieceRenderer`](../-ka-piece-renderer/index.md)s (a stack per [`KaPiece`](../-ka-piece/index.md)) together with [`KaRenderingOption`](../-ka-rendering-option/index.md) values. You can obtain the standard renderer via [`default`](-companion/index.md#default) and derive customized variants with [`copy`](index.md#copy).


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
### copy

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#copy"><span class="nf">copy</span></a><span class="p">(</span>block<span class="o">: </span><a href="../-ka-renderer-builder/index.html">KaRendererBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaRenderer</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a copy of this renderer with the customizations applied by [`block`](index.md#copy) (overriding [`KaRenderingOption`](../-ka-rendering-option/index.md)s or pushing additional [`KaPieceRenderer`](../-ka-piece-renderer/index.md)s). This renderer is left unchanged.

The resulting renderer may call the [`block`](index.md#copy) on-demand. Never rely on exact timing of its call, and keep the [`block`](index.md#copy) free of side effects.


</div>

</div>
### render

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#render">T</a><span class="o">> </span><a href="index.html#render"><span class="nf">render</span></a><span class="p">(</span>
    value<span class="o">: </span><a href="index.html#render">T</a><span class="p">, </span>
    piece<span class="o">: </span><a href="../-ka-piece/index.html">KaPiece</a><span class="o"><</span><a href="index.html#render">T</a><span class="o">></span><span class="p">, </span>
    output<span class="o">: </span><a href="../-ka-rendering-output/index.html">KaRenderingOutput</a>
<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Renders the given [`piece`](index.md#render) [`value`](index.md#render) into the [`output`](index.md#render).


</div>

</div>
### render

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="index.html">KaRenderer</a><span class="p">.</span><a href="index.html#render"><span class="nf">render</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">, </span>output<span class="o">: </span><a href="../-ka-rendering-output/index.html">KaRenderingOutput</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Renders the [`symbol`](index.md#render) into [`output`](index.md#render).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="index.html">KaRenderer</a><span class="p">.</span><a href="index.html#render"><span class="nf">render</span></a><span class="p">(</span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>output<span class="o">: </span><a href="../-ka-rendering-output/index.html">KaRenderingOutput</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Renders the [`type`](index.md#render) into [`output`](index.md#render).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>context<span class="o">: </span><a href="../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">)</span>
<span class="kd">fun </span><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.rendering/index.html">T</a><span class="o">> </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.rendering/index.html"><span class="nf">render</span></a><span class="p">(</span>value<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.rendering/index.html">T</a><span class="p">, </span>piece<span class="o">: </span><a href="../-ka-piece/index.html">KaPiece</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.rendering/index.html">T</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Renders [`value`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.rendering/index.md) as the given [`piece`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.rendering/index.md), dispatching to the corresponding renderer stack.


</div>

</div>
### renderToString

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="index.html">KaRenderer</a><span class="p">.</span><a href="index.html#rendertostring"><span class="nf">renderToString</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NlsSafe</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Renders the [`symbol`](index.md#rendertostring) into a string.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="index.html">KaRenderer</a><span class="p">.</span><a href="index.html#rendertostring"><span class="nf">renderToString</span></a><span class="p">(</span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NlsSafe</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Renders the [`type`](index.md#rendertostring) into a string.


</div>

</div>
