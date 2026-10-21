---
tags:
 - jvm
title: "MultifileClass"
---

# MultifileClass

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../../../org.jetbrains.kotlin.psi/-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">MultifileClass</a> : <a href="../index.html">KotlinFileStubKind.WithPackage.Facade</a>
</span></code></pre></div>Represents a multi-file class facade.

#### See also


 - [`JvmMultifileClass`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-multifile-class/index.html)



</div>

## Properties
### facadeFqName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#facadefqname">facadeFqName</a><span class="o">: </span>FqName
</span></code></pre></div>
</div>


<div markdown>

The file facade class as FqName.

**Example**

`foo.kt`:

```kotlin
package com.example

fun baz() {}
```

Results to `com.example.FooKt`.

`foo.kt`:

```kotlin
@file:JvmName("Doo")
package com.example

fun baz() {}
```

Results to `com.example.Doo`.

`foo.kt`:

```kotlin
@file:JvmName("Doo")
@file:JvmPackageName("another.pack")
package com.example

fun baz() {}
```

Results to `another.pack.Doo`.


</div>

</div>
### facadePartSimpleNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#facadepartsimplenames">facadePartSimpleNames</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A simple names list of all the parts that are associated with a multi-file class facade. Simple names represent the unqualified names of each facade part.

**Example**

`MultifileClass.kt`:

```kotlin
@file:[JvmName("MultifileClass") JvmMultifileClass]
package test

fun p1Fun() {}
```

`SecondPart.kt`:

```kotlin
@file:[JvmName("MultifileClass") JvmMultifileClass]
package test

fun p2Fun() {}
```

[`facadeFqName`](index.md#facadefqname) is `test.MultifileClassKt`, [`facadePartSimpleNames`](index.md#facadepartsimplenames) is `["MultifileClass__MultifileClassKt", "MultifileClass__SecondPartKt"]`.


</div>

</div>
### packageFqName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#packagefqname">packageFqName</a><span class="o">: </span>FqName
</span></code></pre></div>
</div>


<div markdown>

The file package as FqName.

FqName.ROOT is used if the file has no explicit package.


</div>

</div>
