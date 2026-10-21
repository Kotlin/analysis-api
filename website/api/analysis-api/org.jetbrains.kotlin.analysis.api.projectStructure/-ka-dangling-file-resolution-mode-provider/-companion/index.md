---
tags:
 - jvm
title: "Companion"
---

# Companion

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">Companion</a>
</span></code></pre></div>
</div>

## Functions
### calculateMode

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#calculatemode"><span class="nf">calculateMode</span></a><span class="p">(</span>file<span class="o">: </span><a href="../../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">)</span><span class="o">: </span><a href="../../-ka-dangling-file-resolution-mode/index.html">KaDanglingFileResolutionMode</a>
</span></code></pre></div>
</div>


<div markdown>

Calculates [`KaDanglingFileResolutionMode`](../../-ka-dangling-file-resolution-mode/index.md) for the given [`file`](index.md#calculatemode).

This mode is calculated based solely on the difference between the given dangling [`file`](index.md#calculatemode) and its [`copyOrigin`](../../copy-origin.md). If there was an out-of-block modification made in the [`file`](index.md#calculatemode) compared to its [`copyOrigin`](../../copy-origin.md), returns [`KaDanglingFileResolutionMode.PREFER_SELF`](../../-ka-dangling-file-resolution-mode/-p-r-e-f-e-r_-s-e-l-f/index.md). Otherwise, returns [`KaDanglingFileResolutionMode.IGNORE_SELF`](../../-ka-dangling-file-resolution-mode/-i-g-n-o-r-e_-s-e-l-f/index.md).

If the given [`file`](index.md#calculatemode) is not a dangling one, returns [`KaDanglingFileResolutionMode.PREFER_SELF`](../../-ka-dangling-file-resolution-mode/-p-r-e-f-e-r_-s-e-l-f/index.md).


</div>

</div>
