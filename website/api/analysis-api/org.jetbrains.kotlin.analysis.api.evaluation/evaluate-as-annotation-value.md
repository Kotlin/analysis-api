---
tags:
 - jvm
title: "evaluateAsAnnotationValue"
---

# evaluateAsAnnotationValue

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="evaluate-as-annotation-value.html"><span class="nf">evaluateAsAnnotationValue</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-value/index.html">KaAnnotationValue</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to evaluate the given [`KtExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md) to an [`annotation value`](../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-value/index.md) (a constant value which can be used as an annotation argument), or returns `null` if this is not possible.


</div>

</div>
