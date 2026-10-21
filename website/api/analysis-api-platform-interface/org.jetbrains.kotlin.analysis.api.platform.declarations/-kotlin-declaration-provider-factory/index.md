---
tags:
 - jvm
title: "KotlinDeclarationProviderFactory"
---

# KotlinDeclarationProviderFactory

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinDeclarationProviderFactory</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>[`KotlinDeclarationProviderFactory`](index.md) creates a scope-based [`KotlinDeclarationProvider`](../-kotlin-declaration-provider/index.md) which covers all non-generated, physical declarations found in source files and possibly indices/stubs for libraries.

The declaration provider created by [`KotlinDeclarationProviderFactory`](index.md) is considered the <strong>main declaration provider</strong> for the given scope. Other kinds of declaration providers exist, but they usually cover generated declarations for edge cases.

#### See also


 - [`KotlinDeclarationProvider`](../-kotlin-declaration-provider/index.md)



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
### createDeclarationProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createdeclarationprovider"><span class="nf">createDeclarationProvider</span></a><span class="p">(</span>scope<span class="o">: </span>GlobalSearchScope<span class="p">, </span>contextualModule<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a>
</span></code></pre></div>
</div>

</div>
