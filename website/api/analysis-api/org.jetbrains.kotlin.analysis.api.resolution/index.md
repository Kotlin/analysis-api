---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.resolution"
---

# org.jetbrains.kotlin.analysis.api.resolution
## Types
### [`KaAnnotationCall`](-ka-annotation-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-annotation-call/index.html">KaAnnotationCall</a> : <a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A call to an [annotation constructor](https://kotlinlang.org/docs/annotations.html#constructors).


</div>

</div>
### [`KaApplicableCallCandidate`](-ka-applicable-call-candidate/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-applicable-call-candidate/index.html">KaApplicableCallCandidate</a> : <a href="-ka-call-candidate/index.html">KaCallCandidate</a>
</span></code></pre></div>
</div>


<div markdown>

A [`call candidate`](-ka-call-candidate/index.md) that is applicable for a call.


</div>

</div>
### [`KaApplicableCallCandidateInfo`](-ka-applicable-call-candidate-info/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-applicable-call-candidate-info/index.html">KaApplicableCallCandidateInfo</a> : <a href="-ka-call-candidate-info/index.html">KaCallCandidateInfo</a>
</span></code></pre></div>
</div>


<div markdown>

A [`call candidate`](-ka-call-candidate-info/index.md) that is applicable for a call.


</div>

</div>
### [`KaCall`](-ka-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-call/index.html">KaCall</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

A call to a function, a simple/compound access to a property, or a simple/compound access through `get` and `set` convention.


</div>

</div>
### [`KaCallableMemberCall`](-ka-callable-member-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-callable-member-call/index.html">KaCallableMemberCall</a><span class="o"><</span><a href="-ka-callable-member-call/index.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">, </span><a href="-ka-callable-member-call/index.html">C</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="-ka-callable-member-call/index.html">S</a><span class="o">></span><span class="o">></span> : <a href="-ka-call/index.html">KaCall</a>
</span></code></pre></div>
</div>


<div markdown>

A call to a function, or a simple/compound access to a property.


</div>

</div>
### [`KaCallableReferenceCall`](-ka-callable-reference-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-callable-reference-call/index.html">KaCallableReferenceCall</a><span class="o"><</span><a href="-ka-callable-reference-call/index.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">, </span><a href="-ka-callable-reference-call/index.html">C</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="-ka-callable-reference-call/index.html">S</a><span class="o">></span><span class="o">></span> : <a href="-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><a href="-ka-callable-reference-call/index.html">S</a><span class="p">, </span><a href="-ka-callable-reference-call/index.html">C</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A [callable reference](https://kotlinlang.org/docs/reflection.html#function-references) to a function, a property, or a constructor.


</div>

</div>
### [`KaCallCandidate`](-ka-call-candidate/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-call-candidate/index.html">KaCallCandidate</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaCallCandidate`](-ka-call-candidate/index.md) represents one of the candidates considered during [overload resolution](https://kotlinlang.org/spec/overload-resolution.html) of a call.


</div>

</div>
### [`KaCallCandidateInfo`](-ka-call-candidate-info/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-call-candidate-info/index.html">KaCallCandidateInfo</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaCallCandidateInfo`](-ka-call-candidate-info/index.md) represents one of the candidates considered during [overload resolution](https://kotlinlang.org/spec/overload-resolution.html) of a call.


</div>

</div>
### [`KaCallInfo`](-ka-call-info/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-call-info/index.html">KaCallInfo</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Information about a call at the call site retrieved from [`resolveToCall`](../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#resolvetocall). The call may either be resolved successfully ([`KaSuccessCallInfo`](-ka-success-call-info/index.md)), or with errors ([`KaErrorCallInfo`](-ka-error-call-info/index.md)), coming with a list of candidate calls and a diagnostic.


</div>

</div>
### [`KaCallResolutionAttempt`](-ka-call-resolution-attempt/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an attempt to resolve [`KtResolvableCall`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md).


</div>

</div>
### [`KaCompoundAccessCall`](-ka-compound-access-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compound-access-call/index.html">KaCompoundAccessCall</a>
</span></code></pre></div>
</div>


<div markdown>

