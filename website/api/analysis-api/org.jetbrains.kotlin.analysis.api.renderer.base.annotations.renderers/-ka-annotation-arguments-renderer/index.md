---
tags:
 - jvm
title: "KaAnnotationArgumentsRenderer"
---

# KaAnnotationArgumentsRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaAnnotationArgumentsRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`NONE`](-n-o-n-e/index.md)
 - [`IF_ANY`](-i-f_-a-n-y/index.md)



</div>

## Types
### [`IF_ANY`](-i-f_-a-n-y/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-i-f_-a-n-y/index.html">IF_ANY</a> : <a href="index.html">KaAnnotationArgumentsRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`NONE`](-n-o-n-e/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o-n-e/index.html">NONE</a> : <a href="index.html">KaAnnotationArgumentsRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderAnnotationArguments

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#renderannotationarguments"><span class="nf">renderAnnotationArguments</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    annotation<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation/index.html">KaAnnotation</a><span class="p">, </span>
    owner<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a><span class="p">, </span>
    annotationRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.base.annotations/-ka-annotation-renderer/index.html">KaAnnotationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
