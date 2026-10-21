---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.contracts.description.booleans"
---

# org.jetbrains.kotlin.analysis.api.contracts.description.booleans
## Types
### [`KaContractBinaryLogicExpression`](-ka-contract-binary-logic-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-contract-binary-logic-expression/index.html">KaContractBinaryLogicExpression</a> : <a href="-ka-contract-boolean-expression/index.html">KaContractBooleanExpression</a>
</span></code></pre></div>
</div>


<div markdown>

See: [`KaContractBooleanExpression`](-ka-contract-boolean-expression/index.md).


</div>

</div>
### [`KaContractBooleanConstantExpression`](-ka-contract-boolean-constant-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-contract-boolean-constant-expression/index.html">KaContractBooleanConstantExpression</a> : <a href="-ka-contract-boolean-expression/index.html">KaContractBooleanExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents boolean constant reference. The boolean constant can be passed to `booleanExpression` argument of [`kotlin.contracts.SimpleEffect.implies`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-simple-effect/implies.html).


</div>

</div>
### [`KaContractBooleanExpression`](-ka-contract-boolean-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-contract-boolean-expression/index.html">KaContractBooleanExpression</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents `booleanExpression` argument of [`kotlin.contracts.SimpleEffect.implies`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-simple-effect/implies.html).


</div>

</div>
### [`KaContractBooleanValueParameterExpression`](-ka-contract-boolean-value-parameter-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-contract-boolean-value-parameter-expression/index.html">KaContractBooleanValueParameterExpression</a> : <a href="-ka-contract-boolean-expression/index.html">KaContractBooleanExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents boolean parameter reference passed to `booleanExpression` argument of [`kotlin.contracts.SimpleEffect.implies`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-simple-effect/implies.html).


</div>

</div>
### [`KaContractIsInstancePredicateExpression`](-ka-contract-is-instance-predicate-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-contract-is-instance-predicate-expression/index.html">KaContractIsInstancePredicateExpression</a> : <a href="-ka-contract-boolean-expression/index.html">KaContractBooleanExpression</a>
</span></code></pre></div>
</div>


<div markdown>

See: [`KaContractBooleanExpression`](-ka-contract-boolean-expression/index.md).


</div>

</div>
### [`KaContractIsNullPredicateExpression`](-ka-contract-is-null-predicate-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-contract-is-null-predicate-expression/index.html">KaContractIsNullPredicateExpression</a> : <a href="-ka-contract-boolean-expression/index.html">KaContractBooleanExpression</a>
</span></code></pre></div>
</div>


<div markdown>

See: [`KaContractBooleanExpression`](-ka-contract-boolean-expression/index.md).


</div>

</div>
### [`KaContractLogicalNotExpression`](-ka-contract-logical-not-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-contract-logical-not-expression/index.html">KaContractLogicalNotExpression</a> : <a href="-ka-contract-boolean-expression/index.html">KaContractBooleanExpression</a>
</span></code></pre></div>
</div>


<div markdown>

See: [`KaContractBooleanExpression`](-ka-contract-boolean-expression/index.md).


</div>

</div>
