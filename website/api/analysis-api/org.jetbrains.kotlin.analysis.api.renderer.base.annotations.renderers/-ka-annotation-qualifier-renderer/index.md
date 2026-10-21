---
tags:
 - jvm
title: "KaAnnotationQualifierRenderer"
---

# KaAnnotationQualifierRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaAnnotationQualifierRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`WITH_QUALIFIED_NAMES`](-w-i-t-h_-q-u-a-l-i-f-i-e-d_-n-a-m-e-s/index.md)
 - [`WITH_SHORT_NAMES`](-w-i-t-h_-s-h-o-r-t_-n-a-m-e-s/index.md)



</div>

## Types
### [`WITH_QUALIFIED_NAMES`](-w-i-t-h_-q-u-a-l-i-f-i-e-d_-n-a-m-e-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-w-i-t-h_-q-u-a-l-i-f-i-e-d_-n-a-m-e-s/index.html">WITH_QUALIFIED_NAMES</a> : <a href="index.html">KaAnnotationQualifierRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`WITH_SHORT_NAMES`](-w-i-t-h_-s-h-o-r-t_-n-a-m-e-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-w-i-t-h_-s-h-o-r-t_-n-a-m-e-s/index.html">WITH_SHORT_NAMES</a> : <a href="index.html">KaAnnotationQualifierRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderQualifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#renderqualifier"><span class="nf">renderQualifier</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    annotation<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation/index.html">KaAnnotation</a><span class="p">, </span>
    owner<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a><span class="p">, </span>
    annotationRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.base.annotations/-ka-annotation-renderer/index.html">KaAnnotationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
