---
tags:
 - jvm
title: "tryResolveCall"
---

# tryResolveCall

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">.</span><a href="try-resolve-call.html"><span class="nf">tryResolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve the call for the given [`KtResolvableCall`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md).

### Usage Example:
```kotlin
context(session: KaSession)
fun findResolutionDiagnostic(expression: KtCallExpression): KaDiagnostic? {
  val attempt = expression.tryResolveCall() ?: return null
  return attempt.errors.firstOrNull()?.diagnostic
}
```

Returns a [`KaCallResolutionAttempt`](-ka-call-resolution-attempt/index.md), or `null` when there is no call to resolve: the element is not call-shaped, or its reference resolves to something non-callable, such as a qualifier, an import, or a type. Broken code can end up here as well.

A non-null result describes the outcome of an actual resolution. Check it with [`errors`](-ka-compound-symbol-resolution-error/index.md#errors) or [`isSuccessful`](-ka-compound-symbol-resolution-error/index.md#issuccessful) rather than with a type check, which only covers simple attempts. A reported error may carry an empty [`candidateCalls`](-ka-simple-call-resolution-error/index.md#candidatecalls) list.

See [References and Calls](https://kotlin.github.io/analysis-api/references-and-calls.html) for a top-level overview.

#### See also


 - [`resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.html">KtForExpression</a><span class="p">.</span><a href="try-resolve-call.html"><span class="nf">tryResolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-for-loop-call-resolution-attempt/index.html">KaForLoopCallResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve the given [`KtForExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.md) to a [`KaForLoopCallResolutionAttempt`](-ka-for-loop-call-resolution-attempt/index.md) containing the individual resolution results for each desugared operator call (`iterator`, `hasNext`, `next`).

This is a specialized counterpart of [`KtResolvableCall.tryResolveCall`](try-resolve-call.md) focused specifically on `for` loops.

#### See also


 - [`KtForExpression.resolveSuccessfulCall`](resolve-successful-call.md)
 - [`KtResolvableCall.tryResolveCall`](try-resolve-call.md)



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

This is a specialized counterpart of [`KtResolvableCall.tryResolveCall`](try-resolve-call.md) focused specifically on delegated properties.

#### See also


 - [`KtPropertyDelegate.resolveSuccessfulCall`](resolve-successful-call.md)
 - [`KtResolvableCall.tryResolveCall`](try-resolve-call.md)



</div>

</div>
