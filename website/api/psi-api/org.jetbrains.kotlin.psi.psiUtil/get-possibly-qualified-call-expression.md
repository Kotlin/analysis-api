---
tags:
 - jvm
title: "getPossiblyQualifiedCallExpression"
---

# getPossiblyQualifiedCallExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="get-possibly-qualified-call-expression.html"><span class="nf">getPossiblyQualifiedCallExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-call-expression/index.html">KtCallExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the call expression this expression represents: the selector's call for a qualified expression, or this expression if it is itself a call. Returns `null` if there is no call.


</div>

</div>
