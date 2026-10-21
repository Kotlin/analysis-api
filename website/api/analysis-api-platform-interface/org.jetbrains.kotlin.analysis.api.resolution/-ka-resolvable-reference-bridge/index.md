---
tags:
 - jvm
title: "KaResolvableReferenceBridge"
---

# KaResolvableReferenceBridge

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaResolvableReferenceBridge</a>
</span></code></pre></div>This is a temporary bridge to keep [`org.jetbrains.kotlin.analysis.api.components.KaResolver.resolveToSymbols`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-resolver/resolve-to-symbols.md) API in a workable state while allowing to move all reference implementations to the Kotlin IntelliJ plugin.

This bridge should be dropped once the new resolution API is stabilized and all `KtReference` usages are gone from the public API.


</div>

## Functions
### resolveToSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">.</span><a href="index.html#resolvetosymbols"><span class="nf">resolveToSymbols</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The implementation to be used as the engine


</div>

</div>
