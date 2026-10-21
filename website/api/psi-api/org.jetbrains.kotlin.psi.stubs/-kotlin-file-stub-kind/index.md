---
tags:
 - jvm
title: "KotlinFileStubKind"
---

# KotlinFileStubKind

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">KotlinFileStubKind</a>
</span></code></pre></div>Represents different kinds of Kotlin file stubs.

The file can be:

 - [`file`](-with-package/-file/index.md)


 - [`script`](-with-package/-script/index.md)


 - [`facade`](-with-package/-facade/-simple/index.md)


 - [`multifile class`](-with-package/-facade/-multifile-class/index.md)


 - [`invalid`](-invalid/index.md)


#### Inheritors


 - [`WithPackage`](-with-package/index.md)
 - [`Invalid`](-invalid/index.md)



</div>

## Types
### [`Invalid`](-invalid/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.psi/-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-invalid/index.html">Invalid</a> : <a href="index.html">KotlinFileStubKind</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an invalid Kotlin file stub.


</div>

</div>
### [`WithPackage`](-with-package/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-with-package/index.html">WithPackage</a> : <a href="index.html">KotlinFileStubKind</a>
</span></code></pre></div>
</div>


<div markdown>

A file that can hold a package.


</div>

</div>
