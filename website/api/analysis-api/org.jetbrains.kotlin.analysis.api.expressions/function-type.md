---
tags:
 - jvm
title: "functionType"
---

# functionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-function/index.html">KtFunction</a><span class="p">.</span><a href="function-type.html">functionType</a><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The function type of the given [`KtFunction`](../../psi-api/org.jetbrains.kotlin.psi/-kt-function/index.md).

For a regular function, the result is a `kotlin.FunctionN<P1, P2, ..., R>` type where:

 - `N` is the number of value parameters in the function.


 - `Px` is the type of the x-th value parameter.


 - `R` is the return type of the function.


Depending on the function's attributes, such as `suspend` or reflective access, a different functional type such as `SuspendFunction`, `KFunction`, or `KSuspendFunction` will be constructed.


</div>

</div>
