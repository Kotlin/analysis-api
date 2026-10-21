---
tags:
 - jvm
title: "KotlinDefaultAnalysisPermissionOptions"
---

# KotlinDefaultAnalysisPermissionOptions

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KotlinDefaultAnalysisPermissionOptions</a> : <a href="../-kotlin-analysis-permission-options/index.html">KotlinAnalysisPermissionOptions</a>
</span></code></pre></div>
</div>

## Constructors
### KotlinDefaultAnalysisPermissionOptions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### defaultIsAnalysisAllowedInWriteAction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#defaultisanalysisallowedinwriteaction">defaultIsAnalysisAllowedInWriteAction</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

The default setting for [`org.jetbrains.kotlin.analysis.api.permissions.KaAnalysisPermissionRegistry.isAnalysisAllowedInWriteAction`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.permissions/-ka-analysis-permission-registry/is-analysis-allowed-in-write-action.md), when not overridden by [`org.jetbrains.kotlin.analysis.api.permissions.allowAnalysisFromWriteAction`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.permissions/index.md).


</div>

</div>
### defaultIsAnalysisAllowedOnEdt

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#defaultisanalysisallowedonedt">defaultIsAnalysisAllowedOnEdt</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

The default setting for [`org.jetbrains.kotlin.analysis.api.permissions.KaAnalysisPermissionRegistry.isAnalysisAllowedOnEdt`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.permissions/-ka-analysis-permission-registry/is-analysis-allowed-on-edt.md), when not overridden by [`org.jetbrains.kotlin.analysis.api.permissions.allowAnalysisOnEdt`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.permissions/index.md).


</div>

</div>
