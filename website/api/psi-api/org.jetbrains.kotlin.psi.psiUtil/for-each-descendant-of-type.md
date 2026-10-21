---
tags:
 - jvm
title: "forEachDescendantOfType"
---

# forEachDescendantOfType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="for-each-descendant-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="for-each-descendant-of-type.html"><span class="nf">forEachDescendantOfType</span></a><span class="p">(</span><span class="kd">noinline </span>action<span class="o">: </span><span class="p">(</span><a href="for-each-descendant-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Applies [`action`](for-each-descendant-of-type.md) to this element and every descendant of type [`T`](for-each-descendant-of-type.md), in post-order (children before parents).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="for-each-descendant-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="for-each-descendant-of-type.html"><span class="nf">forEachDescendantOfType</span></a><span class="p">(</span><span class="kd">crossinline </span>canGoInside<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span><span class="kd">noinline </span>action<span class="o">: </span><span class="p">(</span><a href="for-each-descendant-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Applies [`action`](for-each-descendant-of-type.md) to this element and every descendant of type [`T`](for-each-descendant-of-type.md), in post-order. [`canGoInside`](for-each-descendant-of-type.md) controls whether each visited element's children are traversed; the element itself is still passed to [`action`](for-each-descendant-of-type.md) when it is a [`T`](for-each-descendant-of-type.md), even if [`canGoInside`](for-each-descendant-of-type.md) returns `false` for it.

### Example:
Given `outerClass` representing:

```kotlin
class Outer {
    class Inner
}
```

The receiver participates in both traversal orders:

```kotlin
val postOrder = mutableListOf<String>()
outerClass.forEachDescendantOfType<KtClass> { postOrder += it.name.orEmpty() }
check(postOrder == listOf("Inner", "Outer"))

val preOrder = mutableListOf<String>()
outerClass.forEachDescendantOfTypeInPreorder<KtClass> { preOrder += it.name.orEmpty() }
check(preOrder == listOf("Outer", "Inner"))
```

Returning `false` from [`canGoInside`](for-each-descendant-of-type.md) prevents traversal into the element's children, but does not prevent the element itself from being passed to [`action`](for-each-descendant-of-type.md):

```kotlin
val pruned = mutableListOf<String>()
outerClass.forEachDescendantOfType<KtClass>(
    canGoInside = { it !== outerClass },
    action = { pruned += it.name.orEmpty() },
)
check(pruned == listOf("Outer"))
```


</div>

</div>
