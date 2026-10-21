---
tags:
 - jvm
title: "KotlinDeserializedDeclarationsOrigin"
---

# KotlinDeserializedDeclarationsOrigin

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="index.html">KotlinDeserializedDeclarationsOrigin</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="index.html">KotlinDeserializedDeclarationsOrigin</a><span class="o">> </span>
</span></code></pre></div>This [`setting`](../-kotlin-platform-settings/index.md) controls where [`declarations`](../../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-declaration-provider/index.md) provided by the platform come from.

The origin directly affects whether declaration providers have to provide library entities in addition to source entities, which is the case for the [`STUBS`](-s-t-u-b-s/index.md) origin.

Internally, the Analysis API engine has to use different implementations of symbol providers for [`BINARIES`](-b-i-n-a-r-i-e-s/index.md) and [`STUBS`](-s-t-u-b-s/index.md).


</div>

## Entries
### [`BINARIES`](-b-i-n-a-r-i-e-s/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-b-i-n-a-r-i-e-s/index.html">BINARIES</a>

</span></code></pre></div>Library content is deserialized from `.class` files, KLIBs, and metadata.


</div>

### [`STUBS`](-s-t-u-b-s/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-s-t-u-b-s/index.html">STUBS</a>

</span></code></pre></div>Library content is pre-indexed to [stubs](https://plugins.jetbrains.com/docs/intellij/stub-indexes.html), which are then provided by [`declaration providers`](../../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-declaration-provider/index.md).


</div>

## Companion properties
### entries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#entries">entries</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="o"><</span><a href="index.html">KotlinDeserializedDeclarationsOrigin</a><span class="o">></span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#valueof"><span class="nf">valueOf</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KotlinDeserializedDeclarationsOrigin</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#values"><span class="nf">values</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="index.html">KotlinDeserializedDeclarationsOrigin</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

The function returns a new instance of the array on every call. The array could be mutated, so working with it may also require defensive copying. Consider using `entries` property as a more efficient alternative returning an immutable list of enum entries.


</div>

</div>
## Properties
### [`name`](../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`ordinal`](../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.md#ordinal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.html#ordinal">ordinal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
