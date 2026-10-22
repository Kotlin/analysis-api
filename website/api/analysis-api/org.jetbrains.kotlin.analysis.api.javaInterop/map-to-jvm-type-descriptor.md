---
tags:
 - jvm
title: "mapToJvmTypeDescriptor"
---

# mapToJvmTypeDescriptor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="map-to-jvm-type-descriptor.html"><span class="nf">mapToJvmTypeDescriptor</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Convert the given [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a JVM type descriptor with the [`KaTypeMappingMode.DEFAULT`](../org.jetbrains.kotlin.analysis.api.types/-ka-type-mapping-mode/-d-e-f-a-u-l-t/index.md). To learn more about JVM descriptors, check out the [JVM specification](https://docs.oracle.com/javase/specs/jvms/se24/html/jvms-4.html#jvms-4.3).


</div>

</div>
