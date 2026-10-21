---
tags:
 - jvm
title: "findDocComment"
---

# findDocComment

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="find-doc-comment.html"><span class="nf">findDocComment</span></a><span class="p">(</span>declaration<span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.kdoc.psi.api/-k-doc/index.html">KDoc</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KDoc`](../org.jetbrains.kotlin.kdoc.psi.api/-k-doc/index.md) comment attached to the given [`declaration`](find-doc-comment.md), or `null` if it has none (or the declaration belongs to a compiled file, where doc comments are not available).


</div>

</div>
