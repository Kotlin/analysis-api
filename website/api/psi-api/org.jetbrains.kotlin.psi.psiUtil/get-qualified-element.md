---
tags:
 - jvm
title: "getQualifiedElement"
---

# getQualifiedElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="get-qualified-element.html"><span class="nf">getQualifiedElement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the enclosing qualified element for this name: a [`KtQualifiedExpression`](../org.jetbrains.kotlin.psi/-kt-qualified-expression/index.md), a [`KtUserType`](../org.jetbrains.kotlin.psi/-kt-user-type/index.md), or this expression itself if there is no such qualifier.


</div>

</div>
