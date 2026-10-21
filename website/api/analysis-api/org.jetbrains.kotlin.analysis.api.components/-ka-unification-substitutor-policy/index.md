---
tags:
 - jvm
title: "KaUnificationSubstitutorPolicy"
---

# KaUnificationSubstitutorPolicy

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="index.html">KaUnificationSubstitutorPolicy</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="index.html">KaUnificationSubstitutorPolicy</a><span class="o">> </span>
</span></code></pre></div><strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.types.KaUnificationSubstitutorPolicy</strong>`](../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/index.md)<strong> instead.</strong>

[`KaUnificationSubstitutorPolicy`](index.md) determines the way unification [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md)s are created in [`KaSubstitutorProvider.createSubtypingUnificationSubstitutor`](../-ka-substitutor-provider/index.md#createsubtypingunificationsubstitutor). Note that the policy only affects the construction when at least one of the involved types is generic, i.e., depends on a type parameter.


</div>

## Entries
### [`ASSIGN_LEFT`](-a-s-s-i-g-n_-l-e-f-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-a-s-s-i-g-n_-l-e-f-t/index.html">ASSIGN_LEFT</a>

</span></code></pre></div>Requires that there exists an instantiation of the left type parameters such that the left type is a subtype of the right type when substituted. Type parameters of the right type are treated as fixed.


</div>

### [`ASSIGN_RIGHT`](-a-s-s-i-g-n_-r-i-g-h-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-a-s-s-i-g-n_-r-i-g-h-t/index.html">ASSIGN_RIGHT</a>

</span></code></pre></div>Requires that there exists an instantiation of the right type parameters such that the right type is a supertype of the left type when substituted. Type parameters of the left type are treated as fixed.


</div>

### [`ASSIGN_ALL`](-a-s-s-i-g-n_-a-l-l/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-a-s-s-i-g-n_-a-l-l/index.html">ASSIGN_ALL</a>

</span></code></pre></div>Requires that there exists an instantiation of the left and right type parameters such that the substituted left type is a subtype of the substituted right type.


</div>

## Companion properties
### entries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#entries">entries</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="o"><</span><a href="index.html">KaUnificationSubstitutorPolicy</a><span class="o">></span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#valueof"><span class="nf">valueOf</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaUnificationSubstitutorPolicy</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#values"><span class="nf">values</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="index.html">KaUnificationSubstitutorPolicy</a><span class="o">></span>
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
