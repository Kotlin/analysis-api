---
tags:
 - jvm
title: "KaLifetimeTracker"
---

# KaLifetimeTracker

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaLifetimeTracker</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-ka-engine-service/index.html">KaEngineService</a>
</span></code></pre></div>[`KaLifetimeTracker`](index.md) is an engine service which tracks the current [`KaLifetimeToken`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md).

It can be used in the implementation of custom lifetime tokens to check that the accessed token is in scope.


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
### currentToken

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#currenttoken">currentToken</a><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KaLifetimeToken`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md) for the currently active analysis, or `null` if no analysis is in progress.


</div>

</div>
