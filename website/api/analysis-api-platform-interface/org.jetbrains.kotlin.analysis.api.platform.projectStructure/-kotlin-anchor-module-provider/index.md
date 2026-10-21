---
tags:
 - jvm
title: "KotlinAnchorModuleProvider"
---

# KotlinAnchorModuleProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinAnchorModuleProvider</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>[`KotlinAnchorModuleProvider`](index.md) provides modules which contain dependencies of libraries.

In the IJ monorepo, anchor modules are required for navigation from Kotlin compiler library sources to IJ platform sources. The Kotlin compiler depends on the IJ platform, but this dependency is not represented as JARs in the monorepo, but rather by certain monorepo source modules, which are made visible to the Kotlin compiler library sources as dependencies via an anchor module.


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
### getAllAnchorModules

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getallanchormodules"><span class="nf">getAllAnchorModules</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-source-module/index.html">KaSourceModule</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all anchor modules configured in the project.


</div>

</div>
### getAllAnchorModulesIfComputed

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getallanchormodulesifcomputed"><span class="nf">getAllAnchorModulesIfComputed</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-source-module/index.html">KaSourceModule</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns all anchor modules configured in the project if they have already been computed and are not invalidated. This function must only be called from a write action to ensure that they are not being computed from another read action.

**Return**

The anchor modules if they are computed and the result is the same as [`getAllAnchorModules`](index.md#getallanchormodules), or `null` otherwise.


</div>

</div>
### getAnchorModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getanchormodule"><span class="nf">getAnchorModule</span></a><span class="p">(</span>libraryModule<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-library-module/index.html">KaLibraryModule</a><span class="p">)</span><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-source-module/index.html">KaSourceModule</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
