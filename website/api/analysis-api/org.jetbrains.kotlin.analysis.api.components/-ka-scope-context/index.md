---
tags:
 - jvm
title: "KaScopeContext"
---

# KaScopeContext

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaScopeContext</a> : <a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>A scope context includes all scopes that are relevant for a given [`KtElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md) position in a [`KtFile`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md), together with all available implicit receivers.

#### See also


 - [`KaScopeProvider.scopeContext`](../-ka-scope-provider/index.md#scopecontext)



</div>

## Properties
### implicitReceivers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="index.html#implicitreceivers">implicitReceivers</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-implicit-receiver/index.html">KaImplicitReceiver</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The implicit receivers available at the context position.

The list is sorted according to the order of scopes in the scope tower (from innermost to outermost).

It is possible to use `this@` + [`KaImplicitReceiver.label`](../-ka-implicit-receiver/index.md#label) to refer to the corresponding implicit receiver.

`this` (without any explicit label) can be used to explicitly refer to the (currently) implicit receiver with the lowest index in the scope tower (= innermost scope).


</div>

</div>
### implicitValues

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#implicitvalues">implicitValues</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-scope-implicit-value/index.html">KaScopeImplicitValue</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The implicit values available at the context position.

The list is sorted according to the order of scopes in the scope tower (from innermost to outermost).

**See also**



 - [`KaScopeKind.indexInTower`](../-ka-scope-kind/-script-member-scope/index.md#indexintower)



</div>

</div>
### possibleSmartCasts

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#possiblesmartcasts">possibleSmartCasts</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-smart-cast-possibility/index.html">KaSmartCastPossibility</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The list of smart casts available at the context position.

Note that an actual smart cast will only appear if the original expression type does not match the expected type. For actual smart cast application, check [`KaDataFlowProvider.smartCastInfo`](../-ka-data-flow-provider/index.md#smartcastinfo).

The list has an arbitrary (but stable) order.


</div>

</div>
### scopes

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#scopes">scopes</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-scope-with-kind/index.html">KaScopeWithKind</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md)s available at the context position. [`KaScopeWithKind`](../-ka-scope-with-kind/index.md) additionally determines the kind of scope at the index in the scope tower.

The list is sorted according to the order of scopes in the scope tower (from innermost to outermost).


</div>

</div>
### [`token`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#token)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#token">token</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaLifetimeToken`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md) which determines the lifetime of the lifetime owner.


</div>

</div>
## Functions
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### compositeScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="index.html">KaScopeContext</a><span class="p">.</span><a href="index.html#compositescope"><span class="nf">compositeScope</span></a><span class="p">(</span>filter<span class="o">: </span><span class="p">(</span><a href="../-ka-scope-kind/index.html">KaScopeKind</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a single [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) that contains declarations from all scopes that satisfy [`filter`](index.md#compositescope).

The order of declarations corresponds to the order of their containing scopes, which are sorted according to their [`indices`](../-ka-scope-kind/-script-member-scope/index.md#indexintower) in the scope tower.


</div>

</div>
### [`isValid`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#isvalid)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#isvalid"><span class="nf">isValid</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the lifetime owner is still valid, i.e. we are still in the scope of the lifetime owner's regular lifetime.


</div>

</div>
### [`withValidityAssertion`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion"><span class="nf">withValidityAssertion</span></a><span class="p">(</span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a>
</span></code></pre></div>
</div>


<div markdown>

Executes [`action`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion) only if the [`KaLifetimeOwner`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.md) is still [`valid`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md#isvalid) and [`accessible`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md#isaccessible). Otherwise, throws a validity exception based on the concrete violation.


</div>

</div>
