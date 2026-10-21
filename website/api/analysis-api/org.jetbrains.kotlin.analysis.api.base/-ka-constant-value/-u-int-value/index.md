---
tags:
 - jvm
title: "UIntValue"
---

# UIntValue

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">UIntValue</a> : <a href="../index.html">KaConstantValue</a>
</span></code></pre></div>Represents a [`UInt`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-int/index.html) value.


</div>

## Properties
### sourcePsi

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-error-value/index.html#sourcepsi">sourcePsi</a><span class="o">: </span><a href="../../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A source element from which the value was created. The PSI might be `null` for constants from non-source files.


</div>

</div>
### value

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#value">value</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-int/index.html">UInt</a>
</span></code></pre></div>
</div>


<div markdown>

The value of the constant. The type of [`value`](../-null-value/index.md#value) matches its represented class, e.g. [`BooleanValue.value`](../-boolean-value/index.md#value) is a [`Boolean`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html).

For [`NullValue`](../-null-value/index.md) and [`ErrorValue`](../-error-value/index.md), [`value`](../-null-value/index.md#value) contains a special value.


</div>

</div>
## Functions
### render

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-error-value/index.html#render"><span class="nf">render</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Renders the value as a representable constant value [`String`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), such as `1`, `2f`, `3u` `null`, `"text"`.


</div>

</div>
