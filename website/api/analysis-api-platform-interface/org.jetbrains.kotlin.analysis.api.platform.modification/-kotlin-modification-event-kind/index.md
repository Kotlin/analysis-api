---
tags:
 - jvm
title: "KotlinModificationEventKind"
---

# KotlinModificationEventKind

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="index.html">KotlinModificationEventKind</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="index.html">KotlinModificationEventKind</a><span class="o">> </span>
</span></code></pre></div>[`KotlinModificationEventKind`](index.md) represents the kinds of [`KotlinModificationEvent`](../-kotlin-modification-event/index.md)s. While it is not required to publish or subscribe to modification events, it can be useful when abstracting over modification events in general, for example in tests.


</div>

## Entries
### [`MODULE_STATE_MODIFICATION`](-m-o-d-u-l-e_-s-t-a-t-e_-m-o-d-i-f-i-c-a-t-i-o-n/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-m-o-d-u-l-e_-s-t-a-t-e_-m-o-d-i-f-i-c-a-t-i-o-n/index.html">MODULE_STATE_MODIFICATION</a>

</span></code></pre></div>
</div>

### [`MODULE_OUT_OF_BLOCK_MODIFICATION`](-m-o-d-u-l-e_-o-u-t_-o-f_-b-l-o-c-k_-m-o-d-i-f-i-c-a-t-i-o-n/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-m-o-d-u-l-e_-o-u-t_-o-f_-b-l-o-c-k_-m-o-d-i-f-i-c-a-t-i-o-n/index.html">MODULE_OUT_OF_BLOCK_MODIFICATION</a>

</span></code></pre></div>
</div>

### [`GLOBAL_MODULE_STATE_MODIFICATION`](-g-l-o-b-a-l_-m-o-d-u-l-e_-s-t-a-t-e_-m-o-d-i-f-i-c-a-t-i-o-n/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-g-l-o-b-a-l_-m-o-d-u-l-e_-s-t-a-t-e_-m-o-d-i-f-i-c-a-t-i-o-n/index.html">GLOBAL_MODULE_STATE_MODIFICATION</a>

</span></code></pre></div>
</div>

### [`GLOBAL_SOURCE_MODULE_STATE_MODIFICATION`](-g-l-o-b-a-l_-s-o-u-r-c-e_-m-o-d-u-l-e_-s-t-a-t-e_-m-o-d-i-f-i-c-a-t-i-o-n/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-g-l-o-b-a-l_-s-o-u-r-c-e_-m-o-d-u-l-e_-s-t-a-t-e_-m-o-d-i-f-i-c-a-t-i-o-n/index.html">GLOBAL_SOURCE_MODULE_STATE_MODIFICATION</a>

</span></code></pre></div>
</div>

### [`GLOBAL_SCRIPT_MODULE_STATE_MODIFICATION`](-g-l-o-b-a-l_-s-c-r-i-p-t_-m-o-d-u-l-e_-s-t-a-t-e_-m-o-d-i-f-i-c-a-t-i-o-n/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-g-l-o-b-a-l_-s-c-r-i-p-t_-m-o-d-u-l-e_-s-t-a-t-e_-m-o-d-i-f-i-c-a-t-i-o-n/index.html">GLOBAL_SCRIPT_MODULE_STATE_MODIFICATION</a>

</span></code></pre></div>
</div>

### [`GLOBAL_SOURCE_OUT_OF_BLOCK_MODIFICATION`](-g-l-o-b-a-l_-s-o-u-r-c-e_-o-u-t_-o-f_-b-l-o-c-k_-m-o-d-i-f-i-c-a-t-i-o-n/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-g-l-o-b-a-l_-s-o-u-r-c-e_-o-u-t_-o-f_-b-l-o-c-k_-m-o-d-i-f-i-c-a-t-i-o-n/index.html">GLOBAL_SOURCE_OUT_OF_BLOCK_MODIFICATION</a>

</span></code></pre></div>
</div>

### [`CODE_FRAGMENT_CONTEXT_MODIFICATION`](-c-o-d-e_-f-r-a-g-m-e-n-t_-c-o-n-t-e-x-t_-m-o-d-i-f-i-c-a-t-i-o-n/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-c-o-d-e_-f-r-a-g-m-e-n-t_-c-o-n-t-e-x-t_-m-o-d-i-f-i-c-a-t-i-o-n/index.html">CODE_FRAGMENT_CONTEXT_MODIFICATION</a>

</span></code></pre></div>
</div>

## Companion properties
### entries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#entries">entries</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="o"><</span><a href="index.html">KotlinModificationEventKind</a><span class="o">></span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#valueof"><span class="nf">valueOf</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KotlinModificationEventKind</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#values"><span class="nf">values</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="index.html">KotlinModificationEventKind</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

The function returns a new instance of the array on every call. The array could be mutated, so working with it may also require defensive copying. Consider using `entries` property as a more efficient alternative returning an immutable list of enum entries.


</div>

</div>
## Properties
### isGlobalLevel

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html">KotlinModificationEventKind</a><span class="p">.</span><a href="index.html#isgloballevel">isGlobalLevel</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### isModuleLevel

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html">KotlinModificationEventKind</a><span class="p">.</span><a href="index.html#ismodulelevel">isModuleLevel</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
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
