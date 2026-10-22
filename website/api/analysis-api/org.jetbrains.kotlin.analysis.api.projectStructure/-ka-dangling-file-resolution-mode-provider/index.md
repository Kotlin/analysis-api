---
tags:
 - jvm
title: "KaDanglingFileResolutionModeProvider"
---

# KaDanglingFileResolutionModeProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaDanglingFileResolutionModeProvider</a>
</span></code></pre></div>A service that provides [`KaDanglingFileResolutionMode`](../-ka-dangling-file-resolution-mode/index.md) for a given [`KtFile`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md) based purely on its content.

The service is aimed at taking unnecessary workload off developers when choosing [`KaDanglingFileResolutionMode`](../-ka-dangling-file-resolution-mode/index.md) for [`analyzeCopy`](../../org.jetbrains.kotlin.analysis.api.session/analyze-copy.md) calls. Rare use-cases with file copies might require some particular resolution mode, however, usually [`KaDanglingFileResolutionMode`](../-ka-dangling-file-resolution-mode/index.md) is just an optimization to avoid unnecessary FIR resolution in file copies. But when working with some generic file copies, it's almost impossible to correctly determine whether an out-of-block modification is present in the file copy without a sophisticated file analysis. Implementing this additional logic for a low-level optimization definitely shouldn't be done by the users of Analysis API. [`KaDanglingFileResolutionModeProvider`](index.md) should be the main source of truth for determining the resolution mode for file copies.


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
### calculateMode

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#calculatemode"><span class="nf">calculateMode</span></a><span class="p">(</span>file<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">)</span><span class="o">: </span><a href="../-ka-dangling-file-resolution-mode/index.html">KaDanglingFileResolutionMode</a>
</span></code></pre></div>
</div>


<div markdown>

Calculates [`KaDanglingFileResolutionMode`](../-ka-dangling-file-resolution-mode/index.md) for the given [`file`](index.md#calculatemode).

This mode is calculated based solely on the difference between the given dangling [`file`](index.md#calculatemode) and its [`copyOrigin`](../copy-origin.md). If there was an out-of-block modification made in the [`file`](index.md#calculatemode) compared to its [`copyOrigin`](../copy-origin.md), returns [`KaDanglingFileResolutionMode.PREFER_SELF`](../-ka-dangling-file-resolution-mode/-p-r-e-f-e-r_-s-e-l-f/index.md). Otherwise, returns [`KaDanglingFileResolutionMode.IGNORE_SELF`](../-ka-dangling-file-resolution-mode/-i-g-n-o-r-e_-s-e-l-f/index.md).

If the given [`file`](index.md#calculatemode) is not a dangling one, returns [`KaDanglingFileResolutionMode.PREFER_SELF`](../-ka-dangling-file-resolution-mode/-p-r-e-f-e-r_-s-e-l-f/index.md).


</div>

</div>
