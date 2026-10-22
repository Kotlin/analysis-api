---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.projectStructure"
---

# org.jetbrains.kotlin.analysis.api.projectStructure
## Types
### [`KaBuiltinsModule`](-ka-builtins-module/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-platform-interface/index.html">KaPlatformInterface::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-builtins-module/index.html">KaBuiltinsModule</a> : <a href="-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

A module which contains Kotlin [builtins](https://kotlinlang.org/spec/built-in-types-and-their-semantics.html) for a specific platform.


</div>

</div>
### [`KaDanglingFileModule`](-ka-dangling-file-module/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-platform-interface/index.html">KaPlatformInterface::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-dangling-file-module/index.html">KaDanglingFileModule</a> : <a href="-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

A module for a dangling file. Such files are usually temporary and are stored in-memory.


</div>

</div>
### [`KaDanglingFileResolutionMode`](-ka-dangling-file-resolution-mode/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-dangling-file-resolution-mode/index.html">KaDanglingFileResolutionMode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-dangling-file-resolution-mode/index.html">KaDanglingFileResolutionMode</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Specifies how references to non-local declarations in dangling files should be resolved.


</div>

</div>
### [`KaDanglingFileResolutionModeProvider`](-ka-dangling-file-resolution-mode-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-dangling-file-resolution-mode-provider/index.html">KaDanglingFileResolutionModeProvider</a>
</span></code></pre></div>
</div>


<div markdown>

A service that provides [`KaDanglingFileResolutionMode`](-ka-dangling-file-resolution-mode/index.md) for a given [`KtFile`](../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md) based purely on its content.


</div>

</div>
### [`KaJvmTarget`](-ka-jvm-target/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-jvm-target/index.html">KaJvmTarget</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a JVM bytecode target version for compilation.


</div>

</div>
### [`KaLibraryFallbackDependenciesModule`](-ka-library-fallback-dependencies-module/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-platform-interface/index.html">KaPlatformInterface::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-library-fallback-dependencies-module/index.html">KaLibraryFallbackDependenciesModule</a> : <a href="-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

A module which stands in for the unknown dependencies of a [`KaLibraryModule`](-ka-library-module/index.md) and [`KaLibrarySourceModule`](-ka-library-source-module/index.md).


</div>

</div>
### [`KaLibraryModule`](-ka-library-module/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-platform-interface/index.html">KaPlatformInterface::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-library-module/index.html">KaLibraryModule</a> : <a href="-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

A module which represents a binary library, such as a JAR or KLIB.


</div>

</div>
### [`KaLibrarySourceModule`](-ka-library-source-module/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-platform-interface/index.html">KaPlatformInterface::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-library-source-module/index.html">KaLibrarySourceModule</a> : <a href="-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

A module which represents the sources for a [`KaLibraryModule`](-ka-library-module/index.md).


</div>

</div>
### [`KaModule`](-ka-module/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-platform-interface/index.html">KaPlatformInterface::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaModule`](-ka-module/index.md) is the Analysis API's view on a module inside a project. A [`KaModule`](-ka-module/index.md) represents a [`source set`](-ka-source-module/index.md) (with production and test sources being separate modules), [`script`](-ka-script-module/index.md), [`library`](-ka-library-module/index.md), and various niche concepts such as [`dangling files`](-ka-dangling-file-module/index.md).


</div>

</div>
### [`KaModuleProvider`](-ka-module-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-module-provider/index.html">KaModuleProvider</a>
</span></code></pre></div>
</div>

</div>
### [`KaNotUnderContentRootModule`](-ka-not-under-content-root-module/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-platform-interface/index.html">KaPlatformInterface::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-not-under-content-root-module/index.html">KaNotUnderContentRootModule</a> : <a href="-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

A module which represents a source file living outside the project's content root. For example, test data files, or the source files of another project.


</div>

</div>
### [`KaScriptDependencyModule`](-ka-script-dependency-module/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-platform-interface/index.html">KaPlatformInterface::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-script-dependency-module/index.html">KaScriptDependencyModule</a> : <a href="-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

A module for Kotlin script dependencies. Must either be a [`KaLibraryModule`](-ka-library-module/index.md) or [`KaLibrarySourceModule`](-ka-library-source-module/index.md).


</div>

</div>
### [`KaScriptModule`](-ka-script-module/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-platform-interface/index.html">KaPlatformInterface::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-script-module/index.html">KaScriptModule</a> : <a href="-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

A module for a Kotlin script file.


</div>

</div>
### [`KaSourceModule`](-ka-source-module/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-platform-interface/index.html">KaPlatformInterface::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-source-module/index.html">KaSourceModule</a> : <a href="-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaModule`](-ka-module/index.md) representing a set of source declarations.


</div>

</div>
## Properties
### [`contextModule`](context-module.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">var </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="context-module.html">contextModule</a><span class="o">: </span><a href="-ka-module/index.html">KaModule</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A context module against which analysis of this in-memory file should be performed. It can only be specified for an in-memory file.


</div>

</div>
### [`copyOrigin`](copy-origin.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiFile<span class="p">.</span><a href="copy-origin.html">copyOrigin</a><span class="o">: </span>PsiFile<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The original file if the given PsiFile is a file copy, or `null` otherwise.


</div>

</div>
### [`danglingFileResolutionMode`](dangling-file-resolution-mode.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="dangling-file-resolution-mode.html">danglingFileResolutionMode</a><span class="o">: </span><a href="-ka-dangling-file-resolution-mode/index.html">KaDanglingFileResolutionMode</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The resolution mode explicitly set for this dangling file, or `null` for files that are not dangling or if the mode was not set.


</div>

</div>
### [`explicitModule`](explicit-module.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">var </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="explicit-module.html">explicitModule</a><span class="o">: </span><a href="-ka-module/index.html">KaModule</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A module to be used for analyzing the given file. Currently, only [`KaDanglingFileModule`](-ka-dangling-file-module/index.md)s can be set as explicit modules.


</div>

</div>
### [`isDangling`](is-dangling.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="is-dangling.html">isDangling</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KtFile`](../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md) is a dangling file.


</div>

</div>
### [`kaModule`](ka-module.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span>PsiElement<span class="p">.</span><a href="ka-module.html">kaModule</a><span class="o">: </span><a href="-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaModule`](-ka-module/index.md) for a given this in the context of the session's [`useSiteModule`](../org.jetbrains.kotlin.analysis.api.session/use-site-module.md).


</div>

</div>
### [`refinedContextModule`](refined-context-module.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">var </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-code-fragment/index.html">KtCodeFragment</a><span class="p">.</span><a href="refined-context-module.html">refinedContextModule</a><span class="o">: </span><a href="-ka-module/index.html">KaModule</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A context module against which analysis of this code fragment should be performed.


</div>

</div>
## Functions
### [`kaModule`](ka-module.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="ka-module.html"><span class="nf">kaModule</span></a><span class="p">(</span>useSiteModule<span class="o">: </span><a href="-ka-module/index.html">KaModule</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaModule`](-ka-module/index.md) for a given this in the context of the [`useSiteModule`](ka-module.md).


</div>

</div>
### [`withDanglingFileResolutionMode`](with-dangling-file-resolution-mode.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="with-dangling-file-resolution-mode.html">R</a><span class="o">> </span><a href="with-dangling-file-resolution-mode.html"><span class="nf">withDanglingFileResolutionMode</span></a><span class="p">(</span>
    file<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>
    mode<span class="o">: </span><a href="-ka-dangling-file-resolution-mode/index.html">KaDanglingFileResolutionMode</a><span class="p">, </span>
    action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="with-dangling-file-resolution-mode.html">R</a>
<span class="p">)</span><span class="o">: </span><a href="with-dangling-file-resolution-mode.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

Runs the [`action`](with-dangling-file-resolution-mode.md) with a resolution mode being explicitly set for the dangling [`file`](with-dangling-file-resolution-mode.md).


</div>

</div>
