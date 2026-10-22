---
tags:
 - jvm
title: "KaDefaultImports"
---

# KaDefaultImports

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaDefaultImports</a>
</span></code></pre></div>Represents information for [default imports](https://kotlinlang.org/docs/packages.html#default-imports) for a specific platform.


</div>

## Properties
### defaultImports

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#defaultimports">defaultImports</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-default-import/index.html">KaDefaultImport</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of [`ImportPath`](../../../psi-api/org.jetbrains.kotlin.resolve/-import-path/index.md) with [`KaDefaultImportPriority`](../-ka-default-import-priority/index.md) that represents a list of imports which are implicitly present by default in every file.

Some of these imports are star imports, and from them, we exclude some specific paths. This information is present in [`excludedFromDefaultImports`](index.md#excludedfromdefaultimports).


</div>

</div>
### excludedFromDefaultImports

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#excludedfromdefaultimports">excludedFromDefaultImports</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.resolve/-import-path/index.html">ImportPath</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of non-star import paths that are excluded from some star default imports provided by [`defaultImports`](index.md#defaultimports).


</div>

</div>
