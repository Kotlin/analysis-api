---
tags:
 - jvm
title: "KaSimpleSymbolResolutionAttempt"
---

# KaSimpleSymbolResolutionAttempt

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">KaSimpleSymbolResolutionAttempt</a> : <a href="../-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a>
</span></code></pre></div>Represents an attempt to resolve a simple (non-compound) [`KtResolvable`](../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md), which is either a [`success`](../-ka-simple-symbol-resolution-success/index.md) or an [`error`](../-ka-simple-symbol-resolution-error/index.md).

#### See also


 - [`KaSymbolResolutionAttempt`](../-ka-symbol-resolution-attempt/index.md)


#### Inheritors


 - [`KaSimpleSymbolResolutionSuccess`](../-ka-simple-symbol-resolution-success/index.md)
 - [`KaSimpleSymbolResolutionError`](../-ka-simple-symbol-resolution-error/index.md)



</div>

## Properties
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#simpleattempts">simpleAttempts</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">KaSimpleSymbolResolutionAttempt</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The flattened list of simple resolution attempts.

 - [`KaSimpleSymbolResolutionAttempt`](index.md): [`this`](../-ka-symbol-resolution-attempt/index.md) attempt as a single-element list.


 - [`KaCompoundSymbolResolutionError`](../-ka-compound-symbol-resolution-error/index.md): the individual [`sub-attempts`](../-ka-compound-symbol-resolution-error/index.md#simpleattempts).


The list is never empty.


</div>

</div>
### successfulSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#successfulsymbols">successfulSymbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The resolved symbols if the resolution succeeded, or an empty list if it failed.

A successful resolution always has at least one symbol, so an empty list always means a failure.

**See also**



 - [`isSuccessful`](../-ka-compound-symbol-resolution-error/index.md#issuccessful)
 - [`KaCallResolutionAttempt.successful`](../-ka-compound-array-access-call-resolution-attempt/index.md#successful)



</div>

</div>
### symbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#symbols">symbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The flattened list of [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md)s for the resolved calls.

 - If [`this`](../-ka-simple-or-multi-call/index.md) is an instance of [`KaSimpleCall`](../-ka-simple-call/index.md), the list will contain only the [`KaSimpleCall.signature`](../-ka-simple-call/index.md#signature)'s symbol


 - If [`this`](../-ka-simple-or-multi-call/index.md) is an instance of [`KaMultiCall`](../-ka-multi-call/index.md), the list will contain symbols from all [`KaMultiCall.calls`](../-ka-for-loop-call/index.md#calls)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#symbols">symbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md).

 - If [`this`](../-ka-symbol-resolution-attempt/index.md) is an instance of [`KaSimpleSymbolResolutionSuccess`](../-ka-simple-symbol-resolution-success/index.md), the list will contain [`KaSimpleSymbolResolutionSuccess.symbols`](../-ka-simple-symbol-resolution-success/index.md#symbols).


 - If [`this`](../-ka-symbol-resolution-attempt/index.md) is an instance of [`KaSimpleSymbolResolutionError`](../-ka-simple-symbol-resolution-error/index.md), the list will contain [`KaSimpleSymbolResolutionError.candidateSymbols`](../-ka-simple-symbol-resolution-error/index.md#candidatesymbols).


 - If [`this`](../-ka-symbol-resolution-attempt/index.md) is an instance of [`KaCompoundSymbolResolutionError`](../-ka-compound-symbol-resolution-error/index.md), the list will contain the combined symbols from all attempts.


**See also**



 - [`KaResolver.tryResolveSymbols`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#tryresolvesymbols)



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
