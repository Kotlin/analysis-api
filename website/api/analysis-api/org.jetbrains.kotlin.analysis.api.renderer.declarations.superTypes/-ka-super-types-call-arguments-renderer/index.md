---
tags:
 - jvm
title: "KaSuperTypesCallArgumentsRenderer"
---

# KaSuperTypesCallArgumentsRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaSuperTypesCallArgumentsRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`NO_ARGS`](-n-o_-a-r-g-s/index.md)
 - [`EMPTY_PARENS`](-e-m-p-t-y_-p-a-r-e-n-s/index.md)



</div>

## Types
### [`EMPTY_PARENS`](-e-m-p-t-y_-p-a-r-e-n-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-e-m-p-t-y_-p-a-r-e-n-s/index.html">EMPTY_PARENS</a> : <a href="index.html">KaSuperTypesCallArgumentsRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`NO_ARGS`](-n-o_-a-r-g-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o_-a-r-g-s/index.html">NO_ARGS</a> : <a href="index.html">KaSuperTypesCallArgumentsRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderSuperTypeArguments

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#rendersupertypearguments"><span class="nf">renderSuperTypeArguments</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">, </span>
    declarationRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
