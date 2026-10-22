---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.platform.projectStructure"
---

# org.jetbrains.kotlin.analysis.api.platform.projectStructure
## Types
### [`KaBuiltinsModuleImpl`](-ka-builtins-module-impl/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-builtins-module-impl/index.html">KaBuiltinsModuleImpl</a><span class="p">(</span><span class="kd">val </span>targetPlatform<span class="o">: </span>TargetPlatform<span class="p">, </span><span class="kd">val </span>project<span class="o">: </span>Project<span class="p">)</span> : <a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-builtins-module/index.html">KaBuiltinsModule</a>, <a href="-ka-module-base/index.html">KaModuleBase</a>
</span></code></pre></div>
</div>


<div markdown>

The default implementation of the builtins module.


</div>

</div>
### [`KaContentScopeProvider`](-ka-content-scope-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-content-scope-provider/index.html">KaContentScopeProvider</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-ka-engine-service/index.html">KaEngineService</a>
</span></code></pre></div>
</div>


<div markdown>

An engine service which must be used to calculate a [`KaModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md)'s [`content scope`](-ka-dangling-file-module-impl/index.md#contentscope) lazily.


</div>

</div>
### [`KaDanglingFileModuleImpl`](-ka-dangling-file-module-impl/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-dangling-file-module-impl/index.html">KaDanglingFileModuleImpl</a><span class="p">(</span>
    files<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="o">></span><span class="p">, </span>
    <span class="kd">val </span>contextModule<span class="o">: </span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">, </span>
    <span class="kd">val </span>resolutionMode<span class="o">: </span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-dangling-file-resolution-mode/index.html">KaDanglingFileResolutionMode</a>
<span class="p">)</span> : <a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-dangling-file-module/index.html">KaDanglingFileModule</a>, <a href="-ka-module-base/index.html">KaModuleBase</a>
</span></code></pre></div>
</div>


<div markdown>

The default implementation of the dangling file module, which provides all knowledge from the context module. Note that if you need custom behavior, you should create a custom implementation of a [`KaDanglingFileModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-dangling-file-module/index.md), as the Analysis API treats this implementation specially (by allowing certain performance optimizations).


</div>

</div>
### [`KaGlobalSearchScopeMerger`](-ka-global-search-scope-merger/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-global-search-scope-merger/index.html">KaGlobalSearchScopeMerger</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-ka-engine-service/index.html">KaEngineService</a>
</span></code></pre></div>
</div>


<div markdown>

Merges GlobalSearchScopes according to registered [`KotlinGlobalSearchScopeMergeStrategy`](-kotlin-global-search-scope-merge-strategy/index.md) with the goal of creating an optimized and flattened combined scope.


</div>

</div>
### [`KaModuleBase`](-ka-module-base/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-ka-module-base/index.html">KaModuleBase</a> : <a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>

</div>
### [`KaModuleConverter`](-ka-module-converter/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-module-converter/index.html">KaModuleConverter</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

A service for converting [`KaModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md) to Module.


</div>

</div>
### [`KaModulePlatformKind`](-ka-module-platform-kind/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-module-platform-kind/index.html">KaModulePlatformKind</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-module-platform-kind/index.html">KaModulePlatformKind</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

The module platform kind classifies a [`KaModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md)'s TargetPlatform into a single kind, determining how the Analysis API interprets the module.


</div>

</div>
### [`KaResolutionScope`](-ka-resolution-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-ka-resolution-scope/index.html">KaResolutionScope</a> : GlobalSearchScope
</span></code></pre></div>
</div>


<div markdown>

The resolution scope for a [`KaModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md). It determines the PSI elements that can be resolved in the context of an analysis session.


</div>

</div>
### [`KaResolutionScopeProvider`](-ka-resolution-scope-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-resolution-scope-provider/index.html">KaResolutionScopeProvider</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-ka-engine-service/index.html">KaEngineService</a>
</span></code></pre></div>
</div>


<div markdown>

Provides a resolution scope for the given [`KaModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md).


</div>

</div>
### [`KotlinActualDeclarationProvider`](-kotlin-actual-declaration-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-actual-declaration-provider/index.html">KotlinActualDeclarationProvider</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

Provides `actual` declarations for the given `expect` [`KtDeclaration`](../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md).


</div>

</div>
### [`KotlinAnchorModuleProvider`](-kotlin-anchor-module-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-anchor-module-provider/index.html">KotlinAnchorModuleProvider</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinAnchorModuleProvider`](-kotlin-anchor-module-provider/index.md) provides modules which contain dependencies of libraries.


</div>

</div>
### [`KotlinCompilerPluginsProvider`](-kotlin-compiler-plugins-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-compiler-plugins-provider/index.html">KotlinCompilerPluginsProvider</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinCompilerPluginsProvider`](-kotlin-compiler-plugins-provider/index.md) provides information about registered compiler plugins.


