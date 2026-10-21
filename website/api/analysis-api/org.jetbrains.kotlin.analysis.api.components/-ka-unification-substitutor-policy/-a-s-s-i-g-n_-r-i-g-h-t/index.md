---
tags:
 - jvm
title: "ASSIGN_RIGHT"
---

# ASSIGN_RIGHT

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="index.html">ASSIGN_RIGHT</a>

</span></code></pre></div>Requires that there exists an instantiation of the right type parameters such that the right type is a supertype of the left type when substituted. Type parameters of the left type are treated as fixed.

The constructed substitutor contains mappings for all type parameters of the right type such that the substituted right type is a supertype of the left type. If a correct instantiation doesn't exist, no substitutor is produced.

### Examples:
```kotlin
fun <T: Number> example(leftType: T, rightType: Number) {}
```

`T: Number` is always a subtype of `Number` with any possible instantiation of `T`. The [`ASSIGN_RIGHT`](index.md) unification substitutor here is empty as the right type doesn't have any type parameters.

```kotlin
fun <T: Int, R: Number> example(leftType: List<T>, rightType: List<R>) {}
```

The [`ASSIGN_RIGHT`](index.md) unification substitutor here is `{ R -> T }`.

```kotlin
fun <T, R: Int> example(leftType: List<T>, rightType: List<R>) {}
```

Since `List<T>` is not guaranteed to be a subtype of `List<R>` for all possible instantiations of `T` (consider `{ T -> kotlin/Number }`), [`ASSIGN_RIGHT`](index.md) unification fails and no substitutor is constructed.


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
