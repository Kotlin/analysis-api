---
tags:
 - jvm
title: "KotlinPackageProviderFactory"
---

# KotlinPackageProviderFactory

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinPackageProviderFactory</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>[`KotlinPackageProviderFactory`](index.md) creates a scope-based [`KotlinPackageProvider`](../-kotlin-package-provider/index.md) which covers all non-generated packages found in source files and possibly indices/stubs for libraries.

The package provider created by [`KotlinPackageProviderFactory`](index.md) is considered the <strong>main package provider</strong> for the given scope. Other kinds of package providers exist, but they usually cover generated packages for edge cases.

#### See also


 - [`KotlinPackageProvider`](../-kotlin-package-provider/index.md)


#### Inheritors


 - [`KotlinCachingPackageProviderFactory`](../-kotlin-caching-package-provider-factory/index.md)



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
### createPackageProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createpackageprovider"><span class="nf">createPackageProvider</span></a><span class="p">(</span>searchScope<span class="o">: </span>GlobalSearchScope<span class="p">)</span><span class="o">: </span><a href="../-kotlin-package-provider/index.html">KotlinPackageProvider</a>
</span></code></pre></div>
</div>

</div>
