---
tags:
 - jvm
title: "KaClassifierBodyRenderer"
---

# KaClassifierBodyRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaClassifierBodyRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`NO_BODY`](-n-o_-b-o-d-y/index.md)
 - [`EMPTY_BRACES`](-e-m-p-t-y_-b-r-a-c-e-s/index.md)
 - [`KaClassifierBodyWithMembersRenderer`](../-ka-classifier-body-with-members-renderer/index.md)



</div>

## Types
### [`BODY_WITH_MEMBERS`](-b-o-d-y_-w-i-t-h_-m-e-m-b-e-r-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-b-o-d-y_-w-i-t-h_-m-e-m-b-e-r-s/index.html">BODY_WITH_MEMBERS</a> : <a href="../-ka-classifier-body-with-members-renderer/index.html">KaClassifierBodyWithMembersRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`BODY_WITH_MEMBERS_OR_EMPTY_BRACES`](-b-o-d-y_-w-i-t-h_-m-e-m-b-e-r-s_-o-r_-e-m-p-t-y_-b-r-a-c-e-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-b-o-d-y_-w-i-t-h_-m-e-m-b-e-r-s_-o-r_-e-m-p-t-y_-b-r-a-c-e-s/index.html">BODY_WITH_MEMBERS_OR_EMPTY_BRACES</a> : <a href="../-ka-classifier-body-with-members-renderer/index.html">KaClassifierBodyWithMembersRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`EMPTY_BRACES`](-e-m-p-t-y_-b-r-a-c-e-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-e-m-p-t-y_-b-r-a-c-e-s/index.html">EMPTY_BRACES</a> : <a href="index.html">KaClassifierBodyRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`NO_BODY`](-n-o_-b-o-d-y/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o_-b-o-d-y/index.html">NO_BODY</a> : <a href="index.html">KaClassifierBodyRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderBody

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#renderbody"><span class="nf">renderBody</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">, </span>
    declarationRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
