---
tags:
 - jvm
title: "KtSdkModuleBuilder"
---

# KtSdkModuleBuilder

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KtSdkModuleBuilder</a><span class="p">(</span>coreApplicationEnvironment<span class="o">: </span>CoreApplicationEnvironment<span class="p">, </span>project<span class="o">: </span>Project<span class="p">)</span> : <a href="../-kt-library-module-builder/index.html">KtLibraryModuleBuilder</a>
</span></code></pre></div>
</div>

## Constructors
### KtSdkModuleBuilder

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>coreApplicationEnvironment<span class="o">: </span>CoreApplicationEnvironment<span class="p">, </span>project<span class="o">: </span>Project<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### contentScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">var </span><a href="index.html#contentscope">contentScope</a><span class="o">: </span>GlobalSearchScope<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### libraryName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">lateinit </span><span class="kd">var </span><a href="index.html#libraryname">libraryName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### libraryScopeConstructionMode

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">var </span><a href="index.html#libraryscopeconstructionmode">libraryScopeConstructionMode</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.standalone.projectStructure/-standalone-library-scope-construction-mode/index.html">StandaloneLibraryScopeConstructionMode</a>
</span></code></pre></div>
</div>


<div markdown>

The [`StandaloneLibraryScopeConstructionMode`](../../org.jetbrains.kotlin.analysis.api.standalone.projectStructure/-standalone-library-scope-construction-mode/index.md) used to build this module's content scope when [`contentScope`](index.md#contentscope) is not set explicitly.

The option is a <strong>workaround</strong> for exceptional cases. See [`StandaloneLibraryScopeConstructionMode`](../../org.jetbrains.kotlin.analysis.api.standalone.projectStructure/-standalone-library-scope-construction-mode/index.md) for more information.

The default construction mode is seeded from the owning provider's [`KaModuleContainerBuilder.libraryScopeConstructionMode`](../-ka-module-container-builder/index.md#libraryscopeconstructionmode) and may be overridden here.


</div>

</div>
### librarySources

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">var </span><a href="index.html#librarysources">librarySources</a><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-library-source-module/index.html">KaLibrarySourceModule</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### platform

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">lateinit </span><span class="kd">var </span><a href="../-kt-source-module-builder/index.html#platform">platform</a><span class="o">: </span>TargetPlatform
</span></code></pre></div>
</div>

</div>
## Functions
### addBinaryRoot

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#addbinaryroot"><span class="nf">addBinaryRoot</span></a><span class="p">(</span>root<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/nio/file/Path.html">Path</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Adds a [`root`](index.md#addbinaryroot) to the current library.

The [`root`](index.md#addbinaryroot) can be:

 - A .jar file for JVM libraries or common metadata KLibs


 - A directory with a set of .classfiles for JVM Libraries


 - A Kotlin/Native, Kotlin/Common, Kotlin/JS KLib. In this case, all KLib dependencies should be provided together with the KLib itself.



</div>

</div>
### addBinaryRoots

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#addbinaryroots"><span class="nf">addBinaryRoots</span></a><span class="p">(</span>roots<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/nio/file/Path.html">Path</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Adds a collection of [`roots`](index.md#addbinaryroots) to the current library.

See [`addBinaryRoot`](index.md#addbinaryroot) for details

**See also**



 - [`addBinaryRoot`](index.md#addbinaryroot): for details





</div>

</div>
### addBinaryRootsFromJdkHome

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#addbinaryrootsfromjdkhome"><span class="nf">addBinaryRootsFromJdkHome</span></a><span class="p">(</span>jdkHome<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/nio/file/Path.html">Path</a><span class="p">, </span>isJre<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### addBinaryVirtualFile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#addbinaryvirtualfile"><span class="nf">addBinaryVirtualFile</span></a><span class="p">(</span>virtualFile<span class="o">: </span>VirtualFile<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### addBinaryVirtualFiles

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#addbinaryvirtualfiles"><span class="nf">addBinaryVirtualFiles</span></a><span class="p">(</span>virtualFiles<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span>VirtualFile<span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### addDependsOnDependency

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-source-module-builder/index.html#adddependsondependency"><span class="nf">addDependsOnDependency</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### addFriendDependency

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-source-module-builder/index.html#addfrienddependency"><span class="nf">addFriendDependency</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### addRegularDependency

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-source-module-builder/index.html#addregulardependency"><span class="nf">addRegularDependency</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### build

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#build"><span class="nf">build</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-library-module/index.html">KaLibraryModule</a>
</span></code></pre></div>
</div>

</div>
