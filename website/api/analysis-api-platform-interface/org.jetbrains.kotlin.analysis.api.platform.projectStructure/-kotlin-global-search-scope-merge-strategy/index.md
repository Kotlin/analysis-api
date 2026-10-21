---
tags:
 - jvm
title: "KotlinGlobalSearchScopeMergeStrategy"
---

# KotlinGlobalSearchScopeMergeStrategy

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinGlobalSearchScopeMergeStrategy</a><span class="o"><</span><a href="index.html">T</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>[`KotlinGlobalSearchScopeMergeStrategy`](index.md) is used to declare a strategy for merging a list of GlobalSearchScopes into a single GlobalSearchScope. Is used by implementations of [`KaGlobalSearchScopeMerger`](../-ka-global-search-scope-merger/index.md) to optimize the merging process and flatten the resulting scope.

Note that [`KotlinGlobalSearchScopeMergeStrategy`](index.md) are applied in the order they are registered.


</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Properties
### targetType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#targettype">targetType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/-k-class/index.html">KClass</a><span class="o"><</span><a href="index.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Defines the target type [`KotlinGlobalSearchScopeMergeStrategy`](index.md) works with. All scopes passed to [`uniteScopes`](index.md#unitescopes) are guaranteed to be a subtype of [`targetType`](index.md#targettype).


</div>

</div>
## Functions
### uniteScopes

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#unitescopes"><span class="nf">uniteScopes</span></a><span class="p">(</span>scopes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">T</a><span class="o">></span><span class="p">, </span>project<span class="o">: </span>Project<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>GlobalSearchScope<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Merges a list of GlobalSearchScopes into an optimized set of GlobalSearchScopes.

 - If [`scopes`](index.md#unitescopes) cannot be optimized, [`uniteScopes`](index.md#unitescopes) should return the same [`scopes`](index.md#unitescopes) list.


 - If [`scopes`](index.md#unitescopes) can be merged into one GlobalSearchScope.EMPTY_SCOPE, then [`uniteScopes`](index.md#unitescopes) should return an empty list.



</div>

</div>
