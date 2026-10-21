---
tags:
 - jvm
title: "KaModuleProvider"
---

# KaModuleProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaModuleProvider</a>
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
### module

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#module"><span class="nf">module</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">, </span>useSiteModule<span class="o">: </span><a href="../-ka-module/index.html">KaModule</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaModule`](../-ka-module/index.md) for a given [`element`](index.md#module) in the context of the [`useSiteModule`](index.md#module).

The resulting [`KaModule`](../-ka-module/index.md) is guaranteed to be [`resolvable`](../-ka-not-under-content-root-module/index.md#isresolvable).

**Use-site Modules**

The use-site module is the [`KaModule`](../-ka-module/index.md) from which [`getModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module-provider/get-module.md) is called. This concept is the same as the use-site module accepted by [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md), and closely related to the concept of a use-site element. In essence, when we are performing analysis, most of the time we do so from the point of view of a particular [`KaModule`](../-ka-module/index.md) or PsiElement. If this module is already known, it should be passed as the [`useSiteModule`](index.md#module) to [`getModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module-provider/get-module.md).

Here, the use-site module is a way to disambiguate the [`KaModule`](../-ka-module/index.md) of [`element`](index.md#module)s with whom multiple modules might be associated:

1. It allows replacing the original [`KaModule`](../-ka-module/index.md) of [`element`](index.md#module) with another module, e.g. for supporting outsider files (see below).


1. It helps to distinguish between multiple possible [`KaModule`](../-ka-module/index.md)s for library elements.


If you have a use-site module in hand, please pass it as an argument to stay consistent. In the future, we may utilize the use-site module for additional purposes not listed above.

**Outsider Modules**

Normally, every Kotlin source file either belongs to some module (e.g. a source module, or a library module), or is self-contained (a script file, or a file outside content roots). However, in certain cases there might be special modules that include both existing source files, and also some additional files.

An example of such a module is one that owns an 'outsider' source file. Outsiders are used in IntelliJ for displaying files that technically belong to some module, but are not included in the module's content roots (e.g. a file from a previous VCS revision). As there might be cross-references between the outsider file and other files in the module, they need to be analyzed as a single synthetic module. Inside an analysis session for such a module (which would be the [`useSiteModule`](index.md#module)), sources that originally belong to a source module should be treated rather as a part of the synthetic one.


</div>

</div>
