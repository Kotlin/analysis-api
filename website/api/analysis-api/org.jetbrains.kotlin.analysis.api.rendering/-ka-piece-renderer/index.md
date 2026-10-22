---
tags:
 - jvm
title: "KaPieceRenderer"
---

# KaPieceRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KaPieceRenderer</a><span class="o"><</span><a href="index.html">T</a><span class="o">></span><span class="p">(</span><span class="kd">val </span>piece<span class="o">: </span><a href="../-ka-piece/index.html">KaPiece</a><span class="o"><</span><a href="index.html">T</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>Renders a single [`KaPiece`](../-ka-piece/index.md) into the contextual [`KaRenderingOutput`](../-ka-rendering-output/index.md).

Renderers for a given [`piece`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.rendering/-ka-piece-renderer/--root--.md) form a stack within a [`KaRenderer`](../-ka-renderer/index.md); [`KaRendererBuilder.push`](../-ka-renderer-builder/index.md#push) adds one on top. A renderer may emit nested pieces via the top-level [`render`](index.md#render) function and fall back to the renderer beneath it by invoking its `next` callback.

#### Parameters


 - piece: the piece this renderer is responsible for.





</div>

## Constructors
### KaPieceRenderer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>piece<span class="o">: </span><a href="../-ka-piece/index.html">KaPiece</a><span class="o"><</span><a href="index.html">T</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

**Parameters**



 - piece: the piece this renderer is responsible for.





</div>

</div>
## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Properties
### piece

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#piece">piece</a><span class="o">: </span><a href="../-ka-piece/index.html">KaPiece</a><span class="o"><</span><a href="index.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

**Parameters**



 - piece: the piece this renderer is responsible for.





</div>

</div>
## Functions
### render

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>
    session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    context<span class="o">: </span><a href="../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">, </span>
    output<span class="o">: </span><a href="../-ka-rendering-output/index.html">KaRenderingOutput</a>
<span class="p">)</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#render"><span class="nf">render</span></a><span class="p">(</span>value<span class="o">: </span><a href="index.html">T</a><span class="p">, </span>next<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Renders [`value`](index.md#render) into the contextual [`KaRenderingOutput`](../-ka-rendering-output/index.md). Returns `true` if the value was handled, or `false` to fall back to the renderer beneath this one.

Invoke [`next`](index.md#render) to render [`value`](index.md#render) with the renderer immediately beneath this one. After calling [`next`](index.md#render), you are supposed to return `true`; otherwise, the `next` will render the `value` twice.


</div>

</div>
