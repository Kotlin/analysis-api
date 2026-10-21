---
tags:
 - jvm
title: "KaInternalsCompletionCandidateChecker"
---

# KaInternalsCompletionCandidateChecker

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaInternalsCompletionCandidateChecker</a>
</span></code></pre></div>
</div>

## Functions
### createExtensionCandidateChecker

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createextensioncandidatechecker"><span class="nf">createExtensionCandidateChecker</span></a><span class="p">(</span>
    originalFile<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>
    nameExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">, </span>
    explicitReceiver<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-completion-extension-candidate-checker/index.html">KaCompletionExtensionCandidateChecker</a>
</span></code></pre></div>
</div>

</div>
