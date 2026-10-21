---
tags:
 - jvm
title: "KaCompilerFacilityModuleActualizer"
---

# KaCompilerFacilityModuleActualizer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="kd">interface </span><a href="index.html">KaCompilerFacilityModuleActualizer</a>
</span></code></pre></div><strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.compilation.KaCompilerFacilityModuleActualizer</strong>`](../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compiler-facility-module-actualizer/index.md)<strong> instead.</strong>

Actualizer for common source modules.

The Kotlin compiler cannot directly compile classes from common modules, as it needs dependencies and language settings from the target platform. Such as, even if the compiled class only uses 'kotlin-stdlib', the JVM compiler still needs the library bytecode to understand JVM facade names and to be able to inline functions (the JVM inliner uses Java bytecode instead of the serialized IR).

[`KaCompilerFacility`](../-ka-compiler-facility/index.md) attempts to find the platform module with an appropriate target by itself and substitutes it instead of the original common module – that way, it can pass all the required information to the compiler. However, there might be multiple platform modules (e.g., Android and JVM); in that case, the facility chooses the first matching one. [`KaCompilerFacilityModuleActualizer`](index.md) is a way to override the default behavior by offering a closer match – e.g., a module with an Android target.


</div>

## Functions
### actualize

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#actualize"><span class="nf">actualize</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a><span class="p">, </span>target<span class="o">: </span><a href="../-ka-compilation-target/index.html">KaCompilationTarget</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Actualizes the [`module`](index.md#actualize) with the common multiplatform target. Returns an actual counterpart of [`module`](index.md#actualize), target of which matches the [`target`](index.md#actualize), or `null` if such a module does not exist.


</div>

</div>
