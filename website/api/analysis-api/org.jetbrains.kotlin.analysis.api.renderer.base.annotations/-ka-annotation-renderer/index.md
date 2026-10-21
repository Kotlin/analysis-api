---
tags:
 - jvm
title: "KaAnnotationRenderer"
---

# KaAnnotationRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KaAnnotationRenderer</a>
</span></code></pre></div>
</div>

## Types
### [`Builder`](-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-builder/index.html">Builder</a>
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
## Properties
### annotationArgumentsRenderer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#annotationargumentsrenderer">annotationArgumentsRenderer</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.base.annotations.renderers/-ka-annotation-arguments-renderer/index.html">KaAnnotationArgumentsRenderer</a>
</span></code></pre></div>
</div>

</div>
### annotationFilter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#annotationfilter">annotationFilter</a><span class="o">: </span><a href="../-ka-renderer-annotations-filter/index.html">KaRendererAnnotationsFilter</a>
</span></code></pre></div>
</div>

</div>
### annotationListRenderer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#annotationlistrenderer">annotationListRenderer</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.base.annotations.renderers/-ka-annotation-list-renderer/index.html">KaAnnotationListRenderer</a>
</span></code></pre></div>
</div>

</div>
### annotationsQualifiedNameRenderer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#annotationsqualifiednamerenderer">annotationsQualifiedNameRenderer</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.base.annotations.renderers/-ka-annotation-qualifier-renderer/index.html">KaAnnotationQualifierRenderer</a>
</span></code></pre></div>
</div>

</div>
### annotationUseSiteTargetRenderer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#annotationusesitetargetrenderer">annotationUseSiteTargetRenderer</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.base.annotations.renderers/-ka-annotation-use-site-target-renderer/index.html">KaAnnotationUseSiteTargetRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderAnnotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#renderannotations"><span class="nf">renderAnnotations</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    owner<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### with

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="index.html#with"><span class="nf">with</span></a><span class="p">(</span>action<span class="o">: </span><a href="-builder/index.html">KaAnnotationRenderer.Builder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaAnnotationRenderer</a>
</span></code></pre></div>
</div>

</div>
