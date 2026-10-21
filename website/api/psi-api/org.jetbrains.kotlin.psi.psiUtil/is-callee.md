---
tags:
 - jvm
title: "isCallee"
---

# isCallee

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="is-callee.html"><span class="nf">isCallee</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this expression can be the callee of a call with the same name.

For example, `foo` is a callee in both `foo()` and `foo(args)`, the `+` operator reference is a callee in `a + b`, and the type name is a callee in a constructor call such as `Foo()`.

By contrast, `this` in `this(args)` is not considered a callee, and `name` in `name++` is not considered a callee either.


</div>

</div>
