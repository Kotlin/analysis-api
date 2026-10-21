---
tags:
 - jvm
title: "KaCompoundVariableAccessCallResolutionAttempt"
---

# KaCompoundVariableAccessCallResolutionAttempt

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaCompoundVariableAccessCallResolutionAttempt</a> : <a href="../-ka-multi-call-resolution-attempt/index.html">KaMultiCallResolutionAttempt</a>
</span></code></pre></div>Represents an attempt to resolve a compound variable access (e.g. `i += 1` or `i++`).

When all sub-calls succeed, [`call`](index.md#call) contains the assembled [`KaCompoundVariableAccessCall`](../-ka-compound-variable-access-call/index.md). When any sub-call fails, [`call`](index.md#call) is `null` but individual attempts still contain their resolution results.

#### See also


 - [`KaCompoundVariableAccessCall`](../-ka-compound-variable-access-call/index.md)



</div>

## Properties
### call

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#call">call</a><span class="o">: </span><a href="../-ka-compound-variable-access-call/index.html">KaCompoundVariableAccessCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The assembled [`KaCompoundVariableAccessCall`](../-ka-compound-variable-access-call/index.md), or `null` if any sub-call failed.

**See also**



 - [`KaCompoundAccessCall.operationCall`](../-ka-compound-array-access-call/index.md#operationcall)



</div>

</div>
### calls

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-call-info/index.html">KaCallInfo</a><span class="p">.</span><a href="../-ka-for-loop-call/index.html#calls">calls</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-call/index.html">KaCall</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The list of [`KaCall`](../-ka-call/index.md)s associated with the [`KaCallInfo`](../-ka-call-info/index.md). The list contains a single [`KaCall`](../-ka-call/index.md) in case of a [`successful call`](../-ka-success-call-info/index.md), but may contain multiple candidates in case of an [`error call`](../-ka-error-call-info/index.md).


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
### errors

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#errors">errors</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-simple-call-resolution-error/index.html">KaSimpleCallResolutionError</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The list of errors that occurred during the resolution.

 - [`KaSimpleCallResolutionSuccess`](../-ka-simple-call-resolution-success/index.md): an empty list.


 - [`KaSimpleCallResolutionError`](../-ka-simple-call-resolution-error/index.md): [`this`](../-ka-call-resolution-attempt/index.md) error as a single-element list.


 - [`KaMultiCallResolutionAttempt`](../-ka-multi-call-resolution-attempt/index.md): the errors among the individual [`sub-attempts`](../-ka-compound-array-access-call-resolution-attempt/index.md#simpleattempts). A multi-call attempt fails as soon as any of its sub-calls fails, so the list is empty if and only if the assembled [`call`](../-ka-multi-call-resolution-attempt/index.md#call) is not `null`.


The list is empty if and only if the resolution succeeded. So, unlike a `this is KaSimpleCallResolutionError` check, which only covers simple attempts, this property detects failures of every attempt kind.

**See also**



 - [`simpleAttempts`](../-ka-compound-symbol-resolution-error/index.md#simpleattempts)
 - [`successful`](../-ka-compound-array-access-call-resolution-attempt/index.md#successful)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#errors">errors</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-simple-symbol-resolution-error/index.html">KaSimpleSymbolResolutionError</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The list of errors that occurred during the resolution.

 - [`KaSimpleSymbolResolutionSuccess`](../-ka-simple-symbol-resolution-success/index.md): an empty list.


 - [`KaSimpleSymbolResolutionError`](../-ka-simple-symbol-resolution-error/index.md): [`this`](../-ka-symbol-resolution-attempt/index.md) error as a single-element list.


 - [`KaCompoundSymbolResolutionError`](../-ka-compound-symbol-resolution-error/index.md): the errors among the individual [`sub-attempts`](../-ka-compound-symbol-resolution-error/index.md#simpleattempts), which always contain at least one.


The list is empty if and only if the resolution succeeded. So, unlike a `this is KaSimpleSymbolResolutionError` check, which only covers simple attempts, this property detects failures of every attempt kind.

**See also**



 - [`isSuccessful`](../-ka-compound-symbol-resolution-error/index.md#issuccessful)



</div>

</div>
### isSuccessful

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#issuccessful">isSuccessful</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the resolution succeeded.

`true` if and only if [`successful`](../-ka-compound-array-access-call-resolution-attempt/index.md#successful) is not `null`, and equivalently if and only if [`errors`](../-ka-compound-symbol-resolution-error/index.md#errors) is empty.

Unlike a `this is KaSimpleCallResolutionSuccess` check, which only covers simple attempts, this property also accounts for [`KaMultiCallResolutionAttempt`](../-ka-multi-call-resolution-attempt/index.md), which fails as soon as any of its sub-calls fails.

**See also**



 - [`successful`](../-ka-compound-array-access-call-resolution-attempt/index.md#successful)
 - [`errors`](../-ka-compound-symbol-resolution-error/index.md#errors)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#issuccessful">isSuccessful</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the resolution succeeded.

`true` if and only if [`errors`](../-ka-compound-symbol-resolution-error/index.md#errors) is empty. A [`KaCompoundSymbolResolutionError`](../-ka-compound-symbol-resolution-error/index.md) is always a failure, even when some of its [`sub-attempts`](../-ka-compound-symbol-resolution-error/index.md#simpleattempts) succeeded.

**See also**



 - [`errors`](../-ka-compound-symbol-resolution-error/index.md#errors)
 - [`successfulSymbols`](../-ka-compound-symbol-resolution-error/index.md#successfulsymbols)



</div>

</div>
### operationCallAttempt

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#operationcallattempt">operationCallAttempt</a><span class="o">: </span><a href="../-ka-simple-call-resolution-attempt/index.html">KaSimpleCallResolutionAttempt</a>
</span></code></pre></div>
</div>


<div markdown>

The resolution attempt for the operation call (e.g. `plus`, `inc`).

**See also**



 - [`KaCompoundAccessCall.operationCall`](../-ka-compound-array-access-call/index.md#operationcall)



</div>

</div>
### simpleAttempts

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-compound-array-access-call-resolution-attempt/index.html#simpleattempts">simpleAttempts</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-simple-call-resolution-attempt/index.html">KaSimpleCallResolutionAttempt</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The list of individual resolution attempts for each sub-call.


</div>

</div>
### simpleAttempts

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#simpleattempts">simpleAttempts</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-simple-call-resolution-attempt/index.html">KaSimpleCallResolutionAttempt</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The flattened list of simple resolution attempts.

 - [`KaSimpleCallResolutionAttempt`](../-ka-simple-call-resolution-attempt/index.md): [`this`](../-ka-call-resolution-attempt/index.md) attempt as a single-element list.


 - [`KaMultiCallResolutionAttempt`](../-ka-multi-call-resolution-attempt/index.md): the individual [`sub-attempts`](../-ka-compound-array-access-call-resolution-attempt/index.md#simpleattempts).


The list is never empty.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#simpleattempts">simpleAttempts</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-simple-symbol-resolution-attempt/index.html">KaSimpleSymbolResolutionAttempt</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The flattened list of simple resolution attempts.

 - [`KaSimpleSymbolResolutionAttempt`](../-ka-simple-symbol-resolution-attempt/index.md): [`this`](../-ka-symbol-resolution-attempt/index.md) attempt as a single-element list.


 - [`KaCompoundSymbolResolutionError`](../-ka-compound-symbol-resolution-error/index.md): the individual [`sub-attempts`](../-ka-compound-symbol-resolution-error/index.md#simpleattempts).


The list is never empty.


</div>

</div>
### single

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-array-access-call-resolution-attempt/index.html#single">single</a><span class="o">: </span><a href="../-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The only call of [`calls`](../-ka-for-loop-call/index.md#calls), or `null` if the attempt has no calls or more than one.

Unlike [`successful`](../-ka-compound-array-access-call-resolution-attempt/index.md#successful), a call is also returned for a failed resolution, as long as [`calls`](../-ka-for-loop-call/index.md#calls) holds exactly one. For a failed [`KaMultiCallResolutionAttempt`](../-ka-multi-call-resolution-attempt/index.md) that entry may come from any sub-attempt — a resolved sub-call, or a candidate of a failed one — so it is not necessarily a candidate for the element itself.

For a successful [`KaMultiCallResolutionAttempt`](../-ka-multi-call-resolution-attempt/index.md), [`calls`](../-ka-for-loop-call/index.md#calls) holds the assembled [`KaMultiCall`](../-ka-multi-call/index.md), so [`single`](../-ka-compound-array-access-call-resolution-attempt/index.md#single) is that multi-call and its [`simple`](../-ka-for-loop-call/index.md#simple)/[`function`](../-ka-for-loop-call/index.md#function)/[`variable`](../-ka-for-loop-call/index.md#variable) narrowings are all `null`.

**Example**

```kotlin
class Foo {
   private fun bar() {}
}

fun usage(foo: Foo) {
   foo.bar()
//     ^^^^^
}
```

`bar()` is resolved to a [`KaSimpleCallResolutionError`](../-ka-simple-call-resolution-error/index.md), so [`successful`](../-ka-compound-array-access-call-resolution-attempt/index.md#successful) is `null`, while [`single`](../-ka-compound-array-access-call-resolution-attempt/index.md#single) is the `bar` candidate call.

**See also**



 - [`calls`](../-ka-for-loop-call/index.md#calls)
 - [`successful`](../-ka-compound-array-access-call-resolution-attempt/index.md#successful)



</div>

</div>
### successful

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-array-access-call-resolution-attempt/index.html#successful">successful</a><span class="o">: </span><a href="../-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The resolved call if the resolution succeeded, or `null` if it failed.

 - [`KaSimpleCallResolutionSuccess`](../-ka-simple-call-resolution-success/index.md): the resolved [`call`](../-ka-simple-call-resolution-success/index.md#call).


 - 
 - [`KaMultiCallResolutionAttempt`](../-ka-multi-call-resolution-attempt/index.md): the assembled [`call`](../-ka-multi-call-resolution-attempt/index.md#call) if all sub-calls succeeded, or `null` otherwise.



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
### variableCallAttempt

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#variablecallattempt">variableCallAttempt</a><span class="o">: </span><a href="../-ka-simple-call-resolution-attempt/index.html">KaSimpleCallResolutionAttempt</a>
</span></code></pre></div>
</div>


<div markdown>

The resolution attempt for the variable access.

**See also**



 - [`KaCompoundVariableAccessCall.variableCall`](../-ka-compound-variable-access-call/index.md#variablecall)



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
### fold

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="../-ka-compound-symbol-resolution-error/index.html#fold">T</a><span class="o">> </span><a href="../-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#fold"><span class="nf">fold</span></a><span class="p">(</span>onSuccess<span class="o">: </span><span class="p">(</span><a href="../-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="p">)</span><span class="o"> -> </span><a href="../-ka-compound-symbol-resolution-error/index.html#fold">T</a><span class="p">, </span>onFailure<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-simple-call-resolution-error/index.html">KaSimpleCallResolutionError</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span><a href="../-ka-compound-symbol-resolution-error/index.html#fold">T</a><span class="p">)</span><span class="o">: </span><a href="../-ka-compound-symbol-resolution-error/index.html#fold">T</a>
</span></code></pre></div>
</div>


<div markdown>

Folds over a [`KaCallResolutionAttempt`](../-ka-call-resolution-attempt/index.md) depending on whether the resolution succeeded.

 - [`KaSimpleCallResolutionSuccess`](../-ka-simple-call-resolution-success/index.md): invokes [`onSuccess`](../-ka-compound-symbol-resolution-error/index.md#fold) with the resolved [`call`](../-ka-simple-call-resolution-success/index.md#call).


 - [`KaSimpleCallResolutionError`](../-ka-simple-call-resolution-error/index.md): invokes [`onFailure`](../-ka-compound-symbol-resolution-error/index.md#fold) with the error wrapped in a single-element list.


 - [`KaMultiCallResolutionAttempt`](../-ka-multi-call-resolution-attempt/index.md): if all sub-calls succeeded, invokes [`onSuccess`](../-ka-compound-symbol-resolution-error/index.md#fold) with the assembled [`call`](../-ka-multi-call-resolution-attempt/index.md#call); otherwise invokes [`onFailure`](../-ka-compound-symbol-resolution-error/index.md#fold) with the [`errors`](../-ka-compound-symbol-resolution-error/index.md#errors) of the failed sub-calls. The successful sub-calls are not passed to [`onFailure`](../-ka-compound-symbol-resolution-error/index.md#fold); use [`simpleAttempts`](../-ka-compound-symbol-resolution-error/index.md#simpleattempts) to reach them.



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="../-ka-compound-symbol-resolution-error/index.html#fold">T</a><span class="o">> </span><a href="../-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#fold"><span class="nf">fold</span></a><span class="p">(</span>onSuccess<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span><a href="../-ka-compound-symbol-resolution-error/index.html#fold">T</a><span class="p">, </span>onFailure<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-simple-symbol-resolution-error/index.html">KaSimpleSymbolResolutionError</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span><a href="../-ka-compound-symbol-resolution-error/index.html#fold">T</a><span class="p">)</span><span class="o">: </span><a href="../-ka-compound-symbol-resolution-error/index.html#fold">T</a>
</span></code></pre></div>
</div>


<div markdown>

Folds over a [`KaSymbolResolutionAttempt`](../-ka-symbol-resolution-attempt/index.md) depending on whether the resolution succeeded.

 - [`KaSimpleSymbolResolutionSuccess`](../-ka-simple-symbol-resolution-success/index.md): invokes [`onSuccess`](../-ka-compound-symbol-resolution-error/index.md#fold) with the resolved [`symbols`](../-ka-simple-symbol-resolution-success/index.md#symbols).


 - [`KaSimpleSymbolResolutionError`](../-ka-simple-symbol-resolution-error/index.md): invokes [`onFailure`](../-ka-compound-symbol-resolution-error/index.md#fold) with the error wrapped in a single-element list.


 - [`KaCompoundSymbolResolutionError`](../-ka-compound-symbol-resolution-error/index.md): invokes [`onFailure`](../-ka-compound-symbol-resolution-error/index.md#fold) with the [`errors`](../-ka-compound-symbol-resolution-error/index.md#errors) of the failed sub-calls. The successful sub-call, if any, is not passed to [`onFailure`](../-ka-compound-symbol-resolution-error/index.md#fold); use [`simpleAttempts`](../-ka-compound-symbol-resolution-error/index.md#simpleattempts) to reach it.



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
