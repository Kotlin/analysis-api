---
tags:
 - jvm
title: "isPrimitiveBacked"
---

# isPrimitiveBacked

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="is-primitive-backed.html">isPrimitiveBacked</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the given [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is backed by a single JVM primitive type.

This is `true` for non-nullable primitive types and for non-nullable inline value class types whose single underlying property is primitive-backed, recursively. It is `false` for nullable types, regular reference types, and types without a single primitive-backed representation.

Only the inline representation counts. A full value class is compiled as a regular class on the JVM, so it is never primitive-backed, even with exactly one primary property; see [`org.jetbrains.kotlin.analysis.api.symbols.KaNamedClassSymbol.isInline`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.md#isinline).

This property describes the type's underlying representation. It does not imply that every use of the type is emitted as a JVM primitive, as boxing can still be required by the use-site context.

For non-JVM modules, the result describes the equivalent JVM representation inferred from the Kotlin declaration.


</div>

</div>
