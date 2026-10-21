---
tags:
 - jvm
title: "BinaryOperationPrecedence"
---

# BinaryOperationPrecedence

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="index.html">BinaryOperationPrecedence</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="index.html">BinaryOperationPrecedence</a><span class="o">> </span>
</span></code></pre></div>The precedence levels of Kotlin's binary operators, ordered from the highest-binding ([`AS`](-a-s/index.md)) to the lowest-binding ([`ASSIGNMENT`](-a-s-s-i-g-n-m-e-n-t/index.md)).

[`higherPriority`](-a-s-s-i-g-n-m-e-n-t/index.md#higherpriority) links each level to the next tighter-binding one, and [`tokens`](-a-s-s-i-g-n-m-e-n-t/index.md#tokens) lists the operator tokens that belong to the level.


</div>

## Entries
### [`AS`](-a-s/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-a-s/index.html">AS</a>

</span></code></pre></div>The `as` and `as?` cast operators.


</div>

### [`MULTIPLICATIVE`](-m-u-l-t-i-p-l-i-c-a-t-i-v-e/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-m-u-l-t-i-p-l-i-c-a-t-i-v-e/index.html">MULTIPLICATIVE</a>

</span></code></pre></div>The multiplicative operators `*`, `/`, and `%`.


</div>

### [`ADDITIVE`](-a-d-d-i-t-i-v-e/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-a-d-d-i-t-i-v-e/index.html">ADDITIVE</a>

</span></code></pre></div>The additive operators `+` and `-`.


</div>

### [`RANGE`](-r-a-n-g-e/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-r-a-n-g-e/index.html">RANGE</a>

</span></code></pre></div>The range operators `..` and `..<`.


</div>

### [`INFIX`](-i-n-f-i-x/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-i-n-f-i-x/index.html">INFIX</a>

</span></code></pre></div>Infix function calls (an identifier used as an operator).


</div>

### [`ELVIS`](-e-l-v-i-s/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-e-l-v-i-s/index.html">ELVIS</a>

</span></code></pre></div>The elvis operator `?:`.


</div>

### [`IN_OR_IS`](-i-n_-o-r_-i-s/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-i-n_-o-r_-i-s/index.html">IN_OR_IS</a>

</span></code></pre></div>The `in`, `!in`, `is`, and `!is` operators.


</div>

### [`COMPARISON`](-c-o-m-p-a-r-i-s-o-n/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-c-o-m-p-a-r-i-s-o-n/index.html">COMPARISON</a>

</span></code></pre></div>The comparison operators `<`, `>`, `<=`, and `>=`.


</div>

### [`EQUALITY`](-e-q-u-a-l-i-t-y/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-e-q-u-a-l-i-t-y/index.html">EQUALITY</a>

</span></code></pre></div>The equality operators `==`, `!=`, `===`, and `!==`.


</div>

### [`CONJUNCTION`](-c-o-n-j-u-n-c-t-i-o-n/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-c-o-n-j-u-n-c-t-i-o-n/index.html">CONJUNCTION</a>

</span></code></pre></div>The conjunction operator `&&`.


</div>

### [`DISJUNCTION`](-d-i-s-j-u-n-c-t-i-o-n/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-d-i-s-j-u-n-c-t-i-o-n/index.html">DISJUNCTION</a>

</span></code></pre></div>The disjunction operator `||`.


</div>

### [`ASSIGNMENT`](-a-s-s-i-g-n-m-e-n-t/index.md)

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="-a-s-s-i-g-n-m-e-n-t/index.html">ASSIGNMENT</a>

</span></code></pre></div>The assignment operators `=`, `+=`, `-=`, `*=`, `/=`, and `%=`.


</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Companion properties
### entries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#entries">entries</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="o"><</span><a href="index.html">BinaryOperationPrecedence</a><span class="o">></span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#valueof"><span class="nf">valueOf</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">BinaryOperationPrecedence</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#values"><span class="nf">values</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="index.html">BinaryOperationPrecedence</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

The function returns a new instance of the array on every call. The array could be mutated, so working with it may also require defensive copying. Consider using `entries` property as a more efficient alternative returning an immutable list of enum entries.


</div>

</div>
## Properties
### higherPriority

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="-a-s-s-i-g-n-m-e-n-t/index.html#higherpriority">higherPriority</a><span class="o">: </span><a href="index.html">BinaryOperationPrecedence</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`name`](../../org.jetbrains.kotlin.psi.stubs/-constant-value-kind/-i-n-t-e-g-e-r_-c-o-n-s-t-a-n-t/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.psi.stubs/-constant-value-kind/-i-n-t-e-g-e-r_-c-o-n-s-t-a-n-t/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`ordinal`](../../org.jetbrains.kotlin.psi.stubs/-constant-value-kind/-i-n-t-e-g-e-r_-c-o-n-s-t-a-n-t/index.md#ordinal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.psi.stubs/-constant-value-kind/-i-n-t-e-g-e-r_-c-o-n-s-t-a-n-t/index.html#ordinal">ordinal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### tokens

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="-a-s-s-i-g-n-m-e-n-t/index.html#tokens">tokens</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="../../org.jetbrains.kotlin.lexer/-kt-token/index.html">KtToken</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### tokenSet

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="-a-s-s-i-g-n-m-e-n-t/index.html#tokenset">tokenSet</a><span class="o">: </span>TokenSet
</span></code></pre></div>
</div>


<div markdown>

The set of operator tokens that belong to this precedence level.


</div>

</div>
