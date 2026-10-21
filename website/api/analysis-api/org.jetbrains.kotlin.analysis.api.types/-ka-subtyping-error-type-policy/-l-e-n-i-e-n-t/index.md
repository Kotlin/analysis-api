---
tags:
 - jvm
title: "LENIENT"
---

# LENIENT

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="index.html">LENIENT</a>

</span></code></pre></div>Error types are equal to and subtypes of all types.

[`LENIENT`](index.md) should be chosen if type errors are expected and should be treated as type holes that can be satisfied by any other type. However, caution should be applied when using [`LENIENT`](index.md), as the policy can swallow type errors which should have been dealt with explicitly. In most cases, explicit type error handling should be preferred.

As a motivating example, consider that we want to find all functions which can be called with an argument of a certain type and show them to a user. The user has provided a type `List<>` with an unspecified type argument, which translates to `List<ERROR>`. We still want to show functions like `foo(list: List<Int>)`, as the user hasn't filled out the type argument yet. With the [`LENIENT`](index.md) policy, `List<ERROR>` is a subtype of `List<Int>`, meaning that `foo(list: List<Int>)` is a valid candidate for our purposes.


</div>

## Properties
### [`name`](../../-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`ordinal`](../../-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md#ordinal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.html#ordinal">ordinal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
