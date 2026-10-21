---
tags:
 - jvm
title: "expressionType"
---

# expressionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="expression-type.html">expressionType</a><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The type of the given [`KtExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md), or `null` if it does not have a type.

In particular:

 - A not-null type for valued expressions (e.g., a variable, a function call, a lambda expression).


 - [`Unit`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html) for statements (e.g., assignments, loops).


 - `null` for [`KtExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md)s that are not a part of the expression tree (e.g., expressions in import or package statements).


### Expression vs. expected type
The Analysis API distinguishes between an expression's type and its expected type, which represent different aspects of the Kotlin type system.

The expression type represents the actual type of an expression after it has been resolved. It reflects the result of type inference, smart casts, and implicit conversions.

The expected type represents the type that is expected for an expression at a specific location in the code. This is determined by the context in which the expression appears, such as a variable type for its initializer, or a parameter type for a function call.


</div>

</div>
