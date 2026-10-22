---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.dataflow"
---

# org.jetbrains.kotlin.analysis.api.dataflow
## Types
### [`KaDataFlowExitPointSnapshot`](-ka-data-flow-exit-point-snapshot/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-data-flow-exit-point-snapshot/index.html">KaDataFlowExitPointSnapshot</a><span class="p">(</span>
    <span class="kd">val </span>defaultExpressionInfo<span class="o">: </span><a href="-ka-data-flow-exit-point-snapshot/-default-expression-info/index.html">KaDataFlowExitPointSnapshot.DefaultExpressionInfo</a><span class="o">?</span><span class="p">, </span>
    <span class="kd">val </span>valuedReturnExpressions<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">></span><span class="p">, </span>
    <span class="kd">val </span>returnValueType<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span><span class="p">, </span>
    <span class="kd">val </span>jumpExpressions<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">></span><span class="p">, </span>
    <span class="kd">val </span>hasJumps<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">val </span>hasEscapingJumps<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">val </span>hasMultipleJumpKinds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">val </span>hasMultipleJumpTargets<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">val </span>variableReassignments<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-ka-data-flow-exit-point-snapshot/-variable-reassignment/index.html">KaDataFlowExitPointSnapshot.VariableReassignment</a><span class="o">></span>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`KaImplicitReceiverSmartCast`](-ka-implicit-receiver-smart-cast/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-implicit-receiver-smart-cast/index.html">KaImplicitReceiverSmartCast</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents type information about an implicit receiver which has been smart-cast to a more specific type. An implicit smart cast is applied to an implicit receiver, such as `substring()` called on an implicit `this` given an earlier smart cast `this is String`.


</div>

</div>
### [`KaImplicitReceiverSmartCastKind`](-ka-implicit-receiver-smart-cast-kind/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-implicit-receiver-smart-cast-kind/index.html">KaImplicitReceiverSmartCastKind</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-implicit-receiver-smart-cast-kind/index.html">KaImplicitReceiverSmartCastKind</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents the kind of implicit receiver affected by the smart cast.


</div>

</div>
### [`KaSmartCastInfo`](-ka-smart-cast-info/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-smart-cast-info/index.html">KaSmartCastInfo</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents smart cast information for an expression.


</div>

</div>
## Properties
### [`implicitReceiverSmartCasts`](implicit-receiver-smart-casts.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="implicit-receiver-smart-casts.html">implicitReceiverSmartCasts</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="-ka-implicit-receiver-smart-cast/index.html">KaImplicitReceiverSmartCast</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The list of [`implicit receiver smart casts`](-ka-implicit-receiver-smart-cast/index.md) which have refined the expression's implicit receivers to a more specific type. These smart casts are required for the expression to be evaluated. The list does not include smart casts for explicit receivers.


</div>

</div>
### [`smartCastInfo`](smart-cast-info.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="smart-cast-info.html">smartCastInfo</a><span class="o">: </span><a href="-ka-smart-cast-info/index.html">KaSmartCastInfo</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

[`Smart cast information`](-ka-smart-cast-info/index.md) for the given [`KtExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md), or `null` if smart casts are not applied to it.


</div>

</div>
## Functions
### [`computeExitPointSnapshot`](compute-exit-point-snapshot.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="compute-exit-point-snapshot.html"><span class="nf">computeExitPointSnapshot</span></a><span class="p">(</span>statements<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="-ka-data-flow-exit-point-snapshot/index.html">KaDataFlowExitPointSnapshot</a>
</span></code></pre></div>
</div>

</div>
