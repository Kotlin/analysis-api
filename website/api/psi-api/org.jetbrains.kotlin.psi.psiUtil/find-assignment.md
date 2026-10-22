---
tags:
 - jvm
title: "findAssignment"
---

# findAssignment

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">tailrec </span><span class="kd">fun </span><a href="find-assignment.html"><span class="nf">findAssignment</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-binary-expression/index.html">KtBinaryExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Walks up from [`element`](find-assignment.md) through qualified/simple-name expressions to find a plain `=` assignment whose LHS it is.


</div>

</div>
