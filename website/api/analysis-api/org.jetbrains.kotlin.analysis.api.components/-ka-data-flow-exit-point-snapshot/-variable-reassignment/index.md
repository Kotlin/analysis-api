---
tags:
 - jvm
title: "VariableReassignment"
---

# VariableReassignment

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">VariableReassignment</a><span class="p">(</span>
    <span class="kd">val </span>expression<span class="o">: </span><a href="../../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">, </span>
    <span class="kd">val </span>variable<span class="o">: </span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a><span class="p">, </span>
    <span class="kd">val </span>isAugmented<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
<span class="p">)</span>
</span></code></pre></div>Represents a local variable reassignment.


</div>

## Constructors
### VariableReassignment

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>
    expression<span class="o">: </span><a href="../../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">, </span>
    variable<span class="o">: </span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a><span class="p">, </span>
    isAugmented<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
<span class="p">)</span>
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

The reassignment expression.


</div>

</div>
### isAugmented

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#isaugmented">isAugmented</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

`true` if the variable is both read and set (as in `x += y` or `x++`).


</div>

</div>
### variable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#variable">variable</a><span class="o">: </span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

Reassigned variable symbol.


</div>

</div>
