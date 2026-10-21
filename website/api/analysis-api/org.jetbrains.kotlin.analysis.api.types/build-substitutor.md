---
tags:
 - jvm
title: "buildSubstitutor"
---

# buildSubstitutor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="build-substitutor.html"><span class="nf">buildSubstitutor</span></a><span class="p">(</span>build<span class="o">: </span><a href="-ka-substitutor-builder/index.html">KaSubstitutorBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="-ka-substitutor/index.html">KaSubstitutor</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a new [`KaSubstitutor`](-ka-substitutor/index.md) from substitutions specified inside [`build`](build-substitutor.md).

When no mappings are provided in [`build`](build-substitutor.md), returns [`KaSubstitutor.Empty`](-ka-substitutor/-empty/index.md). To build [`KaSubstitutor.Empty`](-ka-substitutor/-empty/index.md) specifically, use [`emptySubstitutor`](empty-substitutor.md).


</div>

</div>
