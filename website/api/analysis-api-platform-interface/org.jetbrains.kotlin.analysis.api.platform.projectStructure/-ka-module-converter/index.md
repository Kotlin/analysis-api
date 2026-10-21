---
tags:
 - jvm
title: "KaModuleConverter"
---

# KaModuleConverter

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaModuleConverter</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>A service for converting [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md) to Module.


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
### asOpenApiModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#asopenapimodule"><span class="nf">asOpenApiModule</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span><span class="o">: </span>Module<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns Module corresponding to [`module`](index.md#asopenapimodule) or `null` if not found.

Only supports [`KaSourceModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-source-module/index.md)s. When [`module`](index.md#asopenapimodule) is not a [`KaSourceModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-source-module/index.md), returns `null`.


</div>

</div>
