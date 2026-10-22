---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.renderer.declarations"
---

# org.jetbrains.kotlin.analysis.api.renderer.declarations
## Types
### [`KaCallableReturnTypeFilter`](-ka-callable-return-type-filter/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-callable-return-type-filter/index.html">KaCallableReturnTypeFilter</a>
</span></code></pre></div>
</div>

</div>
### [`KaDeclarationRenderer`](-ka-declaration-renderer/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-declaration-renderer/index.html">KaDeclarationRenderer</a>
</span></code></pre></div>
</div>

</div>
### [`KaRecommendedRendererCodeStyle`](-ka-recommended-renderer-code-style/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-ka-recommended-renderer-code-style/index.html">KaRecommendedRendererCodeStyle</a> : <a href="-ka-renderer-code-style/index.html">KaRendererCodeStyle</a>
</span></code></pre></div>
</div>

</div>
### [`KaRendererCodeStyle`](-ka-renderer-code-style/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-renderer-code-style/index.html">KaRendererCodeStyle</a>
</span></code></pre></div>
</div>

</div>
### [`KaRendererTypeApproximator`](-ka-renderer-type-approximator/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-renderer-type-approximator/index.html">KaRendererTypeApproximator</a>
</span></code></pre></div>
</div>

</div>
## Functions
### [`renderAnnotationsModifiersAndContextReceivers`](render-annotations-modifiers-and-context-receivers.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="render-annotations-modifiers-and-context-receivers.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a>, <a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">> </span><a href="render-annotations-modifiers-and-context-receivers.html"><span class="nf">renderAnnotationsModifiersAndContextReceivers</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="render-annotations-modifiers-and-context-receivers.html">S</a><span class="p">, </span>
    declarationRenderer<span class="o">: </span><a href="-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="render-annotations-modifiers-and-context-receivers.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a>, <a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">> </span><a href="render-annotations-modifiers-and-context-receivers.html"><span class="nf">renderAnnotationsModifiersAndContextReceivers</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="render-annotations-modifiers-and-context-receivers.html">S</a><span class="p">, </span>
    declarationRenderer<span class="o">: </span><a href="-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a><span class="p">, </span>
    keywords<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../psi-api/org.jetbrains.kotlin.lexer/-kt-keyword-token/index.html">KtKeywordToken</a><span class="o">></span>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="render-annotations-modifiers-and-context-receivers.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a>, <a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">> </span><a href="render-annotations-modifiers-and-context-receivers.html"><span class="nf">renderAnnotationsModifiersAndContextReceivers</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="render-annotations-modifiers-and-context-receivers.html">S</a><span class="p">, </span>
    declarationRenderer<span class="o">: </span><a href="-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a><span class="p">, </span>
    keyword<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.lexer/-kt-keyword-token/index.html">KtKeywordToken</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