A compound access of a [`variable`](-ka-compound-variable-access-call/index.md) or an [`array`](-ka-compound-array-access-call/index.md).


</div>

</div>
### [`KaCompoundArrayAccessCall`](-ka-compound-array-access-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compound-array-access-call/index.html">KaCompoundArrayAccessCall</a> : <a href="-ka-multi-call/index.html">KaMultiCall</a>, <a href="-ka-call/index.html">KaCall</a>, <a href="-ka-compound-access-call/index.html">KaCompoundAccessCall</a>
</span></code></pre></div>
</div>


<div markdown>

A compound access using the array access convention, involving calls to both the `get()` and `set()` functions. For example, `a[1] += "foo"` is such an array compound access.


</div>

</div>
### [`KaCompoundArrayAccessCallResolutionAttempt`](-ka-compound-array-access-call-resolution-attempt/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compound-array-access-call-resolution-attempt/index.html">KaCompoundArrayAccessCallResolutionAttempt</a> : <a href="-ka-multi-call-resolution-attempt/index.html">KaMultiCallResolutionAttempt</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an attempt to resolve a compound array access (e.g. `a[1] += "foo"` or `a[0]++`).


</div>

</div>
### [`KaCompoundAssignOperation`](-ka-compound-assign-operation/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compound-assign-operation/index.html">KaCompoundAssignOperation</a> : <a href="-ka-compound-operation/index.html">KaCompoundOperation</a>
</span></code></pre></div>
</div>


<div markdown>

