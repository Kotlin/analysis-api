---
tags:
 - jvm
title: "Used"
---

# Used

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">Used</a> : <a href="../index.html">KaContextSensitiveResolutionStatus</a>
</span></code></pre></div>The name is already resolved through context-sensitive resolution.

#### Example
```kotlin
enum class Foo { BAR }

fun usage(foo: Foo) {}

fun main() {
    usage(BAR) // 'BAR' is resolved against the expected type 'Foo'
}
```


</div>

