---
tags:
 - jvm
title: "KaRendererBodyMemberScopeProvider"
---

# KaRendererBodyMemberScopeProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaRendererBodyMemberScopeProvider</a>
</span></code></pre></div>#### Inheritors


 - [`ALL`](-a-l-l/index.md)
 - [`ALL_DECLARED`](-a-l-l_-d-e-c-l-a-r-e-d/index.md)
 - [`NONE`](-n-o-n-e/index.md)



</div>

## Types
### [`ALL`](-a-l-l/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-a-l-l/index.html">ALL</a> : <a href="index.html">KaRendererBodyMemberScopeProvider</a>
</span></code></pre></div>
</div>

</div>
### [`ALL_DECLARED`](-a-l-l_-d-e-c-l-a-r-e-d/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-a-l-l_-d-e-c-l-a-r-e-d/index.html">ALL_DECLARED</a> : <a href="index.html">KaRendererBodyMemberScopeProvider</a>
</span></code></pre></div>
</div>

</div>
### [`NONE`](-n-o-n-e/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o-n-e/index.html">NONE</a> : <a href="index.html">KaRendererBodyMemberScopeProvider</a>
</span></code></pre></div>
</div>

</div>
## Functions
### getMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getmemberscope"><span class="nf">getMemberScope</span></a><span class="p">(</span>analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
