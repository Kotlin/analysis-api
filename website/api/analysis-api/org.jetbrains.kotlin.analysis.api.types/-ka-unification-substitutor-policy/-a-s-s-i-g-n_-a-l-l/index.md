---
tags:
 - jvm
title: "ASSIGN_ALL"
---

# ASSIGN_ALL

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="index.html">ASSIGN_ALL</a>

</span></code></pre></div>Requires that there exists an instantiation of the left and right type parameters such that the substituted left type is a subtype of the substituted right type.

The constructed substitutor contains mappings for all type parameters of both the left type and the right type such that the substituted left type is a subtype of the substituted right type. If a correct instantiation doesn't exist, no substitutor is produced.

### Examples:
```kotlin
fun <A> rightTypes(rightType1: List<Int>, rightType2: List<A>) {}

fun <B> leftTypes(leftType1: List<B>, leftType2: List<Int>) {}
```

Both [`ASSIGN_RIGHT`](../-a-s-s-i-g-n_-r-i-g-h-t/index.md) and [`ASSIGN_LEFT`](../-a-s-s-i-g-n_-l-e-f-t/index.md) here return no substitutor, as these pairs are inverses of each other. However, [`ASSIGN_ALL`](index.md) is able to freely assign all type parameters, so `{ A -> kotlin/Int, B -> kotlin/Int }` is produced. With this substitution, both constraints are satisfied.


</div>

## Properties
### [`name`](index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`ordinal`](index.md#ordinal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#ordinal">ordinal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
