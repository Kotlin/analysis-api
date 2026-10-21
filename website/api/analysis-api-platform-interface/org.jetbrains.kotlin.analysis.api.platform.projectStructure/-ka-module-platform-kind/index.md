---
tags:
 - jvm
title: "KaModulePlatformKind"
---

# KaModulePlatformKind

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="index.html">KaModulePlatformKind</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="index.html">KaModulePlatformKind</a><span class="o">> </span>
</span></code></pre></div>The module platform kind classifies a [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md)'s TargetPlatform into a single kind, determining how the Analysis API interprets the module.

It is either a single kind of concrete platform ([`JVM`](-j-v-m/index.md), [`JS`](-j-s/index.md), [`WASM`](-w-a-s-m/index.md), [`NATIVE`](-n-a-t-i-v-e/index.md)), or [`METADATA`](-m-e-t-a-d-a-t-a/index.md) when the module's TargetPlatform contains multiple kinds of concrete platforms.

This classification determines:

 - The kind of session built for the module and its platform-specific symbol loading.


 -  - For example, while we load Java symbols in a JVM session, we do not do the same in a JVM+Native metadata session. Java symbols       cannot be accessed from Native, and so such symbols should not be loaded in a metadata context.



 - The module's expected layout (e.g., JAR vs. Klib library roots) and associated content scope restrictions for library modules.


Platform-specific, composable configurations are instead applied based on the TargetPlatform's component platforms.

There is an important difference to isMultiPlatform: A target platform with multiple JvmPlatforms can be multiplatform, while the module platform kind would still be [`JVM`](-j-v-m/index.md) rather than [`METADATA`](-m-e-t-a-d-a-t-a/index.md). A [`METADATA`](-m-e-t-a-d-a-t-a/index.md) module platform kind must always come from a target platform with multiple kinds of component platforms.


</div>

## Entries
### [`METADATA`](-m-e-t-a-d-a-t-a/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-m-e-t-a-d-a-t-a/index.html">METADATA</a>

</span></code></pre></div>Represents a metadata module.


</div>

### [`JVM`](-j-v-m/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-j-v-m/index.html">JVM</a>

</span></code></pre></div>Represents a JVM module.


</div>

### [`JS`](-j-s/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-j-s/index.html">JS</a>

</span></code></pre></div>Represents a JS module.


</div>

### [`WASM`](-w-a-s-m/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-w-a-s-m/index.html">WASM</a>

</span></code></pre></div>Represents a Wasm module.


</div>

### [`NATIVE`](-n-a-t-i-v-e/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-n-a-t-i-v-e/index.html">NATIVE</a>

</span></code></pre></div>Represents a Native module.


</div>

## Companion properties
### entries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#entries">entries</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="o"><</span><a href="index.html">KaModulePlatformKind</a><span class="o">></span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#valueof"><span class="nf">valueOf</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaModulePlatformKind</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#values"><span class="nf">values</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="index.html">KaModulePlatformKind</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

The function returns a new instance of the array on every call. The array could be mutated, so working with it may also require defensive copying. Consider using `entries` property as a more efficient alternative returning an immutable list of enum entries.


</div>

</div>
## Properties
### [`name`](../-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`ordinal`](../-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.md#ordinal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.html#ordinal">ordinal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
