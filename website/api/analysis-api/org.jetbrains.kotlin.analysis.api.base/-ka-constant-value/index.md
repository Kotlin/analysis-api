---
tags:
 - jvm
title: "KaConstantValue"
---

# KaConstantValue

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">KaConstantValue</a>
</span></code></pre></div>Represents a [compile-time constant](https://kotlinlang.org/docs/properties.html#compile-time-constants) value. It can be used as a `const val` initializer or as an annotation argument.

[`KaConstantValue`](index.md) can also represent evaluated values. For example, the constant expression `1 + 2` can be represented as an [`IntValue`](-int-value/index.md) with a value `3`.

#### Inheritors


 - [`NullValue`](-null-value/index.md)
 - [`BooleanValue`](-boolean-value/index.md)
 - [`CharValue`](-char-value/index.md)
 - [`ByteValue`](-byte-value/index.md)
 - [`UByteValue`](-u-byte-value/index.md)
 - [`ShortValue`](-short-value/index.md)
 - [`UShortValue`](-u-short-value/index.md)
 - [`IntValue`](-int-value/index.md)
 - [`UIntValue`](-u-int-value/index.md)
 - [`LongValue`](-long-value/index.md)
 - [`ULongValue`](-u-long-value/index.md)
 - [`FloatValue`](-float-value/index.md)
 - [`DoubleValue`](-double-value/index.md)
 - [`StringValue`](-string-value/index.md)
 - [`ErrorValue`](-error-value/index.md)



</div>

## Types
### [`BooleanValue`](-boolean-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-boolean-value/index.html">BooleanValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`Boolean`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) value.


</div>

</div>
### [`ByteValue`](-byte-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-byte-value/index.html">ByteValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`Byte`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte/index.html) value.


</div>

</div>
### [`CharValue`](-char-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-char-value/index.html">CharValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`Char`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char/index.html) value.


</div>

</div>
### [`DoubleValue`](-double-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-double-value/index.html">DoubleValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`Double`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html) value.


</div>

</div>
### [`ErrorValue`](-error-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-error-value/index.html">ErrorValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents either a non-constant value, or a constant evaluation error (such as a division by zero).


</div>

</div>
### [`FloatValue`](-float-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-float-value/index.html">FloatValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`Float`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html) value.


</div>

</div>
### [`IntValue`](-int-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-int-value/index.html">IntValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an [`Int`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) value.


</div>

</div>
### [`LongValue`](-long-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-long-value/index.html">LongValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`Long`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html) value.


</div>

</div>
### [`NullValue`](-null-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-null-value/index.html">NullValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `null` value of some class type.


</div>

</div>
### [`ShortValue`](-short-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-short-value/index.html">ShortValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`Short`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/index.html) value.


</div>

</div>
### [`StringValue`](-string-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-string-value/index.html">StringValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`String`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) value.


</div>

</div>
### [`UByteValue`](-u-byte-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-u-byte-value/index.html">UByteValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`UByte`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-byte/index.html) value.


</div>

</div>
### [`UIntValue`](-u-int-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-u-int-value/index.html">UIntValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`UInt`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-int/index.html) value.


</div>

</div>
### [`ULongValue`](-u-long-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-u-long-value/index.html">ULongValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`ULong`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-long/index.html) value.


</div>

</div>
### [`UShortValue`](-u-short-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-u-short-value/index.html">UShortValue</a> : <a href="index.html">KaConstantValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`UShort`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-short/index.html) value.


</div>

</div>
## Properties
### sourcePsi

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="-error-value/index.html#sourcepsi">sourcePsi</a><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A source element from which the value was created. The PSI might be `null` for constants from non-source files.


</div>

</div>
### value

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="-null-value/index.html#value">value</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The value of the constant. The type of [`value`](-null-value/index.md#value) matches its represented class, e.g. [`BooleanValue.value`](-boolean-value/index.md#value) is a [`Boolean`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html).

For [`NullValue`](-null-value/index.md) and [`ErrorValue`](-error-value/index.md), [`value`](-null-value/index.md#value) contains a special value.


</div>

</div>
## Functions
### render

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="-error-value/index.html#render"><span class="nf">render</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Renders the value as a representable constant value [`String`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), such as `1`, `2f`, `3u` `null`, `"text"`.


</div>

</div>
