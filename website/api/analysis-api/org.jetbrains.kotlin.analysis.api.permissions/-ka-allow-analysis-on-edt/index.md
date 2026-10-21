---
tags:
 - jvm
title: "KaAllowAnalysisOnEdt"
---

# KaAllowAnalysisOnEdt

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"Analysis should not be allowed to be run from the EDT, as otherwise it may cause IDE freezes."</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="index.html">KaAllowAnalysisOnEdt</a>
</span></code></pre></div>
</div>

