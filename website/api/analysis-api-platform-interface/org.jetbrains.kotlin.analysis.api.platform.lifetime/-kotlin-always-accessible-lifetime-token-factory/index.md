---
tags:
 - jvm
title: "KotlinAlwaysAccessibleLifetimeTokenFactory"
---

# KotlinAlwaysAccessibleLifetimeTokenFactory

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KotlinAlwaysAccessibleLifetimeTokenFactory</a> : <a href="../-kotlin-lifetime-token-factory/index.html">KotlinLifetimeTokenFactory</a>
</span></code></pre></div>
</div>

## Constructors
### KotlinAlwaysAccessibleLifetimeTokenFactory

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### identifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#identifier">identifier</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/-k-class/index.html">KClass</a><span class="o"><</span><span class="kd">out </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
## Functions
### create

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#create"><span class="nf">create</span></a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">, </span>modificationTracker<span class="o">: </span>ModificationTracker<span class="p">)</span><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaLifetimeToken`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md) for a specific analysis session represented by a [`modificationTracker`](../-kotlin-lifetime-token-factory/index.md#create).

**Parameters**



 - modificationTracker: A modification tracker which tracks the validity of the analysis session's content.





</div>

</div>
