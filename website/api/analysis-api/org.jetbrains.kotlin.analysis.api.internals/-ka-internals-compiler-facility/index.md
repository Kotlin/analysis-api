---
tags:
 - jvm
title: "KaInternalsCompilerFacility"
---

# KaInternalsCompilerFacility

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaInternalsCompilerFacility</a>
</span></code></pre></div>
</div>

## Functions
### compile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#compile"><span class="nf">compile</span></a><span class="p">(</span>file<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>options<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-options/index.html">KaCompilationOptions</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-result/index.html">KaCompilationResult</a>
</span></code></pre></div>
</div>

</div>
### createCompilationOptions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createcompilationoptions"><span class="nf">createCompilationOptions</span></a><span class="p">(</span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-options-builder/index.html">KaCompilationOptionsBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-options/index.html">KaCompilationOptions</a>
</span></code></pre></div>
</div>

</div>
### modify

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#modify"><span class="nf">modify</span></a><span class="p">(</span>options<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-options/index.html">KaCompilationOptions</a><span class="p">, </span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-options-builder/index.html">KaCompilationOptionsBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-options/index.html">KaCompilationOptions</a>
</span></code></pre></div>
</div>

</div>
