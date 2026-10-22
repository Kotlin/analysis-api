---
tags:
 - jvm
title: "KaContextSensitiveResolutionStatus"
---

# KaContextSensitiveResolutionStatus

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">KaContextSensitiveResolutionStatus</a>
</span></code></pre></div>Describes how [context-sensitive resolution](https://github.com/Kotlin/KEEP/issues/379) (CSR) relates to a [`org.jetbrains.kotlin.psi.KtSimpleNameExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.md).

It tells both whether the name is already resolved through CSR and whether CSR could be used to drop an otherwise redundant qualifier or import. IDE inspections and shorteners can use this information to suggest removing such qualifiers and imports.

The information is available even when the `-Xcontext-sensitive-resolution` feature is not enabled.

The status of a particular name is obtained via the `contextSensitiveResolutionStatus` property declared in [`KaResolver`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md).

#### Inheritors


 - [`NotAvailable`](-not-available/index.md)
 - [`Used`](-used/index.md)
 - [`QualifierCanBeRemoved`](-qualifier-can-be-removed/index.md)
 - [`ImportCanBeRemoved`](-import-can-be-removed/index.md)



</div>

## Types
### [`ImportCanBeRemoved`](-import-can-be-removed/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-import-can-be-removed/index.html">ImportCanBeRemoved</a> : <a href="index.html">KaContextSensitiveResolutionStatus</a>
</span></code></pre></div>
</div>


<div markdown>

The name is resolved through an import which can be removed: context-sensitive resolution would resolve the same symbol without it.


</div>

</div>
### [`NotAvailable`](-not-available/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-not-available/index.html">NotAvailable</a> : <a href="index.html">KaContextSensitiveResolutionStatus</a>
</span></code></pre></div>
</div>


<div markdown>

Context-sensitive resolution is neither used by, nor applicable to, the name.


</div>

</div>
### [`QualifierCanBeRemoved`](-qualifier-can-be-removed/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-qualifier-can-be-removed/index.html">QualifierCanBeRemoved</a> : <a href="index.html">KaContextSensitiveResolutionStatus</a>
</span></code></pre></div>
</div>


<div markdown>

The name is resolved through an explicit qualifier which can be removed: context-sensitive resolution would resolve the same symbol without it.


</div>

</div>
### [`Used`](-used/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-used/index.html">Used</a> : <a href="index.html">KaContextSensitiveResolutionStatus</a>
</span></code></pre></div>
</div>


<div markdown>

The name is already resolved through context-sensitive resolution.


</div>

</div>
