---
tags:
 - jvm
title: "KaClassInitializerRenderer"
---

# KaClassInitializerRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaClassInitializerRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`INIT_BLOCK_WITH_BRACES`](-i-n-i-t_-b-l-o-c-k_-w-i-t-h_-b-r-a-c-e-s/index.md)



</div>

## Types
### [`INIT_BLOCK_WITH_BRACES`](-i-n-i-t_-b-l-o-c-k_-w-i-t-h_-b-r-a-c-e-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-i-n-i-t_-b-l-o-c-k_-w-i-t-h_-b-r-a-c-e-s/index.html">INIT_BLOCK_WITH_BRACES</a> : <a href="index.html">KaClassInitializerRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderClassInitializer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#renderclassinitializer"><span class="nf">renderClassInitializer</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-initializer-symbol/index.html">KaClassInitializerSymbol</a><span class="p">, </span>
    declarationRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
