---
tags:
 - jvm
title: "findTopLevelCallables"
---

# findTopLevelCallables

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="find-top-level-callables.html"><span class="nf">findTopLevelCallables</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">, </span>name<span class="o">: </span>Name<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Finds top-level functions and properties called [`name`](find-top-level-callables.md) in the package called [`packageFqName`](find-top-level-callables.md). Returns only symbols that are visible from the current use-site module.


</div>

</div>
