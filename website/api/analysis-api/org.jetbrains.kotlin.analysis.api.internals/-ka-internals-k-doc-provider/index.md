---
tags:
 - jvm
title: "KaInternalsKDocProvider"
---

# KaInternalsKDocProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaInternalsKDocProvider</a>
</span></code></pre></div>
</div>

## Functions
### findKDoc

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#findkdoc"><span class="nf">findKDoc</span></a><span class="p">(</span>declaration<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">)</span><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.kdoc.psi.api/-k-doc-comment-descriptor/index.html">KDocCommentDescriptor</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#findkdoc"><span class="nf">findKDoc</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">)</span><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.kdoc.psi.api/-k-doc-comment-descriptor/index.html">KDocCommentDescriptor</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
