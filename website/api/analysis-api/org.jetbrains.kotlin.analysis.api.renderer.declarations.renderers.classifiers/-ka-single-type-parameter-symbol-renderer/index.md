---
tags:
 - jvm
title: "KaSingleTypeParameterSymbolRenderer"
---

# KaSingleTypeParameterSymbolRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaSingleTypeParameterSymbolRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`NO`](-n-o/index.md)
 - [`WITHOUT_BOUNDS`](-w-i-t-h-o-u-t_-b-o-u-n-d-s/index.md)
 - [`WITH_COMMA_SEPARATED_BOUNDS`](-w-i-t-h_-c-o-m-m-a_-s-e-p-a-r-a-t-e-d_-b-o-u-n-d-s/index.md)



</div>

## Types
### [`NO`](-n-o/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o/index.html">NO</a> : <a href="index.html">KaSingleTypeParameterSymbolRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`WITH_COMMA_SEPARATED_BOUNDS`](-w-i-t-h_-c-o-m-m-a_-s-e-p-a-r-a-t-e-d_-b-o-u-n-d-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-w-i-t-h_-c-o-m-m-a_-s-e-p-a-r-a-t-e-d_-b-o-u-n-d-s/index.html">WITH_COMMA_SEPARATED_BOUNDS</a> : <a href="index.html">KaSingleTypeParameterSymbolRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`WITHOUT_BOUNDS`](-w-i-t-h-o-u-t_-b-o-u-n-d-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-w-i-t-h-o-u-t_-b-o-u-n-d-s/index.html">WITHOUT_BOUNDS</a> : <a href="index.html">KaSingleTypeParameterSymbolRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#rendersymbol"><span class="nf">renderSymbol</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">, </span>
    declarationRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
