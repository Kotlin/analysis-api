---
tags:
 - jvm
title: "KaKeywordsRenderer"
---

# KaKeywordsRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KaKeywordsRenderer</a>
</span></code></pre></div>
</div>

## Types
### [`Builder`](-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-builder/index.html">Builder</a>
</span></code></pre></div>
</div>

</div>
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Properties
### keywordFilter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#keywordfilter">keywordFilter</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.declarations.modifiers.renderers/-ka-renderer-keyword-filter/index.html">KaRendererKeywordFilter</a>
</span></code></pre></div>
</div>

</div>
### keywordRenderer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#keywordrenderer">keywordRenderer</a><span class="o">: </span><a href="../-ka-keyword-renderer/index.html">KaKeywordRenderer</a>
</span></code></pre></div>
</div>

</div>
## Functions
### renderKeyword

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#renderkeyword"><span class="nf">renderKeyword</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    keyword<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.lexer/-kt-keyword-token/index.html">KtKeywordToken</a><span class="p">, </span>
    owner<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### renderKeywords

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#renderkeywords"><span class="nf">renderKeywords</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    keywords<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.lexer/-kt-keyword-token/index.html">KtKeywordToken</a><span class="o">></span><span class="p">, </span>
    owner<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### with

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="index.html#with"><span class="nf">with</span></a><span class="p">(</span>action<span class="o">: </span><a href="-builder/index.html">KaKeywordsRenderer.Builder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaKeywordsRenderer</a>
</span></code></pre></div>
</div>

</div>
