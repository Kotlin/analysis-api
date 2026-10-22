---
tags:
 - jvm
title: "KaDanglingFileModule"
---

# KaDanglingFileModule

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-platform-interface/index.html">KaPlatformInterface::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaDanglingFileModule</a> : <a href="../-ka-module/index.html">KaModule</a>
</span></code></pre></div>A module for a dangling file. Such files are usually temporary and are stored in-memory.

Dangling files may be created for various purposes, such as: a code fragment for the evaluator, a sandbox for testing code modification applicability, and so on.


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
### baseContextModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html">KaDanglingFileModule</a><span class="p">.</span><a href="index.html#basecontextmodule">baseContextModule</a><span class="o">: </span><a href="../-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

The non-dangling module that represents the base context of the [`KaDanglingFileModule`](index.md), skipping any context modules which are themselves [`KaDanglingFileModule`](index.md)s.

When a dangling file is a code fragment, the dangling file module may itself have a dangling file module as a context. [`baseContextModule`](index.md#basecontextmodule) can be used to find the non-dangling context at the base of the chain.

**See also**



 - [`KaDanglingFileModule.contextModule`](index.md#contextmodule)



</div>

</div>
### baseContextModuleOrSelf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../-ka-not-under-content-root-module/index.html#basecontextmoduleorself">baseContextModuleOrSelf</a><span class="o">: </span><a href="../-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaModule`](../-ka-module/index.md)'s [`baseContextModule`](index.md#basecontextmodule), or the module itself if it's not a [`KaDanglingFileModule`](index.md).


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
### contextModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#contextmodule">contextModule</a><span class="o">: </span><a href="../-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

The module against which [`files`](index.md#files) are analyzed.


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
### files

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#files">files</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

All dangling files analyzed together, as a single module.

Throws an exception when the files are no longer valid (see [`isValid`](index.md#isvalid)).


</div>

</div>
### isCodeFragment

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#iscodefragment">isCodeFragment</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether at least one of the [`files`](index.md#files) is a code fragment.

This is useful to recognize code fragments when their PSI was collected.


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
### isStable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html">KaDanglingFileModule</a><span class="p">.</span><a href="index.html#isstable">isStable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the dangling file module supports partial invalidation on PSI modifications. The sessions for such modules can be cached for a longer time.

For a dangling file module to be stable, its context module must also be stable. Otherwise, cache inconsistencies may occur.

In more detail, caches for unstable dangling file modules are invalidated after any PSI modification, while stable dangling file modules react to modification events. A stable module with an unstable context risks cache inconsistencies, as the context module's invalidation scope is much broader.


</div>

</div>
### isValid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#isvalid">isValid</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the dangling file module's [`files`](index.md#files) are still valid.

**See also**



 - [`KtFile.isValid`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/is-valid.md)



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
### resolutionMode

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#resolutionmode">resolutionMode</a><span class="o">: </span><a href="../-ka-dangling-file-resolution-mode/index.html">KaDanglingFileResolutionMode</a>
</span></code></pre></div>
</div>


<div markdown>

The mode which determines how references to non-local declarations in the dangling file are resolved.


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
