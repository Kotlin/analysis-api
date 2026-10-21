---
tags:
 - jvm
title: "KaContextReceiversRenderer"
---

# KaContextReceiversRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KaContextReceiversRenderer</a><span class="p">(</span><span class="kd">val </span>contextReceiverListRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.base.contextReceivers.renderers/-ka-context-receiver-list-renderer/index.html">KaContextReceiverListRenderer</a><span class="p">, </span><span class="kd">val </span>contextReceiverLabelRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.base.contextReceivers.renderers/-ka-context-receiver-label-renderer/index.html">KaContextReceiverLabelRenderer</a><span class="p">)</span>
</span></code></pre></div>
</div>

## Constructors
### KaContextReceiversRenderer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>contextReceiverListRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.base.contextReceivers.renderers/-ka-context-receiver-list-renderer/index.html">KaContextReceiverListRenderer</a><span class="p">, </span>contextReceiverLabelRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.base.contextReceivers.renderers/-ka-context-receiver-label-renderer/index.html">KaContextReceiverLabelRenderer</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Types
### [`Builder`](-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-builder/index.html">Builder</a>
</span></code></pre></div>
</div>

</div>
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Properties
### contextReceiverLabelRenderer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#contextreceiverlabelrenderer">contextReceiverLabelRenderer</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.base.contextReceivers.renderers/-ka-context-receiver-label-renderer/index.html">KaContextReceiverLabelRenderer</a>
</span></code></pre></div>
</div>

</div>
### contextReceiverListRenderer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#contextreceiverlistrenderer">contextReceiverListRenderer</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.base.contextReceivers.renderers/-ka-context-receiver-list-renderer/index.html">KaContextReceiverListRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderContextReceivers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#rendercontextreceivers"><span class="nf">renderContextReceivers</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    owner<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.base/-ka-context-receivers-owner/index.html">KaContextReceiversOwner</a><span class="p">, </span>
    typeRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.types/-ka-type-renderer/index.html">KaTypeRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### with

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="index.html#with"><span class="nf">with</span></a><span class="p">(</span>action<span class="o">: </span><a href="-builder/index.html">KaContextReceiversRenderer.Builder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaContextReceiversRenderer</a>
</span></code></pre></div>
</div>

</div>
