---
tags:
 - jvm
title: "KaClassifierBodyWithMembersRenderer"
---

# KaClassifierBodyWithMembersRenderer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KaClassifierBodyWithMembersRenderer</a> : <a href="../-ka-classifier-body-renderer/index.html">KaClassifierBodyRenderer</a>
</span></code></pre></div>#### Inheritors


 - [`BODY_WITH_MEMBERS`](../-ka-classifier-body-renderer/-b-o-d-y_-w-i-t-h_-m-e-m-b-e-r-s/index.md)
 - [`BODY_WITH_MEMBERS_OR_EMPTY_BRACES`](../-ka-classifier-body-renderer/-b-o-d-y_-w-i-t-h_-m-e-m-b-e-r-s_-o-r_-e-m-p-t-y_-b-r-a-c-e-s/index.md)



</div>

## Constructors
### KaClassifierBodyWithMembersRenderer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Functions
### renderBody

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#renderbody"><span class="nf">renderBody</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">, </span>
    declarationRenderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">, </span>
    printer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.utils.printer/-pretty-printer/index.html">PrettyPrinter</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### renderEmptyBodyForEmptyMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#renderemptybodyforemptymemberscope"><span class="nf">renderEmptyBodyForEmptyMemberScope</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
