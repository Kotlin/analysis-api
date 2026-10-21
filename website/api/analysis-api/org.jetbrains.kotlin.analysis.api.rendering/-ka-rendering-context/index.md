---
tags:
 - jvm
title: "KaRenderingContext"
---

# KaRenderingContext

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaRenderingContext</a>
</span></code></pre></div>The rendering state passed to every [`KaPieceRenderer`](../-ka-piece-renderer/index.md), used to render nested pieces and to read [`KaRenderingOption`](../-ka-rendering-option/index.md) values.


</div>

## Functions
### isInside

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#isinside">T</a><span class="o">> </span><a href="index.html#isinside"><span class="nf">isInside</span></a><span class="p">(</span>piece<span class="o">: </span><a href="../-ka-piece/index.html">KaPiece</a><span class="o"><</span><a href="index.html#isinside">T</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the current renderer has been requested by [`piece`](index.md#isinside) (possibly transitively).

The piece which the current renderer renders is not a requester of itself. Passing that piece therefore detects nesting, such as a [`KaPiece.Type`](../-ka-piece/-companion/index.md#type) which is rendered as a type argument of another [`KaPiece.Type`](../-ka-piece/-companion/index.md#type).


</div>

</div>
### render

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#render">T</a><span class="o">> </span><a href="index.html#render"><span class="nf">render</span></a><span class="p">(</span>value<span class="o">: </span><a href="index.html#render">T</a><span class="p">, </span>piece<span class="o">: </span><a href="../-ka-piece/index.html">KaPiece</a><span class="o"><</span><a href="index.html#render">T</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Renders [`value`](index.md#render) as the given [`piece`](index.md#render), dispatching to the corresponding renderer stack.


</div>

</div>

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

Renders [`value`](index.md#render) as the given [`piece`](index.md#render), dispatching to the corresponding renderer stack, but writes the result into [`output`](index.md#render) instead of the output of the current rendering. Nested pieces are written into [`output`](index.md#render) as well.

This allows a renderer to capture the rendered form of a piece, e.g. to post-process it or to render it as a single fragment.


</div>

</div>
### valueFor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#valuefor">T</a><span class="o">> </span><a href="index.html#valuefor"><span class="nf">valueFor</span></a><span class="p">(</span>option<span class="o">: </span><a href="../-ka-rendering-option/index.html">KaRenderingOption</a><span class="o"><</span><a href="index.html#valuefor">T</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="index.html#valuefor">T</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the effective value of [`option`](index.md#valuefor) for this renderer (the overridden value, or its [`KaRenderingOption.defaultValue`](../-ka-rendering-option/index.md#defaultvalue)).


</div>

</div>
