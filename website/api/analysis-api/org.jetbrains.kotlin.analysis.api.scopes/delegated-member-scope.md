---
tags:
 - jvm
title: "delegatedMemberScope"
---

# delegatedMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="delegated-member-scope.html">delegatedMemberScope</a><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](-ka-scope/index.md) containing synthetic callables (functions and properties) created by interface delegation.

#### Example
```kotlin
interface I {
    val foo: Int get() = 2
    fun bar(): String
}

class A(
    private val p: I
) : I by p {
    val regularProperty: Int = 5
}
```

The delegated member scope for `A` has the following entries:

```
override val foo: kotlin.Int
  get()

override fun bar(): kotlin.String
```

`regularProperty` is not contained in the delegated member scope because it is not a delegated property.


</div>

</div>
