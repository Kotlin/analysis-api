---
tags:
 - jvm
title: "Missing"
---

# Missing

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">Missing</a> : <a href="../index.html">KaCallableImplementationState</a>
</span></code></pre></div>The declaration is neither implemented in the target class, nor it has inherited implementations.

Note that it does not necessarily mean it is a compilation error – if the target class is `abstract`, the implementation can legitimately be absent.


</div>

