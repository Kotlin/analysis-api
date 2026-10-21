---
tags:
 - jvm
title: "KaCompilationResult"
---

# KaCompilationResult

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="index.html">KaCompilationResult</a>
</span></code></pre></div><strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.compilation.KaCompilationResult</strong>`](../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-result/index.md)<strong> instead.</strong>

An in-memory compilation result returned from [`KaCompilerFacility`](../-ka-compiler-facility/index.md).

Compilation fails if there are critical errors reported either on the frontend or on the backend side. Keep in mind that [`KaCompilationResult`](index.md) is a part of the Analysis API, so it should only be used inside an [`analysis block`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md).

#### Inheritors


 - [`Success`](-success/index.md)
 - [`Failure`](-failure/index.md)



</div>

## Types
### [`Failure`](-failure/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-failure/index.html">Failure</a><span class="p">(</span><span class="kd">val </span>errors<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic/index.html">KaDiagnostic</a><span class="o">></span><span class="p">, </span>mutedExceptions<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="o">></span><span class="o"> = </span>emptyList()<span class="p">)</span> : <a href="index.html">KaCompilationResult</a>
</span></code></pre></div>
</div>


<div markdown>

A failed compilation result.


</div>

</div>
### [`Success`](-success/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-success/index.html">Success</a><span class="p">(</span>
    <span class="kd">val </span>output<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-compiled-file/index.html">KaCompiledFile</a><span class="o">></span><span class="p">, </span>
    <span class="kd">val </span>capturedValues<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.compile/-ka-code-fragment-captured-value/index.html">KaCodeFragmentCapturedValue</a><span class="o">></span><span class="p">, </span>
    <span class="kd">var </span>canBeCached<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    mutedExceptions<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="o">></span><span class="o"> = </span>emptyList()
<span class="p">)</span> : <a href="index.html">KaCompilationResult</a>
</span></code></pre></div>
</div>


<div markdown>

A successful compilation result.


</div>

</div>
## Properties
### mutedExceptions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="-failure/index.html#mutedexceptions">mutedExceptions</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of exceptions that were thrown during compilation but workaround somehow


</div>

</div>
