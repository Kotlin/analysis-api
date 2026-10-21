---
tags:
 - jvm
title: "KaTypeProjectionRenderer"
---

# KaTypeProjectionRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaTypeProjectionRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`WITH_VARIANCE`](-w-i-t-h_-v-a-r-i-a-n-c-e/index.md)
 - [`WITHOUT_VARIANCE`](-w-i-t-h-o-u-t_-v-a-r-i-a-n-c-e/index.md)



</div>

## Types
### [`WITH_VARIANCE`](-w-i-t-h_-v-a-r-i-a-n-c-e/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-w-i-t-h_-v-a-r-i-a-n-c-e/index.html">WITH_VARIANCE</a> : <a href="index.html">KaTypeProjectionRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`WITHOUT_VARIANCE`](-w-i-t-h-o-u-t_-v-a-r-i-a-n-c-e/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-w-i-t-h-o-u-t_-v-a-r-i-a-n-c-e/index.html">WITHOUT_VARIANCE</a> : <a href="index.html">KaTypeProjectionRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderTypeProjection

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#rendertypeprojection"><span class="nf">renderTypeProjection</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    projection<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-projection/index.html">KaTypeProjection</a><span class="p">, </span>
    typeRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.types/-ka-type-renderer/index.html">KaTypeRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
