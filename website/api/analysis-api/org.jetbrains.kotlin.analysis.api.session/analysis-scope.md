---
tags:
 - jvm
title: "analysisScope"
---

# analysisScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="analysis-scope.html">analysisScope</a><span class="o">: </span>GlobalSearchScope
</span></code></pre></div>
</div>


<div markdown>

A GlobalSearchScope which spans the files that can be analyzed by the current [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md).

For example, [`KaSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md)s can only be built for declarations which are in the analysis scope.


</div>

</div>
