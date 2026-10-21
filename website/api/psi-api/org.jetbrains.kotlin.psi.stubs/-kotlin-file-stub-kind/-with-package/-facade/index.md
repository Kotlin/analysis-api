---
tags:
 - jvm
title: "Facade"
---

# Facade

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">Facade</a> : <a href="../index.html">KotlinFileStubKind.WithPackage</a>
</span></code></pre></div>Represents a file facade.

<strong>Note</strong>: [`packageFqName`](-multifile-class/index.md#packagefqname) might be not the same as FqName.parent on [`facadeFqName`](-multifile-class/index.md#facadefqname) due to [`JvmPackageName`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-package-name/index.html).

See [Package-level functions](https://kotlinlang.org/docs/java-to-kotlin-interop.html#package-level-functions).

#### Inheritors


 - [`Simple`](-simple/index.md)
 - [`MultifileClass`](-multifile-class/index.md)



</div>

## Types
### [`MultifileClass`](-multifile-class/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../../org.jetbrains.kotlin.psi/-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-multifile-class/index.html">MultifileClass</a> : <a href="index.html">KotlinFileStubKind.WithPackage.Facade</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a multi-file class facade.


</div>

</div>
### [`Simple`](-simple/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../../org.jetbrains.kotlin.psi/-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-simple/index.html">Simple</a> : <a href="index.html">KotlinFileStubKind.WithPackage.Facade</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a simple class facade.


</div>

</div>
## Properties
### facadeFqName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="-multifile-class/index.html#facadefqname">facadeFqName</a><span class="o">: </span>FqName
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
### packageFqName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="-multifile-class/index.html#packagefqname">packageFqName</a><span class="o">: </span>FqName
</span></code></pre></div>
</div>


<div markdown>

The file package as FqName.

FqName.ROOT is used if the file has no explicit package.


</div>

</div>
