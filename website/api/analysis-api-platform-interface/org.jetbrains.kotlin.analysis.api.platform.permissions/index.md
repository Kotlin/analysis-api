---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.platform.permissions"
---

# org.jetbrains.kotlin.analysis.api.platform.permissions
## Types
### [`KaAnalysisPermissionChecker`](-ka-analysis-permission-checker/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-analysis-permission-checker/index.html">KaAnalysisPermissionChecker</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-ka-engine-service/index.html">KaEngineService</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaAnalysisPermissionChecker`](-ka-analysis-permission-checker/index.md) is an engine service which allows checking whether analysis is currently allowed.


</div>

</div>
### [`KotlinAnalysisPermissionOptions`](-kotlin-analysis-permission-options/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-analysis-permission-options/index.html">KotlinAnalysisPermissionOptions</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinAnalysisPermissionOptions`](-kotlin-analysis-permission-options/index.md) gives an Analysis API platform the choice whether to allow analysis on the EDT and in write actions by default.


</div>

</div>
### [`KotlinDefaultAnalysisPermissionOptions`](-kotlin-default-analysis-permission-options/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-default-analysis-permission-options/index.html">KotlinDefaultAnalysisPermissionOptions</a> : <a href="-kotlin-analysis-permission-options/index.html">KotlinAnalysisPermissionOptions</a>
</span></code></pre></div>
</div>

</div>