A [compound assignment](https://kotlinlang.org/docs/operator-overloading.html#augmented-assignments) that reads, computes, and writes the computed value. Calls to `<op>Assign` are not represented by [`KaCompoundAssignOperation`](-ka-compound-assign-operation/index.md).


</div>

</div>
### [`KaCompoundOperation`](-ka-compound-operation/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-compound-operation/index.html">KaCompoundOperation</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

The type of compound operation applied to a variable or an array element using the array access convention.


</div>

</div>
### [`KaCompoundSymbolResolutionError`](-ka-compound-symbol-resolution-error/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compound-symbol-resolution-error/index.html">KaCompoundSymbolResolutionError</a> : <a href="-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a failed resolution of a compound (multi) call at the symbol level.


</div>

</div>
### [`KaCompoundUnaryOperation`](-ka-compound-unary-operation/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compound-unary-operation/index.html">KaCompoundUnaryOperation</a> : <a href="-ka-compound-operation/index.html">KaCompoundOperation</a>
</span></code></pre></div>
</div>


<div markdown>

A [compound unary access](https://kotlinlang.org/docs/operator-overloading.html#increments-and-decrements) that reads, increments or decrements, and writes the computed value.


</div>

</div>
### [`KaCompoundVariableAccessCall`](-ka-compound-variable-access-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compound-variable-access-call/index.html">KaCompoundVariableAccessCall</a> : <a href="-ka-multi-call/index.html">KaMultiCall</a>, <a href="-ka-call/index.html">KaCall</a>, <a href="-ka-compound-access-call/index.html">KaCompoundAccessCall</a>
</span></code></pre></div>
</div>


<div markdown>

A compound access of a mutable variable. Such accesses combine reading, modifying, and writing to the variable in a single expression, using operators like `+=`, `-=`, `++`, or `--`.


</div>

</div>
### [`KaCompoundVariableAccessCallResolutionAttempt`](-ka-compound-variable-access-call-resolution-attempt/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compound-variable-access-call-resolution-attempt/index.html">KaCompoundVariableAccessCallResolutionAttempt</a> : <a href="-ka-multi-call-resolution-attempt/index.html">KaMultiCallResolutionAttempt</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an attempt to resolve a compound variable access (e.g. `i += 1` or `i++`).


</div>

</div>
### [`KaContextSensitiveResolutionStatus`](-ka-context-sensitive-resolution-status/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-context-sensitive-resolution-status/index.html">KaContextSensitiveResolutionStatus</a>
</span></code></pre></div>
</div>


<div markdown>

Describes how [context-sensitive resolution](https://github.com/Kotlin/KEEP/issues/379) (CSR) relates to a [`org.jetbrains.kotlin.psi.KtSimpleNameExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.md).


</div>

</div>
### [`KaDelegatedConstructorCall`](-ka-delegated-constructor-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a> : <a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A call to another constructor within the same class, or to a superclass constructor. This corresponds to the use of `this(...)` or `super(...)` within a constructor's body to delegate initialization to another constructor.


</div>

</div>
### [`KaDelegatedPropertyCall`](-ka-delegated-property-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-delegated-property-call/index.html">KaDelegatedPropertyCall</a> : <a href="-ka-multi-call/index.html">KaMultiCall</a>, <a href="-ka-call/index.html">KaCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a resolved delegated property, which desugars into up to three operator calls: [`getValue()`](-ka-delegated-property-call/index.md#valuegettercall), [`setValue()`](-ka-delegated-property-call/index.md#valuesettercall), and [`provideDelegate()`](-ka-delegated-property-call/index.md#providedelegatecall).


</div>

</div>
### [`KaDelegatedPropertyCallResolutionAttempt`](-ka-delegated-property-call-resolution-attempt/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-delegated-property-call-resolution-attempt/index.html">KaDelegatedPropertyCallResolutionAttempt</a> : <a href="-ka-multi-call-resolution-attempt/index.html">KaMultiCallResolutionAttempt</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an attempt to resolve a delegated property, which desugars into up to three operator calls: [`getValue()`](-ka-delegated-property-call-resolution-attempt/index.md#valuegettercallattempt), [`setValue()`](-ka-delegated-property-call-resolution-attempt/index.md#valuesettercallattempt), and [`provideDelegate()`](-ka-delegated-property-call-resolution-attempt/index.md#providedelegatecallattempt).


</div>

</div>
### [`KaErrorCallInfo`](-ka-error-call-info/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-error-call-info/index.html">KaErrorCallInfo</a> : <a href="-ka-call-info/index.html">KaCallInfo</a>
</span></code></pre></div>
</div>


<div markdown>

An erroneous call. The [`candidateCalls`](-ka-error-call-info/index.md#candidatecalls) and [`diagnostic`](-ka-error-call-info/index.md#diagnostic) can be used to further analyze the error.


</div>

</div>
### [`KaExplicitReceiverValue`](-ka-explicit-receiver-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-explicit-receiver-value/index.html">KaExplicitReceiverValue</a> : <a href="-ka-receiver-value/index.html">KaReceiverValue</a>
</span></code></pre></div>
</div>


<div markdown>

An explicit receiver value.


</div>

</div>
### [`KaForLoopCall`](-ka-for-loop-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-for-loop-call/index.html">KaForLoopCall</a> : <a href="-ka-multi-call/index.html">KaMultiCall</a>, <a href="-ka-call/index.html">KaCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a resolved `for` loop, which desugars into three operator calls: [`iterator()`](-ka-for-loop-call/index.md#iteratorcall), [`hasNext()`](-ka-for-loop-call/index.md#hasnextcall), and [`next()`](-ka-for-loop-call/index.md#nextcall).


</div>

</div>
### [`KaForLoopCallResolutionAttempt`](-ka-for-loop-call-resolution-attempt/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-for-loop-call-resolution-attempt/index.html">KaForLoopCallResolutionAttempt</a> : <a href="-ka-multi-call-resolution-attempt/index.html">KaMultiCallResolutionAttempt</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an attempt to resolve a `for` loop, which desugars into three operator calls: [`iterator()`](-ka-for-loop-call-resolution-attempt/index.md#iteratorcallattempt), [`hasNext()`](-ka-for-loop-call-resolution-attempt/index.md#hasnextcallattempt), and [`next()`](-ka-for-loop-call-resolution-attempt/index.md#nextcallattempt).


</div>

</div>
### [`KaFunctionCall`](-ka-function-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="-ka-function-call/index.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">></span> : <a href="-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><a href="-ka-function-call/index.html">S</a><span class="p">, </span><a href="../org.jetbrains.kotlin.analysis.api.signatures/-ka-function-signature/index.html">KaFunctionSignature</a><span class="o"><</span><a href="-ka-function-call/index.html">S</a><span class="o">></span><span class="o">> </span>, <a href="-ka-callable-member-call/index.html">KaCallableMemberCall</a><span class="o"><</span><a href="-ka-function-call/index.html">S</a><span class="p">, </span><a href="../org.jetbrains.kotlin.analysis.api.signatures/-ka-function-signature/index.html">KaFunctionSignature</a><span class="o"><</span><a href="-ka-function-call/index.html">S</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A call to a function within Kotlin code. This includes calls to regular functions, constructors, constructors of superclasses, and annotations.


</div>

</div>
### [`KaImplicitInvokeCall`](-ka-implicit-invoke-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-implicit-invoke-call/index.html">KaImplicitInvokeCall</a> : <a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A call to an [implicit invoke call](https://kotlinlang.org/docs/operator-overloading.html#invoke-operator).


</div>

</div>
### [`KaImplicitReceiverValue`](-ka-implicit-receiver-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-implicit-receiver-value/index.html">KaImplicitReceiverValue</a> : <a href="-ka-receiver-value/index.html">KaReceiverValue</a>
</span></code></pre></div>
</div>


<div markdown>

An implicit receiver value.


</div>

</div>
### [`KaInapplicableCallCandidate`](-ka-inapplicable-call-candidate/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-inapplicable-call-candidate/index.html">KaInapplicableCallCandidate</a> : <a href="-ka-call-candidate/index.html">KaCallCandidate</a>
</span></code></pre></div>
</div>


<div markdown>

A [`call candidate`](-ka-call-candidate/index.md) that is not applicable for a call.


</div>

</div>
### [`KaInapplicableCallCandidateInfo`](-ka-inapplicable-call-candidate-info/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-inapplicable-call-candidate-info/index.html">KaInapplicableCallCandidateInfo</a> : <a href="-ka-call-candidate-info/index.html">KaCallCandidateInfo</a>
</span></code></pre></div>
</div>


<div markdown>

A [`call candidate`](-ka-call-candidate-info/index.md) that is not applicable for a call.


</div>

</div>
### [`KaMultiCall`](-ka-multi-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-multi-call/index.html">KaMultiCall</a> : <a href="-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a successful resolution resulting in multiple calls.


</div>

</div>
### [`KaMultiCallResolutionAttempt`](-ka-multi-call-resolution-attempt/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-multi-call-resolution-attempt/index.html">KaMultiCallResolutionAttempt</a> : <a href="-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an attempt to resolve a compound (multi) call, such as a for-loop, delegated property access, or compound assignment. The assembled [`call`](-ka-multi-call-resolution-attempt/index.md#call) is always a [`KaMultiCall`](-ka-multi-call/index.md).


</div>

</div>
### [`KaPartiallyAppliedFunctionSymbol`](-ka-partially-applied-function-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">typealias </span><a href="-ka-partially-applied-function-symbol/index.html">KaPartiallyAppliedFunctionSymbol</a><span class="o"><</span><a href="-ka-partially-applied-function-symbol/index.html">S</a><span class="o">></span><span class="o"> = </span><a href="-ka-partially-applied-symbol/index.html">KaPartiallyAppliedSymbol</a><span class="o"><</span><a href="-ka-partially-applied-function-symbol/index.html">S</a><span class="p">, </span><a href="../org.jetbrains.kotlin.analysis.api.signatures/-ka-function-signature/index.html">KaFunctionSignature</a><span class="o"><</span><a href="-ka-partially-applied-function-symbol/index.html">S</a><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`KaPartiallyAppliedSymbol`](-ka-partially-applied-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-partially-applied-symbol/index.html">KaPartiallyAppliedSymbol</a><span class="o"><</span><span class="kd">out </span><a href="-ka-partially-applied-symbol/index.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">, </span><span class="kd">out </span><a href="-ka-partially-applied-symbol/index.html">C</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="-ka-partially-applied-symbol/index.html">S</a><span class="o">></span><span class="o">></span> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

A callable symbol partially applied with receivers and type arguments. Essentially, this is a call that misses some information. For properties, the missing information is the type of access (read, write, or compound access) to this property. For functions, the missing information is the value arguments for the call.


</div>

</div>
### [`KaPartiallyAppliedVariableSymbol`](-ka-partially-applied-variable-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">typealias </span><a href="-ka-partially-applied-variable-symbol/index.html">KaPartiallyAppliedVariableSymbol</a><span class="o"><</span><a href="-ka-partially-applied-variable-symbol/index.html">S</a><span class="o">></span><span class="o"> = </span><a href="-ka-partially-applied-symbol/index.html">KaPartiallyAppliedSymbol</a><span class="o"><</span><a href="-ka-partially-applied-variable-symbol/index.html">S</a><span class="p">, </span><a href="../org.jetbrains.kotlin.analysis.api.signatures/-ka-variable-signature/index.html">KaVariableSignature</a><span class="o"><</span><a href="-ka-partially-applied-variable-symbol/index.html">S</a><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`KaReceiverValue`](-ka-receiver-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-receiver-value/index.html">KaReceiverValue</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

A [receiver](https://kotlin.github.io/analysis-api/receivers.html) value of a call, which represents either an [`explicit`](-ka-explicit-receiver-value/index.md), [`implicit`](-ka-implicit-receiver-value/index.md), or [`smart-casted`](-ka-smart-casted-receiver-value/index.md) receiver.


</div>

</div>
### [`KaSimpleCall`](-ka-simple-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><a href="-ka-simple-call/index.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">, </span><a href="-ka-simple-call/index.html">C</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="-ka-simple-call/index.html">S</a><span class="o">></span><span class="o">></span> : <a href="-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a successful resolution resulting in a simple call.


</div>

</div>
### [`KaSimpleCallResolutionAttempt`](-ka-simple-call-resolution-attempt/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-simple-call-resolution-attempt/index.html">KaSimpleCallResolutionAttempt</a> : <a href="-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an attempt to resolve a simple call (as opposed to a [`multi-call`](-ka-multi-call-resolution-attempt/index.md)), which is either a [`success`](-ka-simple-call-resolution-success/index.md) or an [`error`](-ka-simple-call-resolution-error/index.md).


</div>

</div>
### [`KaSimpleCallResolutionError`](-ka-simple-call-resolution-error/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-simple-call-resolution-error/index.html">KaSimpleCallResolutionError</a> : <a href="-ka-simple-call-resolution-attempt/index.html">KaSimpleCallResolutionAttempt</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an error that occurred during the resolution of a [`KtResolvableCall`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md)


</div>

</div>
### [`KaSimpleCallResolutionSuccess`](-ka-simple-call-resolution-success/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-simple-call-resolution-success/index.html">KaSimpleCallResolutionSuccess</a> : <a href="-ka-simple-call-resolution-attempt/index.html">KaSimpleCallResolutionAttempt</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a successful resolution of a simple [`KtResolvableCall`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md).


</div>

</div>
### [`KaSimpleOrMultiCall`](-ka-simple-or-multi-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a resolved call that can be either a simple call or a multi call.


</div>

</div>
### [`KaSimpleSymbolResolutionAttempt`](-ka-simple-symbol-resolution-attempt/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-simple-symbol-resolution-attempt/index.html">KaSimpleSymbolResolutionAttempt</a> : <a href="-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an attempt to resolve a simple (non-compound) [`KtResolvable`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md), which is either a [`success`](-ka-simple-symbol-resolution-success/index.md) or an [`error`](-ka-simple-symbol-resolution-error/index.md).


</div>

</div>
### [`KaSimpleSymbolResolutionError`](-ka-simple-symbol-resolution-error/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-simple-symbol-resolution-error/index.html">KaSimpleSymbolResolutionError</a> : <a href="-ka-simple-symbol-resolution-attempt/index.html">KaSimpleSymbolResolutionAttempt</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an error that occurred during the resolution of a [`KtResolvable`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md)


</div>

</div>
### [`KaSimpleSymbolResolutionSuccess`](-ka-simple-symbol-resolution-success/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-simple-symbol-resolution-success/index.html">KaSimpleSymbolResolutionSuccess</a> : <a href="-ka-simple-symbol-resolution-attempt/index.html">KaSimpleSymbolResolutionAttempt</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a successful resolution result.


</div>

</div>
### [`KaSmartCastedReceiverValue`](-ka-smart-casted-receiver-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-smart-casted-receiver-value/index.html">KaSmartCastedReceiverValue</a> : <a href="-ka-receiver-value/index.html">KaReceiverValue</a>
</span></code></pre></div>
</div>


<div markdown>

A smart-casted receiver value.


</div>

</div>
### [`KaSuccessCallInfo`](-ka-success-call-info/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-success-call-info/index.html">KaSuccessCallInfo</a> : <a href="-ka-call-info/index.html">KaCallInfo</a>
</span></code></pre></div>
</div>


<div markdown>

A successfully resolved call.


</div>

</div>
### [`KaSymbolResolutionAttempt`](-ka-symbol-resolution-attempt/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

This interface represents an attempt on resolving some [`KtResolvable`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md) through [`KaResolver.tryResolveSymbols`](../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#tryresolvesymbols) API.


</div>

</div>
### [`KaVariableAccessCall`](-ka-variable-access-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-variable-access-call/index.html">KaVariableAccessCall</a> : <a href="-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a><span class="p">, </span><a href="../org.jetbrains.kotlin.analysis.api.signatures/-ka-variable-signature/index.html">KaVariableSignature</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a><span class="o">></span><span class="o">> </span>, <a href="-ka-callable-member-call/index.html">KaCallableMemberCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a><span class="p">, </span><a href="../org.jetbrains.kotlin.analysis.api.signatures/-ka-variable-signature/index.html">KaVariableSignature</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Access to variables (including properties).


</div>

</div>
## Properties
## Functions
### [`collectCallCandidates`](collect-call-candidates.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">.</span><a href="collect-call-candidates.html"><span class="nf">collectCallCandidates</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-ka-call-candidate/index.html">KaCallCandidate</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all candidates considered during [overload resolution](https://kotlinlang.org/spec/overload-resolution.html) for the call corresponding to the given [`KtResolvableCall`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md).


</div>

</div>
### [`resolveSuccessfulCall`](resolve-successful-call.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-annotation-call/index.html">KaAnnotationCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtAnnotationEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.md) to an annotation constructor call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.html">KtArrayAccessExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtArrayAccessExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.md) to a simple function call representing `get`/`set` operator invocation.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.html">KtCallElement</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtCallElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.md) to a function call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.html">KtCallableReferenceExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-callable-reference-call/index.html">KaCallableReferenceCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtCallableReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.md) to a callable member call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.html">KtCollectionLiteralExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtCollectionLiteralExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.md) to a simple function call representing the corresponding array factory invocation.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.html">KtConstructorCalleeExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtConstructorCalleeExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.md) to a constructor call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtConstructorDelegationCall`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.md) to a delegated constructor call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.html">KtConstructorDelegationReferenceExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtConstructorDelegationReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.md) to a delegated constructor call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtDestructuringDeclarationEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.md) to a call representing the `componentN` invocation (for positional destructuring) or the property access (for name-based destructuring).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.html">KtEnumEntrySuperclassReferenceExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtEnumEntrySuperclassReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md) to a delegated constructor call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.html">KtForExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-for-loop-call/index.html">KaForLoopCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtForExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.md) to a [`KaForLoopCall`](-ka-for-loop-call/index.md) representing the desugared `for` loop.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.html">KtNameReferenceExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtNameReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md) to a call representing the referenced declaration.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.html">KtPropertyDelegate</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-delegated-property-call/index.html">KaDelegatedPropertyCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtPropertyDelegate`](../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.md) to a [`KaDelegatedPropertyCall`](-ka-delegated-property-call/index.md) representing the desugared delegated property.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtQualifiedExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.md) to a call representing the member or extension access.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.html">KtSuperTypeCallEntry</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtSuperTypeCallEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.md) to a constructor call of the referenced supertype.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.html">KtWhenConditionInRange</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtWhenConditionInRange`](../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.md) to a simple function call representing the corresponding `contains` operator invocation used by the `in`/`!in` branch condition.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the call for the given [`KtResolvableCall`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md).


</div>

</div>
### [`resolveSuccessfulSymbol`](resolve-successful-symbol.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol of the annotation referenced by the given [`KtAnnotationEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.html">KtArrayAccessExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the operator function symbol targeted by the given [`KtArrayAccessExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.html">KtCallElement</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the function symbol targeted by the given [`KtCallElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.html">KtCallableReferenceExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the callable symbol targeted by the given [`KtCallableReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-class-literal-expression/index.html">KtClassLiteralExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtClassLiteralExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-class-literal-expression/index.md) (`Foo::class`).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.html">KtCollectionLiteralExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the function symbol targeted by the given [`KtCollectionLiteralExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.html">KtConstructorCalleeExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol referenced by the given [`KtConstructorCalleeExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol referenced by the given [`KtConstructorDelegationCall`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.html">KtConstructorDelegationReferenceExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol referenced by the given [`KtConstructorDelegationReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-delegated-super-type-entry/index.html">KtDelegatedSuperTypeEntry</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtDelegatedSuperTypeEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-delegated-super-type-entry/index.md) (`class Foo : Bar by baz`).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the callable symbol targeted by the given [`KtDestructuringDeclarationEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.html">KtEnumEntrySuperclassReferenceExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the enum class symbol referenced by the given [`KtEnumEntrySuperclassReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-function-type/index.html">KtFunctionType</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the synthetic function class symbol referenced by the given [`KtFunctionType`](../../psi-api/org.jetbrains.kotlin.psi/-kt-function-type/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-instance-expression-with-label/index.html">KtInstanceExpressionWithLabel</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the declaration symbol referenced by the given [`KtInstanceExpressionWithLabel`](../../psi-api/org.jetbrains.kotlin.psi/-kt-instance-expression-with-label/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-label-reference-expression/index.html">KtLabelReferenceExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the declaration symbol targeted by the given [`KtLabelReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-label-reference-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-nullable-type/index.html">KtNullableType</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtNullableType`](../../psi-api/org.jetbrains.kotlin.psi/-kt-nullable-type/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the callable symbol targeted by the given [`KtQualifiedExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-return-expression/index.html">KtReturnExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the function symbol targeted by the given [`KtReturnExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-return-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.html">KtSuperTypeCallEntry</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol by the given [`KtSuperTypeCallEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-entry/index.html">KtSuperTypeEntry</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtSuperTypeEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-entry/index.md) (the no-parens form `class Foo : Bar`).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.html">KtTypeReference</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtTypeReference`](../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.html">KtWhenConditionInRange</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the operator function symbol targeted by the given [`KtWhenConditionInRange`](../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves a single symbol for the given [`KtResolvable`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md).


</div>

</div>
### [`resolveSuccessfulSymbols`](resolve-successful-symbols.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">.</span><a href="resolve-successful-symbols.html"><span class="nf">resolveSuccessfulSymbols</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Resolves symbols for the given [`KtResolvable`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md).


</div>

</div>
### [`tryResolveCall`](try-resolve-call.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.html">KtForExpression</a><span class="p">.</span><a href="try-resolve-call.html"><span class="nf">tryResolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-for-loop-call-resolution-attempt/index.html">KaForLoopCallResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve the given [`KtForExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.md) to a [`KaForLoopCallResolutionAttempt`](-ka-for-loop-call-resolution-attempt/index.md) containing the individual resolution results for each desugared operator call (`iterator`, `hasNext`, `next`).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.html">KtPropertyDelegate</a><span class="p">.</span><a href="try-resolve-call.html"><span class="nf">tryResolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-delegated-property-call-resolution-attempt/index.html">KaDelegatedPropertyCallResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve the given [`KtPropertyDelegate`](../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.md) to a [`KaDelegatedPropertyCallResolutionAttempt`](-ka-delegated-property-call-resolution-attempt/index.md) containing the individual resolution results for each desugared operator call (`getValue`, `setValue`, `provideDelegate`).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">.</span><a href="try-resolve-call.html"><span class="nf">tryResolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve the call for the given [`KtResolvableCall`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md).


</div>

</div>
### [`tryResolveSymbols`](try-resolve-symbols.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">.</span><a href="try-resolve-symbols.html"><span class="nf">tryResolveSymbols</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve a symbol for the given [`KtResolvable`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md).


</div>

</div>
