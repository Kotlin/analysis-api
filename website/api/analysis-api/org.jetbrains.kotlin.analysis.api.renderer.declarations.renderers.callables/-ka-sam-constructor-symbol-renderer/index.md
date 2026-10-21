---
tags:
 - jvm
title: "KaSamConstructorSymbolRenderer"
---

# KaSamConstructorSymbolRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaSamConstructorSymbolRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`NOT_RENDER`](-n-o-t_-r-e-n-d-e-r/index.md)
 - [`AS_FUNCTION`](-a-s_-f-u-n-c-t-i-o-n/index.md)



</div>

## Types
### [`AS_FUNCTION`](-a-s_-f-u-n-c-t-i-o-n/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-a-s_-f-u-n-c-t-i-o-n/index.html">AS_FUNCTION</a> : <a href="index.html">KaSamConstructorSymbolRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`NOT_RENDER`](-n-o-t_-r-e-n-d-e-r/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o-t_-r-e-n-d-e-r/index.html">NOT_RENDER</a> : <a href="index.html">KaSamConstructorSymbolRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#rendersymbol"><span class="nf">renderSymbol</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-sam-constructor-symbol/index.html">KaSamConstructorSymbol</a><span class="p">, </span>
    declarationRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
