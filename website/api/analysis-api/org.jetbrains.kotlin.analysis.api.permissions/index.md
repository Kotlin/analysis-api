---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.permissions"
---

# org.jetbrains.kotlin.analysis.api.permissions
## Types
### [`KaAllowAnalysisFromWriteAction`](-ka-allow-analysis-from-write-action/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"Analysis should not be allowed to be run from a write action, as otherwise it may cause incorrect behavior and IDE freezes."</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-ka-allow-analysis-from-write-action/index.html">KaAllowAnalysisFromWriteAction</a>
</span></code></pre></div>
</div>

</div>
### [`KaAllowAnalysisOnEdt`](-ka-allow-analysis-on-edt/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"Analysis should not be allowed to be run from the EDT, as otherwise it may cause IDE freezes."</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-ka-allow-analysis-on-edt/index.html">KaAllowAnalysisOnEdt</a>
</span></code></pre></div>
</div>

</div>
### [`KaAnalysisPermissionRegistry`](-ka-analysis-permission-registry/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-analysis-permission-registry/index.html">KaAnalysisPermissionRegistry</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaAnalysisPermissionRegistry`](-ka-analysis-permission-registry/index.md) stores settings required by permission functions such as [`forbidAnalysis`](forbid-analysis.md), [`allowAnalysisOnEdt`](allow-analysis-on-edt.md), and [`allowAnalysisFromWriteAction`](allow-analysis-from-write-action.md).


</div>

</div>
## Functions
### [`allowAnalysisFromWriteAction`](allow-analysis-from-write-action.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="allow-analysis-from-write-action.html">T</a><span class="o">> </span><a href="allow-analysis-from-write-action.html"><span class="nf">allowAnalysisFromWriteAction</span></a><span class="p">(</span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="allow-analysis-from-write-action.html">T</a><span class="p">)</span><span class="o">: </span><a href="allow-analysis-from-write-action.html">T</a>
</span></code></pre></div>
</div>


<div markdown>

Allows [`analyze`](../org.jetbrains.kotlin.analysis.api.session/analyze.md) to be called from a write action in the given [`action`](allow-analysis-from-write-action.md), which is normally not allowed.


</div>

</div>
### [`allowAnalysisOnEdt`](allow-analysis-on-edt.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="allow-analysis-on-edt.html">T</a><span class="o">> </span><a href="allow-analysis-on-edt.html"><span class="nf">allowAnalysisOnEdt</span></a><span class="p">(</span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="allow-analysis-on-edt.html">T</a><span class="p">)</span><span class="o">: </span><a href="allow-analysis-on-edt.html">T</a>
</span></code></pre></div>
</div>


<div markdown>

Allows [`analyze`](../org.jetbrains.kotlin.analysis.api.session/analyze.md) to be called on the EDT in the given [`action`](allow-analysis-on-edt.md), which is normally not allowed.


</div>

</div>
### [`forbidAnalysis`](forbid-analysis.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="forbid-analysis.html">R</a><span class="o">> </span><a href="forbid-analysis.html"><span class="nf">forbidAnalysis</span></a><span class="p">(</span>description<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="forbid-analysis.html">R</a><span class="p">)</span><span class="o">: </span><a href="forbid-analysis.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

Forbids [`analyze`](../org.jetbrains.kotlin.analysis.api.session/analyze.md) to be called in the given [`action`](forbid-analysis.md).


</div>

</div>
