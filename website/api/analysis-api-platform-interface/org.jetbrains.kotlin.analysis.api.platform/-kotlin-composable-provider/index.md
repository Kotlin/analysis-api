---
tags:
 - jvm
title: "KotlinComposableProvider"
---

# KotlinComposableProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinComposableProvider</a>
</span></code></pre></div>A marker interface for a provider that can be composed, i.e. multiple instances of the same provider can be composed into a single provider.

Composable providers share certain traits: There is a notion of a sequentially composed [`KotlinCompositeProvider`](../-kotlin-composite-provider/index.md) of that kind, and there is usually a merge function which allows to create a single provider from a list of providers. Mergers of composable providers may produce a merged provider which is more efficient than the naive sequential composite provider.

#### See also


 - [`KotlinDeclarationProvider`](../../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-declaration-provider/index.md)
 - [`KotlinPackageProvider`](../../org.jetbrains.kotlin.analysis.api.platform.packages/-kotlin-package-provider/index.md)


#### Inheritors


 - [`KotlinCompositeProvider`](../-kotlin-composite-provider/index.md)
 - [`KotlinDeclarationProvider`](../../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-declaration-provider/index.md)
 - [`KotlinPackageProvider`](../../org.jetbrains.kotlin.analysis.api.platform.packages/-kotlin-package-provider/index.md)



</div>

