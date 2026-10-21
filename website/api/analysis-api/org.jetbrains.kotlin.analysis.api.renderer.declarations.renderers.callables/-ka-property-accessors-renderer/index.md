---
tags:
 - jvm
title: "KaPropertyAccessorsRenderer"
---

# KaPropertyAccessorsRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaPropertyAccessorsRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`ALL`](-a-l-l/index.md)
 - [`NO_DEFAULT`](-n-o_-d-e-f-a-u-l-t/index.md)
 - [`NONE`](-n-o-n-e/index.md)



</div>

## Types
### [`ALL`](-a-l-l/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-a-l-l/index.html">ALL</a> : <a href="index.html">KaPropertyAccessorsRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`NO_DEFAULT`](-n-o_-d-e-f-a-u-l-t/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o_-d-e-f-a-u-l-t/index.html">NO_DEFAULT</a> : <a href="index.html">KaPropertyAccessorsRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`NONE`](-n-o-n-e/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o-n-e/index.html">NONE</a> : <a href="index.html">KaPropertyAccessorsRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderAccessors

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#renderaccessors"><span class="nf">renderAccessors</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-property-symbol/index.html">KaPropertySymbol</a><span class="p">, </span>
    declarationRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
