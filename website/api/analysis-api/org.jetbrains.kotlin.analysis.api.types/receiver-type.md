---
tags:
 - jvm
title: "receiverType"
---

# receiverType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-double-colon-expression/index.html">KtDoubleColonExpression</a><span class="p">.</span><a href="receiver-type.html">receiverType</a><span class="o">: </span><a href="-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtDoubleColonExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-double-colon-expression/index.md) to the [`KaType`](-ka-type/index.md) of its receiver.

The result may be `null` if the resolution fails or the resolved callable reference is not a reflection type.

#### Example
```kotlin
class Foo {
    fun bar() { }
}

val foo = Foo()
foo::bar
```

Here, `receiverType` for `foo::bar` is `Foo` (the type of `foo`).


</div>

</div>
