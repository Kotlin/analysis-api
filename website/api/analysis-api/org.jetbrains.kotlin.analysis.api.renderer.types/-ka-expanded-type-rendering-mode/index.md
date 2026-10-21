---
tags:
 - jvm
title: "KaExpandedTypeRenderingMode"
---

# KaExpandedTypeRenderingMode

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="index.html">KaExpandedTypeRenderingMode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="index.html">KaExpandedTypeRenderingMode</a><span class="o">> </span>
</span></code></pre></div>[`KaExpandedTypeRenderingMode`](index.md) controls how [`KaTypeRenderer`](../-ka-type-renderer/index.md) renders expanded types (with an associated abbreviated type) and type aliases which can still be expanded.


</div>

## Entries
### [`RENDER_ABBREVIATED_TYPE`](-r-e-n-d-e-r_-a-b-b-r-e-v-i-a-t-e-d_-t-y-p-e/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-r-e-n-d-e-r_-a-b-b-r-e-v-i-a-t-e-d_-t-y-p-e/index.html">RENDER_ABBREVIATED_TYPE</a>

</span></code></pre></div>Renders only the abbreviated type as-is, e.g. `foo.bar.StringAlias`.


</div>

### [`RENDER_ABBREVIATED_TYPE_WITH_EXPANDED_TYPE_COMMENT`](-r-e-n-d-e-r_-a-b-b-r-e-v-i-a-t-e-d_-t-y-p-e_-w-i-t-h_-e-x-p-a-n-d-e-d_-t-y-p-e_-c-o-m-m-e-n-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-r-e-n-d-e-r_-a-b-b-r-e-v-i-a-t-e-d_-t-y-p-e_-w-i-t-h_-e-x-p-a-n-d-e-d_-t-y-p-e_-c-o-m-m-e-n-t/index.html">RENDER_ABBREVIATED_TYPE_WITH_EXPANDED_TYPE_COMMENT</a>

</span></code></pre></div>Renders the abbreviated type as-is and its expansion in a comment, e.g. `foo.bar.StringAlias /* = kotlin.String */`.


</div>

### [`RENDER_EXPANDED_TYPE`](-r-e-n-d-e-r_-e-x-p-a-n-d-e-d_-t-y-p-e/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-r-e-n-d-e-r_-e-x-p-a-n-d-e-d_-t-y-p-e/index.html">RENDER_EXPANDED_TYPE</a>

</span></code></pre></div>Renders the expanded type as-is, e.g. `kotlin.String`.


</div>

### [`RENDER_EXPANDED_TYPE_WITH_ABBREVIATED_TYPE_COMMENT`](-r-e-n-d-e-r_-e-x-p-a-n-d-e-d_-t-y-p-e_-w-i-t-h_-a-b-b-r-e-v-i-a-t-e-d_-t-y-p-e_-c-o-m-m-e-n-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-r-e-n-d-e-r_-e-x-p-a-n-d-e-d_-t-y-p-e_-w-i-t-h_-a-b-b-r-e-v-i-a-t-e-d_-t-y-p-e_-c-o-m-m-e-n-t/index.html">RENDER_EXPANDED_TYPE_WITH_ABBREVIATED_TYPE_COMMENT</a>

</span></code></pre></div>Renders the expanded type as-is and its abbreviated type in a comment, e.g. `kotlin.String /* from: foo.bar.StringAlias */`.


</div>

## Companion properties
### entries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#entries">entries</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="o"><</span><a href="index.html">KaExpandedTypeRenderingMode</a><span class="o">></span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#valueof"><span class="nf">valueOf</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaExpandedTypeRenderingMode</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#values"><span class="nf">values</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="index.html">KaExpandedTypeRenderingMode</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

The function returns a new instance of the array on every call. The array could be mutated, so working with it may also require defensive copying. Consider using `entries` property as a more efficient alternative returning an immutable list of enum entries.


</div>

</div>
## Properties
### [`name`](../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`ordinal`](../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md#ordinal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.html#ordinal">ordinal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
