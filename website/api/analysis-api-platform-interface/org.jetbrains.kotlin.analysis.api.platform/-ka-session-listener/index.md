---
tags:
 - jvm
title: "KaSessionListener"
---

# KaSessionListener

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaSessionListener</a>
</span></code></pre></div>An extension point for platforms hosting the Kotlin Analysis API to receive callbacks on analysis session creation, entry, and exit.

In the absence of exceptions, the lifecycle of a listener is as follows:

1. [`beforeAcquiringSession`](index.md#beforeacquiringsession) is called for each listener.


1. The session is acquired.


1. [`afterAcquiringSession`](index.md#afteracquiringsession) is called for each listener.


1. [`beforeEnteringAnalysis`](index.md#beforeenteringanalysis) is called for each listener.


1. The analysis body runs.


1. [`afterLeavingAnalysis`](index.md#afterleavinganalysis) is called for each listener.


If an exception is thrown by a listener implementation method itself, it is caught, logged, and isolated so that it does not crash analysis or prevent remaining listeners from executing.


</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Functions
### afterAcquiringSession

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#afteracquiringsession"><span class="nf">afterAcquiringSession</span></a><span class="p">(</span>useSiteModule<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">, </span>useSiteElement<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Called after a [`org.jetbrains.kotlin.analysis.api.KaSession`](../../../analysis-api/org.jetbrains.kotlin.analysis.api/-ka-session/index.md) has been acquired, or after [`onSessionAcquisitionException`](index.md#onsessionacquisitionexception) if an exception occurred.


</div>

</div>
### afterLeavingAnalysis

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#afterleavinganalysis"><span class="nf">afterLeavingAnalysis</span></a><span class="p">(</span>useSiteModule<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">, </span>useSiteElement<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Called after the analysis block is finished, or after [`onAnalysisException`](index.md#onanalysisexception) if an exception occurred.


</div>

</div>
### beforeAcquiringSession

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#beforeacquiringsession"><span class="nf">beforeAcquiringSession</span></a><span class="p">(</span>useSiteModule<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">, </span>useSiteElement<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Called on entry to the [`org.jetbrains.kotlin.analysis.api.session.analyze`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.session/index.md) call, before the [`org.jetbrains.kotlin.analysis.api.KaSession`](../../../analysis-api/org.jetbrains.kotlin.analysis.api/-ka-session/index.md) is looked up for the use-site module or element.


</div>

</div>
### beforeEnteringAnalysis

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#beforeenteringanalysis"><span class="nf">beforeEnteringAnalysis</span></a><span class="p">(</span>useSiteModule<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">, </span>useSiteElement<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Called immediately after [`afterAcquiringSession`](index.md#afteracquiringsession) and before the body of the analysis block is executed.


</div>

</div>
### onAnalysisException

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#onanalysisexception"><span class="nf">onAnalysisException</span></a><span class="p">(</span>
    useSiteModule<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">, </span>
    useSiteElement<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">, </span>
    throwable<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a>
<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Called when an exception is thrown by the analysis block.


</div>

</div>
### onSessionAcquisitionException

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#onsessionacquisitionexception"><span class="nf">onSessionAcquisitionException</span></a><span class="p">(</span>
    useSiteModule<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">, </span>
    useSiteElement<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">, </span>
    throwable<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a>
<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Called when an exception is thrown during [`org.jetbrains.kotlin.analysis.api.KaSession`](../../../analysis-api/org.jetbrains.kotlin.analysis.api/-ka-session/index.md) creation.


</div>

</div>
