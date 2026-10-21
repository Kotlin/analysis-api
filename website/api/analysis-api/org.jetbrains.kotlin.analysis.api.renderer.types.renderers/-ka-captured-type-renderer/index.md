---
tags:
 - jvm
title: "KaCapturedTypeRenderer"
---

# KaCapturedTypeRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaCapturedTypeRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`AS_PROJECTION`](-a-s_-p-r-o-j-e-c-t-i-o-n/index.md)
 - [`AS_CAPTURED_TYPE_WITH_PROJECTION`](-a-s_-c-a-p-t-u-r-e-d_-t-y-p-e_-w-i-t-h_-p-r-o-j-e-c-t-i-o-n/index.md)



</div>

## Types
### [`AS_CAPTURED_TYPE_WITH_PROJECTION`](-a-s_-c-a-p-t-u-r-e-d_-t-y-p-e_-w-i-t-h_-p-r-o-j-e-c-t-i-o-n/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-a-s_-c-a-p-t-u-r-e-d_-t-y-p-e_-w-i-t-h_-p-r-o-j-e-c-t-i-o-n/index.html">AS_CAPTURED_TYPE_WITH_PROJECTION</a> : <a href="index.html">KaCapturedTypeRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`AS_PROJECTION`](-a-s_-p-r-o-j-e-c-t-i-o-n/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-a-s_-p-r-o-j-e-c-t-i-o-n/index.html">AS_PROJECTION</a> : <a href="index.html">KaCapturedTypeRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#rendertype"><span class="nf">renderType</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-captured-type/index.html">KaCapturedType</a><span class="p">, </span>
    typeRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.types/-ka-type-renderer/index.html">KaTypeRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
