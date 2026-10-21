---
tags:
 - jvm
title: "KaAnalysisPermissionRegistry"
---

# KaAnalysisPermissionRegistry

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaAnalysisPermissionRegistry</a>
</span></code></pre></div>[`KaAnalysisPermissionRegistry`](index.md) stores settings required by permission functions such as [`forbidAnalysis`](../forbid-analysis.md), [`allowAnalysisOnEdt`](../allow-analysis-on-edt.md), and [`allowAnalysisFromWriteAction`](../allow-analysis-from-write-action.md).

[`KaAnalysisPermissionRegistry`](index.md) is an application service because we want users to call permission functions without having to pass a project, which would be required if this class was a project service.


</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
### [`KaExplicitAnalysisRestriction`](-ka-explicit-analysis-restriction/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-explicit-analysis-restriction/index.html">KaExplicitAnalysisRestriction</a><span class="p">(</span><span class="kd">val </span>description<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### explicitAnalysisRestriction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">var </span><a href="index.html#explicitanalysisrestriction">explicitAnalysisRestriction</a><span class="o">: </span><a href="-ka-explicit-analysis-restriction/index.html">KaAnalysisPermissionRegistry.KaExplicitAnalysisRestriction</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### isAnalysisAllowedInWriteAction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">var </span><a href="index.html#isanalysisallowedinwriteaction">isAnalysisAllowedInWriteAction</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### isAnalysisAllowedOnEdt

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">var </span><a href="index.html#isanalysisallowedonedt">isAnalysisAllowedOnEdt</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
