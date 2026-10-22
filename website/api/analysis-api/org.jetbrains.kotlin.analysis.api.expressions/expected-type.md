---
tags:
 - jvm
title: "expectedType"
---

# expectedType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span>PsiElement<span class="p">.</span><a href="expected-type.html">expectedType</a><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The expected [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) for the given PsiElement if it is an expression, or `null` if the element does not have an expected type. The expected type represents the type that is expected for an expression at a specific location in the code.

See [`expressionType`](expression-type.md) for a discussion about the expression type vs. the expected type.


</div>

</div>
