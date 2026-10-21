---
tags:
 - jvm
title: "KaPiece"
---

# KaPiece

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KaPiece</a><span class="o"><</span><a href="index.html">T</a><span class="o">></span>
</span></code></pre></div>A typed, enumerated key that identifies a specific piece of a symbol or a type to render.

Each [`KaPiece`](index.md) is associated with a stack of [`KaPieceRenderer`](../-ka-piece-renderer/index.md)s in a [`KaRenderer`](../-ka-renderer/index.md). Renderers may render other pieces via [`KaRenderingContext`](../-ka-rendering-context/index.md), which allows customizing individual parts of the output without reimplementing the whole rendering.

The two top-level entry points are [`Symbol`](-companion/index.md#symbol) (renders any [`org.jetbrains.kotlin.analysis.api.symbols.KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md)) and [`Type`](-companion/index.md#type) (renders any [`org.jetbrains.kotlin.analysis.api.types.KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)).


</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
