---
tags:
 - jvm
title: "effectiveDeclarations"
---

# effectiveDeclarations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">.</span><a href="effective-declarations.html"><span class="nf">effectiveDeclarations</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the body declarations of this class or object in source order, followed by the class's primary-constructor `val`/`var` property parameters in parameter order.

### Example:
Given `accountClass` representing:

```kotlin
class Account(val id: Int, name: String) {
    fun save() {}
}
```

`accountClass.effectiveDeclarations().mapNotNull { it.name }` returns `listOf("save", "id")`: `id` is included because it declares a property, while the ordinary constructor parameter `name` is not.


</div>

</div>
