---
tags:
 - jvm
title: "KaClassTypeQualifierRenderer"
---

# KaClassTypeQualifierRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaClassTypeQualifierRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`WITH_SHORT_NAMES`](-w-i-t-h_-s-h-o-r-t_-n-a-m-e-s/index.md)
 - [`WITH_SHORT_NAMES_WITH_NESTED_CLASSIFIERS`](-w-i-t-h_-s-h-o-r-t_-n-a-m-e-s_-w-i-t-h_-n-e-s-t-e-d_-c-l-a-s-s-i-f-i-e-r-s/index.md)
 - [`WITH_QUALIFIED_NAMES`](-w-i-t-h_-q-u-a-l-i-f-i-e-d_-n-a-m-e-s/index.md)



</div>

## Types
### [`WITH_QUALIFIED_NAMES`](-w-i-t-h_-q-u-a-l-i-f-i-e-d_-n-a-m-e-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-w-i-t-h_-q-u-a-l-i-f-i-e-d_-n-a-m-e-s/index.html">WITH_QUALIFIED_NAMES</a> : <a href="index.html">KaClassTypeQualifierRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`WITH_SHORT_NAMES`](-w-i-t-h_-s-h-o-r-t_-n-a-m-e-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-w-i-t-h_-s-h-o-r-t_-n-a-m-e-s/index.html">WITH_SHORT_NAMES</a> : <a href="index.html">KaClassTypeQualifierRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`WITH_SHORT_NAMES_WITH_NESTED_CLASSIFIERS`](-w-i-t-h_-s-h-o-r-t_-n-a-m-e-s_-w-i-t-h_-n-e-s-t-e-d_-c-l-a-s-s-i-f-i-e-r-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-w-i-t-h_-s-h-o-r-t_-n-a-m-e-s_-w-i-t-h_-n-e-s-t-e-d_-c-l-a-s-s-i-f-i-e-r-s/index.html">WITH_SHORT_NAMES_WITH_NESTED_CLASSIFIERS</a> : <a href="index.html">KaClassTypeQualifierRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderClassTypeQualifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#renderclasstypequalifier"><span class="nf">renderClassTypeQualifier</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    qualifiers<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type-qualifier/index.html">KaClassTypeQualifier</a><span class="o">></span><span class="p">, </span>
    typeRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.types/-ka-type-renderer/index.html">KaTypeRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
