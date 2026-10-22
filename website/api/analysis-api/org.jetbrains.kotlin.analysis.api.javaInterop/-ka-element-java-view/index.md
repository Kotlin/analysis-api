---
tags:
 - jvm
title: "KaElementJavaView"
---

# KaElementJavaView

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaElementJavaView</a>
</span></code></pre></div>A view on Kotlin [`KtElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md)s from Java perspective.

#### Inheritors


 - [`KaSymbolJavaView`](../-ka-symbol-java-view/index.md)



</div>

## Properties
### kotlinOrigin

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-symbol-java-view/index.html#kotlinorigin">kotlinOrigin</a><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

[`KtElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md) from which this view was constructed from.

Note that [`kotlinOrigin`](../-ka-symbol-java-view/index.md#kotlinorigin) might not point to the exact represented declaration. That's because some elements might be synthetic and not have a physical PSI.


</div>

</div>
