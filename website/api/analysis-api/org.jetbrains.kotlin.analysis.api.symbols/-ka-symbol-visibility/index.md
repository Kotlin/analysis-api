---
tags:
 - jvm
title: "KaSymbolVisibility"
---

# KaSymbolVisibility

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="index.html">KaSymbolVisibility</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="index.html">KaSymbolVisibility</a><span class="o">> </span>
</span></code></pre></div>The [visibility](https://kotlinlang.org/docs/visibility-modifiers.html) of a [`KaSymbol`](../-ka-symbol/index.md). As symbols can represent both Kotlin and Java declarations, [`KaSymbolVisibility`](index.md) covers both visibility definitions.

The entry order does not carry any particular meaning. If you need to sort declarations based on their visibility, use a custom comparator.

In addition, the following articles contain information about how visibility is affected by Kotlin and Java interoperability:

 - [Calling Java from Kotlin](https://kotlinlang.org/docs/java-interop.html)


 - [Calling Kotlin from Java](https://kotlinlang.org/docs/java-to-kotlin-interop.html#visibility)



</div>

## Entries
### [`PUBLIC`](-p-u-b-l-i-c/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-p-u-b-l-i-c/index.html">PUBLIC</a>

</span></code></pre></div>A public declaration is visible everywhere. This is the default visibility in Kotlin.


</div>

### [`PROTECTED`](-p-r-o-t-e-c-t-e-d/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-p-r-o-t-e-c-t-e-d/index.html">PROTECTED</a>

</span></code></pre></div>A protected declaration is visible inside its containing declaration and all its members, as well as in subclasses.


</div>

### [`INTERNAL`](-i-n-t-e-r-n-a-l/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-i-n-t-e-r-n-a-l/index.html">INTERNAL</a>

</span></code></pre></div>An internal declaration is visible everywhere in the same module. If the declaration is a class member, the class must also be visible for the internal member to be visible.


</div>

### [`PACKAGE_PROTECTED`](-p-a-c-k-a-g-e_-p-r-o-t-e-c-t-e-d/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-p-a-c-k-a-g-e_-p-r-o-t-e-c-t-e-d/index.html">PACKAGE_PROTECTED</a>

</span></code></pre></div>A package-protected Java declaration is visible in its class, package, and in all subclasses (even outside the package).


</div>

### [`PACKAGE_PRIVATE`](-p-a-c-k-a-g-e_-p-r-i-v-a-t-e/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-p-a-c-k-a-g-e_-p-r-i-v-a-t-e/index.html">PACKAGE_PRIVATE</a>

</span></code></pre></div>A package-private Java declaration is visible in its class and package. This is the default visibility in Java.


</div>

### [`PRIVATE`](-p-r-i-v-a-t-e/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-p-r-i-v-a-t-e/index.html">PRIVATE</a>

</span></code></pre></div>A private declaration is visible inside its containing declaration and all its members, or inside the whole file if the declaration is top-level.


</div>

### [`LOCAL`](-l-o-c-a-l/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-l-o-c-a-l/index.html">LOCAL</a>

</span></code></pre></div>The visibility of local declarations.


</div>

### [`UNKNOWN`](-u-n-k-n-o-w-n/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-u-n-k-n-o-w-n/index.html">UNKNOWN</a>

</span></code></pre></div>An unknown visibility, for example in the case of erroneous code where it is impossible to infer the proper visibility.


</div>

## Companion properties
### entries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#entries">entries</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="o"><</span><a href="index.html">KaSymbolVisibility</a><span class="o">></span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#valueof"><span class="nf">valueOf</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaSymbolVisibility</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#values"><span class="nf">values</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="index.html">KaSymbolVisibility</a><span class="o">></span>
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
