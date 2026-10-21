---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.platform.declarations"
---

# org.jetbrains.kotlin.analysis.api.platform.declarations
## Types
### [`KotlinAnnotationsResolver`](-kotlin-annotations-resolver/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-annotations-resolver/index.html">KotlinAnnotationsResolver</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinAnnotationsResolver`](-kotlin-annotations-resolver/index.md) matches declarations with their annotations and vice versa.


</div>

</div>
### [`KotlinAnnotationsResolverFactory`](-kotlin-annotations-resolver-factory/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-annotations-resolver-factory/index.html">KotlinAnnotationsResolverFactory</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KotlinCompositeDeclarationProvider`](-kotlin-composite-declaration-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-composite-declaration-provider/index.html">KotlinCompositeDeclarationProvider</a> : <a href="-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-composite-provider/index.html">KotlinCompositeProvider</a><span class="o"><</span><a href="-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A composite [`KotlinDeclarationProvider`](-kotlin-declaration-provider/index.md) which combines all declarations provided by its child [`providers`](-kotlin-composite-declaration-provider/index.md#providers). It should be created with [`KotlinCompositeDeclarationProvider.create`](-kotlin-composite-declaration-provider/-companion/index.md#create).


</div>

</div>
### [`KotlinDeclarationProvider`](-kotlin-declaration-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-composable-provider/index.html">KotlinComposableProvider</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KotlinDeclarationProvider`](-kotlin-declaration-provider/index.md) provides Kotlin PSI declarations for the project as well as additional information about them. The declarations may come from sources, libraries in case of [`stubbing`](../org.jetbrains.kotlin.analysis.api.platform/-kotlin-deserialized-declarations-origin/-s-t-u-b-s/index.md), or declaration generation.


</div>

</div>
### [`KotlinDeclarationProviderFactory`](-kotlin-declaration-provider-factory/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-declaration-provider-factory/index.html">KotlinDeclarationProviderFactory</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinDeclarationProviderFactory`](-kotlin-declaration-provider-factory/index.md) creates a scope-based [`KotlinDeclarationProvider`](-kotlin-declaration-provider/index.md) which covers all non-generated, physical declarations found in source files and possibly indices/stubs for libraries.


</div>

</div>
### [`KotlinDeclarationProviderMerger`](-kotlin-declaration-provider-merger/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-declaration-provider-merger/index.html">KotlinDeclarationProviderMerger</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-composable-provider-merger/index.html">KotlinComposableProviderMerger</a><span class="o"><</span><a href="-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a><span class="o">> </span>, <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

While the main declaration provider created via [`createDeclarationProvider`](create-declaration-provider.md) is scope-based, there are other declaration providers which are not, such as file-based declaration providers. Not all declarations provided by such declaration providers can be provided by the main declaration provider, even if the correct scope is provided (such as a file-based scope). For example, the main declaration provider may be based on an index which doesn't contain the declarations provided by file-based declaration providers.


</div>

</div>
### [`KotlinDirectInheritorsProvider`](-kotlin-direct-inheritors-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-direct-inheritors-provider/index.html">KotlinDirectInheritorsProvider</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KotlinEmptyDeclarationProvider`](-kotlin-empty-declaration-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-kotlin-empty-declaration-provider/index.html">KotlinEmptyDeclarationProvider</a> : <a href="-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a>
</span></code></pre></div>
</div>

</div>
### [`KotlinFileBasedDeclarationProvider`](-kotlin-file-based-declaration-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-file-based-declaration-provider/index.html">KotlinFileBasedDeclarationProvider</a><span class="p">(</span><span class="kd">val </span>kotlinFile<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">)</span> : <a href="-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a>
</span></code></pre></div>
</div>

</div>
### [`KotlinForeignValueProviderService`](-kotlin-foreign-value-provider-service/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-foreign-value-provider-service/index.html">KotlinForeignValueProviderService</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KotlinForwardDeclarationProviderFactory`](-kotlin-forward-declaration-provider-factory/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-forward-declaration-provider-factory/index.html">KotlinForwardDeclarationProviderFactory</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinForwardDeclarationProviderFactory`](-kotlin-forward-declaration-provider-factory/index.md) creates [`KotlinDeclarationProvider`](-kotlin-declaration-provider/index.md)s for Kotlin/Native forward declarations.


</div>

</div>
## Functions
### [`createAnnotationResolver`](create-annotation-resolver.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="create-annotation-resolver.html"><span class="nf">createAnnotationResolver</span></a><span class="p">(</span>searchScope<span class="o">: </span>GlobalSearchScope<span class="p">)</span><span class="o">: </span><a href="-kotlin-annotations-resolver/index.html">KotlinAnnotationsResolver</a>
</span></code></pre></div>
</div>

</div>
### [`createDeclarationProvider`](create-declaration-provider.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="create-declaration-provider.html"><span class="nf">createDeclarationProvider</span></a><span class="p">(</span>scope<span class="o">: </span>GlobalSearchScope<span class="p">, </span>contextualModule<span class="o">: </span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KotlinDeclarationProvider`](-kotlin-declaration-provider/index.md) providing symbols within the given [`scope`](create-declaration-provider.md).


</div>

</div>
### [`createForwardDeclarationProvider`](create-forward-declaration-provider.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="create-forward-declaration-provider.html"><span class="nf">createForwardDeclarationProvider</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span><span class="o">: </span><a href="-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a Kotlin/Native forward declaration provider for [`module`](create-forward-declaration-provider.md), or `null` if the module cannot contain forward declarations.


</div>

</div>
### [`mergeDeclarationProviders`](merge-declaration-providers.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="merge-declaration-providers.html"><span class="nf">mergeDeclarationProviders</span></a><span class="p">(</span>declarationProviders<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a>
</span></code></pre></div>
</div>

</div>
