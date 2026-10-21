---
tags:
 - jvm
title: "KaTypeMappingMode"
---

# KaTypeMappingMode

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="index.html">KaTypeMappingMode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="index.html">KaTypeMappingMode</a><span class="o">> </span>
</span></code></pre></div>[`KaTypeMappingMode`](index.md) determines how a Kotlin type is mapped to a Java type when calling [`KaType.asPsiType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.md#aspsitype).


</div>

## Entries
### [`DEFAULT`](-d-e-f-a-u-l-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-d-e-f-a-u-l-t/index.html">DEFAULT</a>

</span></code></pre></div>Kotlin primitives are mapped to Java primitives in non-generic usages. For example, `kotlin.Int` is mapped to `int`.


</div>

### [`DEFAULT_UAST`](-d-e-f-a-u-l-t_-u-a-s-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-d-e-f-a-u-l-t_-u-a-s-t/index.html">DEFAULT_UAST</a>

</span></code></pre></div>Similar to [`DEFAULT`](-d-e-f-a-u-l-t/index.md), but type aliases are additionally mapped to their expanded form.


</div>

### [`GENERIC_ARGUMENT`](-g-e-n-e-r-i-c_-a-r-g-u-m-e-n-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-g-e-n-e-r-i-c_-a-r-g-u-m-e-n-t/index.html">GENERIC_ARGUMENT</a>

</span></code></pre></div>Kotlin primitives are mapped to Java boxed types in non-generic usages. For example, `kotlin.Int` is mapped to `java.lang.Integer`.


</div>

### [`SUPER_TYPE`](-s-u-p-e-r_-t-y-p-e/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-s-u-p-e-r_-t-y-p-e/index.html">SUPER_TYPE</a>

</span></code></pre></div>Kotlin primitives are mapped to Java boxed types in non-generic usages. For example, `kotlin.Int` is mapped to `java.lang.Integer`.


</div>

### [`SUPER_TYPE_KOTLIN_COLLECTIONS_AS_IS`](-s-u-p-e-r_-t-y-p-e_-k-o-t-l-i-n_-c-o-l-l-e-c-t-i-o-n-s_-a-s_-i-s/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-s-u-p-e-r_-t-y-p-e_-k-o-t-l-i-n_-c-o-l-l-e-c-t-i-o-n-s_-a-s_-i-s/index.html">SUPER_TYPE_KOTLIN_COLLECTIONS_AS_IS</a>

</span></code></pre></div>Similar to [`SUPER_TYPE`](-s-u-p-e-r_-t-y-p-e/index.md), except that Kotlin collections are not converted to their Java equivalents.


</div>

### [`RETURN_TYPE_BOXED`](-r-e-t-u-r-n_-t-y-p-e_-b-o-x-e-d/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-r-e-t-u-r-n_-t-y-p-e_-b-o-x-e-d/index.html">RETURN_TYPE_BOXED</a>

</span></code></pre></div>Kotlin primitives in method return types are mapped to Java boxed types. For example, `kotlin.Int` is mapped to `java.lang.Integer`.


</div>

### [`RETURN_TYPE`](-r-e-t-u-r-n_-t-y-p-e/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-r-e-t-u-r-n_-t-y-p-e/index.html">RETURN_TYPE</a>

</span></code></pre></div>The optimal mode to convert a declaration's return type if it's part of the signature.


</div>

### [`FUNCTION_RETURN_TYPE`](-f-u-n-c-t-i-o-n_-r-e-t-u-r-n_-t-y-p-e/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-f-u-n-c-t-i-o-n_-r-e-t-u-r-n_-t-y-p-e/index.html">FUNCTION_RETURN_TYPE</a>

</span></code></pre></div>Same as [`RETURN_TYPE`](-r-e-t-u-r-n_-t-y-p-e/index.md), but Kotlin Unit is mapped to Java `void`. Should be used only for return types of functions (not properties or getters), because `void` type can't be used anywhere else.


</div>

### [`VALUE_PARAMETER`](-v-a-l-u-e_-p-a-r-a-m-e-t-e-r/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-v-a-l-u-e_-p-a-r-a-m-e-t-e-r/index.html">VALUE_PARAMETER</a>

</span></code></pre></div>The optimal mode to convert a value parameter's type if it's part of the signature.


</div>

### [`VALUE_PARAMETER_BOXED`](-v-a-l-u-e_-p-a-r-a-m-e-t-e-r_-b-o-x-e-d/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-v-a-l-u-e_-p-a-r-a-m-e-t-e-r_-b-o-x-e-d/index.html">VALUE_PARAMETER_BOXED</a>

</span></code></pre></div>The same as [`VALUE_PARAMETER`](-v-a-l-u-e_-p-a-r-a-m-e-t-e-r/index.md), but value classes are boxed.


</div>

## Companion properties
### entries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#entries">entries</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="o"><</span><a href="index.html">KaTypeMappingMode</a><span class="o">></span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#valueof"><span class="nf">valueOf</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaTypeMappingMode</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#values"><span class="nf">values</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="index.html">KaTypeMappingMode</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

The function returns a new instance of the array on every call. The array could be mutated, so working with it may also require defensive copying. Consider using `entries` property as a more efficient alternative returning an immutable list of enum entries.


</div>

</div>
## Properties
### [`name`](../-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`ordinal`](../-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md#ordinal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.html#ordinal">ordinal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
