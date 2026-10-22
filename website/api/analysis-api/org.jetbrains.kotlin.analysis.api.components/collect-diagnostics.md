---
tags:
 - jvm
title: "collectDiagnostics"
---

# collectDiagnostics

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="collect-diagnostics.html"><span class="nf">collectDiagnostics</span></a><span class="p">(</span>filter<span class="o">: </span><a href="-ka-diagnostic-checker-filter/index.html">KaDiagnosticCheckerFilter</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic-with-psi/index.html">KaDiagnosticWithPsi</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Collects all diagnostics for the given file.

Eager version of [`KtFile.diagnostics`](../../analysis-api/org.jetbrains.kotlin.analysis.api.components/index.md).

#### See also


 - [`KtFile.diagnostics`](../../analysis-api/org.jetbrains.kotlin.analysis.api.components/index.md)



</div>

</div>
