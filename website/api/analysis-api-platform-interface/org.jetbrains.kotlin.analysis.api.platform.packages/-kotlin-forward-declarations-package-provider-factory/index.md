---
tags:
 - jvm
title: "KotlinForwardDeclarationsPackageProviderFactory"
---

# KotlinForwardDeclarationsPackageProviderFactory

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinForwardDeclarationsPackageProviderFactory</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>[`KotlinForwardDeclarationsPackageProviderFactory`](index.md) creates [`KotlinPackageProvider`](../-kotlin-package-provider/index.md)s for Kotlin/Native forward declarations.

Implementations should be consistent with their corresponding [`KotlinForwardDeclarationProviderFactory`](../../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-forward-declaration-provider-factory/index.md) implementation.


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
### createPackageProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createpackageprovider"><span class="nf">createPackageProvider</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span><span class="o">: </span><a href="../-kotlin-package-provider/index.html">KotlinPackageProvider</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a package provider for Kotlin/Native forward declaration packages in [`module`](index.md#createpackageprovider), or `null` if the module cannot contain forward declarations.


</div>

</div>
