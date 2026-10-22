---
tags:
 - jvm
title: "KaModuleBase"
---

# KaModuleBase

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KaModuleBase</a> : <a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a>
</span></code></pre></div>#### Inheritors


 - [`KaBuiltinsModuleImpl`](../-ka-builtins-module-impl/index.md)
 - [`KaDanglingFileModuleImpl`](../-ka-dangling-file-module-impl/index.md)



</div>

## Constructors
### KaModuleBase

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### [`baseContentScope`](index.md#basecontentscope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#basecontentscope">baseContentScope</a><span class="o">: </span>GlobalSearchScope
</span></code></pre></div>
</div>

</div>
### contentScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#contentscope">contentScope</a><span class="o">: </span>GlobalSearchScope
</span></code></pre></div>
</div>

</div>
### [`directDependsOnDependencies`](index.md#directdependsondependencies)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#directdependsondependencies">directDependsOnDependencies</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`directFriendDependencies`](index.md#directfrienddependencies)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#directfrienddependencies">directFriendDependencies</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`directRegularDependencies`](index.md#directregulardependencies)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#directregulardependencies">directRegularDependencies</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`moduleDescription`](index.md#moduledescription)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#moduledescription">moduleDescription</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### platformKind

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">.</span><a href="index.html#platformkind">platformKind</a><span class="o">: </span><a href="../-ka-module-platform-kind/index.html">KaModulePlatformKind</a>
</span></code></pre></div>
</div>


<div markdown>

**See also**



 - [`KaModulePlatformKind`](../-ka-module-platform-kind/index.md)



</div>

</div>
### [`project`](index.md#project)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#project">project</a><span class="o">: </span>Project
</span></code></pre></div>
</div>

</div>
### [`stableModuleName`](index.md#stablemodulename)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="index.html#stablemodulename">stableModuleName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`targetPlatform`](index.md#targetplatform)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#targetplatform">targetPlatform</a><span class="o">: </span>TargetPlatform
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">.</span><a href="index.html#arecompilerpluginssupported"><span class="nf">areCompilerPluginsSupported</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### asDebugString

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">.</span><a href="index.html#asdebugstring"><span class="nf">asDebugString</span></a><span class="p">(</span>indent<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="o"> = </span><span class="nb">0</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
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
