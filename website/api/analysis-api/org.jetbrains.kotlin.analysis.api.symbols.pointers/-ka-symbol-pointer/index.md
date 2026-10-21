---
tags:
 - jvm
title: "KaSymbolPointer"
---

# KaSymbolPointer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KaSymbolPointer</a><span class="o"><</span><span class="kd">out </span><a href="index.html">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>[`KaSymbolPointer`](index.md) allows to point to a [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) and later retrieve it in another [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md). A pointer is necessary because [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md)s cannot be shared past the boundaries of the [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) they were created in, as they are valid only there.

#### See also


 - [`KaLifetimeToken`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md)



</div>

## Constructors
### KaSymbolPointer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Functions
### pointsToTheSameSymbolAs

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#pointstothesamesymbolas"><span class="nf">pointsToTheSameSymbolAs</span></a><span class="p">(</span>other<span class="o">: </span><a href="index.html">KaSymbolPointer</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`other`](index.md#pointstothesamesymbolas) pointer can be restored to the same symbol. The operation is symmetric and transitive.


</div>

</div>
### restoreSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#restoresymbol"><span class="nf">restoreSymbol</span></a><span class="p">(</span>analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span><span class="o">: </span><a href="index.html">S</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the restored [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) (possibly a new symbol instance) if the pointer is still valid, `null` otherwise.

Do not use this function directly, as it is an implementation detail. Use [`KaSession.restoreSymbol`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md#restoresymbol) instead.


</div>

</div>
### restoreSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><span class="o"><</span><a href="index.html#restoresymbol">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">> </span><a href="index.html">KaSymbolPointer</a><span class="o"><</span><a href="index.html#restoresymbol">S</a><span class="o">></span><span class="p">.</span><a href="index.html#restoresymbol"><span class="nf">restoreSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="index.html#restoresymbol">S</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the restored [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) (possibly a new symbol instance) if the pointer is still valid, or `null` otherwise.


</div>

</div>
### toString

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#tostring"><span class="nf">toString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
