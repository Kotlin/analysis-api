---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.compilation"
---

# org.jetbrains.kotlin.analysis.api.compilation
## Types
### [`KaCodeCompilationException`](-ka-code-compilation-exception/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-code-compilation-exception/index.html">KaCodeCompilationException</a><span class="p">(</span>cause<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="p">)</span> : <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/RuntimeException.html">RuntimeException</a>
</span></code></pre></div>
</div>


<div markdown>

Thrown when an exception occurred while analyzing the code to be compiled, or during target platform code generation.


</div>

</div>
### [`KaCompilationOptions`](-ka-compilation-options/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compilation-options/index.html">KaCompilationOptions</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

An immutable set of options for in-memory compilation via [`compile`](compile.md).


</div>

</div>
### [`KaCompilationOptionsBuilder`](-ka-compilation-options-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compilation-options-builder/index.html">KaCompilationOptionsBuilder</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

A DSL builder for [`KaCompilationOptions`](-ka-compilation-options/index.md).


</div>

</div>
### [`KaCompilationResult`](-ka-compilation-result/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-compilation-result/index.html">KaCompilationResult</a>
</span></code></pre></div>
</div>


<div markdown>

An in-memory compilation result returned from [`compile`](compile.md).


</div>

</div>
### [`KaCompilationTarget`](-ka-compilation-target/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-compilation-target/index.html">KaCompilationTarget</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-compilation-target/index.html">KaCompilationTarget</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

The target platform of the compilation performed by [`compile`](compile.md).


</div>

</div>
### [`KaCompiledClassHandler`](-ka-compiled-class-handler/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="kd">interface </span><a href="-ka-compiled-class-handler/index.html">KaCompiledClassHandler</a>
</span></code></pre></div>
</div>


<div markdown>

A handler which is called whenever a new class file is produced, when compiling sources to the JVM target.


</div>

</div>
### [`KaCompiledFile`](-ka-compiled-file/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compiled-file/index.html">KaCompiledFile</a>
</span></code></pre></div>
</div>


<div markdown>

A single file produced by an in-memory compilation performed by [`compile`](compile.md).


</div>

</div>
### [`KaCompilerFacilityModuleActualizer`](-ka-compiler-facility-module-actualizer/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="kd">interface </span><a href="-ka-compiler-facility-module-actualizer/index.html">KaCompilerFacilityModuleActualizer</a>
</span></code></pre></div>
</div>


<div markdown>

Actualizer for common source modules.


</div>

</div>
## Properties
## Functions
### [`compile`](compile.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="compile.html"><span class="nf">compile</span></a><span class="p">(</span>file<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>options<span class="o">: </span><a href="-ka-compilation-options/index.html">KaCompilationOptions</a><span class="p">)</span><span class="o">: </span><a href="-ka-compilation-result/index.html">KaCompilationResult</a>
</span></code></pre></div>
</div>


<div markdown>

Compiles the given [`file`](compile.md) in-memory using the specified [`options`](compile.md).


</div>

</div>
### [`createCompilationOptions`](create-compilation-options.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="create-compilation-options.html"><span class="nf">createCompilationOptions</span></a><span class="p">(</span>init<span class="o">: </span><a href="-ka-compilation-options-builder/index.html">KaCompilationOptionsBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="-ka-compilation-options/index.html">KaCompilationOptions</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a new [`KaCompilationOptions`](-ka-compilation-options/index.md) instance using the given DSL [`init`](create-compilation-options.md) block.


</div>

</div>
