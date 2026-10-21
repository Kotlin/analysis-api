---
tags:
 - jvm
title: "KaClassTypeRenderingMode"
---

# KaClassTypeRenderingMode

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="index.html">KaClassTypeRenderingMode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="index.html">KaClassTypeRenderingMode</a><span class="o">> </span>
</span></code></pre></div>Controls how a class type which involves a type alias is rendered: either as the abbreviation (the type alias application, e.g. `foo.bar.StringAlias`) or as its expansion (e.g. `kotlin.String`), optionally with the other one in a comment.

The mode applies both to a type which carries an [`abbreviation`](../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.md#abbreviation) and to an unexpanded type alias application (a class type whose symbol is a [`KaTypeAliasSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-alias-symbol/index.md)). All modes render the same output for any other type.

#### See also


 - [`KaRenderingOption.ClassTypeRenderingMode`](../-ka-rendering-option/-companion/index.md#classtyperenderingmode)



</div>

## Entries
### [`ABBREVIATION`](-a-b-b-r-e-v-i-a-t-i-o-n/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-a-b-b-r-e-v-i-a-t-i-o-n/index.html">ABBREVIATION</a>

</span></code></pre></div>Only the abbreviation, e.g. `foo.bar.StringAlias`.


</div>

### [`ABBREVIATION_WITH_EXPANSION_COMMENT`](-a-b-b-r-e-v-i-a-t-i-o-n_-w-i-t-h_-e-x-p-a-n-s-i-o-n_-c-o-m-m-e-n-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-a-b-b-r-e-v-i-a-t-i-o-n_-w-i-t-h_-e-x-p-a-n-s-i-o-n_-c-o-m-m-e-n-t/index.html">ABBREVIATION_WITH_EXPANSION_COMMENT</a>

</span></code></pre></div>The abbreviation, followed by its expansion in a comment, e.g. `foo.bar.StringAlias /* = kotlin.String */`.


</div>

### [`EXPANSION`](-e-x-p-a-n-s-i-o-n/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-e-x-p-a-n-s-i-o-n/index.html">EXPANSION</a>

</span></code></pre></div>Only the expansion, e.g. `kotlin.String`.


</div>

### [`EXPANSION_WITH_ABBREVIATION_COMMENT`](-e-x-p-a-n-s-i-o-n_-w-i-t-h_-a-b-b-r-e-v-i-a-t-i-o-n_-c-o-m-m-e-n-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-e-x-p-a-n-s-i-o-n_-w-i-t-h_-a-b-b-r-e-v-i-a-t-i-o-n_-c-o-m-m-e-n-t/index.html">EXPANSION_WITH_ABBREVIATION_COMMENT</a>

</span></code></pre></div>The expansion, followed by the abbreviation in a comment, e.g. `kotlin.String /* from: foo.bar.StringAlias */`.


</div>

## Companion properties
### entries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#entries">entries</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="o"><</span><a href="index.html">KaClassTypeRenderingMode</a><span class="o">></span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#valueof"><span class="nf">valueOf</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaClassTypeRenderingMode</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#values"><span class="nf">values</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="index.html">KaClassTypeRenderingMode</a><span class="o">></span>
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
