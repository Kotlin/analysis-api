---
tags:
 - jvm
title: "KaCallableSignatureRenderer"
---

# KaCallableSignatureRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaCallableSignatureRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`FOR_SOURCE`](-f-o-r_-s-o-u-r-c-e/index.md)



</div>

## Types
### [`FOR_SOURCE`](-f-o-r_-s-o-u-r-c-e/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-f-o-r_-s-o-u-r-c-e/index.html">FOR_SOURCE</a> : <a href="index.html">KaCallableSignatureRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderCallableSignature

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#rendercallablesignature"><span class="nf">renderCallableSignature</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">, </span>
    keyword<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.lexer/-kt-keyword-token/index.html">KtKeywordToken</a><span class="o">?</span><span class="p">, </span>
    declarationRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
