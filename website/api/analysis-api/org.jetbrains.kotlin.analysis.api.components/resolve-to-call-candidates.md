---
tags:
 - jvm
title: "resolveToCallCandidates"
---

# resolveToCallCandidates

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="resolve-to-call-candidates.html"><span class="nf">resolveToCallCandidates</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-candidate-info/index.html">KaCallCandidateInfo</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all candidates considered during [overload resolution](https://kotlinlang.org/spec/overload-resolution.html) for the call corresponding to this [`KtElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md).

To compare, the [`resolveToCall`](resolve-to-call.md) function only returns the final result of overload resolution, i.e. the most specific callable passing all compatibility checks.

Consider using the [new resolution API](https://kotlin.github.io/analysis-api/migrating-resolution-api.html).

#### See also


 - [`KtResolvableCall.collectCallCandidates`](../org.jetbrains.kotlin.analysis.api.resolution/collect-call-candidates.md)



</div>

</div>