</div>

</div>
### [`KotlinContentScopeRefiner`](-kotlin-content-scope-refiner/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-content-scope-refiner/index.html">KotlinContentScopeRefiner</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

A contributor to [`KaModule.contentScope`](-ka-dangling-file-module-impl/index.md#contentscope).


</div>

</div>
### [`KotlinGlobalSearchScopeMergeStrategy`](-kotlin-global-search-scope-merge-strategy/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-global-search-scope-merge-strategy/index.html">KotlinGlobalSearchScopeMergeStrategy</a><span class="o"><</span><a href="-kotlin-global-search-scope-merge-strategy/index.html">T</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinGlobalSearchScopeMergeStrategy`](-kotlin-global-search-scope-merge-strategy/index.md) is used to declare a strategy for merging a list of GlobalSearchScopes into a single GlobalSearchScope. Is used by implementations of [`KaGlobalSearchScopeMerger`](-ka-global-search-scope-merger/index.md) to optimize the merging process and flatten the resulting scope.


</div>

</div>
### [`KotlinIntersectionScopeMergeTarget`](-kotlin-intersection-scope-merge-target/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-intersection-scope-merge-target/index.html">KotlinIntersectionScopeMergeTarget</a>
</span></code></pre></div>
</div>


<div markdown>

A marker interface for GlobalSearchScopes that can be factored out of an intersection scope using the distributive property. This helps the intersection scope merge strategy to pick the correct targets.


</div>

</div>
### [`KotlinModuleDependentsProvider`](-kotlin-module-dependents-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-module-dependents-provider/index.html">KotlinModuleDependentsProvider</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinModuleDependentsProvider`](-kotlin-module-dependents-provider/index.md) provides dependents for a [`KaModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md), which are modules that depend on the [`KaModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md).


</div>

</div>
### [`KotlinModuleDependentsProviderBase`](-kotlin-module-dependents-provider-base/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kotlin-module-dependents-provider-base/index.html">KotlinModuleDependentsProviderBase</a> : <a href="-kotlin-module-dependents-provider/index.html">KotlinModuleDependentsProvider</a>
</span></code></pre></div>
</div>

</div>
### [`KotlinModuleInformationProvider`](-kotlin-module-information-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-module-information-provider/index.html">KotlinModuleInformationProvider</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinModuleInformationProvider`](-kotlin-module-information-provider/index.md) offers additional, secondary information about [`KaModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md)s.


</div>

</div>
### [`KotlinModuleOutputProvider`](-kotlin-module-output-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-module-output-provider/index.html">KotlinModuleOutputProvider</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinModuleOutputProvider`](-kotlin-module-output-provider/index.md) provides build output directories for [`KaModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md)s.


</div>

</div>
### [`KotlinProjectStructureProvider`](-kotlin-project-structure-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-project-structure-provider/index.html">KotlinProjectStructureProvider</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinProjectStructureProvider`](-kotlin-project-structure-provider/index.md) provides information about the project's structure as managed by the Analysis API platform.


</div>

</div>
### [`KotlinProjectStructureProviderBase`](-kotlin-project-structure-provider-base/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kotlin-project-structure-provider-base/index.html">KotlinProjectStructureProviderBase</a> : <a href="-kotlin-project-structure-provider/index.html">KotlinProjectStructureProvider</a>
</span></code></pre></div>
</div>

</div>
## Properties
### [`resolveExtensionFileModule`](resolve-extension-file-module.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">var </span>VirtualFile<span class="p">.</span><a href="resolve-extension-file-module.html">resolveExtensionFileModule</a><span class="o">: </span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Used by implementations of [`KaResolveExtensionProvider`](../../analysis-api/org.jetbrains.kotlin.analysis.api.resolve.extensions/-ka-resolve-extension-provider/index.md) to store a reference of the [`KaModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md) for which a VirtualFile was generated.


</div>

</div>
## Functions
### [`computeTransitiveDependsOnDependencies`](compute-transitive-depends-on-dependencies.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="compute-transitive-depends-on-dependencies.html"><span class="nf">computeTransitiveDependsOnDependencies</span></a><span class="p">(</span>directDependsOnDependencies<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Computes the transitive `dependsOn` dependencies of [`directDependsOnDependencies`](compute-transitive-depends-on-dependencies.md). [`computeTransitiveDependsOnDependencies`](compute-transitive-depends-on-dependencies.md) is the default computation strategy to provide [`KaModule.transitiveDependsOnDependencies`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/transitive-depends-on-dependencies.md).


</div>

</div>
### [`toModulePlatformKind`](to-module-platform-kind.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>TargetPlatform<span class="p">.</span><a href="to-module-platform-kind.html"><span class="nf">toModulePlatformKind</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-module-platform-kind/index.html">KaModulePlatformKind</a>
</span></code></pre></div>
</div>

</div>
