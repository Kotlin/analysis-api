---
tags:
 - jvm
title: "render"
---

# render

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="render.html"><span class="nf">render</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Renders the given [`KaDeclarationSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) to a string using the default rendering strategy ([`KaDeclarationRendererForSource.WITH_QUALIFIED_NAMES`](../org.jetbrains.kotlin.analysis.api.renderer.declarations.impl/-ka-declaration-renderer-for-source/index.md#with_qualified_names)).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="render.html"><span class="nf">render</span></a><span class="p">(</span>renderer<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Renders the given [`KaDeclarationSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) to a string. The particular rendering strategy is defined by the [`renderer`](render.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="render.html"><span class="nf">render</span></a><span class="p">(</span>position<span class="o">: </span>Variance<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Renders the given [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) into a string using the default rendering strategy ([`KaTypeRendererForSource.WITH_QUALIFIED_NAMES`](../org.jetbrains.kotlin.analysis.api.renderer.types.impl/-ka-type-renderer-for-source/index.md#with_qualified_names)).

[`position`](render.md) controls the way the given type is approximated using [`KaTypeRenderer.typeApproximator`](../org.jetbrains.kotlin.analysis.api.renderer.types/-ka-type-renderer/index.md#typeapproximator).

Specifically, when [`KaRendererTypeApproximator.TO_DENOTABLE`](../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-renderer-type-approximator/-t-o_-d-e-n-o-t-a-b-l-e/index.md) is used, no approximation is performed for Variance.INVARIANT, a denotable subtype is rendered for Variance.IN_VARIANCE, and a denotable supertype is rendered for Variance.OUT_VARIANCE.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="render.html"><span class="nf">render</span></a><span class="p">(</span>renderer<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.renderer.types/-ka-type-renderer/index.html">KaTypeRenderer</a><span class="p">, </span>position<span class="o">: </span>Variance<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Renders the given [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) into a string. The particular rendering strategy is defined by the [`renderer`](render.md).

[`position`](render.md) controls the way the given type is approximated using [`KaTypeRenderer.typeApproximator`](../org.jetbrains.kotlin.analysis.api.renderer.types/-ka-type-renderer/index.md#typeapproximator).

Specifically, when [`KaRendererTypeApproximator.TO_DENOTABLE`](../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-renderer-type-approximator/-t-o_-d-e-n-o-t-a-b-l-e/index.md) is used, no approximation is performed for Variance.INVARIANT, a denotable subtype is rendered for Variance.IN_VARIANCE, and a denotable supertype is rendered for Variance.OUT_VARIANCE.


</div>

</div>
