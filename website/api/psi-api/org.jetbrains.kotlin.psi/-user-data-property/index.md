---
tags:
 - jvm
title: "UserDataProperty"
---

# UserDataProperty

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">UserDataProperty</a><span class="o"><</span><span class="kd">in </span><a href="index.html">R</a><span class="o"> : </span>UserDataHolder<span class="p">, </span><a href="index.html">T</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">(</span><span class="kd">val </span>key<span class="o">: </span>Key<span class="o"><</span><a href="index.html">T</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>A property delegate that reads and writes a value stored in a UserDataHolder under the given [`key`](index.md#key).

It lets user data — the platform's mechanism for attaching arbitrary values to a UserDataHolder such as a PSI element — be accessed as an ordinary, type-safe (nullable) Kotlin property.

### Example:
```kotlin
private val KEY = Key.create<Boolean>("MY_FLAG")
var PsiElement.myFlag: Boolean? by UserDataProperty(KEY)
```

#### Type Parameters


 - R: the type of user-data holder this property applies to


 - T: the type of the stored value





</div>

## Constructors
### UserDataProperty

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>key<span class="o">: </span>Key<span class="o"><</span><a href="index.html">T</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

**Type Parameters**



 - R: the type of user-data holder this property applies to


 - T: the type of the stored value





</div>

</div>
## Properties
### key

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#key">key</a><span class="o">: </span>Key<span class="o"><</span><a href="index.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
## Functions
### getValue

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">operator </span><span class="kd">fun </span><a href="index.html#getvalue"><span class="nf">getValue</span></a><span class="p">(</span>thisRef<span class="o">: </span><a href="index.html">R</a><span class="p">, </span>desc<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/-k-property/index.html">KProperty</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="index.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Reads the value stored under [`key`](index.md#key) on [`thisRef`](index.md#getvalue), or `null` if none is set.


</div>

</div>
### setValue

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">operator </span><span class="kd">fun </span><a href="index.html#setvalue"><span class="nf">setValue</span></a><span class="p">(</span>
    thisRef<span class="o">: </span><a href="index.html">R</a><span class="p">, </span>
    desc<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/-k-property/index.html">KProperty</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="p">, </span>
    value<span class="o">: </span><a href="index.html">T</a><span class="o">?</span>
<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Stores [`value`](index.md#setvalue) under [`key`](index.md#key) on [`thisRef`](index.md#setvalue) (or removes it when [`value`](index.md#setvalue) is `null`).


</div>

</div>
