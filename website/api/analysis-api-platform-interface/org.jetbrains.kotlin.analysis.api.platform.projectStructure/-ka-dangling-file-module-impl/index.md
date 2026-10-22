---
tags:
 - jvm
title: "KaDanglingFileModuleImpl"
---

# KaDanglingFileModuleImpl

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KaDanglingFileModuleImpl</a><span class="p">(</span>
    files<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="o">></span><span class="p">, </span>
    <span class="kd">val </span>contextModule<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">, </span>
    <span class="kd">val </span>resolutionMode<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-dangling-file-resolution-mode/index.html">KaDanglingFileResolutionMode</a>
<span class="p">)</span> : <a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-dangling-file-module/index.html">KaDanglingFileModule</a>, <a href="../-ka-module-base/index.html">KaModuleBase</a>
</span></code></pre></div>The default implementation of the dangling file module, which provides all knowledge from the context module. Note that if you need custom behavior, you should create a custom implementation of a [`KaDanglingFileModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-dangling-file-module/index.md), as the Analysis API treats this implementation specially (by allowing certain performance optimizations).


</div>

## Constructors
### KaDanglingFileModuleImpl

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>
    files<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="o">></span><span class="p">, </span>
    contextModule<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">, </span>
    resolutionMode<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-dangling-file-resolution-mode/index.html">KaDanglingFileResolutionMode</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### baseContentScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#basecontentscope">baseContentScope</a><span class="o">: </span>GlobalSearchScope
</span></code></pre></div>
</div>

</div>
### [`contentScope`](index.md#contentscope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="index.html#contentscope">contentScope</a><span class="o">: </span>GlobalSearchScope
</span></code></pre></div>
</div>

</div>
### contextModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#contextmodule">contextModule</a><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>

</div>
### directDependsOnDependencies

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#directdependsondependencies">directDependsOnDependencies</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### directFriendDependencies

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#directfrienddependencies">directFriendDependencies</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### directRegularDependencies

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#directregulardependencies">directRegularDependencies</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### files

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#files">files</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### isCodeFragment

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#iscodefragment">isCodeFragment</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### isValid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#isvalid">isValid</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`moduleDescription`](index.md#moduledescription)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#moduledescription">moduleDescription</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### platformKind

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../-ka-module-base/index.html#platformkind">platformKind</a><span class="o">: </span><a href="../-ka-module-platform-kind/index.html">KaModulePlatformKind</a>
</span></code></pre></div>
</div>


<div markdown>

**See also**



 - [`KaModulePlatformKind`](../-ka-module-platform-kind/index.md)



</div>

</div>
### project

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#project">project</a><span class="o">: </span>Project
</span></code></pre></div>
</div>

</div>
### resolutionMode

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#resolutionmode">resolutionMode</a><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-dangling-file-resolution-mode/index.html">KaDanglingFileResolutionMode</a>
</span></code></pre></div>
</div>

</div>
### [`stableModuleName`](../-ka-module-base/index.md#stablemodulename)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../-ka-module-base/index.html#stablemodulename">stableModuleName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### targetPlatform

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#targetplatform">targetPlatform</a><span class="o">: </span>TargetPlatform
</span></code></pre></div>
</div>

</div>
### transitiveDependsOnDependencies

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#transitivedependsondependencies">transitiveDependsOnDependencies</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
## Functions
### areCompilerPluginsSupported

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../-ka-module-base/index.html#arecompilerpluginssupported"><span class="nf">areCompilerPluginsSupported</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### asDebugString

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../-ka-module-base/index.html#asdebugstring"><span class="nf">asDebugString</span></a><span class="p">(</span>indent<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="o"> = </span><span class="nb">0</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### equals

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">operator override </span><span class="kd">fun </span><a href="index.html#equals"><span class="nf">equals</span></a><span class="p">(</span>other<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### hashCode

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#hashcode"><span class="nf">hashCode</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`publishCodeFragmentContextModificationEvent`](../../org.jetbrains.kotlin.analysis.api.platform.modification/publish-code-fragment-context-modification-event.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.platform.modification/publish-code-fragment-context-modification-event.html"><span class="nf">publishCodeFragmentContextModificationEvent</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Publishes a [`KotlinCodeFragmentContextModificationEvent`](../../org.jetbrains.kotlin.analysis.api.platform.modification/-kotlin-code-fragment-context-modification-event/index.md) for this [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md). Must be called in a write action.


</div>

</div>
### [`publishModuleOutOfBlockModificationEvent`](../../org.jetbrains.kotlin.analysis.api.platform.modification/publish-module-out-of-block-modification-event.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.platform.modification/publish-module-out-of-block-modification-event.html"><span class="nf">publishModuleOutOfBlockModificationEvent</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Publishes a [`KotlinModuleOutOfBlockModificationEvent`](../../org.jetbrains.kotlin.analysis.api.platform.modification/-kotlin-module-out-of-block-modification-event/index.md) for this [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md). Must be called in a write action.


</div>

</div>
### [`publishModuleStateModificationEvent`](../../org.jetbrains.kotlin.analysis.api.platform.modification/publish-module-state-modification-event.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.platform.modification/publish-module-state-modification-event.html"><span class="nf">publishModuleStateModificationEvent</span></a><span class="p">(</span>modificationKind<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.platform.modification/-kotlin-module-state-modification-kind/index.html">KotlinModuleStateModificationKind</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Publishes a [`KotlinModuleStateModificationEvent`](../../org.jetbrains.kotlin.analysis.api.platform.modification/-kotlin-module-state-modification-event/index.md) for this [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md). Must be called in a write action.


</div>

</div>
### toString

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#tostring"><span class="nf">toString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
