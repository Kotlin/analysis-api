---
tags:
 - jvm
title: "KotlinAnalysisPermissionOptions"
---

# KotlinAnalysisPermissionOptions

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinAnalysisPermissionOptions</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>[`KotlinAnalysisPermissionOptions`](index.md) gives an Analysis API platform the choice whether to allow analysis on the EDT and in write actions by default.

#### See also


 - [`KotlinDefaultAnalysisPermissionOptions`](../-kotlin-default-analysis-permission-options/index.md)


#### Inheritors


 - [`KotlinDefaultAnalysisPermissionOptions`](../-kotlin-default-analysis-permission-options/index.md)



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
### defaultIsAnalysisAllowedInWriteAction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#defaultisanalysisallowedinwriteaction">defaultIsAnalysisAllowedInWriteAction</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

The default setting for [`org.jetbrains.kotlin.analysis.api.permissions.KaAnalysisPermissionRegistry.isAnalysisAllowedInWriteAction`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.permissions/-ka-analysis-permission-registry/is-analysis-allowed-in-write-action.md), when not overridden by [`org.jetbrains.kotlin.analysis.api.permissions.allowAnalysisFromWriteAction`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.permissions/index.md).


</div>

</div>
### defaultIsAnalysisAllowedOnEdt

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#defaultisanalysisallowedonedt">defaultIsAnalysisAllowedOnEdt</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

The default setting for [`org.jetbrains.kotlin.analysis.api.permissions.KaAnalysisPermissionRegistry.isAnalysisAllowedOnEdt`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.permissions/-ka-analysis-permission-registry/is-analysis-allowed-on-edt.md), when not overridden by [`org.jetbrains.kotlin.analysis.api.permissions.allowAnalysisOnEdt`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.permissions/index.md).


</div>

</div>
