---
tags:
 - jvm
title: "Write"
---

# Write

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">Write</a> : <a href="../index.html">KaVariableAccessCall.Kind</a>
</span></code></pre></div>The [`variable access`](../../index.md) writes to the variable.


</div>

## Properties
### value

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#value">value</a><span class="o">: </span><a href="../../../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KtExpression`](../../../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md) that represents the new value which is assigned to this variable, or `null` if the assignment is incomplete and lacks the new value.


</div>

</div>
