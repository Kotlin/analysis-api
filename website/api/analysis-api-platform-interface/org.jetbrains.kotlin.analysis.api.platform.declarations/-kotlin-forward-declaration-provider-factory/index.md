---
tags:
 - jvm
title: "KotlinForwardDeclarationProviderFactory"
---

# KotlinForwardDeclarationProviderFactory

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinForwardDeclarationProviderFactory</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>[`KotlinForwardDeclarationProviderFactory`](index.md) creates [`KotlinDeclarationProvider`](../-kotlin-declaration-provider/index.md)s for Kotlin/Native forward declarations.

The declarations from the provider are used as a source <strong>representation</strong> for forward declaration symbols. The special provider is necessary because forward declarations are mere qualified names by themselves. It is a responsibility of the implementor to make the source representation correct. Symbol's properties are not affected by its source representation.

Implementations should be consistent with their corresponding [`KotlinForwardDeclarationsPackageProviderFactory`](../../org.jetbrains.kotlin.analysis.api.platform.packages/-kotlin-forward-declarations-package-provider-factory/index.md) implementation.


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
### createDeclarationProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createdeclarationprovider"><span class="nf">createDeclarationProvider</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span><span class="o">: </span><a href="../-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a Kotlin/Native forward declaration provider for [`module`](index.md#createdeclarationprovider), or `null` if the module cannot contain forward declarations.

Generally, only Kotlin/Native KLIB libraries can declare forward declarations. For other types of [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md)s the provider normally shouldn't be created.


</div>

</div>
