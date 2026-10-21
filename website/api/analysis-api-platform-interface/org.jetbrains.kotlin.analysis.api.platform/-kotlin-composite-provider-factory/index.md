---
tags:
 - jvm
title: "KotlinCompositeProviderFactory"
---

# KotlinCompositeProviderFactory

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KotlinCompositeProviderFactory</a><span class="o"><</span><a href="index.html">P</a><span class="o"> : </span><a href="../-kotlin-composable-provider/index.html">KotlinComposableProvider</a><span class="o">></span><span class="p">(</span>emptyProvider<span class="o">: </span><a href="index.html">P</a><span class="p">, </span>composeProviders<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">P</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>[`KotlinCompositeProviderFactory`](index.md) is used by various [`KotlinCompositeProvider`](../-kotlin-composite-provider/index.md)s to share code related to provider creation and flattening.


</div>

## Constructors
### KotlinCompositeProviderFactory

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>emptyProvider<span class="o">: </span><a href="index.html">P</a><span class="p">, </span>composeProviders<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">P</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Functions
### create

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#create"><span class="nf">create</span></a><span class="p">(</span>providers<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">P</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="index.html">P</a>
</span></code></pre></div>
</div>

</div>
### createFlattened

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createflattened"><span class="nf">createFlattened</span></a><span class="p">(</span>providers<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">P</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="index.html">P</a>
</span></code></pre></div>
</div>

</div>
### flatten

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#flatten"><span class="nf">flatten</span></a><span class="p">(</span>providers<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">P</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">P</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
