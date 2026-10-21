---
tags:
 - jvm
title: "mergeSpecificProviders"
---

# mergeSpecificProviders

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="merge-specific-providers.html">P</a><span class="o"> : </span><a href="-kotlin-composable-provider/index.html">KotlinComposableProvider</a><span class="p">, </span><span class="kd">reified </span><a href="merge-specific-providers.html">T</a><span class="o"> : </span><a href="merge-specific-providers.html">P</a><span class="o">> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="merge-specific-providers.html">P</a><span class="o">></span><span class="p">.</span><a href="merge-specific-providers.html"><span class="nf">mergeSpecificProviders</span></a><span class="p">(</span>factory<span class="o">: </span><a href="-kotlin-composite-provider-factory/index.html">KotlinCompositeProviderFactory</a><span class="o"><</span><a href="merge-specific-providers.html">P</a><span class="o">></span><span class="p">, </span><span class="kd">crossinline </span>mergeTargets<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="merge-specific-providers.html">T</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span><a href="merge-specific-providers.html">P</a><span class="p">)</span><span class="o">: </span><a href="merge-specific-providers.html">P</a>
</span></code></pre></div>
</div>


<div markdown>

Uses the given [`factory`](merge-specific-providers.md) to merge all providers of type [`T`](merge-specific-providers.md) with the given [`mergeTargets`](merge-specific-providers.md) strategy. Other providers (not of type [`T`](merge-specific-providers.md)) are added to the resulting composite provider unmerged.


</div>

</div>
