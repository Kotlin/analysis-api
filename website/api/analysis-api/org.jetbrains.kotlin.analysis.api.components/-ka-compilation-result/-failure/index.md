---
tags:
 - jvm
title: "Failure"
---

# Failure

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">Failure</a><span class="p">(</span><span class="kd">val </span>errors<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic/index.html">KaDiagnostic</a><span class="o">></span><span class="p">, </span>mutedExceptions<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="o">></span><span class="o"> = </span>emptyList()<span class="p">)</span> : <a href="../index.html">KaCompilationResult</a>
</span></code></pre></div>A failed compilation result.


</div>

## Constructors
### Failure

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>errors<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic/index.html">KaDiagnostic</a><span class="o">></span><span class="p">, </span>mutedExceptions<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="o">></span><span class="o"> = </span>emptyList()<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### errors

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#errors">errors</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic/index.html">KaDiagnostic</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### mutedExceptions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#mutedexceptions">mutedExceptions</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of exceptions that were thrown during compilation but workaround somehow


</div>

</div>
