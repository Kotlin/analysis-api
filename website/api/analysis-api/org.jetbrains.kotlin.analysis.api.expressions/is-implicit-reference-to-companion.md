---
tags:
 - jvm
title: "isImplicitReferenceToCompanion"
---

# isImplicitReferenceToCompanion

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="is-implicit-reference-to-companion.html">isImplicitReferenceToCompanion</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks if the [`KtSimpleNameExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.md) is an implicit reference to a companion object via the containing class.

#### Example
```
class A {
   companion object {
      fun foo() {}
   }
}
```

Given a call `A.foo()`, `A` is an implicit reference to the companion object, so `isImplicitReferenceToCompanion` returns `true`.


</div>

</div>
