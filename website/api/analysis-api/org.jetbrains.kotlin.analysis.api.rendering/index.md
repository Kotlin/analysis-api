---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.rendering"
---

# org.jetbrains.kotlin.analysis.api.rendering
## Types
### [`KaClassTypeQualification`](-ka-class-type-qualification/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-class-type-qualification/index.html">KaClassTypeQualification</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-class-type-qualification/index.html">KaClassTypeQualification</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Controls how qualified the name of a class type is rendered.


</div>

</div>
### [`KaClassTypeRenderingMode`](-ka-class-type-rendering-mode/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-class-type-rendering-mode/index.html">KaClassTypeRenderingMode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-class-type-rendering-mode/index.html">KaClassTypeRenderingMode</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Controls how a class type which involves a type alias is rendered: either as the abbreviation (the type alias application, e.g. `foo.bar.StringAlias`) or as its expansion (e.g. `kotlin.String`), optionally with the other one in a comment.


</div>

</div>
### [`KaPiece`](-ka-piece/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-piece/index.html">KaPiece</a><span class="o"><</span><a href="-ka-piece/index.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A typed, enumerated key that identifies a specific piece of a symbol or a type to render.


</div>

</div>
### [`KaPieceRenderer`](-ka-piece-renderer/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-ka-piece-renderer/index.html">KaPieceRenderer</a><span class="o"><</span><a href="-ka-piece-renderer/index.html">T</a><span class="o">></span><span class="p">(</span><span class="kd">val </span>piece<span class="o">: </span><a href="-ka-piece/index.html">KaPiece</a><span class="o"><</span><a href="-ka-piece-renderer/index.html">T</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Renders a single [`KaPiece`](-ka-piece/index.md) into the contextual [`KaRenderingOutput`](-ka-rendering-output/index.md).


</div>

</div>
### [`KaRenderer`](-ka-renderer/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-renderer/index.html">KaRenderer</a>
</span></code></pre></div>
</div>


<div markdown>

Renders Analysis API entities such as [`KaSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md)s or [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)s into a [`KaRenderingOutput`](-ka-rendering-output/index.md) as human-readable, Kotlin-like text.


</div>

</div>
### [`KaRendererBuilder`](-ka-renderer-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-renderer-builder/index.html">KaRendererBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

A mutable builder for customizing a [`KaRenderer`](-ka-renderer/index.md), available within [`KaRenderer.copy`](-ka-renderer/index.md#copy).


</div>

</div>
### [`KaRendererBuilderDslMarker`](-ka-renderer-builder-dsl-marker/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-dsl-marker/index.html"><span class="se">DslMarker</span></a>
<span class="kd">annotation class </span><a href="-ka-renderer-builder-dsl-marker/index.html">KaRendererBuilderDslMarker</a>
</span></code></pre></div>
</div>


<div markdown>

A DSL marker used to annotate entities related to the renderer customization in [`KaRendererBuilder`](-ka-renderer-builder/index.md).


</div>

</div>
### [`KaRenderingContext`](-ka-rendering-context/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-rendering-context/index.html">KaRenderingContext</a>
</span></code></pre></div>
</div>


<div markdown>

The rendering state passed to every [`KaPieceRenderer`](-ka-piece-renderer/index.md), used to render nested pieces and to read [`KaRenderingOption`](-ka-rendering-option/index.md) values.


</div>

</div>
### [`KaRenderingOption`](-ka-rendering-option/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-rendering-option/index.html">KaRenderingOption</a><span class="o"><</span><a href="-ka-rendering-option/index.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A typed configuration flag that influences rendering. Its [`defaultValue`](-ka-rendering-option/index.md#defaultvalue) is used unless overridden via [`KaRendererBuilder.set`](-ka-renderer-builder/index.md#set).


</div>

</div>
### [`KaRenderingOutput`](-ka-rendering-output/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-rendering-output/index.html">KaRenderingOutput</a>
</span></code></pre></div>
</div>


<div markdown>

A destination for rendered output. A [`KaRenderer`](-ka-renderer/index.md) writes text fragments, each tagged with [`KaTextAttribute`](-ka-text-attribute/index.md)s that describe its semantic role, so an output may add syntax highlighting, produce plain text, or ignore the attributes entirely.


</div>

</div>
### [`KaTextAttribute`](-ka-text-attribute/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-text-attribute/index.html">KaTextAttribute</a>
</span></code></pre></div>
</div>


<div markdown>

Describes the semantic role of a fragment of rendered text, e.g. for syntax highlighting.


</div>

</div>
### [`KaTypeApproximation`](-ka-type-approximation/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-type-approximation/index.html">KaTypeApproximation</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-type-approximation/index.html">KaTypeApproximation</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Controls whether rendered types are approximated to denotable types (types which can be written in Kotlin source code), and in which direction.


</div>

</div>
## Properties
### [`output`](output.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>output<span class="o">: </span><a href="-ka-rendering-output/index.html">KaRenderingOutput</a><span class="p">)</span>
<span class="kd">val </span><a href="output.html">output</a><span class="o">: </span><a href="-ka-rendering-output/index.html">KaRenderingOutput</a>
</span></code></pre></div>
</div>


<div markdown>

A convenience property allowing to get the [`KaRenderingOutput`](-ka-rendering-output/index.md) inside the rendering block without `contextOf<KaRenderingOutput>()`.


</div>

</div>
## Functions
