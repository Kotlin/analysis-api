---
tags:
 - jvm
title: "withDanglingFileResolutionMode"
---

# withDanglingFileResolutionMode

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

Avoid using this function in client-side code. Use [`analyzeCopy`](../org.jetbrains.kotlin.analysis.api.session/analyze-copy.md) instead.


</div>

</div>
