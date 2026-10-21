---
tags:
 - jvm
title: "KaRendererModalityModifierProvider"
---

# KaRendererModalityModifierProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaRendererModalityModifierProvider</a>
</span></code></pre></div>#### Inheritors


 - [`WITH_IMPLICIT_MODALITY`](-w-i-t-h_-i-m-p-l-i-c-i-t_-m-o-d-a-l-i-t-y/index.md)
 - [`WITHOUT_IMPLICIT_MODALITY`](-w-i-t-h-o-u-t_-i-m-p-l-i-c-i-t_-m-o-d-a-l-i-t-y/index.md)



</div>

## Types
### [`WITH_IMPLICIT_MODALITY`](-w-i-t-h_-i-m-p-l-i-c-i-t_-m-o-d-a-l-i-t-y/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-w-i-t-h_-i-m-p-l-i-c-i-t_-m-o-d-a-l-i-t-y/index.html">WITH_IMPLICIT_MODALITY</a> : <a href="index.html">KaRendererModalityModifierProvider</a>
</span></code></pre></div>
</div>

</div>
### [`WITHOUT_IMPLICIT_MODALITY`](-w-i-t-h-o-u-t_-i-m-p-l-i-c-i-t_-m-o-d-a-l-i-t-y/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-w-i-t-h-o-u-t_-i-m-p-l-i-c-i-t_-m-o-d-a-l-i-t-y/index.html">WITHOUT_IMPLICIT_MODALITY</a> : <a href="index.html">KaRendererModalityModifierProvider</a>
</span></code></pre></div>
</div>

</div>
## Functions
### getModalityModifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getmodalitymodifier"><span class="nf">getModalityModifier</span></a><span class="p">(</span>analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">)</span><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### onlyIf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="-w-i-t-h-o-u-t_-i-m-p-l-i-c-i-t_-m-o-d-a-l-i-t-y/index.html#onlyif"><span class="nf">onlyIf</span></a><span class="p">(</span>condition<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">.</span><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaRendererModalityModifierProvider</a>
</span></code></pre></div>
</div>

</div>
