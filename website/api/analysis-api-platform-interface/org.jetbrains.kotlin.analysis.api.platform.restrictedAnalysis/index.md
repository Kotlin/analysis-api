---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.platform.restrictedAnalysis"
---

# org.jetbrains.kotlin.analysis.api.platform.restrictedAnalysis
## Types
### [`KaRestrictedAnalysisException`](-ka-restricted-analysis-exception/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-ka-restricted-analysis-exception/index.html">KaRestrictedAnalysisException</a><span class="p">(</span>cause<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="p">)</span> : <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html">Exception</a>
</span></code></pre></div>
</div>


<div markdown>

An exception which occurred during [`restricted analysis`](-kotlin-restricted-analysis-service/index.md).


</div>

</div>
### [`KotlinRestrictedAnalysisService`](-kotlin-restricted-analysis-service/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-restricted-analysis-service/index.html">KotlinRestrictedAnalysisService</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

Allows the platform to communicate to the Analysis API about restricted analysis. When analysis is restricted, the platform typically lacks full, up-to-date information about the project. For example, [`declaration providers`](../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-declaration-provider/index.md) might return incomplete results. In addition, the available information might change without associated [`modification events`](../org.jetbrains.kotlin.analysis.api.platform.modification/-kotlin-modification-event-kind/index.md).


</div>

</div>
## Functions
