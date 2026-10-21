---
tags:
 - jvm
title: "getQualifiedElementOrCallableRef"
---

# getQualifiedElementOrCallableRef

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="get-qualified-element-or-callable-ref.html"><span class="nf">getQualifiedElementOrCallableRef</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Like [`getQualifiedElement`](get-qualified-element.md), but also returns the enclosing [`KtCallableReferenceExpression`](../org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.md) when this name is its callable reference.


</div>

</div>
