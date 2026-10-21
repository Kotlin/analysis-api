---
tags:
 - jvm
title: "createInheritanceTypeSubstitutor"
---

# createInheritanceTypeSubstitutor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="create-inheritance-type-substitutor.html"><span class="nf">createInheritanceTypeSubstitutor</span></a><span class="p">(</span>subClass<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">, </span>superClass<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="-ka-substitutor/index.html">KaSubstitutor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](-ka-substitutor/index.md) based on the inheritance relationship between [`subClass`](create-inheritance-type-substitutor.md) and [`superClass`](create-inheritance-type-substitutor.md). [`subClass`](create-inheritance-type-substitutor.md) must inherit from [`superClass`](create-inheritance-type-substitutor.md) and there may not be any error types in the inheritance path. Otherwise, `null` is returned.

The semantics of the resulting [`KaSubstitutor`](-ka-substitutor/index.md) are as follows: When applied to a member of [`superClass`](create-inheritance-type-substitutor.md), such as a function, its type parameters are substituted in such a way that the resulting member can be used with an instance of [`subClass`](create-inheritance-type-substitutor.md).

In other words, the substitutor is a composition of inheritance-based substitutions incorporating the whole inheritance chain.

#### Example
```
class A : B<String>
class B<T> : C<T, Int>
class C<X, Y>
```

 - `createInheritanceTypeSubstitutor(A, B)` returns `KaSubstitutor { T -> String }`


 - `createInheritanceTypeSubstitutor(B, C)` returns `KaSubstitutor { X -> T, Y -> Int }`


 - `createInheritanceTypeSubstitutor(A, C)` returns `KaSubstitutor { X -> T, Y -> Int } and then KaSubstitutor { T -> String }`



</div>

</div>
