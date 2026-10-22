---
tags:
 - jvm
title: "KtExperimentalApi"
---

# KtExperimentalApi

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html">AnnotationTarget.CLASS</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html">AnnotationTarget.CONSTRUCTOR</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html">AnnotationTarget.TYPEALIAS</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"Experimental API with no compatibility guarantees"</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="index.html">KtExperimentalApi</a>
</span></code></pre></div>Marks an API as experimental. The API is intended for user consumption, but it's not stable and might change at any moment, or even be removed, without a deprecation cycle.


</div>

