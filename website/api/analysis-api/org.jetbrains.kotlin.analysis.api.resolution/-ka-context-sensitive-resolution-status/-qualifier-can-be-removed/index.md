---
tags:
 - jvm
title: "QualifierCanBeRemoved"
---

# QualifierCanBeRemoved

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">QualifierCanBeRemoved</a> : <a href="../index.html">KaContextSensitiveResolutionStatus</a>
</span></code></pre></div>The name is resolved through an explicit qualifier which can be removed: context-sensitive resolution would resolve the same symbol without it.

#### Example
```kotlin
enum class Foo { BAR }

fun usage(): Foo {
    return Foo.BAR // the 'Foo.' qualifier can be removed
}
```


</div>

