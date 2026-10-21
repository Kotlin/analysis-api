---
tags:
 - jvm
title: "KaResolveExtension"
---

# KaResolveExtension

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KaResolveExtension</a> : Disposable
</span></code></pre></div>A resolve extension provides additional Kotlin files containing generated declarations, which will be included in the resolution as if they were regular source files in the module.

Each resolve extension is defined for a specific [`KaModule`](../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md), which is determined by the [`KaResolveExtensionProvider`](../-ka-resolve-extension-provider/index.md) which creates the resolve extension.

All member implementations should:

 - Consider caching the results for subsequent invocations.


 - Be lightweight and avoid building the whole file structure eagerly.


 - Avoid using Kotlin resolution, as these functions are called during session initialization, so Analysis API access is forbidden.


### Lifecycle Management
A resolve extension is tied to the lifetime of its module's [`analysis session`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md). It is created by [`KaResolveExtensionProvider`](../-ka-resolve-extension-provider/index.md) during creation of an analysis session, and disposed after the analysis session has been invalidated.

[`KaResolveExtension`](index.md) implements the Disposable interface. The resolve extension can then act as a parent disposable, e.g. for a message bus connection.

You must not implement resolve extensions as module-level services, due to the following reasons:

1. The IntelliJ platform SDK [discourages](https://plugins.jetbrains.com/docs/intellij/plugin-services.html#types) the use of     module-level services due to memory consumption. In particular, resolve extensions implemented as module-level services live longer     than their corresponding analysis session, so the resolve extension would not be garbage collected after its corresponding analysis     session has been invalidated.


1. The module-level service living longer than the analysis session increases the risk of caching invalidated entities in a resolve     extension.


1. Because the resolve extension is a Disposable, if implemented as a module-level service, the service would be disposed too early     during invalidation of the corresponding analysis session.


#### See also


 - [`KaResolveExtensionFile`](../-ka-resolve-extension-file/index.md)
 - [`KaResolveExtensionProvider`](../-ka-resolve-extension-provider/index.md)



</div>

## Constructors
### KaResolveExtension

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Functions
### dispose

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#dispose"><span class="nf">dispose</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### getContainedPackages

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getcontainedpackages"><span class="nf">getContainedPackages</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>FqName<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the set of packages that are contained in the files provided by [`getKtFiles`](index.md#getktfiles). It should be an exact set of all file packages.


</div>

</div>
### getKtFiles

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getktfiles"><span class="nf">getKtFiles</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-resolve-extension-file/index.html">KaResolveExtensionFile</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the list of files that should be generated for the module. The files should contain valid Kotlin code.

**Modification and Invalidation**

If the content of these files becomes invalid (e.g., because the source declarations they were based on changed), the resolve extension must publish an out-of-block modification event via the Analysis API message bus: `KotlinModificationTopics.MODULE_OUT_OF_BLOCK_MODIFICATION`.

To react to changes in Kotlin sources, the resolve extension may subscribe to Analysis API modification topics: `KotlinModificationTopics`. If the resolve extension both subscribes to and publishes modification events, care needs to be taken that no cycles are introduced. In general, the resolve extension should never publish an event for a module A in a listener for the same module A.

An out-of-block modification event for the resolve extension's associated module does not need to be published in response to an out-of-block modification event for the same module, because the original event suffices for invalidation.

**See also**



 - [`KaResolveExtensionFile`](../-ka-resolve-extension-file/index.md)



</div>

</div>
### getShadowedScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getshadowedscope"><span class="nf">getShadowedScope</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>GlobalSearchScope
</span></code></pre></div>
</div>


<div markdown>

Returns the scope of files that should be shadowed by the files provided by [`getKtFiles`](index.md#getktfiles).

Any files in the module that are included in this scope will be removed from analysis results. This allows the files provided by [`getKtFiles`](index.md#getktfiles) to cleanly replace those files from the module.

Resolve extensions may be used to generate declarations that would normally be provided by sources generated by an external build task, such as a resource compiler or annotation processor. In such a case, the resolve extension should provide a shadowed scope that covers those externally generated sources. This will prevent collisions between the definitions provided by [`getKtFiles`](index.md#getktfiles) and those provided by the (potentially stale) externally generated sources.


</div>

</div>
