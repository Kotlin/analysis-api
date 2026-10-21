---
tags:
 - jvm
title: "KaCallableImplementationState"
---

# KaCallableImplementationState

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">KaCallableImplementationState</a>
</span></code></pre></div><strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.symbols.KaCallableImplementationState</strong>`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-implementation-state/index.md)<strong> instead.</strong>

Describes the implementation state of a [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) in the context of a specific [`KaClassSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md).

An implementation state captures whether a callable is explicitly implemented in the class, has an inherited implementation, can be overridden, or must be explicitly overridden.

#### See also


 - [`KaSymbolRelationProvider.implementationState`](../-ka-symbol-relation-provider/index.md#implementationstate)


#### Inheritors


 - [`Explicit`](-explicit/index.md)
 - [`Inherited`](-inherited/index.md)
 - [`Missing`](-missing/index.md)



</div>

## Types
### [`Explicit`](-explicit/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-explicit/index.html">Explicit</a> : <a href="index.html">KaCallableImplementationState</a>
</span></code></pre></div>
</div>


<div markdown>

The declaration is directly implemented or explicitly overridden in the target class.


</div>

</div>
### [`Inherited`](-inherited/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-inherited/index.html">Inherited</a> : <a href="index.html">KaCallableImplementationState</a>
</span></code></pre></div>
</div>


<div markdown>

The declaration has the implementation provided by a supertype or multiple supertypes, and <strong>does not</strong> have explicit implementation in the target class.


</div>

</div>
### [`Missing`](-missing/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-missing/index.html">Missing</a> : <a href="index.html">KaCallableImplementationState</a>
</span></code></pre></div>
</div>


<div markdown>

The declaration is neither implemented in the target class, nor it has inherited implementations.


</div>

</div>
