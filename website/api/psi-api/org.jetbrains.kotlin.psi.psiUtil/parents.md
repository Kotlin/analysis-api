---
tags:
 - jvm
title: "parents"
---

# parents

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>ASTNode<span class="p">.</span><a href="parents.html"><span class="nf">parents</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>ASTNode<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The ancestor nodes of this AST node, from its parent upward, as a lazy sequence.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="parents.html">parents</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The ancestors of this element, from its immediate parent up to and including the containing file.


</div>

</div>
