---
tags:
 - jvm
title: "asCompositeScope"
---

# asCompositeScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-ka-scope/index.html">KaScope</a><span class="o">></span><span class="p">.</span><a href="as-composite-scope.html"><span class="nf">asCompositeScope</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

Combines a list of [`KaScope`](-ka-scope/index.md)s into a single composite [`KaScope`](-ka-scope/index.md). The resulting scope contains all members of its constituent scopes.


</div>

</div>
