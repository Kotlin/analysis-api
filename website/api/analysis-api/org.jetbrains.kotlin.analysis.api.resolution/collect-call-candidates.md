---
tags:
 - jvm
title: "collectCallCandidates"
---

# collectCallCandidates

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">.</span><a href="collect-call-candidates.html"><span class="nf">collectCallCandidates</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-ka-call-candidate/index.html">KaCallCandidate</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all candidates considered during [overload resolution](https://kotlinlang.org/spec/overload-resolution.html) for the call corresponding to the given [`KtResolvableCall`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md).

In contrast, [`resolveSuccessfulCall`](resolve-successful-call.md) returns only the final result, i.e., the most specific callable that passes all compatibility checks.

#### See also


 - [`resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>
