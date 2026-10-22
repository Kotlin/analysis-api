---
tags:
 - jvm
title: "KaSuccessCallInfo"
---

# KaSuccessCallInfo

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaSuccessCallInfo</a> : <a href="../-ka-call-info/index.html">KaCallInfo</a>
</span></code></pre></div>A successfully resolved call.


</div>

## Properties
### call

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#call">call</a><span class="o">: </span><a href="../-ka-call/index.html">KaCall</a>
</span></code></pre></div>
</div>


<div markdown>

The successfully resolved [`KaCall`](../-ka-call/index.md).


</div>

</div>
### calls

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-call-info/index.html">KaCallInfo</a><span class="p">.</span><a href="../-ka-for-loop-call/index.html#calls">calls</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-call/index.html">KaCall</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The list of [`KaCall`](../-ka-call/index.md)s associated with the [`KaCallInfo`](../-ka-call-info/index.md). The list contains a single [`KaCall`](../-ka-call/index.md) in case of a [`successful call`](index.md), but may contain multiple candidates in case of an [`error call`](../-ka-error-call-info/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-array-access-call-resolution-attempt/index.html#calls">calls</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The flattened list of resolved calls.

 - [`KaSimpleCallResolutionSuccess`](../-ka-simple-call-resolution-success/index.md): the resolved [`call`](../-ka-simple-call-resolution-success/index.md#call) as a single-element list.


 - [`KaSimpleCallResolutionError`](../-ka-simple-call-resolution-error/index.md): the [`candidate calls`](../-ka-simple-call-resolution-error/index.md#candidatecalls).


 - [`KaMultiCallResolutionAttempt`](../-ka-multi-call-resolution-attempt/index.md): the assembled [`call`](../-ka-multi-call-resolution-attempt/index.md#call) if all sub-calls succeeded, or the combined calls from individual [`simpleAttempts`](../-ka-compound-array-access-call-resolution-attempt/index.md#simpleattempts) otherwise.



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="p">.</span><a href="../-ka-for-loop-call/index.html#calls">calls</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The flattened list of [`KaSimpleCall`](../-ka-simple-call/index.md)s.

 - If [`this`](../-ka-simple-or-multi-call/index.md) is an instance of [`KaSimpleCall`](../-ka-simple-call/index.md), the list will contain only [`this`](../-ka-simple-or-multi-call/index.md) call


 - If [`this`](../-ka-simple-or-multi-call/index.md) is an instance of [`KaMultiCall`](../-ka-multi-call/index.md), the list will contain [`KaMultiCall.calls`](../-ka-for-loop-call/index.md#calls)



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
### singleCallOrNull

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../-ka-error-call-info/index.html#singlecallornull">T</a><span class="o"> : </span><a href="../-ka-call/index.html">KaCall</a><span class="o">> </span><a href="../-ka-call-info/index.html">KaCallInfo</a><span class="p">.</span><a href="../-ka-error-call-info/index.html#singlecallornull"><span class="nf">singleCallOrNull</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-error-call-info/index.html#singlecallornull">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the single [`KaCall`](../-ka-call/index.md) of type [`T`](../-ka-error-call-info/index.md#singlecallornull) associated with the [`KaCallInfo`](../-ka-call-info/index.md), or `null` if there is no such exact single call.

In the case of an [`error call`](../-ka-error-call-info/index.md), returns a single [`candidate call`](../-ka-error-call-info/index.md#candidatecalls) of type [`T`](../-ka-error-call-info/index.md#singlecallornull).


</div>

</div>
### singleConstructorCallOrNull

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-ka-call-info/index.html">KaCallInfo</a><span class="p">.</span><a href="../-ka-error-call-info/index.html#singleconstructorcallornull"><span class="nf">singleConstructorCallOrNull</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the single [`KaFunctionCall`](../-ka-function-call/index.md) with a [`KaConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) associated with the [`KaCallInfo`](../-ka-call-info/index.md), or `null` if there is no such exact single call.

**See also**



 - [`singleCallOrNull`](../-ka-error-call-info/index.md#singlecallornull)



</div>

</div>
### singleFunctionCallOrNull

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-ka-call-info/index.html">KaCallInfo</a><span class="p">.</span><a href="../-ka-error-call-info/index.html#singlefunctioncallornull"><span class="nf">singleFunctionCallOrNull</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the single [`KaFunctionCall`](../-ka-function-call/index.md) associated with the [`KaCallInfo`](../-ka-call-info/index.md), or `null` if there is no such exact single call.

**See also**



 - [`singleCallOrNull`](../-ka-error-call-info/index.md#singlecallornull)



</div>

</div>
### singleVariableAccessCall

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-ka-call-info/index.html">KaCallInfo</a><span class="p">.</span><a href="../-ka-error-call-info/index.html#singlevariableaccesscall"><span class="nf">singleVariableAccessCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-variable-access-call/index.html">KaVariableAccessCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the single [`KaVariableAccessCall`](../-ka-variable-access-call/index.md) associated with the [`KaCallInfo`](../-ka-call-info/index.md), or `null` if there is no such exact single call.

**See also**



 - [`singleCallOrNull`](../-ka-error-call-info/index.md#singlecallornull)



</div>

</div>
### successfulCallOrNull

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../-ka-error-call-info/index.html#successfulcallornull">T</a><span class="o"> : </span><a href="../-ka-call/index.html">KaCall</a><span class="o">> </span><a href="../-ka-call-info/index.html">KaCallInfo</a><span class="p">.</span><a href="../-ka-error-call-info/index.html#successfulcallornull"><span class="nf">successfulCallOrNull</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-error-call-info/index.html#successfulcallornull">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the successful [`KaCall`](../-ka-call/index.md) of type [`T`](../-ka-error-call-info/index.md#successfulcallornull) associated with the [`KaCallInfo`](../-ka-call-info/index.md), or `null` if there is no such exact call (either the call is not successful, or the successful call is of another type).


</div>

</div>
### successfulConstructorCallOrNull

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-ka-call-info/index.html">KaCallInfo</a><span class="p">.</span><a href="../-ka-error-call-info/index.html#successfulconstructorcallornull"><span class="nf">successfulConstructorCallOrNull</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the successful [`KaFunctionCall`](../-ka-function-call/index.md) with a [`KaConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) associated with the [`KaCallInfo`](../-ka-call-info/index.md), or `null` if there is no such exact call.

**See also**



 - [`successfulCallOrNull`](../-ka-error-call-info/index.md#successfulcallornull)



</div>

</div>
### successfulFunctionCallOrNull

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-ka-call-info/index.html">KaCallInfo</a><span class="p">.</span><a href="../-ka-error-call-info/index.html#successfulfunctioncallornull"><span class="nf">successfulFunctionCallOrNull</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the successful [`KaFunctionCall`](../-ka-function-call/index.md) associated with the [`KaCallInfo`](../-ka-call-info/index.md), or `null` if there is no such exact call.

**See also**



 - [`successfulCallOrNull`](../-ka-error-call-info/index.md#successfulcallornull)



</div>

</div>
### successfulVariableAccessCall

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-ka-call-info/index.html">KaCallInfo</a><span class="p">.</span><a href="../-ka-error-call-info/index.html#successfulvariableaccesscall"><span class="nf">successfulVariableAccessCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-variable-access-call/index.html">KaVariableAccessCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the successful [`KaVariableAccessCall`](../-ka-variable-access-call/index.md) associated with the [`KaCallInfo`](../-ka-call-info/index.md), or `null` if there is no such exact call.

**See also**



 - [`successfulCallOrNull`](../-ka-error-call-info/index.md#successfulcallornull)



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
