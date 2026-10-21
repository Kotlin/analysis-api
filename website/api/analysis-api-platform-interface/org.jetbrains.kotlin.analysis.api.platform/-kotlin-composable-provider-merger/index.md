---
tags:
 - jvm
title: "KotlinComposableProviderMerger"
---

# KotlinComposableProviderMerger

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinComposableProviderMerger</a><span class="o"><</span><a href="index.html">P</a><span class="o"> : </span><a href="../-kotlin-composable-provider/index.html">KotlinComposableProvider</a><span class="o">></span>
</span></code></pre></div>#### Inheritors


 - [`KotlinDeclarationProviderMerger`](../../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-declaration-provider-merger/index.md)
 - [`KotlinPackageProviderMerger`](../../org.jetbrains.kotlin.analysis.api.platform.packages/-kotlin-package-provider-merger/index.md)



</div>

## Functions
### merge

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.platform.packages/-kotlin-package-provider-merger/index.html#merge"><span class="nf">merge</span></a><span class="p">(</span>providers<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">P</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="index.html">P</a>
</span></code></pre></div>
</div>


<div markdown>

Merges the given [`providers`](../../org.jetbrains.kotlin.analysis.api.platform.packages/-kotlin-package-provider-merger/index.md#merge) into a single provider. When possible, mergers will try to create a provider that is more efficient compared to the naive sequential composite provider. Not all providers might be mergeable, or there might be multiple separate sets of providers that can be merged individually, so the resulting provider may be a composite provider.


</div>

</div>
