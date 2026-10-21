---
tags:
 - jvm
title: "forbidAnalysis"
---

# forbidAnalysis

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="forbid-analysis.html">R</a><span class="o">> </span><a href="forbid-analysis.html"><span class="nf">forbidAnalysis</span></a><span class="p">(</span>description<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="forbid-analysis.html">R</a><span class="p">)</span><span class="o">: </span><a href="forbid-analysis.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

Forbids [`analyze`](../org.jetbrains.kotlin.analysis.api.session/analyze.md) to be called in the given [`action`](forbid-analysis.md).

#### Parameters


 - description: A human-readable description of the [`action`](forbid-analysis.md), which is used to generate error messages when [`analyze`](../org.jetbrains.kotlin.analysis.api.session/analyze.md) is called.





</div>

</div>
