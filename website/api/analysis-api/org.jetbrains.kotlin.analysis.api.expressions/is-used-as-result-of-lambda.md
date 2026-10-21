---
tags:
 - jvm
title: "isUsedAsResultOfLambda"
---

# isUsedAsResultOfLambda

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="is-used-as-result-of-lambda.html">isUsedAsResultOfLambda</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the value of the given [`KtExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md) is used as the resulting expression of some lambda block.

Note that [`isUsedAsResultOfLambda`](is-used-as-result-of-lambda.md) performs a <strong>conservative check</strong> instead of exhaustive control-flow analysis and `isUsedAsResultOfLambda` being `true` doesn't imply that the containing lambda itself is used.

It's also vital to not confuse lambda expressions with regular scope blocks (like `if` branches).

#### Example
In the following examples, `x` is used as a result of a lambda (`x.isUsedAsResultOfLambda == true`):

 - `{ x -> println(0); x }`


 - `{ { x }; 5 }`


In these expressions, `x` is not used as a result of a lambda (`x.isUsedAsResultOfLambda == false`)

 - `{ x -> println(0); x + 1 }`


 - `{ x; println(50) }`


 - `{ if (true) { x } else { x } }`


 - `fun(x: Int) = x`



</div>

</div>
