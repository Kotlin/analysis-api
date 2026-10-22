---
tags:
 - jvm
title: "type"
---

# type

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.html">KtTypeReference</a><span class="p">.</span><a href="type.html">type</a><span class="o">: </span><a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtTypeReference`](../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.md) to its corresponding [`KaType`](-ka-type/index.md).

This may raise an exception if the resolution ends up with an unexpected result.


</div>

</div>
