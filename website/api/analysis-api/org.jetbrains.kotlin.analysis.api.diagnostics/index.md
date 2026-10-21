---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.diagnostics"
---

# org.jetbrains.kotlin.analysis.api.diagnostics
## Types
### [`KaDiagnostic`](-ka-diagnostic/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-diagnostic/index.html">KaDiagnostic</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

A diagnostic message reported by the compiler checker.


</div>

</div>
### [`KaDiagnosticCheckerKind`](-ka-diagnostic-checker-kind/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-diagnostic-checker-kind/index.html">KaDiagnosticCheckerKind</a>
</span></code></pre></div>
</div>


<div markdown>

A kind of compiler checkers which report [`diagnostics`](-ka-diagnostic/index.md).


</div>

</div>
### [`KaDiagnostics`](-ka-diagnostics/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-diagnostics/index.html">KaDiagnostics</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>, <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="-ka-diagnostic-with-psi/index.html">KaDiagnosticWithPsi</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A description of a diagnostic query, which yields the requested [`diagnostics`](-ka-diagnostic-with-psi/index.md) on iteration.


</div>

</div>
### [`KaDiagnosticWithPsi`](-ka-diagnostic-with-psi/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-diagnostic-with-psi/index.html">KaDiagnosticWithPsi</a><span class="o"><</span><span class="kd">out </span><a href="-ka-diagnostic-with-psi/index.html">PSI</a><span class="o"> : </span>PsiElement<span class="o">></span> : <a href="-ka-diagnostic/index.html">KaDiagnostic</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaDiagnostic`](-ka-diagnostic/index.md) reported on a PsiElement of type [`PSI`](-ka-diagnostic-with-psi/index.md).


</div>

</div>
### [`KaSeverity`](-ka-severity/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-severity/index.html">KaSeverity</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-severity/index.html">KaSeverity</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

The severity of a [`KaDiagnostic`](-ka-diagnostic/index.md).


</div>

</div>
## Functions
### [`diagnostics`](diagnostics.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="diagnostics.html"><span class="nf">diagnostics</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-diagnostics/index.html">KaDiagnostics</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`diagnostics`](-ka-diagnostics/index.md) reported on the given [`KtElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md).


</div>

</div>
