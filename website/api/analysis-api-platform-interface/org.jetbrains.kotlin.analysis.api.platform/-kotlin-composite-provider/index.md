---
tags:
 - jvm
title: "KotlinCompositeProvider"
---

# KotlinCompositeProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinCompositeProvider</a><span class="o"><</span><a href="index.html">P</a><span class="o"> : </span><a href="../-kotlin-composable-provider/index.html">KotlinComposableProvider</a><span class="o">></span> : <a href="../-kotlin-composable-provider/index.html">KotlinComposableProvider</a>
</span></code></pre></div>A [`KotlinCompositeProvider`](index.md) is the sequential composition of a specific kind of composable provider [`P`](index.md).

A composite provider should only contain providers of the same base type as the composite provider itself, so implementations of [`KotlinCompositeProvider`](index.md) should always be a subtype of their type argument [`P`](index.md). (This is not enforceable in the Kotlin type system.)

#### Inheritors


 - [`KotlinCompositeDeclarationProvider`](../../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-composite-declaration-provider/index.md)
 - [`KotlinCompositePackageProvider`](../../org.jetbrains.kotlin.analysis.api.platform.packages/-kotlin-composite-package-provider/index.md)



</div>

## Properties
### providers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#providers">providers</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">P</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
