---
tags:
 - jvm
title: "KaTypePointer"
---

# KaTypePointer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaTypePointer</a><span class="o"><</span><span class="kd">out </span><a href="index.html">T</a><span class="o"> : </span><a href="../-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>[`KaTypePointer`](index.md) allows to point to a [`KaType`](../-ka-type/index.md) and later retrieve it in another [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md). A pointer is necessary because [`KaType`](../-ka-type/index.md)s cannot be shared past the boundaries of the [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) they were created in, as they are valid only there.

#### See also


 - [`KaSymbolPointer`](../../org.jetbrains.kotlin.analysis.api.symbols.pointers/-ka-symbol-pointer/index.md)
 - [`KaLifetimeToken`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md)



</div>

## Functions
### restore

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#restore"><span class="nf">restore</span></a><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span><span class="o">: </span><a href="index.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the restored [`KaType`](../-ka-type/index.md) (possibly a new type instance) if the pointer is still valid, or `null` otherwise.

Do not use this function directly, as it is an implementation detail. Use [`KaSession.restore`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md#restore) instead.


</div>

</div>
### restore

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><span class="o"><</span><a href="index.html#restore">T</a><span class="o"> : </span><a href="../-ka-type/index.html">KaType</a><span class="o">> </span><a href="index.html">KaTypePointer</a><span class="o"><</span><a href="index.html#restore">T</a><span class="o">></span><span class="p">.</span><a href="index.html#restore"><span class="nf">restore</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="index.html#restore">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the restored [`KaType`](../-ka-type/index.md) (possibly a new type instance) if the pointer is still valid, or `null` otherwise.


</div>

</div>
