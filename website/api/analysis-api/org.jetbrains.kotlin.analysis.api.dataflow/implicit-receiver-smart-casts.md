---
tags:
 - jvm
title: "implicitReceiverSmartCasts"
---

# implicitReceiverSmartCasts

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="implicit-receiver-smart-casts.html">implicitReceiverSmartCasts</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="-ka-implicit-receiver-smart-cast/index.html">KaImplicitReceiverSmartCast</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The list of [`implicit receiver smart casts`](-ka-implicit-receiver-smart-cast/index.md) which have refined the expression's implicit receivers to a more specific type. These smart casts are required for the expression to be evaluated. The list does not include smart casts for explicit receivers.

#### Example
```kotlin
if (this is String) {
  this.substring()   // 'this' receiver is explicit, so there is no implicit smart cast here.

  smartcast()        // 'this' receiver is implicit, therefore there is an implicit smart cast involved.
}
```


</div>

</div>
