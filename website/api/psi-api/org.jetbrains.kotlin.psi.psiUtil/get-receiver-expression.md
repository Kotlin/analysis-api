---
tags:
 - jvm
title: "getReceiverExpression"
---

# getReceiverExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="get-receiver-expression.html"><span class="nf">getReceiverExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the receiver this name is applied to, considering qualified expressions, binary/unary operators, and qualified user types, or `null` if this name has no receiver.

For example, the receiver of `b` in `a.b` is `a`, the receiver of the `+` operator in `a + b` is `a`, the receiver of the `++` operator in `a++` is `a`, and the receiver of `B` in the user type `A.B` is `A`. A bare, unqualified name has no receiver, so the result is `null`.


</div>

</div>
