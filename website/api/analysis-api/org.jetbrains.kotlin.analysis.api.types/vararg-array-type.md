---
tags:
 - jvm
title: "varargArrayType"
---

# varargArrayType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.html">KaValueParameterSymbol</a><span class="p">.</span><a href="vararg-array-type.html">varargArrayType</a><span class="o">: </span><a href="-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The array type that represents the list of arguments passed to this parameter if [`this`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.md) is a [vararg](https://kotlinlang.org/docs/functions.html#variable-number-of-arguments-varargs) parameter.

If [`this`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.md) is not a `vararg` parameter, [`varargArrayType`](vararg-array-type.md) is `null`. If [`this`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.md) is an invalid (e.g., in case of multiple `vararg` parameters) or useless (in anonymous functions) `vararg` parameter, [`varargArrayType`](vararg-array-type.md) still contains a type for it.


</div>

</div>
