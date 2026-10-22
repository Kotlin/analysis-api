---
tags:
 - jvm
title: "KaResolutionScope"
---

# KaResolutionScope

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KaResolutionScope</a> : GlobalSearchScope
</span></code></pre></div>The resolution scope for a [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md). It determines the PSI elements that can be resolved in the context of an analysis session.

A resolution scope is mainly built from its use-site module's [`KaModule.contentScope`](../-ka-dangling-file-module-impl/index.md#contentscope) and its dependencies' content scopes.


</div>

## Constructors
### KaResolutionScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

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
### [`displayName`](index.md#displayname)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">Nls</span><span class="p">(</span>capitalization<span class="o"> = </span>Nls.Capitalization.Sentence<span class="p">)</span>
<span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">val </span><a href="index.html#displayname">displayName</a><span class="o">: </span><span class="se">@</span><span class="se">Nls</span><span class="p">(</span>capitalization<span class="o"> = </span>Nls.Capitalization.Sentence<span class="p">)</span> <span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`icon`](index.md#icon)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">val </span><a href="index.html#icon">icon</a><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="https://docs.oracle.com/javase/8/docs/api/javax/swing/Icon.html">Icon</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`isForceSearchingInLibrarySources`](index.md#isforcesearchinginlibrarysources)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="index.html#isforcesearchinginlibrarysources">isForceSearchingInLibrarySources</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isSearchInLibraries`](index.md#issearchinlibraries)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#issearchinlibraries">isSearchInLibraries</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`project`](index.md#project)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">val </span><a href="index.html#project">project</a><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> Project<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### underlyingSearchScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#underlyingsearchscope">underlyingSearchScope</a><span class="o">: </span>GlobalSearchScope
</span></code></pre></div>
</div>


<div markdown>

The underlying GlobalSearchScope that covers all physical files contained in the resolution scope. <strong>Only intended for test purposes.</strong>


</div>

</div>
### [`unloadedModulesBelongingToScope`](index.md#unloadedmodulesbelongingtoscope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">val </span><a href="index.html#unloadedmodulesbelongingtoscope">unloadedModulesBelongingToScope</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span>UnloadedModuleDescription<span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>
## Functions
### [`accept`](index.md#accept)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#accept"><span class="nf">accept</span></a><span class="p">(</span>file<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> VirtualFile<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`and`](index.md#and)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#and"><span class="nf">and</span></a><span class="p">(</span>other<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> VirtualFileFilter<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> VirtualFileFilter
</span></code></pre></div>
</div>

</div>
### [`compare`](index.md#compare)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#compare"><span class="nf">compare</span></a><span class="p">(</span>file1<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> VirtualFile<span class="p">, </span>file2<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> VirtualFile<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`contains`](index.md#contains)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">operator </span><span class="kd">fun </span><a href="index.html#contains"><span class="nf">contains</span></a><span class="p">(</span>p0<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> VirtualFile<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#contains"><span class="nf">contains</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether a PsiElement is contained in the resolution scope, i.e., the containing file is present in the resolution scope.


</div>

</div>
### [`hashCode`](index.md#hashcode)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#hashcode"><span class="nf">hashCode</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`intersectWith`](index.md#intersectwith)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#intersectwith"><span class="nf">intersectWith</span></a><span class="p">(</span>scope<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> GlobalSearchScope<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> GlobalSearchScope
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#intersectwith"><span class="nf">intersectWith</span></a><span class="p">(</span>localScope2<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> LocalSearchScope<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> LocalSearchScope
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#intersectwith"><span class="nf">intersectWith</span></a><span class="p">(</span>scope2<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> SearchScope<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> SearchScope
</span></code></pre></div>
</div>

</div>
### [`isSearchInModuleContent`](index.md#issearchinmodulecontent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#issearchinmodulecontent"><span class="nf">isSearchInModuleContent</span></a><span class="p">(</span>p0<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Module<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#issearchinmodulecontent"><span class="nf">isSearchInModuleContent</span></a><span class="p">(</span>aModule<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Module<span class="p">, </span>testSources<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`toFullString`](index.md#tofullstring)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#tofullstring"><span class="nf">toFullString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`union`](index.md#union)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#union"><span class="nf">union</span></a><span class="p">(</span>scope<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> LocalSearchScope<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> GlobalSearchScope
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#union"><span class="nf">union</span></a><span class="p">(</span>scope<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> SearchScope<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> GlobalSearchScope
</span></code></pre></div>
</div>

</div>
### [`uniteWith`](index.md#unitewith)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#unitewith"><span class="nf">uniteWith</span></a><span class="p">(</span>scope<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> GlobalSearchScope<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> GlobalSearchScope
</span></code></pre></div>
</div>

</div>
