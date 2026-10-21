---
tags:
 - jvm
title: "KaBuiltinFunctionTypeFamilies"
---

# KaBuiltinFunctionTypeFamilies

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaBuiltinFunctionTypeFamilies</a>
</span></code></pre></div>Provides access to the four built-in [`function type families`](../-ka-function-type-family/index.md).

#### See also


 - [`builtinFunctionTypeFamilies`](../builtin-function-type-families.md)


#### Inheritors


 - [`KaBuiltinFunctionTypeFamilies`](../../org.jetbrains.kotlin.analysis.api.components/-ka-builtin-function-type-families/index.md)



</div>

## Properties
### function

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#function">function</a><span class="o">: </span><a href="../-ka-function-type-family/index.html">KaFunctionTypeFamily</a>
</span></code></pre></div>
</div>


<div markdown>

The `Function` family representing regular function types (e.g., `Function0`, `Function1`, ..., `FunctionN`).


</div>

</div>
### kFunction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#kfunction">kFunction</a><span class="o">: </span><a href="../-ka-function-type-family/index.html">KaFunctionTypeFamily</a>
</span></code></pre></div>
</div>


<div markdown>

The `KFunction` family representing reflection types for regular functions (e.g., `KFunction0`, `KFunction1`, ..., `KFunctionN`).


</div>

</div>
### kSuspendFunction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#ksuspendfunction">kSuspendFunction</a><span class="o">: </span><a href="../-ka-function-type-family/index.html">KaFunctionTypeFamily</a>
</span></code></pre></div>
</div>


<div markdown>

The `KSuspendFunction` family representing reflection types for suspend functions (e.g., `KSuspendFunction0`, `KSuspendFunction1`, ..., `KSuspendFunctionN`).


</div>

</div>
### suspendFunction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#suspendfunction">suspendFunction</a><span class="o">: </span><a href="../-ka-function-type-family/index.html">KaFunctionTypeFamily</a>
</span></code></pre></div>
</div>


<div markdown>

The `SuspendFunction` family representing suspend function types (e.g., `SuspendFunction0`, `SuspendFunction1`, ..., `SuspendFunctionN`).


</div>

</div>
