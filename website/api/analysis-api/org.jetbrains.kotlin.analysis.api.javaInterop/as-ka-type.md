---
tags:
 - jvm
title: "asKaType"
---

# asKaType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span>PsiType<span class="p">.</span><a href="as-ka-type.html"><span class="nf">asKaType</span></a><span class="p">(</span>useSitePosition<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given PsiType to a [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) in the context of the [`useSitePosition`](as-ka-type.md).

[`useSitePosition`](as-ka-type.md) clarifies how to resolve some parts of the PsiType. For instance, it can be used to collect type parameters and apply them during the conversion.

#### Receiver
The PsiType to be converted.

#### Return
The converted [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md), or `null` if conversion is not possible. For example, PsiType might not be resolvable.


</div>

</div>
