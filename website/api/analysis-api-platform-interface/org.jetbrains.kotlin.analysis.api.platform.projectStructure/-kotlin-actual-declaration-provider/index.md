---
tags:
 - jvm
title: "KotlinActualDeclarationProvider"
---

# KotlinActualDeclarationProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinActualDeclarationProvider</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>Provides `actual` declarations for the given `expect` [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md).

The implementation should be consistent with the `KaSymbolRelationProvider.getExpectsForActual`.


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
### getActualDeclarations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getactualdeclarations"><span class="nf">getActualDeclarations</span></a><span class="p">(</span>declaration<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns `actual` declarations for the given `expect` [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md) from all available implementing modules.


</div>

</div>
