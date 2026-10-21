---
tags:
 - jvm
title: "analyze"
---

# analyze

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="analyze.html">R</a><span class="o">> </span><a href="analyze.html"><span class="nf">analyze</span></a><span class="p">(</span>useSiteElement<span class="o">: </span>PsiElement<span class="p">, </span>action<span class="o">: </span><span class="kd">context</span><span class="p">(</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">) </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="analyze.html">R</a><span class="p">)</span><span class="o">: </span><a href="analyze.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

Executes the given [`action`](analyze.md) in an [`analysis session`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) context.

The [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) is provided as a context parameter, so members of the Analysis API are available inside [`action`](analyze.md) without an explicit receiver.

The project will be analyzed from the perspective of [`useSiteElement`](analyze.md)'s [`module`](../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md), also called the use-site module.

Neither the analysis session nor any other [`lifetime owners`](../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.md) may be leaked outside the [`analyze`](analyze.md) block. Please consult the documentation of [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) for important information about lifetime management.

#### See also


 - [`KaModuleProvider.getModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module-provider/get-module.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="analyze.html">R</a><span class="o">> </span><a href="analyze.html"><span class="nf">analyze</span></a><span class="p">(</span>useSiteModule<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a><span class="p">, </span>action<span class="o">: </span><span class="kd">context</span><span class="p">(</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">) </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="analyze.html">R</a><span class="p">)</span><span class="o">: </span><a href="analyze.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

Executes the given [`action`](analyze.md) in an [`analysis session`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) context.

The [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) is provided as a context parameter, so members of the Analysis API are available inside [`action`](analyze.md) without an explicit receiver.

The project will be analyzed from the perspective of the given [`useSiteModule`](analyze.md).

Neither the analysis session nor any other [`lifetime owners`](../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.md) may be leaked outside the [`analyze`](analyze.md) block. Please consult the documentation of [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) for important information about lifetime management.


</div>

</div>
