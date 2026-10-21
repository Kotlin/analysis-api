---
tags:
 - jvm
title: "KotlinDeclarationProviderMerger"
---

# KotlinDeclarationProviderMerger

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinDeclarationProviderMerger</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-composable-provider-merger/index.html">KotlinComposableProviderMerger</a><span class="o"><</span><a href="../-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a><span class="o">> </span>, <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>While the main declaration provider created via [`createDeclarationProvider`](../create-declaration-provider.md) is scope-based, there are other declaration providers which are not, such as file-based declaration providers. Not all declarations provided by such declaration providers can be provided by the main declaration provider, even if the correct scope is provided (such as a file-based scope). For example, the main declaration provider may be based on an index which doesn't contain the declarations provided by file-based declaration providers.

Hence, [`KotlinDeclarationProvider`](../-kotlin-declaration-provider/index.md)s cannot just be combined by combining the scopes of all declaration providers and calling [`createDeclarationProvider`](../create-declaration-provider.md). [`KotlinDeclarationProviderMerger`](index.md) should implement proper merging logic that takes these concerns into account.

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
### [`merge`](../../org.jetbrains.kotlin.analysis.api.platform.packages/-kotlin-package-provider-merger/index.md#merge)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.platform.packages/-kotlin-package-provider-merger/index.html#merge"><span class="nf">merge</span></a><span class="p">(</span>providers<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a>
</span></code></pre></div>
</div>


<div markdown>

Merges the given [`providers`](../../org.jetbrains.kotlin.analysis.api.platform.packages/-kotlin-package-provider-merger/index.md#merge) into a single provider. When possible, mergers will try to create a provider that is more efficient compared to the naive sequential composite provider. Not all providers might be mergeable, or there might be multiple separate sets of providers that can be merged individually, so the resulting provider may be a composite provider.


</div>

</div>
