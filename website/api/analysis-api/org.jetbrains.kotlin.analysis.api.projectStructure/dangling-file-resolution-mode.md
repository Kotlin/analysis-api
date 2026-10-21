---
tags:
 - jvm
title: "danglingFileResolutionMode"
---

# danglingFileResolutionMode

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="dangling-file-resolution-mode.html">danglingFileResolutionMode</a><span class="o">: </span><a href="-ka-dangling-file-resolution-mode/index.html">KaDanglingFileResolutionMode</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The resolution mode explicitly set for this dangling file, or `null` for files that are not dangling or if the mode was not set.

Use the [`analyzeCopy`](../org.jetbrains.kotlin.analysis.api.session/analyze-copy.md) function for specifying the analysis mode. The effect is thread-local by design, as the file might potentially be resolved concurrently in different threads.

The resolution mode affects equality of [`KaDanglingFileModule`](-ka-dangling-file-module/index.md)s. For each resolution mode, a separate resolution module and session will be created.


</div>

</div>
