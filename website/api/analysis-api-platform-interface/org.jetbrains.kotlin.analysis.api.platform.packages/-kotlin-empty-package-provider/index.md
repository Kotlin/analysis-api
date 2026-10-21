---
tags:
 - jvm
title: "KotlinEmptyPackageProvider"
---

# KotlinEmptyPackageProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">KotlinEmptyPackageProvider</a> : <a href="../-kotlin-package-provider/index.html">KotlinPackageProvider</a>
</span></code></pre></div>
</div>

## Functions
### doesKotlinOnlyPackageExist

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#doeskotlinonlypackageexist"><span class="nf">doesKotlinOnlyPackageExist</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks if a package named [`packageFqName`](../-kotlin-package-provider-base/index.md#doeskotlinonlypackageexist) exists. The package should contain Kotlin declarations.

Note that for Kotlin, a package doesn't need to correspond to a directory structure like in Java. So, a file's package FqName is determined by the `package` directive.


</div>

</div>
### doesPackageExist

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#doespackageexist"><span class="nf">doesPackageExist</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">, </span>platform<span class="o">: </span>TargetPlatform<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks if a package named [`packageFqName`](../-kotlin-package-provider/index.md#doespackageexist) exists in the context of the given [`platform`](../-kotlin-package-provider/index.md#doespackageexist). This includes Kotlin packages as well as [`platform`](../-kotlin-package-provider/index.md#doespackageexist)-specific packages.

Generally, the result is equal to: [`doesKotlinOnlyPackageExist`](../-kotlin-package-provider-base/index.md#doeskotlinonlypackageexist) || [`doesPlatformSpecificPackageExist`](../-kotlin-package-provider/index.md#doesplatformspecificpackageexist).


</div>

</div>
### doesPlatformSpecificPackageExist

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#doesplatformspecificpackageexist"><span class="nf">doesPlatformSpecificPackageExist</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">, </span>platform<span class="o">: </span>TargetPlatform<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks if a package named [`packageFqName`](../-kotlin-package-provider/index.md#doesplatformspecificpackageexist) exists. The package should contain [`platform`](../-kotlin-package-provider/index.md#doesplatformspecificpackageexist)-specific declarations.


</div>

</div>
### getKotlinOnlySubpackageNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getkotlinonlysubpackagenames"><span class="nf">getKotlinOnlySubpackageNames</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the list of subpackages of a given package which contain Kotlin declarations.


</div>

</div>
### getPlatformSpecificSubpackageNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getplatformspecificsubpackagenames"><span class="nf">getPlatformSpecificSubpackageNames</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">, </span>platform<span class="o">: </span>TargetPlatform<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the list of subpackages of a given package which contain [`platform`](../-kotlin-package-provider/index.md#getplatformspecificsubpackagenames)-specific declarations.


</div>

</div>
### getSubpackageNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getsubpackagenames"><span class="nf">getSubpackageNames</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">, </span>platform<span class="o">: </span>TargetPlatform<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the list of subpackages of a given package.

The returned subpackage list contains both Kotlin and [`platform`](../-kotlin-package-provider/index.md#getsubpackagenames)-specific subpackages (e.g., for Kotlin/JVM, it should include Java packages).

Generally, the result is equal to: [`getKotlinOnlySubpackageNames`](../-kotlin-package-provider-base/index.md#getkotlinonlysubpackagenames) union [`getPlatformSpecificSubpackageNames`](../-kotlin-package-provider/index.md#getplatformspecificsubpackagenames).


</div>

</div>
