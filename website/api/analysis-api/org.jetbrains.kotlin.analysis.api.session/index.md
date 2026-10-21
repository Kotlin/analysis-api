---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.session"
---

# org.jetbrains.kotlin.analysis.api.session
## Types
### [`KaSessionProvider`](-ka-session-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-session-provider/index.html">KaSessionProvider</a><span class="p">(</span><span class="kd">val </span>project<span class="o">: </span>Project<span class="p">)</span> : Disposable
</span></code></pre></div>
</div>


<div markdown>

Provides [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)s by use-site PsiElements or [`KaModule`](../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md)s.


</div>

</div>
## Properties
### [`analysisScope`](analysis-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="analysis-scope.html">analysisScope</a><span class="o">: </span>GlobalSearchScope
</span></code></pre></div>
</div>


<div markdown>

A GlobalSearchScope which spans the files that can be analyzed by the current [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md).


</div>

</div>
### [`useSiteModule`](use-site-module.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="use-site-module.html">useSiteModule</a><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaModule`](../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md) from whose perspective the analysis is performed. The use-site module defines the resolution scope of the [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md), which signifies where symbols are located (such as sources, dependencies, and so on) and which symbols can be found in the first place.


</div>

</div>
### [`useSiteSession`](use-site-session.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="use-site-session.html">useSiteSession</a><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) of the current analysis context.


</div>

</div>
## Functions
### [`analyze`](analyze.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="analyze.html">R</a><span class="o">> </span><a href="analyze.html"><span class="nf">analyze</span></a><span class="p">(</span>useSiteElement<span class="o">: </span>PsiElement<span class="p">, </span>action<span class="o">: </span><span class="kd">context</span><span class="p">(</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">) </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="analyze.html">R</a><span class="p">)</span><span class="o">: </span><a href="analyze.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

Executes the given [`action`](analyze.md) in an [`analysis session`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) context.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="analyze.html">R</a><span class="o">> </span><a href="analyze.html"><span class="nf">analyze</span></a><span class="p">(</span>useSiteModule<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a><span class="p">, </span>action<span class="o">: </span><span class="kd">context</span><span class="p">(</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">) </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="analyze.html">R</a><span class="p">)</span><span class="o">: </span><a href="analyze.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

Executes the given [`action`](analyze.md) in an [`analysis session`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) context.


</div>

</div>
### [`analyzeCopy`](analyze-copy.md)

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


</div>

</div>
### [`canBeAnalysed`](can-be-analysed.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span>PsiElement<span class="p">.</span><a href="can-be-analysed.html"><span class="nf">canBeAnalysed</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether the PsiElement is inside the [`analysisScope`](analysis-scope.md).


</div>

</div>
