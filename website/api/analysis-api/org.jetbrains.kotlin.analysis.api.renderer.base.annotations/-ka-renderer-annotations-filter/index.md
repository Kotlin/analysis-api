---
tags:
 - jvm
title: "KaRendererAnnotationsFilter"
---

# KaRendererAnnotationsFilter

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaRendererAnnotationsFilter</a>
</span></code></pre></div>#### Inheritors


 - [`ALL`](-a-l-l/index.md)
 - [`NO_NULLABILITY`](-n-o_-n-u-l-l-a-b-i-l-i-t-y/index.md)
 - [`NO_PARAMETER_NAME`](-n-o_-p-a-r-a-m-e-t-e-r_-n-a-m-e/index.md)
 - [`NONE`](-n-o-n-e/index.md)



</div>

## Types
### [`ALL`](-a-l-l/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-a-l-l/index.html">ALL</a> : <a href="index.html">KaRendererAnnotationsFilter</a>
</span></code></pre></div>
</div>

</div>
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
### [`NO_NULLABILITY`](-n-o_-n-u-l-l-a-b-i-l-i-t-y/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o_-n-u-l-l-a-b-i-l-i-t-y/index.html">NO_NULLABILITY</a> : <a href="index.html">KaRendererAnnotationsFilter</a>
</span></code></pre></div>
</div>

</div>
### [`NO_PARAMETER_NAME`](-n-o_-p-a-r-a-m-e-t-e-r_-n-a-m-e/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o_-p-a-r-a-m-e-t-e-r_-n-a-m-e/index.html">NO_PARAMETER_NAME</a> : <a href="index.html">KaRendererAnnotationsFilter</a>
</span></code></pre></div>
</div>

</div>
### [`NONE`](-n-o-n-e/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o-n-e/index.html">NONE</a> : <a href="index.html">KaRendererAnnotationsFilter</a>
</span></code></pre></div>
</div>

</div>
## Functions
### and

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">infix </span><span class="kd">fun </span><a href="-n-o-n-e/index.html#and"><span class="nf">and</span></a><span class="p">(</span>other<span class="o">: </span><a href="index.html">KaRendererAnnotationsFilter</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaRendererAnnotationsFilter</a>
</span></code></pre></div>
</div>

</div>
### filter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#filter"><span class="nf">filter</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    annotation<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation/index.html">KaAnnotation</a><span class="p">, </span>
    owner<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a>
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### or

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">infix </span><span class="kd">fun </span><a href="-n-o-n-e/index.html#or"><span class="nf">or</span></a><span class="p">(</span>other<span class="o">: </span><a href="index.html">KaRendererAnnotationsFilter</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaRendererAnnotationsFilter</a>
</span></code></pre></div>
</div>

</div>
