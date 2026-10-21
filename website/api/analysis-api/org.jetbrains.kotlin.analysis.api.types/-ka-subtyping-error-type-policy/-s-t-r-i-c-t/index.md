---
tags:
 - jvm
title: "STRICT"
---

# STRICT

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="index.html">STRICT</a>

</span></code></pre></div>Error types are not considered equal to or subtypes of any other type.

[`STRICT`](index.md) is the default policy for the following reasons:

1. In general, considering an error type equal to all other types is unintuitive. It essentially turns error types into dynamic `Any`      or `Nothing` types (depending on the typing position). This can produce a lot of typing relationships which do not make any sense,      such as `Int = UnresolvedClass`.


1. It forces the user to handle error types explicitly, which reduces the risk of false positives.


1. It is consistent with most of the behavior of the Kotlin compiler.



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
