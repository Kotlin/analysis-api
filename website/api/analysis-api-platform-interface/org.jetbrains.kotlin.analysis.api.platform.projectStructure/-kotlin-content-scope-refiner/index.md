---
tags:
 - jvm
title: "KotlinContentScopeRefiner"
---

# KotlinContentScopeRefiner

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinContentScopeRefiner</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>A contributor to [`KaModule.contentScope`](../-ka-dangling-file-module-impl/index.md#contentscope).

This extension point allows extending and restricting content scopes inside [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md). All the refiners are lazily applied to [`KaModule.baseContentScope`](../-ka-module-base/index.md#basecontentscope) to build [`KaModule.contentScope`](../-ka-dangling-file-module-impl/index.md#contentscope). The computation of the refined content scope happens inside [`KaContentScopeProvider`](../-ka-content-scope-provider/index.md).

For example, this allows extensions providing synthetic non-Kotlin sources to bring those source files into the relevant module, library, or SDK scopes and shadow existing sources in a backend-agnostic manner.

Note that implementations of [`KotlinContentScopeRefiner`](index.md) cannot access [`KaModule.contentScope`](../-ka-dangling-file-module-impl/index.md#contentscope), as it's not yet built when [`getEnlargementScopes`](index.md#getenlargementscopes)/[`getRestrictionScopes`](index.md#getrestrictionscopes) are called. Furthermore, implementations must not use [`KotlinProjectStructureProvider`](../-kotlin-project-structure-provider/index.md), as the content scope may be accessed during [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md) computation.


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
### getEnlargementScopes

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getenlargementscopes"><span class="nf">getEnlargementScopes</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>GlobalSearchScope<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Given a [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md), [`getEnlargementScopes`](index.md#getenlargementscopes) returns GlobalSearchScopes which enlarge [`KaModule.baseContentScope`](../-ka-module-base/index.md#basecontentscope) to form [`KaModule.contentScope`](../-ka-dangling-file-module-impl/index.md#contentscope). An enlargement expands the base content scope with the files contained in the enlargement scope.

If some file contained in [`getEnlargementScopes`](index.md#getenlargementscopes) is also already contained in [`KaModule.baseContentScope`](../-ka-module-base/index.md#basecontentscope), the enlargement scope will have no additional effect with respect to this file.

If the refiner doesn't provide any enlargements, [`emptyList`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/index.html) is expected to be returned.


</div>

</div>
### getRestrictionScopes

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getrestrictionscopes"><span class="nf">getRestrictionScopes</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>GlobalSearchScope<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Given a [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md), [`getRestrictionScopes`](index.md#getrestrictionscopes) returns GlobalSearchScopes which restrict [`KaModule.baseContentScope`](../-ka-module-base/index.md#basecontentscope) to form [`KaModule.contentScope`](../-ka-dangling-file-module-impl/index.md#contentscope). A restriction limits the base content scope to the files contained in the restriction scope.

If some file not contained in [`getRestrictionScopes`](index.md#getrestrictionscopes) is also not contained in [`KaModule.baseContentScope`](../-ka-module-base/index.md#basecontentscope), the restriction scope will have no additional effect with respect to this file.

If the refiner doesn't provide any restrictions, [`emptyList`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/index.html) is expected to be returned.


</div>

</div>
