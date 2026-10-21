---
tags:
 - jvm
title: "KaSpiExtensionPoint"
---

# KaSpiExtensionPoint

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"An API designed for implementation only. Direct usage has no compatibility guarantees."</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="index.html">KaSpiExtensionPoint</a>
</span></code></pre></div>Marks an API as a service provider interface extension point. Such APIs are designed to be implemented, not called directly. There are no compatibility guarantees for usage of these APIs, only for their implementation.

#### See also


 - [`KaSpi`](../../../analysis-api/org.jetbrains.kotlin.analysis.api/-ka-spi/index.md)



</div>

