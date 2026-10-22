---
tags:
 - jvm
title: "isUsedAsExpression"
---

# isUsedAsExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="is-used-as-expression.html">isUsedAsExpression</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the value of the given [`KtExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md) is used. In other words, `true` if the value of the expression is not safe to discard.

[`isUsedAsExpression`](is-used-as-expression.md) performs a <strong>conservative check</strong> instead of exhaustive control-flow analysis. For example, `x` in the following example is possibly used, even though the value is never consumed at runtime: `x + try { throw Exception() } finally { return }`.

#### Example
In the following examples, `x` is used as a value (`x.isUsedAsExpression == true`):

 - `if (x) { ... } else { ... }`


 - `val a = x`


 - `x + 8`


 - `when (x) { 1 -> ...; else -> ... }`


In these expressions, `x` is not used as a value (`x.isUsedAsExpression == false`)

 - `run { x; println(50) }`


 - `when (x) { else -> ... }`



</div>

</div>
