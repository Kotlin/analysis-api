---
tags:
 - jvm
title: "KotlinPackageProvider"
---

# KotlinPackageProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinPackageProvider</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-composable-provider/index.html">KotlinComposableProvider</a>
</span></code></pre></div>[`KotlinPackageProvider`](index.md) provides information about packages that are visible to Kotlin in a certain context. The provider covers not only packages with Kotlin declarations, but also packages with declarations that match a specified TargetPlatform. For example, packages with Java declarations on the JVM platform.

Package providers usually don't cover the whole project, but rather a restricted context. This usually means being limited to a specific scope, but the details depend on the kind of package provider.

The main kind of package providers is created via [`KotlinPackageProviderFactory`](../-kotlin-package-provider-factory/index.md) and it is scope-based, but there are other kinds of package providers, such as those created by [`KotlinForwardDeclarationsPackageProviderFactory`](../-kotlin-forward-declarations-package-provider-factory/index.md).

Package providers are critical for performance, so implementations should cache results.

### Lifetime
[`KotlinPackageProvider`](index.md) has the same lifetime guarantees as [`KotlinDeclarationProvider`](../../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-declaration-provider/index.md).

#### Inheritors


 - [`KotlinCompositePackageProvider`](../-kotlin-composite-package-provider/index.md)
 - [`KotlinEmptyPackageProvider`](../-kotlin-empty-package-provider/index.md)
 - [`KotlinPackageProviderBase`](../-kotlin-package-provider-base/index.md)



</div>

## Functions
### doesKotlinOnlyPackageExist

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-kotlin-package-provider-base/index.html#doeskotlinonlypackageexist"><span class="nf">doesKotlinOnlyPackageExist</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#doespackageexist"><span class="nf">doesPackageExist</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">, </span>platform<span class="o">: </span>TargetPlatform<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks if a package named [`packageFqName`](index.md#doespackageexist) exists in the context of the given [`platform`](index.md#doespackageexist). This includes Kotlin packages as well as [`platform`](index.md#doespackageexist)-specific packages.

Generally, the result is equal to: [`doesKotlinOnlyPackageExist`](../-kotlin-package-provider-base/index.md#doeskotlinonlypackageexist) || [`doesPlatformSpecificPackageExist`](index.md#doesplatformspecificpackageexist).


</div>

</div>
### doesPlatformSpecificPackageExist

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#doesplatformspecificpackageexist"><span class="nf">doesPlatformSpecificPackageExist</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">, </span>platform<span class="o">: </span>TargetPlatform<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks if a package named [`packageFqName`](index.md#doesplatformspecificpackageexist) exists. The package should contain [`platform`](index.md#doesplatformspecificpackageexist)-specific declarations.


</div>

</div>
### getKotlinOnlySubpackageNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-kotlin-package-provider-base/index.html#getkotlinonlysubpackagenames"><span class="nf">getKotlinOnlySubpackageNames</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the list of subpackages of a given package which contain Kotlin declarations.


</div>

</div>
### getPlatformSpecificSubpackageNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getplatformspecificsubpackagenames"><span class="nf">getPlatformSpecificSubpackageNames</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">, </span>platform<span class="o">: </span>TargetPlatform<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the list of subpackages of a given package which contain [`platform`](index.md#getplatformspecificsubpackagenames)-specific declarations.


</div>

</div>
### getSubpackageNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getsubpackagenames"><span class="nf">getSubpackageNames</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">, </span>platform<span class="o">: </span>TargetPlatform<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the list of subpackages of a given package.

The returned subpackage list contains both Kotlin and [`platform`](index.md#getsubpackagenames)-specific subpackages (e.g., for Kotlin/JVM, it should include Java packages).

Generally, the result is equal to: [`getKotlinOnlySubpackageNames`](../-kotlin-package-provider-base/index.md#getkotlinonlysubpackagenames) union [`getPlatformSpecificSubpackageNames`](index.md#getplatformspecificsubpackagenames).


</div>

</div>
