---
tags:
 - jvm
title: "KaSymbolLocation"
---

# KaSymbolLocation

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="index.html">KaSymbolLocation</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="index.html">KaSymbolLocation</a><span class="o">> </span>
</span></code></pre></div>Describes the location where a [`KaSymbol`](../-ka-symbol/index.md) is declared in code.

#### Example
```kotlin
package my.pack // TOP_LEVEL

class TopLevelClass { // TOP_LEVEL
  class NestedClass { // CLASS
    fun memberFunction() { // CLASS
      val foo = 4 // LOCAL
    }
  }
}

val topLevelProperty: Int // TOP_LEVEL
  get() = 0 // PROPERTY

fun topLevelFunction() { // TOP_LEVEL
  class LocalClass { // LOCAL
    val memberProperty = 0 // CLASS

    fun memberFunction() { // CLASS
      fun localFunction() {} // LOCAL
    }
  }
}
```


</div>

## Entries
### [`TOP_LEVEL`](-t-o-p_-l-e-v-e-l/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-t-o-p_-l-e-v-e-l/index.html">TOP_LEVEL</a>

</span></code></pre></div>Symbols which are not a part of other symbols.


</div>

### [`CLASS`](-c-l-a-s-s/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-c-l-a-s-s/index.html">CLASS</a>

</span></code></pre></div>Symbols which are a part of a [`KaClassSymbol`](../-ka-class-symbol/index.md).


</div>

### [`PROPERTY`](-p-r-o-p-e-r-t-y/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-p-r-o-p-e-r-t-y/index.html">PROPERTY</a>

</span></code></pre></div>Symbols which are a part of a [`KaPropertySymbol`](../-ka-property-symbol/index.md), such as [`KaPropertyAccessorSymbol`](../-ka-property-accessor-symbol/index.md) and [`KaBackingFieldSymbol`](../-ka-backing-field-symbol/index.md).


</div>

### [`LOCAL`](-l-o-c-a-l/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-l-o-c-a-l/index.html">LOCAL</a>

</span></code></pre></div>Symbols which are defined directly inside a body.


</div>

## Companion properties
### entries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#entries">entries</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="o"><</span><a href="index.html">KaSymbolLocation</a><span class="o">></span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#valueof"><span class="nf">valueOf</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaSymbolLocation</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#values"><span class="nf">values</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="index.html">KaSymbolLocation</a><span class="o">></span>
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
