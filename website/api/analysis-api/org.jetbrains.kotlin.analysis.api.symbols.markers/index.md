---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.symbols.markers"
---

# org.jetbrains.kotlin.analysis.api.symbols.markers
## Types
### [`KaAnnotatedSymbol`](-ka-annotated-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-annotated-symbol/index.html">KaAnnotatedSymbol</a> : <a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a>, <a href="../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) representing a declaration which may have annotations applied to it.


</div>

</div>
### [`KaDeclarationContainerSymbol`](-ka-declaration-container-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a> : <a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) which may contain declarations. These declarations may be accessed through the [`KaScope`](../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md)s provided by [`KaScopeProvider`](../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md).


</div>

</div>
### [`KaNamedSymbol`](-ka-named-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-named-symbol/index.html">KaNamedSymbol</a> : <a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) with a [`name`](-ka-named-symbol/index.md#name).


</div>

</div>
