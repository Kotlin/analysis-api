---
tags:
 - jvm
title: "KotlinDirectInheritorsProvider"
---

# KotlinDirectInheritorsProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinDirectInheritorsProvider</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Functions
### getDirectKotlinInheritors

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getdirectkotlininheritors"><span class="nf">getDirectKotlinInheritors</span></a><span class="p">(</span>
    ktClass<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-class/index.html">KtClass</a><span class="p">, </span>
    scope<span class="o">: </span>GlobalSearchScope<span class="p">, </span>
    includeLocalInheritors<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span>
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/index.html">Iterable</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all direct Kotlin inheritors of [`ktClass`](index.md#getdirectkotlininheritors) that can be found in the given [`scope`](index.md#getdirectkotlininheritors).

[`ktClass`](index.md#getdirectkotlininheritors) must not be a class from a dangling file, but rather should be a class from a physical source, like a source module. The scope should cover the [`ktClass`](index.md#getdirectkotlininheritors) itself. In case inheritors for a dangling class are needed, [`getDirectKotlinInheritors`](index.md#getdirectkotlininheritors) should be called with the same class from a non-dangling context module. This removes the burden of handling dangling files from the provider, simplifying its implementation.

The implementation of [`getDirectKotlinInheritors`](index.md#getdirectkotlininheritors) is allowed to lazy-resolve symbols up to the `SUPER_TYPES` phase. This is required to check subtyping for potential inheritors. Hence, if [`getDirectKotlinInheritors`](index.md#getdirectkotlininheritors) is invoked during lazy resolution, it requires a phase of `SEALED_CLASS_INHERITORS` or later.

**Parameters**



 - includeLocalInheritors: If `false`, only non-local inheritors will be searched and returned.





</div>

</div>
