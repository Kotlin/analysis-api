---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.contracts.description"
---

# org.jetbrains.kotlin.analysis.api.contracts.description
## Types
### [`KaContractCallsInPlaceContractEffectDeclaration`](-ka-contract-calls-in-place-contract-effect-declaration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-contract-calls-in-place-contract-effect-declaration/index.html">KaContractCallsInPlaceContractEffectDeclaration</a> : <a href="-ka-contract-effect-declaration/index.html">KaContractEffectDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents [`kotlin.contracts.ContractBuilder.callsInPlace`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-contract-builder/calls-in-place.html).


</div>

</div>
### [`KaContractConditionalContractEffectDeclaration`](-ka-contract-conditional-contract-effect-declaration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-contract-conditional-contract-effect-declaration/index.html">KaContractConditionalContractEffectDeclaration</a> : <a href="-ka-contract-effect-declaration/index.html">KaContractEffectDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents [`kotlin.contracts.SimpleEffect.implies`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-simple-effect/implies.html).


</div>

</div>
### [`KaContractConstantValue`](-ka-contract-constant-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-contract-constant-value/index.html">KaContractConstantValue</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents constant reference that can be passed to `value` argument of [`kotlin.contracts.ContractBuilder.returns`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-contract-builder/returns.html).


</div>

</div>
### [`KaContractEffectDeclaration`](-ka-contract-effect-declaration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-contract-effect-declaration/index.html">KaContractEffectDeclaration</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents [`kotlin.contracts.Effect`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-effect/index.html).


</div>

</div>
### [`KaContractExplicitParameterValue`](-ka-contract-explicit-parameter-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-contract-explicit-parameter-value/index.html">KaContractExplicitParameterValue</a> : <a href="-ka-contract-parameter-value/index.html">KaContractParameterValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an explicit parameter which is declared on the corresponding contract owner. Examples: all [`KaParameterSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-parameter-symbol/index.md) hierarchy.


</div>

</div>
### [`KaContractHoldsInEffectDeclaration`](-ka-contract-holds-in-effect-declaration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-contract-holds-in-effect-declaration/index.html">KaContractHoldsInEffectDeclaration</a> : <a href="-ka-contract-effect-declaration/index.html">KaContractEffectDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents [`kotlin.contracts.ContractBuilder.holdsIn`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-contract-builder/holds-in.html).


</div>

</div>
### [`KaContractInvocationKind`](-ka-contract-invocation-kind/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-contract-invocation-kind/index.html">KaContractInvocationKind</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-contract-invocation-kind/index.html">KaContractInvocationKind</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Describes how many times a callable parameter is invoked by a function with a `callsInPlace` contract.


</div>

</div>
### [`KaContractOwnerParameterValue`](-ka-contract-owner-parameter-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-contract-owner-parameter-value/index.html">KaContractOwnerParameterValue</a> : <a href="-ka-contract-parameter-value/index.html">KaContractParameterValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an owner of the corresponding contract owner. Example:


</div>

</div>
### [`KaContractParameterValue`](-ka-contract-parameter-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-contract-parameter-value/index.html">KaContractParameterValue</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents parameter that can be passed to `value` argument of [`kotlin.contracts.ContractBuilder.callsInPlace`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-contract-builder/calls-in-place.html) or [`kotlin.contracts.ContractBuilder.holdsIn`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-contract-builder/holds-in.html).


</div>

</div>
### [`KaContractReturnsContractEffectDeclaration`](-ka-contract-returns-contract-effect-declaration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-contract-returns-contract-effect-declaration/index.html">KaContractReturnsContractEffectDeclaration</a> : <a href="-ka-contract-effect-declaration/index.html">KaContractEffectDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents [`kotlin.contracts.ContractBuilder.returnsNotNull`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-contract-builder/returns-not-null.html)&[`kotlin.contracts.ContractBuilder.returns`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-contract-builder/returns.html).


</div>

</div>
### [`KaContractReturnsParameterEffectDeclaration`](-ka-contract-returns-parameter-effect-declaration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-contract-returns-parameter-effect-declaration/index.html">KaContractReturnsParameterEffectDeclaration</a> : <a href="-ka-contract-effect-declaration/index.html">KaContractEffectDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents [`kotlin.contracts.ContractBuilder.returnsParameter`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-contract-builder/returns-parameter.html).


</div>

</div>
### [`KaContractReturnsResultOfEffectDeclaration`](-ka-contract-returns-result-of-effect-declaration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-contract-returns-result-of-effect-declaration/index.html">KaContractReturnsResultOfEffectDeclaration</a> : <a href="-ka-contract-effect-declaration/index.html">KaContractEffectDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents [`kotlin.contracts.ContractBuilder.returnsResultOf`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-contract-builder/returns-result-of.html).


</div>

</div>
