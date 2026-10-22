---
tags:
 - jvm
title: "analyzeCopy"
---

# analyzeCopy

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="analyze-copy.html">R</a><span class="o">> </span><a href="analyze-copy.html"><span class="nf">analyzeCopy</span></a><span class="p">(</span>
    useSiteElement<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">, </span>
    resolutionMode<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-dangling-file-resolution-mode/index.html">KaDanglingFileResolutionMode</a><span class="p">, </span>
    <span class="kd">crossinline </span>action<span class="o">: </span><span class="kd">context</span><span class="p">(</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">) </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="analyze-copy.html">R</a>
<span class="p">)</span><span class="o">: </span><a href="analyze-copy.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

Executes the given [`action`](analyze-copy.md) in a [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) context.

The [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) is provided as a context parameter, so members of the Analysis API are available inside [`action`](analyze-copy.md) without an explicit receiver.

The [`useSiteElement`](analyze-copy.md) must be inside a dangling file copy (specifically, [`PsiFile.copyOrigin`](../org.jetbrains.kotlin.analysis.api.projectStructure/copy-origin.md) must point to the copy source). Depending on the passed [`resolutionMode`](analyze-copy.md), declarations inside the file copy will be treated in a specific way.

The project will be analyzed from the perspective of [`useSiteElement`](analyze-copy.md)'s module, also called the use-site module.

Neither the analysis session nor any other [`lifetime owners`](../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.md) may be leaked outside the [`analyze`](analyze.md) block. Please consult the documentation of [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) for important information about lifetime management.


</div>

</div>
