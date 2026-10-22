---
tags:
 - jvm
title: "KotlinModuleOutputProvider"
---

# KotlinModuleOutputProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinModuleOutputProvider</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>[`KotlinModuleOutputProvider`](index.md) provides build output directories for [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md)s.


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
### getCompilationOutput

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getcompilationoutput"><span class="nf">getCompilationOutput</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-source-module/index.html">KaSourceModule</a><span class="p">)</span><span class="o">: </span>VirtualFile<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the compilation output file/directory for the [`module`](index.md#getcompilationoutput), or `null` if it is unset or unknown.


</div>

</div>
