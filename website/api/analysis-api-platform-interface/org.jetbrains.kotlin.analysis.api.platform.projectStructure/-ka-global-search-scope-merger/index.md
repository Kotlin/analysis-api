---
tags:
 - jvm
title: "KaGlobalSearchScopeMerger"
---

# KaGlobalSearchScopeMerger

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaGlobalSearchScopeMerger</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-ka-engine-service/index.html">KaEngineService</a>
</span></code></pre></div>Merges GlobalSearchScopes according to registered [`KotlinGlobalSearchScopeMergeStrategy`](../-kotlin-global-search-scope-merge-strategy/index.md) with the goal of creating an optimized and flattened combined scope.


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
### union

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#union"><span class="nf">union</span></a><span class="p">(</span>scopes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span>GlobalSearchScope<span class="o">></span><span class="p">)</span><span class="o">: </span>GlobalSearchScope
</span></code></pre></div>
</div>


<div markdown>

Creates a merged GlobalSearchScope which represents a union of all [`scopes`](index.md#union).


</div>

</div>
