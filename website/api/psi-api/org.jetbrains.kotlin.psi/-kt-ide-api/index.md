---
tags:
 - jvm
title: "KtIdeApi"
---

# KtIdeApi

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html">AnnotationTarget.CLASS</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html">AnnotationTarget.CONSTRUCTOR</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html">AnnotationTarget.TYPEALIAS</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"Internal API which is used only from the IntelliJ Kotlin plugin. Such an API should not be used in other places since it has no compatibility guarantees"</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="index.html">KtIdeApi</a>
</span></code></pre></div>Marks an API as designed for and internal to the Kotlin IntelliJ plugin. The API is not intended for public user consumption and does not have any compatibility guarantees.

The motivation behind [`KtIdeApi`](index.md) is the following: in a few cases, implementing functionality in the Kotlin PSI API is more efficient or more straightforward than implementing it in the Kotlin IntelliJ plugin. The resulting API is normally too specific to be considered a general, public part of the PSI API.


</div>

