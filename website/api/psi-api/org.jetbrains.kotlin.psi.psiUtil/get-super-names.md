---
tags:
 - jvm
title: "getSuperNames"
---

# getSuperNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>StubBasedPsiElementBase<span class="o"><</span><span class="kd">out </span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-class-or-object-stub/index.html">KotlinClassOrObjectStub</a><span class="o"><</span><span class="kd">out </span><a href="../org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="o">></span><span class="o">></span><span class="p">.</span><a href="get-super-names.html"><span class="nf">getSuperNames</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the unqualified names indexed as this class's superclass names. For names that might be imported through an alias, this includes both the original and aliased names; reference resolution during inheritor search disambiguates them.

### Example:
Given `derivedClass` representing:

```kotlin
import library.Base as Alias

class Derived : Alias
```

`derivedClass.getSuperNames()` returns `listOf("Alias", "Base")`.

#### Return
the list of possible superclass names


</div>

</div>
