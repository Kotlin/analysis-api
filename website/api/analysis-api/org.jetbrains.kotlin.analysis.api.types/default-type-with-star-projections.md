---
tags:
 - jvm
title: "defaultTypeWithStarProjections"
---

# defaultTypeWithStarProjections

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="p">.</span><a href="default-type-with-star-projections.html">defaultTypeWithStarProjections</a><span class="o">: </span><a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The representation of [`this`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) in terms of [`KaType`](-ka-type/index.md).

Type parameters are substituted with [`KaStarTypeProjection`](-ka-star-type-projection/index.md), e.g. `List<*>` for the `List` class.

#### See also


 - [`KaTypeCreator`](../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.md)



</div>

</div>
