---
tags:
 - jvm
title: "KaUnresolvedClassErrorTypeRenderer"
---

# KaUnresolvedClassErrorTypeRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaUnresolvedClassErrorTypeRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`UNRESOLVED_QUALIFIER`](-u-n-r-e-s-o-l-v-e-d_-q-u-a-l-i-f-i-e-r/index.md)
 - [`AS_ERROR_WORD`](-a-s_-e-r-r-o-r_-w-o-r-d/index.md)
 - [`WITH_ERROR_MESSAGE`](-w-i-t-h_-e-r-r-o-r_-m-e-s-s-a-g-e/index.md)



</div>

## Types
### [`AS_ERROR_WORD`](-a-s_-e-r-r-o-r_-w-o-r-d/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-a-s_-e-r-r-o-r_-w-o-r-d/index.html">AS_ERROR_WORD</a> : <a href="index.html">KaUnresolvedClassErrorTypeRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`UNRESOLVED_QUALIFIER`](-u-n-r-e-s-o-l-v-e-d_-q-u-a-l-i-f-i-e-r/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-u-n-r-e-s-o-l-v-e-d_-q-u-a-l-i-f-i-e-r/index.html">UNRESOLVED_QUALIFIER</a> : <a href="index.html">KaUnresolvedClassErrorTypeRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`WITH_ERROR_MESSAGE`](-w-i-t-h_-e-r-r-o-r_-m-e-s-s-a-g-e/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-w-i-t-h_-e-r-r-o-r_-m-e-s-s-a-g-e/index.html">WITH_ERROR_MESSAGE</a> : <a href="index.html">KaUnresolvedClassErrorTypeRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#rendertype"><span class="nf">renderType</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-class-error-type/index.html">KaClassErrorType</a><span class="p">, </span>
    typeRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.types/-ka-type-renderer/index.html">KaTypeRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
