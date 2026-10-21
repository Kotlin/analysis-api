---
tags:
 - jvm
title: "KaLibraryModule"
---

# KaLibraryModule

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-platform-interface/index.html">KaPlatformInterface::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaLibraryModule</a> : <a href="../-ka-module/index.html">KaModule</a>
</span></code></pre></div>A module which represents a binary library, such as a JAR or KLIB.

### Dependencies
[`KaLibraryModule`](index.md)s can have their own dependencies (e.g. [`directRegularDependencies`](../-ka-not-under-content-root-module/index.md#directregulardependencies)). These dependencies are only relevant when the library is analyzed as a use-site module (e.g. its decompiled sources are viewed in the IDE). When the library module is used as a dependency of another module, its own dependencies are irrelevant.

The library module should either have the exact dependencies it was compiled with or, if unknown, a single [`KaLibraryFallbackDependenciesModule`](../-ka-library-fallback-dependencies-module/index.md).

### Platform-specific content scope restriction
The [`contentScope`](../-ka-not-under-content-root-module/index.md#contentscope) of the library module excludes file types that are harmful for the [`targetPlatform`](../-ka-not-under-content-root-module/index.md#targetplatform). For example, a JVM library module filters out `.kotlin_metadata` and `.knm` files, which excludes Kotlin declarations from non-JVM platforms. It also filters out source files.

While most proper library module setups don't need such filtering, there are both pathological as well as legitimate use cases in the wild. For example, certain Kotlin stdlib setups required both the `kotlin-stdlib` and `kotlin-stdlib-common` JARs to be part of the same [`KaLibraryModule`](index.md) (this has been fixed with 2.x stdlibs). Such a library module has the JVM target platform, and we need to exclude `.kotlin_metadata` files from the content scope.

As another example, a JVM library module might accidentally include source JARs in its binary roots. These sources must be excluded. Otherwise, the Analysis API might accidentally try to load library declarations from them.


</div>

## Properties
### baseContentScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-not-under-content-root-module/index.html#basecontentscope">baseContentScope</a><span class="o">: </span>GlobalSearchScope
</span></code></pre></div>
</div>


<div markdown>

A base content scope of the module, which is not yet refined by extension and restriction scopes provided by `KotlinContentScopeRefiner`.

Note that [`baseContentScope`](../-ka-not-under-content-root-module/index.md#basecontentscope) doesn't represent the actual content scope of the current module. To get a content scope of the module, [`contentScope`](../-ka-not-under-content-root-module/index.md#contentscope) should be used instead.


</div>

</div>
### baseContextModuleOrSelf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../-ka-not-under-content-root-module/index.html#basecontextmoduleorself">baseContextModuleOrSelf</a><span class="o">: </span><a href="../-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaModule`](../-ka-module/index.md)'s [`baseContextModule`](../-ka-dangling-file-module/index.md#basecontextmodule), or the module itself if it's not a [`KaDanglingFileModule`](../-ka-dangling-file-module/index.md).


</div>

</div>
### binaryRoots

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#binaryroots">binaryRoots</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/nio/file/Path.html">Path</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of binary roots which constitute the library. The list can contain JARs, KLIBs, folders with `.class` files, and so on.

The paths should be consistent with the [`contentScope`](../-ka-not-under-content-root-module/index.md#contentscope), so the following equivalence should hold:

```
library.contentScope.contains(file) <=> library.binaryRoots.listRecursively().contains(file)
```


</div>

</div>
### binaryVirtualFiles

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#binaryvirtualfiles">binaryVirtualFiles</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span>VirtualFile<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of binary roots which constitute the library, in VirtualFile form. Like [`binaryRoots`](index.md#binaryroots), the list can contain JARs, KLIBs, folders with `.class` files, and so on.

Originally, this property was only intended to cover libraries in an in-memory file system, whose roots cannot be represented as paths in [`binaryRoots`](index.md#binaryroots). However, not every disk-based binary root can be represented as a path either (e.g. roots in a JAR file system), so the Analysis API is moving towards virtual files as the canonical representation of binary roots (see [KT-72676](https://youtrack.jetbrains.com/issue/KT-72676)): [`binaryVirtualFiles`](index.md#binaryvirtualfiles) is to cover all binary roots, and [`binaryRoots`](index.md#binaryroots) will eventually change its return type to a collection of VirtualFiles (after a deprecation cycle), at which point this property will be removed. The IntelliJ platform implementation already exposes all binary roots through this property, while the Standalone platform currently exposes only in-memory roots, keeping disk-based roots in [`binaryRoots`](index.md#binaryroots).


</div>

</div>
### [`compilerPluginGeneratedDeclarations`](../../org.jetbrains.kotlin.analysis.api.compilerPlugins/compiler-plugin-generated-declarations.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.compilerPlugins/compiler-plugin-generated-declarations.html">compilerPluginGeneratedDeclarations</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.compilerPlugins/-ka-compiler-plugin-generated-declarations/index.html">KaCompilerPluginGeneratedDeclarations</a>
</span></code></pre></div>
</div>


<div markdown>

[`Declarations`](../../org.jetbrains.kotlin.analysis.api.compilerPlugins/-ka-compiler-plugin-generated-declarations/index.md) generated by compiler plugins for [`this`](../-ka-module/index.md) module, not including the generated declarations for dependencies of this module.


</div>

</div>
### contentScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-not-under-content-root-module/index.html#contentscope">contentScope</a><span class="o">: </span>GlobalSearchScope
</span></code></pre></div>
</div>


<div markdown>

Represents the content scope of a current module, i.e., a GlobalSearchScope which determines all the files that are contained in the module.

This scope should be lazily built from [`baseContentScope`](../-ka-not-under-content-root-module/index.md#basecontentscope) using `KotlinContentScopeRefiner` extension points.


</div>

</div>
### directDependsOnDependencies

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-not-under-content-root-module/index.html#directdependsondependencies">directDependsOnDependencies</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The module's [`dependsOn` dependencies](https://kotlinlang.org/api/kotlin-gradle-plugin/kotlin-gradle-plugin-api/org.jetbrains.kotlin.gradle.plugin/-kotlin-source-set/depends-on.html).

A `dependsOn` dependency expresses that the current module can provide `actual` declarations for `expect` declarations from the dependency module, as well as see internal symbols of the dependency module. As such, `dependsOn` dependencies are a Kotlin Multiplatform concept.

`dependsOn` dependencies in general are transitive, but the resulting list is not a transitive closure. To get all transitive `dependsOn` dependencies, [`transitiveDependsOnDependencies`](../-ka-not-under-content-root-module/index.md#transitivedependsondependencies) should be used. The list also does not include the current module.


</div>

</div>
### directFriendDependencies

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-not-under-content-root-module/index.html#directfrienddependencies">directFriendDependencies</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The module's friend dependencies. Friend dependencies allow the current module to use internal symbols from the dependency module.

The resulting list is not transitive and does not include the current module.


</div>

</div>
### directRegularDependencies

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-not-under-content-root-module/index.html#directregulardependencies">directRegularDependencies</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The module's regular dependencies. Regular dependencies allow the current module to use symbols from the dependency module.

The resulting list is not transitive and does not include the current module.


</div>

</div>
### isResolvable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../-ka-not-under-content-root-module/index.html#isresolvable">isResolvable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the given [`KaModule`](../-ka-module/index.md) can be the use-site module of an [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) call. A module which is not resolvable will be rejected by [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) with an exception.

All modules returned by [`KaModuleProvider.getModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module-provider/get-module.md) are guaranteed to be resolvable. By extension, all possible use-site PsiElements are also part of resolvable modules. As such, module resolvability is normally not a concern of an Analysis API user.


</div>

</div>
### isSdk

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#issdk">isSdk</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the module represents an SDK, such as the JDK.


</div>

</div>
### libraryName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#libraryname">libraryName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

The name of the library.

In practice, the specific format of the [`libraryName`](index.md#libraryname) depends on the Analysis API platform which provides the [`KaLibraryModule`](index.md) implementation.


</div>

</div>
### librarySources

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#librarysources">librarySources</a><span class="o">: </span><a href="../-ka-library-source-module/index.html">KaLibrarySourceModule</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The library sources for the binary library, if any.

For example, if this module is a binary JAR, then [`librarySources`](index.md#librarysources) corresponds to the sources JAR.


</div>

</div>
### moduleDescription

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#moduledescription">moduleDescription</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

A human-readable description of the module, such as "main sources of module 'analysis-api'".


</div>

</div>
### project

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-not-under-content-root-module/index.html#project">project</a><span class="o">: </span>Project
</span></code></pre></div>
</div>


<div markdown>

The Project to which the module belongs.

All the module's dependencies should belong to the same Project as the module itself.


</div>

</div>
### stableModuleName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../-ka-not-under-content-root-module/index.html#stablemodulename">stableModuleName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A stable binary name of module from the Kotlin point of view. Having a correct module name is critical for `internal`-visibility mangling.

NOTE: [`stableModuleName`](../-ka-not-under-content-root-module/index.md#stablemodulename) will be removed in the future and replaced with a platform interface service.


</div>

</div>
### targetPlatform

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-not-under-content-root-module/index.html#targetplatform">targetPlatform</a><span class="o">: </span>TargetPlatform
</span></code></pre></div>
</div>


<div markdown>

A platform which the module represents (e.g, JVM, JS, Native).

**See also**



 - TargetPlatform



</div>

</div>
### transitiveDependsOnDependencies

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-not-under-content-root-module/index.html#transitivedependsondependencies">transitiveDependsOnDependencies</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of [`directDependsOnDependencies`](../-ka-not-under-content-root-module/index.md#directdependsondependencies) and all of their own `dependsOn` dependencies (directly and indirectly), sorted topologically with the nearest dependencies first in the list. The list does not include the current module.


</div>

</div>
## Functions
### allDirectDependencies

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../-ka-not-under-content-root-module/index.html#alldirectdependencies"><span class="nf">allDirectDependencies</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of all modules that the given module directly depends on.

**See also**



 - [`KaModule.directRegularDependencies`](../-ka-not-under-content-root-module/index.md#directregulardependencies)
 - [`KaModule.directDependsOnDependencies`](../-ka-not-under-content-root-module/index.md#directdependsondependencies)
 - [`KaModule.directFriendDependencies`](../-ka-not-under-content-root-module/index.md#directfrienddependencies)



</div>

</div>
### allDirectDependenciesOfType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../-ka-not-under-content-root-module/index.html#alldirectdependenciesoftype">M</a><span class="o"> : </span><a href="../-ka-module/index.html">KaModule</a><span class="o">> </span><a href="../-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../-ka-not-under-content-root-module/index.html#alldirectdependenciesoftype"><span class="nf">allDirectDependenciesOfType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-ka-not-under-content-root-module/index.html#alldirectdependenciesoftype">M</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of all modules of type [`M`](../-ka-not-under-content-root-module/index.md#alldirectdependenciesoftype) that the given module directly depends on.

**See also**



 - [`KaModule.directRegularDependencies`](../-ka-not-under-content-root-module/index.md#directregulardependencies)
 - [`KaModule.directDependsOnDependencies`](../-ka-not-under-content-root-module/index.md#directdependsondependencies)
 - [`KaModule.directFriendDependencies`](../-ka-not-under-content-root-module/index.md#directfrienddependencies)



</div>

</div>
### directDependsOnDependenciesOfType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../-ka-not-under-content-root-module/index.html#directdependsondependenciesoftype">M</a><span class="o"> : </span><a href="../-ka-module/index.html">KaModule</a><span class="o">> </span><a href="../-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../-ka-not-under-content-root-module/index.html#directdependsondependenciesoftype"><span class="nf">directDependsOnDependenciesOfType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-ka-not-under-content-root-module/index.html#directdependsondependenciesoftype">M</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of all modules of type [`M`](../-ka-not-under-content-root-module/index.md#directdependsondependenciesoftype) that the given module directly depends on with a depends-on dependency.

**See also**



 - [`KaModule.directDependsOnDependencies`](../-ka-not-under-content-root-module/index.md#directdependsondependencies)



</div>

</div>
### directFriendDependenciesOfType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../-ka-not-under-content-root-module/index.html#directfrienddependenciesoftype">M</a><span class="o"> : </span><a href="../-ka-module/index.html">KaModule</a><span class="o">> </span><a href="../-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../-ka-not-under-content-root-module/index.html#directfrienddependenciesoftype"><span class="nf">directFriendDependenciesOfType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-ka-not-under-content-root-module/index.html#directfrienddependenciesoftype">M</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of all modules of type [`M`](../-ka-not-under-content-root-module/index.md#directfrienddependenciesoftype) that the given module directly depends on with a friend dependency.

**See also**



 - [`KaModule.directFriendDependencies`](../-ka-not-under-content-root-module/index.md#directfrienddependencies)



</div>

</div>
### directRegularDependenciesOfType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../-ka-not-under-content-root-module/index.html#directregulardependenciesoftype">M</a><span class="o"> : </span><a href="../-ka-module/index.html">KaModule</a><span class="o">> </span><a href="../-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../-ka-not-under-content-root-module/index.html#directregulardependenciesoftype"><span class="nf">directRegularDependenciesOfType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-ka-not-under-content-root-module/index.html#directregulardependenciesoftype">M</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of all modules of type [`M`](../-ka-not-under-content-root-module/index.md#directregulardependenciesoftype) that the given module directly depends on with a regular dependency.

**See also**



 - [`KaModule.directRegularDependencies`](../-ka-not-under-content-root-module/index.md#directregulardependencies)



</div>

</div>
