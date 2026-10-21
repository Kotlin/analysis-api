---
tags:
 - jvm
title: "KotlinCachingPackageProviderFactory"
---

# KotlinCachingPackageProviderFactory

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KotlinCachingPackageProviderFactory</a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span> : <a href="../-kotlin-package-provider-factory/index.html">KotlinPackageProviderFactory</a>, Disposable
</span></code></pre></div>A [`KotlinPackageProviderFactory`](../-kotlin-package-provider-factory/index.md) which caches [`KotlinPackageProvider`](../-kotlin-package-provider/index.md)s based on their GlobalSearchScopes. The major advantage here is that [`KotlinPackageProvider`](../-kotlin-package-provider/index.md) usually caches its own results, which can only be beneficial if it's not recreated with every call to [`createPackageProvider`](index.md#createpackageprovider).


</div>

## Constructors
### KotlinCachingPackageProviderFactory

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Functions
### createPackageProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#createpackageprovider"><span class="nf">createPackageProvider</span></a><span class="p">(</span>searchScope<span class="o">: </span>GlobalSearchScope<span class="p">)</span><span class="o">: </span><a href="../-kotlin-package-provider/index.html">KotlinPackageProvider</a>
</span></code></pre></div>
</div>

</div>
### dispose

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#dispose"><span class="nf">dispose</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
