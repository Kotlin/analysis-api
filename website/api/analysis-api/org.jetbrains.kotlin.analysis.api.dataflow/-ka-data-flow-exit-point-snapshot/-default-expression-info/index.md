---
tags:
 - jvm
title: "DefaultExpressionInfo"
---

# DefaultExpressionInfo

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">DefaultExpressionInfo</a><span class="p">(</span><span class="kd">val </span>expression<span class="o">: </span><a href="../../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">, </span><span class="kd">val </span>type<span class="o">: </span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span>
</span></code></pre></div>Represents a default expression (generally, a last given statement if it has a meaningful result type). Expressions that always return [`Nothing`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-nothing/index.html), such as `return`, `break`, `continue` or `throw`, cannot be default expressions.


</div>

## Constructors
### DefaultExpressionInfo

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>expression<span class="o">: </span><a href="../../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">, </span>type<span class="o">: </span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### expression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#expression">expression</a><span class="o">: </span><a href="../../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

The default expression.


</div>

</div>
### type

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#type">type</a><span class="o">: </span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The default expression type.


</div>

</div>
