---
tags:
 - jvm
title: "State"
---

# State

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="index.html">State</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="index.html">KtPsiFactory.CallableBuilder.State</a><span class="o">> </span>
</span></code></pre></div>The stages in the expected order for building a callable.


</div>

## Entries
### [`MODIFIERS`](-m-o-d-i-f-i-e-r-s/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-m-o-d-i-f-i-e-r-s/index.html">MODIFIERS</a>

</span></code></pre></div>
</div>

### [`NAME`](-n-a-m-e/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-n-a-m-e/index.html">NAME</a>

</span></code></pre></div>
</div>

### [`RECEIVER`](-r-e-c-e-i-v-e-r/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-r-e-c-e-i-v-e-r/index.html">RECEIVER</a>

</span></code></pre></div>
</div>

### [`FIRST_PARAM`](-f-i-r-s-t_-p-a-r-a-m/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-f-i-r-s-t_-p-a-r-a-m/index.html">FIRST_PARAM</a>

</span></code></pre></div>
</div>

### [`REST_PARAMS`](-r-e-s-t_-p-a-r-a-m-s/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-r-e-s-t_-p-a-r-a-m-s/index.html">REST_PARAMS</a>

</span></code></pre></div>
</div>

### [`TYPE_CONSTRAINTS`](-t-y-p-e_-c-o-n-s-t-r-a-i-n-t-s/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-t-y-p-e_-c-o-n-s-t-r-a-i-n-t-s/index.html">TYPE_CONSTRAINTS</a>

</span></code></pre></div>
</div>

### [`BODY`](-b-o-d-y/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-b-o-d-y/index.html">BODY</a>

</span></code></pre></div>
</div>

### [`DONE`](-d-o-n-e/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-d-o-n-e/index.html">DONE</a>

</span></code></pre></div>
</div>

## Companion properties
### entries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#entries">entries</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="o"><</span><a href="index.html">KtPsiFactory.CallableBuilder.State</a><span class="o">></span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#valueof"><span class="nf">valueOf</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.CallableBuilder.State</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#values"><span class="nf">values</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="index.html">KtPsiFactory.CallableBuilder.State</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

The function returns a new instance of the array on every call. The array could be mutated, so working with it may also require defensive copying. Consider using `entries` property as a more efficient alternative returning an immutable list of enum entries.


</div>

</div>
## Properties
### [`name`](../../../../org.jetbrains.kotlin.psi.stubs/-constant-value-kind/-i-n-t-e-g-e-r_-c-o-n-s-t-a-n-t/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../../../org.jetbrains.kotlin.psi.stubs/-constant-value-kind/-i-n-t-e-g-e-r_-c-o-n-s-t-a-n-t/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`ordinal`](../../../../org.jetbrains.kotlin.psi.stubs/-constant-value-kind/-i-n-t-e-g-e-r_-c-o-n-s-t-a-n-t/index.md#ordinal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../../../org.jetbrains.kotlin.psi.stubs/-constant-value-kind/-i-n-t-e-g-e-r_-c-o-n-s-t-a-n-t/index.html#ordinal">ordinal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
