---
tags:
 - jvm
title: "createSubstitutor"
---

# createSubstitutor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="create-substitutor.html"><span class="nf">createSubstitutor</span></a><span class="p">(</span>mappings<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">, </span><a href="-ka-type/index.html">KaType</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="-ka-substitutor/index.html">KaSubstitutor</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](-ka-substitutor/index.md) based on the given [`mappings`](create-substitutor.md).

Usually, [`buildSubstitutor`](build-substitutor.md) should be preferred to build a new substitutor from scratch.

When [`mappings`](create-substitutor.md) is empty, returns [`KaSubstitutor.Empty`](-ka-substitutor/-empty/index.md). To build [`KaSubstitutor.Empty`](-ka-substitutor/-empty/index.md) specifically, use [`emptySubstitutor`](empty-substitutor.md).

#### See also


 - [`KaSubstitutor`](-ka-substitutor/index.md)



</div>

</div>
