---
tags:
 - jvm
title: "KaRendererBuilder"
---

# KaRendererBuilder

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaRendererBuilder</a>
</span></code></pre></div>A mutable builder for customizing a [`KaRenderer`](../-ka-renderer/index.md), available within [`KaRenderer.copy`](../-ka-renderer/index.md#copy).


</div>

## Functions
### get

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#get">T</a><span class="o">> </span><a href="index.html#get"><span class="nf">get</span></a><span class="p">(</span>option<span class="o">: </span><a href="../-ka-rendering-option/index.html">KaRenderingOption</a><span class="o"><</span><a href="index.html#get">T</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="index.html#get">T</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the current effective value of [`option`](index.md#get).


</div>

</div>
### push

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#push">T</a><span class="o">> </span><a href="index.html#push"><span class="nf">push</span></a><span class="p">(</span>renderer<span class="o">: </span><a href="../-ka-piece-renderer/index.html">KaPieceRenderer</a><span class="o"><</span><a href="index.html#push">T</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Pushes [`renderer`](index.md#push) on top of the stack for its [`KaPieceRenderer.piece`](../-ka-piece-renderer/index.md#piece), so it takes precedence over the renderers below it.


</div>

</div>
### push

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#push">T</a><span class="o">> </span><a href="index.html">KaRendererBuilder</a><span class="p">.</span><a href="index.html#push"><span class="nf">push</span></a><span class="p">(</span>piece<span class="o">: </span><a href="../-ka-piece/index.html">KaPiece</a><span class="o"><</span><a href="index.html#push">T</a><span class="o">></span><span class="p">, </span>block<span class="o">: </span><span class="kd">context</span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span><a href="../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">, </span><a href="../-ka-rendering-output/index.html">KaRenderingOutput</a><span class="p">) </span><span class="p">(</span>value<span class="o">: </span><a href="index.html#push">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Pushes a simple, always-consuming [`KaPieceRenderer`](../-ka-piece-renderer/index.md) for the given [`piece`](index.md#push), which is created using the provided rendering [`block`](index.md#push).


</div>

</div>
### pushEmpty

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#pushempty">T</a><span class="o">> </span><a href="index.html">KaRendererBuilder</a><span class="p">.</span><a href="index.html#pushempty"><span class="nf">pushEmpty</span></a><span class="p">(</span>piece<span class="o">: </span><a href="../-ka-piece/index.html">KaPiece</a><span class="o"><</span><a href="index.html#pushempty">T</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Pushes a no-op, always-consuming [`KaPieceRenderer`](../-ka-piece-renderer/index.md) for the given [`piece`](index.md#pushempty).


</div>

</div>
### reset

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#reset">T</a><span class="o">> </span><a href="index.html">KaRendererBuilder</a><span class="p">.</span><a href="index.html#reset"><span class="nf">reset</span></a><span class="p">(</span>option<span class="o">: </span><a href="../-ka-rendering-option/index.html">KaRenderingOption</a><span class="o"><</span><a href="index.html#reset">T</a><span class="o">></span><span class="p">, </span>provider<span class="o">: </span><span class="p">(</span><a href="index.html#reset">T</a><span class="p">)</span><span class="o"> -> </span><a href="index.html#reset">T</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Resets the [`option`](index.md#reset) to a value returned from the [`provider`](index.md#reset) using the previous effective value.


</div>

</div>
### set

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#set">T</a><span class="o">> </span><a href="index.html#set"><span class="nf">set</span></a><span class="p">(</span>option<span class="o">: </span><a href="../-ka-rendering-option/index.html">KaRenderingOption</a><span class="o"><</span><a href="index.html#set">T</a><span class="o">></span><span class="p">, </span>value<span class="o">: </span><a href="index.html#set">T</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Overrides the value of [`option`](index.md#set).


</div>

</div>
### unset

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#unset">T</a><span class="o">> </span><a href="index.html#unset"><span class="nf">unset</span></a><span class="p">(</span>option<span class="o">: </span><a href="../-ka-rendering-option/index.html">KaRenderingOption</a><span class="o"><</span><a href="index.html#unset">T</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Resets [`option`](index.md#unset) back to its [`KaRenderingOption.defaultValue`](../-ka-rendering-option/index.md#defaultvalue).


</div>

</div>
