---
tags:
 - jvm
title: "WithPackage"
---

# WithPackage

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">WithPackage</a> : <a href="../index.html">KotlinFileStubKind</a>
</span></code></pre></div>A file that can hold a package.

#### Inheritors


 - [`File`](-file/index.md)
 - [`Script`](-script/index.md)
 - [`Facade`](-facade/index.md)



</div>

## Types
### [`Facade`](-facade/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-facade/index.html">Facade</a> : <a href="index.html">KotlinFileStubKind.WithPackage</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a file facade.


</div>

</div>
### [`File`](-file/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../org.jetbrains.kotlin.psi/-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-file/index.html">File</a> : <a href="index.html">KotlinFileStubKind.WithPackage</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a file that is a regular file.


</div>

</div>
### [`Script`](-script/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../org.jetbrains.kotlin.psi/-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-script/index.html">Script</a> : <a href="index.html">KotlinFileStubKind.WithPackage</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a file that is a script.


</div>

</div>
## Properties
### packageFqName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="-facade/-multifile-class/index.html#packagefqname">packageFqName</a><span class="o">: </span>FqName
</span></code></pre></div>
</div>


<div markdown>

The file package as FqName.

FqName.ROOT is used if the file has no explicit package.


</div>

</div>
