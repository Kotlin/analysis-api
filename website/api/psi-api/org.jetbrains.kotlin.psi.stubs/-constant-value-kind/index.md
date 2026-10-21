---
tags:
 - jvm
title: "ConstantValueKind"
---

# ConstantValueKind

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="index.html">ConstantValueKind</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="index.html">ConstantValueKind</a><span class="o">> </span>
</span></code></pre></div>
</div>

## Entries
### [`NULL`](-n-u-l-l/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-n-u-l-l/index.html">NULL</a>

</span></code></pre></div>
</div>

### [`BOOLEAN_CONSTANT`](-b-o-o-l-e-a-n_-c-o-n-s-t-a-n-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-b-o-o-l-e-a-n_-c-o-n-s-t-a-n-t/index.html">BOOLEAN_CONSTANT</a>

</span></code></pre></div>
</div>

### [`FLOAT_CONSTANT`](-f-l-o-a-t_-c-o-n-s-t-a-n-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-f-l-o-a-t_-c-o-n-s-t-a-n-t/index.html">FLOAT_CONSTANT</a>

</span></code></pre></div>
</div>

### [`CHARACTER_CONSTANT`](-c-h-a-r-a-c-t-e-r_-c-o-n-s-t-a-n-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-c-h-a-r-a-c-t-e-r_-c-o-n-s-t-a-n-t/index.html">CHARACTER_CONSTANT</a>

</span></code></pre></div>
</div>

### [`INTEGER_CONSTANT`](-i-n-t-e-g-e-r_-c-o-n-s-t-a-n-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-i-n-t-e-g-e-r_-c-o-n-s-t-a-n-t/index.html">INTEGER_CONSTANT</a>

</span></code></pre></div>
</div>

## Companion properties
### entries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#entries">entries</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="o"><</span><a href="index.html">ConstantValueKind</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an immutable [`kotlin.enums.EnumEntries`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html) list containing the constants of this enum type, in the order they're declared.


</div>

</div>
## Companion functions
### valueOf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#valueof"><span class="nf">valueOf</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">ConstantValueKind</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

**Throws**



[`kotlin.IllegalArgumentException`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html)

:   if this enum type has no constant with the specified name





</div>

</div>
### values

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#values"><span class="nf">values</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="index.html">ConstantValueKind</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

The function returns a new instance of the array on every call. The array could be mutated, so working with it may also require defensive copying. Consider using `entries` property as a more efficient alternative returning an immutable list of enum entries.


</div>

</div>
## Properties
### [`name`](-i-n-t-e-g-e-r_-c-o-n-s-t-a-n-t/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="-i-n-t-e-g-e-r_-c-o-n-s-t-a-n-t/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`ordinal`](-i-n-t-e-g-e-r_-c-o-n-s-t-a-n-t/index.md#ordinal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="-i-n-t-e-g-e-r_-c-o-n-s-t-a-n-t/index.html#ordinal">ordinal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
## Functions
### [`toConstantExpressionElementType`](../../org.jetbrains.kotlin.psi.utils/to-constant-expression-element-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">ConstantValueKind</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.utils/to-constant-expression-element-type.html"><span class="nf">toConstantExpressionElementType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin/-kt-node-type/index.html">KtNodeType</a>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`ConstantValueKind`](index.md) to the corresponding com.intellij.psi.tree.IElementType.


</div>

</div>
