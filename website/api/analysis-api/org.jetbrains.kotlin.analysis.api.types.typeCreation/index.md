---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.types.typeCreation"
---

# org.jetbrains.kotlin.analysis.api.types.typeCreation
## Types
### [`KaArrayTypeBuilder`](-ka-array-type-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-array-type-builder/index.html">KaArrayTypeBuilder</a> : <a href="-ka-type-builder-with-annotations/index.html">KaTypeBuilderWithAnnotations</a>
</span></code></pre></div>
</div>


<div markdown>

A builder for array types.


</div>

</div>
### [`KaCapturedTypeBuilder`](-ka-captured-type-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-captured-type-builder/index.html">KaCapturedTypeBuilder</a> : <a href="-ka-type-builder-with-annotations/index.html">KaTypeBuilderWithAnnotations</a>
</span></code></pre></div>
</div>


<div markdown>

A builder for [`KaCapturedType`](../org.jetbrains.kotlin.analysis.api.types/-ka-captured-type/index.md).


</div>

</div>
### [`KaClassTypeBuilder`](-ka-class-type-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-class-type-builder/index.html">KaClassTypeBuilder</a> : <a href="-ka-type-builder-with-annotations/index.html">KaTypeBuilderWithAnnotations</a>
</span></code></pre></div>
</div>


<div markdown>

A builder for [`KaClassType`](../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.md).


</div>

</div>
### [`KaDefinitelyNotNullTypeBuilder`](-ka-definitely-not-null-type-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-definitely-not-null-type-builder/index.html">KaDefinitelyNotNullTypeBuilder</a> : <a href="-ka-type-builder-with-annotations/index.html">KaTypeBuilderWithAnnotations</a>
</span></code></pre></div>
</div>


<div markdown>

A builder for [`KaDefinitelyNotNullType`](../org.jetbrains.kotlin.analysis.api.types/-ka-definitely-not-null-type/index.md).


</div>

</div>
### [`KaDynamicTypeBuilder`](-ka-dynamic-type-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-dynamic-type-builder/index.html">KaDynamicTypeBuilder</a> : <a href="-ka-type-builder-with-annotations/index.html">KaTypeBuilderWithAnnotations</a>
</span></code></pre></div>
</div>


<div markdown>

A builder for [`KaDynamicType`](../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.md).


</div>

</div>
### [`KaFlexibleTypeBuilder`](-ka-flexible-type-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-flexible-type-builder/index.html">KaFlexibleTypeBuilder</a> : <a href="-ka-type-builder-with-annotations/index.html">KaTypeBuilderWithAnnotations</a>
</span></code></pre></div>
</div>


<div markdown>

A builder for [`KaFlexibleType`](../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md).


</div>

</div>
### [`KaFunctionTypeBuilder`](-ka-function-type-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-function-type-builder/index.html">KaFunctionTypeBuilder</a> : <a href="-ka-type-builder-with-annotations/index.html">KaTypeBuilderWithAnnotations</a>
</span></code></pre></div>
</div>


<div markdown>

A builder for [`KaFunctionType`](../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.md).


</div>

</div>
### [`KaIntersectionTypeBuilder`](-ka-intersection-type-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-intersection-type-builder/index.html">KaIntersectionTypeBuilder</a> : <a href="-ka-type-builder/index.html">KaTypeBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

A builder for [`KaIntersectionType`](../org.jetbrains.kotlin.analysis.api.types/-ka-intersection-type/index.md).


</div>

</div>
### [`KaTypeBuilder`](-ka-type-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type-builder/index.html">KaTypeBuilder</a> : <a href="-ka-type-creator/index.html">KaTypeCreator</a>
</span></code></pre></div>
</div>


<div markdown>

A base interface for all concrete type builders.


</div>

</div>
### [`KaTypeBuilderWithAnnotations`](-ka-type-builder-with-annotations/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type-builder-with-annotations/index.html">KaTypeBuilderWithAnnotations</a> : <a href="-ka-type-builder/index.html">KaTypeBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

A builder interface derived from [`KaTypeBuilder`](-ka-type-builder/index.md) allowing creating annotated types.


</div>

</div>
### [`KaTypeCreator`](-ka-type-creator/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type-creator/index.html">KaTypeCreator</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

An entry point for type building facilities.


</div>

</div>
### [`KaTypeCreatorDslMarker`](-ka-type-creator-dsl-marker/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-dsl-marker/index.html"><span class="se">DslMarker</span></a>
<span class="kd">annotation class </span><a href="-ka-type-creator-dsl-marker/index.html">KaTypeCreatorDslMarker</a>
</span></code></pre></div>
</div>


<div markdown>

A DSL marker used to annotate entities related to the type building infrastructure in [`KaTypeCreator`](-ka-type-creator/index.md).


</div>

</div>
### [`KaTypeParameterTypeBuilder`](-ka-type-parameter-type-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type-parameter-type-builder/index.html">KaTypeParameterTypeBuilder</a> : <a href="-ka-type-builder-with-annotations/index.html">KaTypeBuilderWithAnnotations</a>
</span></code></pre></div>
</div>


<div markdown>

A builder for [`KaTypeParameterType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.md).


</div>

</div>
## Properties
### [`typeCreator`](type-creator.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="type-creator.html">typeCreator</a><span class="o">: </span><a href="-ka-type-creator/index.html">KaTypeCreator</a>
</span></code></pre></div>
</div>


<div markdown>

A single entry point for the type building infrastructure.


</div>

</div>
## Functions
### [`copy`](copy.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><span class="o"><</span><a href="copy.html">T</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.html">KaClassType</a><span class="o">> </span><a href="copy.html">T</a><span class="p">.</span><a href="copy.html"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.html">KaClassType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaClassType`](../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.md) with modifications applied via the [`init`](copy.md) block.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.html">KaFunctionType</a><span class="p">.</span><a href="copy.html"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="-ka-function-type-builder/index.html">KaFunctionTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.html">KaFunctionType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaFunctionType`](../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.md) with modifications applied via the [`init`](copy.md) block.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a><span class="p">.</span><a href="copy.html"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="-ka-type-parameter-type-builder/index.html">KaTypeParameterTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaTypeParameterType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.md) with modifications applied via the [`init`](copy.md) block.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/index.html">KaUsualClassType</a><span class="p">.</span><a href="copy.html"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/index.html">KaUsualClassType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaUsualClassType`](../org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/index.md) with modifications applied via the [`init`](copy.md) block.


</div>

</div>
