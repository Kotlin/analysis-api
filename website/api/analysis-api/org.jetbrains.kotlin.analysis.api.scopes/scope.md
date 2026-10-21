---
tags:
 - jvm
title: "scope"
---

# scope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="scope.html">scope</a><span class="o">: </span><a href="-ka-type-scope/index.html">KaTypeScope</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeScope`](-ka-type-scope/index.md) for the given [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md), or `null` if the type is [`erroneous`](../org.jetbrains.kotlin.analysis.api.types/-ka-error-type/index.md). The scope includes all members which are callable on a given type. It also includes [synthetic Java properties](https://kotlinlang.org/docs/java-interop.html#getters-and-setters).

Comparing to [`KaScope`](-ka-scope/index.md), the [`KaTypeScope`](-ka-type-scope/index.md) contains members whose use-site type parameters have been substituted.

#### Example
```kotlin
fun foo(list: List<String>) {
    list
}
```

We can get a [`KaTypeScope`](-ka-type-scope/index.md) for the [`expression type`](../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.md#expressiontype) of `list`. This scope contains a `get(index: Int): String` function, where the return type `E` from [`List.get`](../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-list/index.md#get) is substituted with the type argument `String`.

#### See also


 - [`KaTypeScope`](-ka-type-scope/index.md)
 - [`KaTypeProvider.type`](../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#type)
 - [`KaExpressionTypeProvider.expressionType`](../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.md#expressiontype)



</div>

</div>
