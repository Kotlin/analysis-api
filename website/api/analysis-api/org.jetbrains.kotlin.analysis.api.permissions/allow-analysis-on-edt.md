---
tags:
 - jvm
title: "allowAnalysisOnEdt"
---

# allowAnalysisOnEdt

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="allow-analysis-on-edt.html">T</a><span class="o">> </span><a href="allow-analysis-on-edt.html"><span class="nf">allowAnalysisOnEdt</span></a><span class="p">(</span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="allow-analysis-on-edt.html">T</a><span class="p">)</span><span class="o">: </span><a href="allow-analysis-on-edt.html">T</a>
</span></code></pre></div>
</div>


<div markdown>

Allows [`analyze`](../org.jetbrains.kotlin.analysis.api.session/analyze.md) to be called on the EDT in the given [`action`](allow-analysis-on-edt.md), which is normally not allowed.

Analysis is not supposed to be invoked from the EDT, as it may cause freezes. Use at your own risk!


</div>

</div>
