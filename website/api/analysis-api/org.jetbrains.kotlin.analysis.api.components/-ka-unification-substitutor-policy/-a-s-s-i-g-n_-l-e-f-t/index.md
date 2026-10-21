---
tags:
 - jvm
title: "ASSIGN_LEFT"
---

# ASSIGN_LEFT

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="index.html">ASSIGN_LEFT</a>

</span></code></pre></div>Requires that there exists an instantiation of the left type parameters such that the left type is a subtype of the right type when substituted. Type parameters of the right type are treated as fixed.

The constructed substitutor contains mappings for all type parameters of the left type such that the substituted left type is a subtype of the right type. If a correct instantiation doesn't exist, no substitutor is produced.

### Examples:
```kotlin
interface A<T> : B<T>
interface B<T> : C<Int, T>
interface C<X, Y>

fun <K> test(leftType: A<K>, rightType: C<Int, String>) {}
```

The left type here is generic `A<K>` and the right type is a fixed supertype `C<Int, String>`. For this case, [`ASSIGN_LEFT`](index.md) will produce `{ K -> String }` as with such a substitution, `A<String>` is a subtype of `C<Int, String>`.

```kotlin
fun <T, R: Int> example(leftType: List<T>, rightType: List<R>) {}
```

[`ASSIGN_LEFT`](index.md) produces `{ T -> R }` mapping as with such a substitution, `List<T>` is a subtype of `List<R>`.

```kotlin
fun <T: Number> example(leftType: Number, rightType: T) {}
```

There are no free type parameters as the left type `Number` is concrete. `T` is not guaranteed to be exactly `Number` to satisfy the constraint (e.g., with `{ T -> kotlin/Int }`), so [`ASSIGN_LEFT`](index.md) produces no substitutor.


</div>

## Properties
### [`name`](../../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`ordinal`](../../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md#ordinal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.html#ordinal">ordinal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
