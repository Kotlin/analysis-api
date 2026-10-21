---
tags:
 - jvm
title: "KtProjectionKind"
---

# KtProjectionKind

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="index.html">KtProjectionKind</a>
</span></code></pre></div>The kind of variance projection applied to a type argument in a [`KtTypeProjection`](../-kt-type-projection/index.md). 

 - [`IN`](-i-n/index.md) — a contravariant projection, written `#!java in T`.
 - [`OUT`](-o-u-t/index.md) — a covariant projection, written `#!java out T`.
 - [`STAR`](-s-t-a-r/index.md) — a star projection, written `#!java *`.
 - [`NONE`](-n-o-n-e/index.md) — an invariant type argument with no projection keyword.
### Example:
```java

fun copy(from: Array<out Any>, to: Array<in Any>) {}
//                   ^^^                 ^^
//                   OUT                 IN

```


</div>

## Entries
### [`IN`](-i-n/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-i-n/index.html">IN</a>

</span></code></pre></div>A contravariant projection, written `#!java in T`.


</div>

### [`OUT`](-o-u-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-o-u-t/index.html">OUT</a>

</span></code></pre></div>A covariant projection, written `#!java out T`.


</div>

### [`STAR`](-s-t-a-r/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-s-t-a-r/index.html">STAR</a>

</span></code></pre></div>A star projection, written `#!java *`.


</div>

### [`NONE`](-n-o-n-e/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-n-o-n-e/index.html">NONE</a>

</span></code></pre></div>An invariant type argument with no projection keyword.


</div>

## Companion functions
### valueOf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#valueof"><span class="nf">valueOf</span></a><span class="p">(</span>name<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KtProjectionKind</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

**Return**

the enum constant with the specified name

**Throws**



[`java.lang.IllegalArgumentException`](https://docs.oracle.com/javase/8/docs/api/java/lang/IllegalArgumentException.html)

:   if this enum type has no constant with the specified name





</div>

</div>
### values

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#values"><span class="nf">values</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="index.html">KtProjectionKind</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

**Return**

an array containing the constants of this enum type, in the order they're declared


</div>

</div>
## Properties
### token

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">Nullable</span>
<span class="kd">val </span><a href="index.html#token">token</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a>
</span></code></pre></div>
</div>

</div>
