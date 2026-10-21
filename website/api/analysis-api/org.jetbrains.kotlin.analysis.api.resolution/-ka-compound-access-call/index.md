---
tags:
 - jvm
title: "KaCompoundAccessCall"
---

# KaCompoundAccessCall

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaCompoundAccessCall</a>
</span></code></pre></div>A compound access of a [`variable`](../-ka-compound-variable-access-call/index.md) or an [`array`](../-ka-compound-array-access-call/index.md).

#### Inheritors


 - [`KaCompoundVariableAccessCall`](../-ka-compound-variable-access-call/index.md)
 - [`KaCompoundArrayAccessCall`](../-ka-compound-array-access-call/index.md)



</div>

## Properties
### compoundOperation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-compound-array-access-call/index.html#compoundoperation">compoundOperation</a><span class="o">: </span><a href="../-ka-compound-operation/index.html">KaCompoundOperation</a>
</span></code></pre></div>
</div>


<div markdown>

The corresponding [`compound operation`](../-ka-compound-operation/index.md).


</div>

</div>
### operationCall

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../-ka-compound-array-access-call/index.html#operationcall">operationCall</a><span class="o">: </span><a href="../-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Represents a call of the operator


</div>

</div>
