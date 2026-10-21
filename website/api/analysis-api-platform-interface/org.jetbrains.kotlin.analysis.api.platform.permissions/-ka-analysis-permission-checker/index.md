---
tags:
 - jvm
title: "KaAnalysisPermissionChecker"
---

# KaAnalysisPermissionChecker

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaAnalysisPermissionChecker</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-ka-engine-service/index.html">KaEngineService</a>
</span></code></pre></div>[`KaAnalysisPermissionChecker`](index.md) is an engine service which allows checking whether analysis is currently allowed.

In general, analysis can be prohibited in the following cases:

 - If analysis is invoked from the EDT, it is prohibited unless explicitly allowed via [`allowAnalysisOnEdt`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.permissions/index.md) or [`KotlinAnalysisPermissionOptions`](../-kotlin-analysis-permission-options/index.md).


 - If analysis is invoked from a write action, it is prohibited unless explicitly allowed via [`allowAnalysisFromWriteAction`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.permissions/index.md) or [`KotlinAnalysisPermissionOptions`](../-kotlin-analysis-permission-options/index.md).


 - Analysis can also be explicitly forbidden via [`forbidAnalysis`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.permissions/index.md), which in contrast to the above points cannot be controlled with [`KotlinAnalysisPermissionOptions`](../-kotlin-analysis-permission-options/index.md).



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
### getRejectionReason

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getrejectionreason"><span class="nf">getRejectionReason</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### isAnalysisAllowed

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#isanalysisallowed"><span class="nf">isAnalysisAllowed</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
