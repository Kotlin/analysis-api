---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.platform.lifetime"
---

# org.jetbrains.kotlin.analysis.api.platform.lifetime
## Types
### [`KaLifetimeTracker`](-ka-lifetime-tracker/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-lifetime-tracker/index.html">KaLifetimeTracker</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-ka-engine-service/index.html">KaEngineService</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaLifetimeTracker`](-ka-lifetime-tracker/index.md) is an engine service which tracks the current [`KaLifetimeToken`](../../analysis-api/org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md).


</div>

</div>
### [`KotlinAlwaysAccessibleLifetimeToken`](-kotlin-always-accessible-lifetime-token/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-always-accessible-lifetime-token/index.html">KotlinAlwaysAccessibleLifetimeToken</a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span> : <a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a>
</span></code></pre></div>
</div>

</div>
### [`KotlinAlwaysAccessibleLifetimeTokenFactory`](-kotlin-always-accessible-lifetime-token-factory/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-always-accessible-lifetime-token-factory/index.html">KotlinAlwaysAccessibleLifetimeTokenFactory</a> : <a href="-kotlin-lifetime-token-factory/index.html">KotlinLifetimeTokenFactory</a>
</span></code></pre></div>
</div>

</div>
### [`KotlinLifetimeTokenFactory`](-kotlin-lifetime-token-factory/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-lifetime-token-factory/index.html">KotlinLifetimeTokenFactory</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KotlinReadActionConfinementLifetimeToken`](-kotlin-read-action-confinement-lifetime-token/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-read-action-confinement-lifetime-token/index.html">KotlinReadActionConfinementLifetimeToken</a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">, </span>modificationTracker<span class="o">: </span>ModificationTracker<span class="p">)</span> : <a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a>
</span></code></pre></div>
</div>

</div>
### [`KotlinReadActionConfinementLifetimeTokenFactory`](-kotlin-read-action-confinement-lifetime-token-factory/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-read-action-confinement-lifetime-token-factory/index.html">KotlinReadActionConfinementLifetimeTokenFactory</a> : <a href="-kotlin-lifetime-token-factory/index.html">KotlinLifetimeTokenFactory</a>
</span></code></pre></div>
</div>

</div>
### [`ModificationTrackerWithInvalidationReason`](-modification-tracker-with-invalidation-reason/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-modification-tracker-with-invalidation-reason/index.html">ModificationTrackerWithInvalidationReason</a> : ModificationTracker
</span></code></pre></div>
</div>


<div markdown>

A ModificationTracker that provides a reason for invalidation since its creation.


</div>

</div>
