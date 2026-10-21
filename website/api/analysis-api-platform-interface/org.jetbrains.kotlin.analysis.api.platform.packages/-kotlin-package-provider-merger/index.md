---
tags:
 - jvm
title: "KotlinPackageProviderMerger"
---

# KotlinPackageProviderMerger

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinPackageProviderMerger</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-composable-provider-merger/index.html">KotlinComposableProviderMerger</a><span class="o"><</span><a href="../-kotlin-package-provider/index.html">KotlinPackageProvider</a><span class="o">> </span>, <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>[`KotlinPackageProviderMerger`](index.md) allows merging multiple [`KotlinPackageProvider`](../-kotlin-package-provider/index.md)s into a more efficient package provider.

Package providers should not be naively merged by combining scopes and calling [`createPackageProvider`](../create-package-provider.md), because there may be additional package providers which do not operate based on scopes (e.g. resolve extension package providers).

The provider merger should consider merging scopes with [`KaGlobalSearchScopeMerger`](../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-ka-global-search-scope-merger/index.md) if there is a useful implementation provided by the platform.


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
### [`merge`](index.md#merge)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#merge"><span class="nf">merge</span></a><span class="p">(</span>providers<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-kotlin-package-provider/index.html">KotlinPackageProvider</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../-kotlin-package-provider/index.html">KotlinPackageProvider</a>
</span></code></pre></div>
</div>


<div markdown>

Merges the given [`providers`](index.md#merge) into a single provider. When possible, mergers will try to create a provider that is more efficient compared to the naive sequential composite provider. Not all providers might be mergeable, or there might be multiple separate sets of providers that can be merged individually, so the resulting provider may be a composite provider.


</div>

</div>
