---
tags:
 - jvm
title: "unwrapNullability"
---

# unwrapNullability

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">tailrec </span><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-type-element/index.html">KtTypeElement</a><span class="p">.</span><a href="unwrap-nullability.html"><span class="nf">unwrapNullability</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-type-element/index.html">KtTypeElement</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns this type after stripping all outer [`KtNullableType`](../org.jetbrains.kotlin.psi/-kt-nullable-type/index.md) layers. Returns `null` only if a nullable-type node is malformed and has no inner type.


</div>

</div>
