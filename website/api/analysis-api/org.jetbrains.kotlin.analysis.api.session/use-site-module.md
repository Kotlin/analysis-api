---
tags:
 - jvm
title: "useSiteModule"
---

# useSiteModule

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
