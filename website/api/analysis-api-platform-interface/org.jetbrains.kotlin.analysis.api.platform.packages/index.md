---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.platform.packages"
---

# org.jetbrains.kotlin.analysis.api.platform.packages
## Types
### [`KotlinCachingPackageProviderFactory`](-kotlin-caching-package-provider-factory/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kotlin-caching-package-provider-factory/index.html">KotlinCachingPackageProviderFactory</a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span> : <a href="-kotlin-package-provider-factory/index.html">KotlinPackageProviderFactory</a>, Disposable
</span></code></pre></div>
</div>


<div markdown>

A [`KotlinPackageProviderFactory`](-kotlin-package-provider-factory/index.md) which caches [`KotlinPackageProvider`](-kotlin-package-provider/index.md)s based on their GlobalSearchScopes. The major advantage here is that [`KotlinPackageProvider`](-kotlin-package-provider/index.md) usually caches its own results, which can only be beneficial if it's not recreated with every call to [`createPackageProvider`](-kotlin-caching-package-provider-factory/index.md#createpackageprovider).


</div>

</div>
### [`KotlinCompositePackageProvider`](-kotlin-composite-package-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-composite-package-provider/index.html">KotlinCompositePackageProvider</a> : <a href="-kotlin-package-provider/index.html">KotlinPackageProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-composite-provider/index.html">KotlinCompositeProvider</a><span class="o"><</span><a href="-kotlin-package-provider/index.html">KotlinPackageProvider</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A composite [`KotlinPackageProvider`](-kotlin-package-provider/index.md) which combines all packages provided by its child [`providers`](-kotlin-composite-package-provider/index.md#providers). It should be created with [`KotlinCompositePackageProvider.create`](-kotlin-composite-package-provider/-companion/index.md#create).


</div>

</div>
### [`KotlinEmptyPackageProvider`](-kotlin-empty-package-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-kotlin-empty-package-provider/index.html">KotlinEmptyPackageProvider</a> : <a href="-kotlin-package-provider/index.html">KotlinPackageProvider</a>
</span></code></pre></div>
</div>

</div>
### [`KotlinForwardDeclarationsPackageProviderFactory`](-kotlin-forward-declarations-package-provider-factory/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-forward-declarations-package-provider-factory/index.html">KotlinForwardDeclarationsPackageProviderFactory</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinForwardDeclarationsPackageProviderFactory`](-kotlin-forward-declarations-package-provider-factory/index.md) creates [`KotlinPackageProvider`](-kotlin-package-provider/index.md)s for Kotlin/Native forward declarations.


</div>

</div>
### [`KotlinPackagePartProviderFactory`](-kotlin-package-part-provider-factory/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-package-part-provider-factory/index.html">KotlinPackagePartProviderFactory</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KotlinPackageProvider`](-kotlin-package-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-package-provider/index.html">KotlinPackageProvider</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-composable-provider/index.html">KotlinComposableProvider</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinPackageProvider`](-kotlin-package-provider/index.md) provides information about packages that are visible to Kotlin in a certain context. The provider covers not only packages with Kotlin declarations, but also packages with declarations that match a specified TargetPlatform. For example, packages with Java declarations on the JVM platform.


</div>

</div>
### [`KotlinPackageProviderBase`](-kotlin-package-provider-base/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kotlin-package-provider-base/index.html">KotlinPackageProviderBase</a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">, </span><span class="kd">val </span>searchScope<span class="o">: </span>GlobalSearchScope<span class="p">)</span> : <a href="-kotlin-package-provider/index.html">KotlinPackageProvider</a>
</span></code></pre></div>
</div>

</div>
### [`KotlinPackageProviderFactory`](-kotlin-package-provider-factory/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-package-provider-factory/index.html">KotlinPackageProviderFactory</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinPackageProviderFactory`](-kotlin-package-provider-factory/index.md) creates a scope-based [`KotlinPackageProvider`](-kotlin-package-provider/index.md) which covers all non-generated packages found in source files and possibly indices/stubs for libraries.


</div>

</div>
### [`KotlinPackageProviderMerger`](-kotlin-package-provider-merger/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-package-provider-merger/index.html">KotlinPackageProviderMerger</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-composable-provider-merger/index.html">KotlinComposableProviderMerger</a><span class="o"><</span><a href="-kotlin-package-provider/index.html">KotlinPackageProvider</a><span class="o">> </span>, <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinPackageProviderMerger`](-kotlin-package-provider-merger/index.md) allows merging multiple [`KotlinPackageProvider`](-kotlin-package-provider/index.md)s into a more efficient package provider.


</div>

</div>
## Functions
### [`createForwardDeclarationsPackageProvider`](create-forward-declarations-package-provider.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="create-forward-declarations-package-provider.html"><span class="nf">createForwardDeclarationsPackageProvider</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span><span class="o">: </span><a href="-kotlin-package-provider/index.html">KotlinPackageProvider</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a package provider for Kotlin/Native forward declaration packages in [`module`](create-forward-declarations-package-provider.md), or `null` if the module cannot contain forward declarations.


</div>

</div>
### [`createPackagePartProvider`](create-package-part-provider.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="create-package-part-provider.html"><span class="nf">createPackagePartProvider</span></a><span class="p">(</span>scope<span class="o">: </span>GlobalSearchScope<span class="p">)</span><span class="o">: </span>PackagePartProvider
</span></code></pre></div>
</div>


<div markdown>

Create a PackagePartProvider for a given scope. PackagePartProvider is responsible for searching sub packages in a library.


</div>

</div>
### [`createPackageProvider`](create-package-provider.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="create-package-provider.html"><span class="nf">createPackageProvider</span></a><span class="p">(</span>searchScope<span class="o">: </span>GlobalSearchScope<span class="p">)</span><span class="o">: </span><a href="-kotlin-package-provider/index.html">KotlinPackageProvider</a>
</span></code></pre></div>
</div>

</div>
### [`mergePackageProviders`](merge-package-providers.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="merge-package-providers.html"><span class="nf">mergePackageProviders</span></a><span class="p">(</span>packageProviders<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-kotlin-package-provider/index.html">KotlinPackageProvider</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="-kotlin-package-provider/index.html">KotlinPackageProvider</a>
</span></code></pre></div>
</div>

</div>
