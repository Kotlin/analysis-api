---
tags:
 - jvm
title: "KotlinModuleDependentsProvider"
---

# KotlinModuleDependentsProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinModuleDependentsProvider</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>[`KotlinModuleDependentsProvider`](index.md) provides dependents for a [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md), which are modules that depend on the [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md).

[`getDirectDependents`](../-kotlin-module-dependents-provider-base/index.md#getdirectdependents) and [`getTransitiveDependents`](index.md#gettransitivedependents) may return an empty set for [`KaBuiltinsModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-builtins-module/index.md)s and SDK [`KaLibraryModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-library-module/index.md)s even though most modules depend on builtins/SDKs, because it is often not feasible to compute that set. Instead, users of [`KotlinModuleDependentsProvider`](index.md) should keep this limitation in mind and handle it separately. For example, a global modification event should be published for builtins and SDK changes.

An empty set is also returned for [`KaDanglingFileModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-dangling-file-module/index.md)s. Additionally, dangling file modules are never included in the dependents of their context modules. This is because dangling files are created ad-hoc, and it's not economical to keep track of them.

Implementations of this provider should ensure that results are provided in reasonable time, for example by caching results, as its functions may be called frequently.

#### Inheritors


 - [`KotlinModuleDependentsProviderBase`](../-kotlin-module-dependents-provider-base/index.md)



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
### getDirectDependents

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-kotlin-module-dependents-provider-base/index.html#getdirectdependents"><span class="nf">getDirectDependents</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all direct dependents of [`module`](../-kotlin-module-dependents-provider-base/index.md#getdirectdependents), excluding [`module`](../-kotlin-module-dependents-provider-base/index.md#getdirectdependents) if it depends on itself.


</div>

</div>
### getRefinementDependents

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-kotlin-module-dependents-provider-base/index.html#getrefinementdependents"><span class="nf">getRefinementDependents</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all refinement/depends-on dependents of [`module`](../-kotlin-module-dependents-provider-base/index.md#getrefinementdependents), excluding [`module`](../-kotlin-module-dependents-provider-base/index.md#getrefinementdependents) itself. The result is transitive because refinement dependencies are implicitly transitive.


</div>

</div>
### getTransitiveDependents

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#gettransitivedependents"><span class="nf">getTransitiveDependents</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all direct and indirect dependents of [`module`](index.md#gettransitivedependents), excluding [`module`](index.md#gettransitivedependents) if it depends on itself.


</div>

</div>
