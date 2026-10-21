---
tags:
 - jvm
title: "KaAnnotationListRenderer"
---

# KaAnnotationListRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaAnnotationListRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`FOR_SOURCE`](-f-o-r_-s-o-u-r-c-e/index.md)



</div>

## Types
### [`FOR_SOURCE`](-f-o-r_-s-o-u-r-c-e/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-f-o-r_-s-o-u-r-c-e/index.html">FOR_SOURCE</a> : <a href="index.html">KaAnnotationListRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderAnnotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#renderannotations"><span class="nf">renderAnnotations</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    owner<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a><span class="p">, </span>
    annotationRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.base.annotations/-ka-annotation-renderer/index.html">KaAnnotationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
