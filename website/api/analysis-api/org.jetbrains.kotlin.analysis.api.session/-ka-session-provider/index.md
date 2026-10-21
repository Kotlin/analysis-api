---
tags:
 - jvm
title: "KaSessionProvider"
---

# KaSessionProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KaSessionProvider</a><span class="p">(</span><span class="kd">val </span>project<span class="o">: </span>Project<span class="p">)</span> : Disposable
</span></code></pre></div>Provides [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)s by use-site PsiElements or [`KaModule`](../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md)s.

This provider should not be used directly. Please use [`analyze`](../analyze.md) or [`analyzeCopy`](../analyze-copy.md) instead.


</div>

## Constructors
### KaSessionProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Properties
### project

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#project">project</a><span class="o">: </span>Project
</span></code></pre></div>
</div>

</div>
## Functions
### afterLeavingAnalysis

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#afterleavinganalysis"><span class="nf">afterLeavingAnalysis</span></a><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>useSiteElement<span class="o">: </span>PsiElement<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

[`afterLeavingAnalysis`](index.md#afterleavinganalysis) hooks into analysis after [`analyze`](index.md#analyze)'s action has been executed.

The signature of [`afterLeavingAnalysis`](index.md#afterleavinganalysis) should be kept stable to avoid breaking binary compatibility, since [`analyze`](index.md#analyze) is inlined.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#afterleavinganalysis"><span class="nf">afterLeavingAnalysis</span></a><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>useSiteElement<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span>
</span></code></pre></div><div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#afterleavinganalysis"><span class="nf">afterLeavingAnalysis</span></a><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>useSiteModule<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

This function has the same contracts as [`afterLeavingAnalysis`](index.md#afterleavinganalysis) for PsiElements.


</div>

</div>
### analyze

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#analyze">R</a><span class="o">> </span><a href="index.html#analyze"><span class="nf">analyze</span></a><span class="p">(</span>useSiteElement<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">, </span>action<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="index.html#analyze">R</a><span class="p">)</span><span class="o">: </span><a href="index.html#analyze">R</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#analyze">R</a><span class="o">> </span><a href="index.html#analyze"><span class="nf">analyze</span></a><span class="p">(</span>useSiteElement<span class="o">: </span>PsiElement<span class="p">, </span>action<span class="o">: </span><span class="kd">context</span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">) </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="index.html#analyze">R</a><span class="p">)</span><span class="o">: </span><a href="index.html#analyze">R</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#analyze">R</a><span class="o">> </span><a href="index.html#analyze"><span class="nf">analyze</span></a><span class="p">(</span>useSiteModule<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a><span class="p">, </span>action<span class="o">: </span><span class="kd">context</span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">) </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="index.html#analyze">R</a><span class="p">)</span><span class="o">: </span><a href="index.html#analyze">R</a>
</span></code></pre></div>
</div>

</div>
### beforeEnteringAnalysis

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#beforeenteringanalysis"><span class="nf">beforeEnteringAnalysis</span></a><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>useSiteElement<span class="o">: </span>PsiElement<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

[`beforeEnteringAnalysis`](index.md#beforeenteringanalysis) hooks into analysis before [`analyze`](index.md#analyze)'s action is executed.

The signature of [`beforeEnteringAnalysis`](index.md#beforeenteringanalysis) should be kept stable to avoid breaking binary compatibility, since [`analyze`](index.md#analyze) is inlined.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#beforeenteringanalysis"><span class="nf">beforeEnteringAnalysis</span></a><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>useSiteElement<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span>
</span></code></pre></div><div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#beforeenteringanalysis"><span class="nf">beforeEnteringAnalysis</span></a><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>useSiteModule<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

This function has the same contracts as [`beforeEnteringAnalysis`](index.md#beforeenteringanalysis) for PsiElements.


</div>

</div>
### clearCaches

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#clearcaches"><span class="nf">clearCaches</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### dispose

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#dispose"><span class="nf">dispose</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### getAnalysisSession

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getanalysissession"><span class="nf">getAnalysisSession</span></a><span class="p">(</span>useSiteElement<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#getanalysissession"><span class="nf">getAnalysisSession</span></a><span class="p">(</span>useSiteElement<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getanalysissession"><span class="nf">getAnalysisSession</span></a><span class="p">(</span>useSiteModule<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a>
</span></code></pre></div>
</div>

</div>
### handleAnalysisException

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#handleanalysisexception"><span class="nf">handleAnalysisException</span></a><span class="p">(</span>
    throwable<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="p">, </span>
    session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    useSiteElement<span class="o">: </span>PsiElement
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-nothing/index.html">Nothing</a>
</span></code></pre></div>
</div>


<div markdown>

[`handleAnalysisException`](index.md#handleanalysisexception) handles any [`Throwable`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html) that occurred during analysis and was caught by [`analyze`](index.md#analyze).

[`Error`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-error/index.html)s should generally be rethrown. That said, the signature includes [`Throwable`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html) and not [`Exception`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-exception/index.html) to stay as wide as possible to avoid risking breaking binary compatibility down the line.

The signature of [`handleAnalysisException`](index.md#handleanalysisexception) should be kept stable to avoid breaking binary compatibility, since [`analyze`](index.md#analyze) is inlined.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#handleanalysisexception"><span class="nf">handleAnalysisException</span></a><span class="p">(</span>
    throwable<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="p">, </span>
    session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    useSiteElement<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a>
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-nothing/index.html">Nothing</a>
</span></code></pre></div><div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#handleanalysisexception"><span class="nf">handleAnalysisException</span></a><span class="p">(</span>
    throwable<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="p">, </span>
    session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    useSiteModule<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a>
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-nothing/index.html">Nothing</a>
</span></code></pre></div>
</div>


<div markdown>

This function has the same contracts as [`handleAnalysisException`](index.md#handleanalysisexception) for PsiElements.


</div>

</div>
