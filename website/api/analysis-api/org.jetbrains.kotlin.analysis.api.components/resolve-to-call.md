---
tags:
 - jvm
title: "resolveToCall"
---

# resolveToCall

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="resolve-to-call.html"><span class="nf">resolveToCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/index.html">KaCallInfo</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md) to a [`KaCallInfo`](../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/index.md) object. [`KaCallInfo`](../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/index.md) either contains a successfully resolved call or an error with a list of candidate calls and a diagnostic.

Returns `null` if the element does not correspond to a call.

Consider using the [new resolution API](https://kotlin.github.io/analysis-api/migrating-resolution-api.html).

#### See also


 - [`KtResolvableCall.tryResolveCall`](../org.jetbrains.kotlin.analysis.api.resolution/try-resolve-call.md)



</div>

</div>
