---
tags:
 - jvm
title: "KaTypeParametersRenderer"
---

# KaTypeParametersRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaTypeParametersRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`NO_TYPE_PARAMETERS`](-n-o_-t-y-p-e_-p-a-r-a-m-e-t-e-r-s/index.md)
 - [`WITHOUT_BOUNDS`](-w-i-t-h-o-u-t_-b-o-u-n-d-s/index.md)
 - [`WITH_BOUNDS_IN_WHERE_CLAUSE`](-w-i-t-h_-b-o-u-n-d-s_-i-n_-w-h-e-r-e_-c-l-a-u-s-e/index.md)



</div>

## Types
### [`NO_TYPE_PARAMETERS`](-n-o_-t-y-p-e_-p-a-r-a-m-e-t-e-r-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o_-t-y-p-e_-p-a-r-a-m-e-t-e-r-s/index.html">NO_TYPE_PARAMETERS</a> : <a href="index.html">KaTypeParametersRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`WITH_BOUNDS_IN_WHERE_CLAUSE`](-w-i-t-h_-b-o-u-n-d-s_-i-n_-w-h-e-r-e_-c-l-a-u-s-e/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-w-i-t-h_-b-o-u-n-d-s_-i-n_-w-h-e-r-e_-c-l-a-u-s-e/index.html">WITH_BOUNDS_IN_WHERE_CLAUSE</a> : <a href="index.html">KaTypeParametersRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`WITHOUT_BOUNDS`](-w-i-t-h-o-u-t_-b-o-u-n-d-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-w-i-t-h-o-u-t_-b-o-u-n-d-s/index.html">WITHOUT_BOUNDS</a> : <a href="index.html">KaTypeParametersRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderTypeParameters

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#rendertypeparameters"><span class="nf">renderTypeParameters</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">, </span>
    declarationRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### renderWhereClause

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#renderwhereclause"><span class="nf">renderWhereClause</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">, </span>
    declarationRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
