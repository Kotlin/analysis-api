---
tags:
 - jvm
title: "KaRendererTypeApproximator"
---

# KaRendererTypeApproximator

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaRendererTypeApproximator</a>
</span></code></pre></div>#### Inheritors


 - [`TO_DENOTABLE`](-t-o_-d-e-n-o-t-a-b-l-e/index.md)
 - [`NO_APPROXIMATION`](-n-o_-a-p-p-r-o-x-i-m-a-t-i-o-n/index.md)



</div>

## Types
### [`NO_APPROXIMATION`](-n-o_-a-p-p-r-o-x-i-m-a-t-i-o-n/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o_-a-p-p-r-o-x-i-m-a-t-i-o-n/index.html">NO_APPROXIMATION</a> : <a href="index.html">KaRendererTypeApproximator</a>
</span></code></pre></div>
</div>

</div>
### [`TO_DENOTABLE`](-t-o_-d-e-n-o-t-a-b-l-e/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-t-o_-d-e-n-o-t-a-b-l-e/index.html">TO_DENOTABLE</a> : <a href="index.html">KaRendererTypeApproximator</a>
</span></code></pre></div>
</div>

</div>
## Functions
### approximateType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#approximatetype"><span class="nf">approximateType</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    position<span class="o">: </span>Variance
<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>

</div>
