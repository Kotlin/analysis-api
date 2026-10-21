---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.components"
---

# org.jetbrains.kotlin.analysis.api.components
## Types
### [`KaAnalysisScopeProvider`](-ka-analysis-scope-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-analysis-scope-provider/index.html">KaAnalysisScopeProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaArrayTypeBuilder`](-ka-array-type-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-array-type-builder/index.html">KaArrayTypeBuilder</a> : <a href="-ka-type-builder/index.html">KaTypeBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

A builder for array types.


</div>

</div>
### [`KaBuiltinFunctionTypeFamilies`](-ka-builtin-function-type-families/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-builtin-function-type-families/index.html">KaBuiltinFunctionTypeFamilies</a> : <a href="../org.jetbrains.kotlin.analysis.api.types/-ka-builtin-function-type-families/index.html">KaBuiltinFunctionTypeFamilies</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.types.KaBuiltinFunctionTypeFamilies</strong>`](../org.jetbrains.kotlin.analysis.api.types/-ka-builtin-function-type-families/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaBuiltinTypes`](-ka-builtin-types/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-builtin-types/index.html">KaBuiltinTypes</a> : <a href="../org.jetbrains.kotlin.analysis.api.types/-ka-builtin-types/index.html">KaBuiltinTypes</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.types.KaBuiltinTypes</strong>`](../org.jetbrains.kotlin.analysis.api.types/-ka-builtin-types/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaCallableImplementationState`](-ka-callable-implementation-state/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-callable-implementation-state/index.html">KaCallableImplementationState</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.symbols.KaCallableImplementationState</strong>`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-implementation-state/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaClassTypeBuilder`](-ka-class-type-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-class-type-builder/index.html">KaClassTypeBuilder</a> : <a href="-ka-type-builder/index.html">KaTypeBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

A builder for class types.


</div>

</div>
### [`KaCodeCompilationException`](-ka-code-compilation-exception/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-code-compilation-exception/index.html">KaCodeCompilationException</a><span class="p">(</span>cause<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="p">)</span> : <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/RuntimeException.html">RuntimeException</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.compilation.KaCodeCompilationException</strong>`](../org.jetbrains.kotlin.analysis.api.compilation/-ka-code-compilation-exception/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaCompilationOptions`](-ka-compilation-options/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compilation-options/index.html">KaCompilationOptions</a> : <a href="../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-options/index.html">KaCompilationOptions</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.compilation.KaCompilationOptions</strong>`](../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-options/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaCompilationOptionsBuilder`](-ka-compilation-options-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compilation-options-builder/index.html">KaCompilationOptionsBuilder</a> : <a href="../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-options-builder/index.html">KaCompilationOptionsBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.compilation.KaCompilationOptionsBuilder</strong>`](../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-options-builder/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaCompilationResult`](-ka-compilation-result/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-compilation-result/index.html">KaCompilationResult</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.compilation.KaCompilationResult</strong>`](../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-result/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaCompilationTarget`](-ka-compilation-target/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-compilation-target/index.html">KaCompilationTarget</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-compilation-target/index.html">KaCompilationTarget</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.compilation.KaCompilationTarget</strong>`](../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-target/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaCompiledClassHandler`](-ka-compiled-class-handler/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="kd">interface </span><a href="-ka-compiled-class-handler/index.html">KaCompiledClassHandler</a> : <a href="../org.jetbrains.kotlin.analysis.api.compilation/-ka-compiled-class-handler/index.html">KaCompiledClassHandler</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.compilation.KaCompiledClassHandler</strong>`](../org.jetbrains.kotlin.analysis.api.compilation/-ka-compiled-class-handler/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaCompiledFile`](-ka-compiled-file/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compiled-file/index.html">KaCompiledFile</a> : <a href="../org.jetbrains.kotlin.analysis.api.compilation/-ka-compiled-file/index.html">KaCompiledFile</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.compilation.KaCompiledFile</strong>`](../org.jetbrains.kotlin.analysis.api.compilation/-ka-compiled-file/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaCompilerFacility`](-ka-compiler-facility/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compiler-facility/index.html">KaCompilerFacility</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaCompilerFacilityModuleActualizer`](-ka-compiler-facility-module-actualizer/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="kd">interface </span><a href="-ka-compiler-facility-module-actualizer/index.html">KaCompilerFacilityModuleActualizer</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.compilation.KaCompilerFacilityModuleActualizer</strong>`](../org.jetbrains.kotlin.analysis.api.compilation/-ka-compiler-facility-module-actualizer/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaCompilerPluginGeneratedDeclarations`](-ka-compiler-plugin-generated-declarations/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compiler-plugin-generated-declarations/index.html">KaCompilerPluginGeneratedDeclarations</a> : <a href="../org.jetbrains.kotlin.analysis.api.compilerPlugins/-ka-compiler-plugin-generated-declarations/index.html">KaCompilerPluginGeneratedDeclarations</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.compilerPlugins.KaCompilerPluginGeneratedDeclarations</strong>`](../org.jetbrains.kotlin.analysis.api.compilerPlugins/-ka-compiler-plugin-generated-declarations/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaCompilerPluginGeneratedDeclarationsProvider`](-ka-compiler-plugin-generated-declarations-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-compiler-plugin-generated-declarations-provider/index.html">KaCompilerPluginGeneratedDeclarationsProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>


<div markdown>

Provides declarations generated by compiler plugins.


</div>

</div>
### [`KaCompletionCandidateChecker`](-ka-completion-candidate-checker/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-completion-candidate-checker/index.html">KaCompletionCandidateChecker</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaCompletionExtensionCandidateChecker`](-ka-completion-extension-candidate-checker/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-completion-extension-candidate-checker/index.html">KaCompletionExtensionCandidateChecker</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>

</div>
### [`KaDataFlowExitPointSnapshot`](-ka-data-flow-exit-point-snapshot/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-data-flow-exit-point-snapshot/index.html">KaDataFlowExitPointSnapshot</a><span class="p">(</span>
    <span class="kd">val </span>defaultExpressionInfo<span class="o">: </span><a href="-ka-data-flow-exit-point-snapshot/-default-expression-info/index.html">KaDataFlowExitPointSnapshot.DefaultExpressionInfo</a><span class="o">?</span><span class="p">, </span>
    <span class="kd">val </span>valuedReturnExpressions<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">></span><span class="p">, </span>
    <span class="kd">val </span>returnValueType<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span><span class="p">, </span>
    <span class="kd">val </span>jumpExpressions<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">></span><span class="p">, </span>
    <span class="kd">val </span>hasJumps<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">val </span>hasEscapingJumps<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">val </span>hasMultipleJumpKinds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">val </span>hasMultipleJumpTargets<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">val </span>variableReassignments<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-ka-data-flow-exit-point-snapshot/-variable-reassignment/index.html">KaDataFlowExitPointSnapshot.VariableReassignment</a><span class="o">></span>
<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.dataflow.KaDataFlowExitPointSnapshot</strong>`](../org.jetbrains.kotlin.analysis.api.dataflow/-ka-data-flow-exit-point-snapshot/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaDataFlowProvider`](-ka-data-flow-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-data-flow-provider/index.html">KaDataFlowProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaDeprecation`](-ka-deprecation/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-deprecation/index.html">KaDeprecation</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.symbols.KaDeprecation</strong>`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-deprecation/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaDeprecationLevel`](-ka-deprecation-level/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-deprecation-level/index.html">KaDeprecationLevel</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.symbols.KaDeprecationLevel</strong>`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-deprecation-level/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaDiagnosticCheckerFilter`](-ka-diagnostic-checker-filter/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-diagnostic-checker-filter/index.html">KaDiagnosticCheckerFilter</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-diagnostic-checker-filter/index.html">KaDiagnosticCheckerFilter</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

[`KaDiagnosticCheckerFilter`](-ka-diagnostic-checker-filter/index.md) controls which kinds of diagnostics are included in the result of diagnostic collection.


</div>

</div>
### [`KaDiagnosticProvider`](-ka-diagnostic-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-diagnostic-provider/index.html">KaDiagnosticProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaEvaluator`](-ka-evaluator/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-evaluator/index.html">KaEvaluator</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaExpressionInformationProvider`](-ka-expression-information-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-expression-information-provider/index.html">KaExpressionInformationProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaExpressionTypeProvider`](-ka-expression-type-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-expression-type-provider/index.html">KaExpressionTypeProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaExtensionApplicabilityResult`](-ka-extension-applicability-result/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-extension-applicability-result/index.html">KaExtensionApplicabilityResult</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents the result of checking the applicability of an extension callable in a specific context.


</div>

</div>
### [`KaFunctionTypeFamily`](-ka-function-type-family/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-function-type-family/index.html">KaFunctionTypeFamily</a> : <a href="../org.jetbrains.kotlin.analysis.api.types/-ka-function-type-family/index.html">KaFunctionTypeFamily</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.types.KaFunctionTypeFamily</strong>`](../org.jetbrains.kotlin.analysis.api.types/-ka-function-type-family/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaImplicitReceiver`](-ka-implicit-receiver/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-implicit-receiver/index.html">KaImplicitReceiver</a> : <a href="-ka-scope-implicit-receiver-value/index.html">KaScopeImplicitReceiverValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an implicit receiver available in a particular context.


</div>

</div>
### [`KaImplicitReceiverSmartCast`](-ka-implicit-receiver-smart-cast/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-implicit-receiver-smart-cast/index.html">KaImplicitReceiverSmartCast</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.dataflow.KaImplicitReceiverSmartCast</strong>`](../org.jetbrains.kotlin.analysis.api.dataflow/-ka-implicit-receiver-smart-cast/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaImplicitReceiverSmartCastKind`](-ka-implicit-receiver-smart-cast-kind/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-implicit-receiver-smart-cast-kind/index.html">KaImplicitReceiverSmartCastKind</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-implicit-receiver-smart-cast-kind/index.html">KaImplicitReceiverSmartCastKind</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.dataflow.KaImplicitReceiverSmartCastKind</strong>`](../org.jetbrains.kotlin.analysis.api.dataflow/-ka-implicit-receiver-smart-cast-kind/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaJavaInteroperabilityComponent`](-ka-java-interoperability-component/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-java-interoperability-component/index.html">KaJavaInteroperabilityComponent</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaKDocProvider`](-ka-k-doc-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-k-doc-provider/index.html">KaKDocProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>


<div markdown>

Component that locates KDoc for [`KtDeclaration`](../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md) and [`KaDeclarationSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md).


</div>

</div>
### [`KaReferenceShortener`](-ka-reference-shortener/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-reference-shortener/index.html">KaReferenceShortener</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaRenderer`](-ka-renderer/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-renderer/index.html">KaRenderer</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>


<div markdown>

Provides services for rendering [`declaration symbols`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) and [`types`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to strings.


</div>

</div>
### [`KaResolveExtensionInfoProvider`](-ka-resolve-extension-info-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-resolve-extension-info-provider/index.html">KaResolveExtensionInfoProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaResolver`](-ka-resolver/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-resolver/index.html">KaResolver</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaReturnValueStatus`](-ka-return-value-status/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-return-value-status/index.html">KaReturnValueStatus</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.symbols.KaReturnValueStatus</strong>`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-return-value-status/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaScopeContext`](-ka-scope-context/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-scope-context/index.html">KaScopeContext</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

A scope context includes all scopes that are relevant for a given [`KtElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md) position in a [`KtFile`](../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md), together with all available implicit receivers.


</div>

</div>
### [`KaScopeImplicitArgumentValue`](-ka-scope-implicit-argument-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-scope-implicit-argument-value/index.html">KaScopeImplicitArgumentValue</a> : <a href="-ka-scope-implicit-value/index.html">KaScopeImplicitValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an implicit argument available in a particular [`KaScopeContext`](-ka-scope-context/index.md).


</div>

</div>
### [`KaScopeImplicitReceiverValue`](-ka-scope-implicit-receiver-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-scope-implicit-receiver-value/index.html">KaScopeImplicitReceiverValue</a> : <a href="-ka-scope-implicit-value/index.html">KaScopeImplicitValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an implicit receiver available in a particular [`KaScopeContext`](-ka-scope-context/index.md).


</div>

</div>
### [`KaScopeImplicitValue`](-ka-scope-implicit-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-scope-implicit-value/index.html">KaScopeImplicitValue</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a value which can be used implicitly inside a particular [`KaScopeContext`](-ka-scope-context/index.md).


</div>

</div>
### [`KaScopeKind`](-ka-scope-kind/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-scope-kind/index.html">KaScopeKind</a>
</span></code></pre></div>
</div>

</div>
### [`KaScopeKinds`](-ka-scope-kinds/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-ka-scope-kinds/index.html">KaScopeKinds</a>
</span></code></pre></div>
</div>

</div>
### [`KaScopeProvider`](-ka-scope-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-scope-provider/index.html">KaScopeProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaScopeWithKind`](-ka-scope-with-kind/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-scope-with-kind/index.html">KaScopeWithKind</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

A wrapper around a [`KaScope`](../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) which is additionally positioned in the scope tower of a [`KaScopeContext`](-ka-scope-context/index.md), represented by [`KaScopeKind`](-ka-scope-kind/index.md).


</div>

</div>
### [`KaScopeWithKindImpl`](-ka-scope-with-kind-impl/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-scope-with-kind-impl/index.html">KaScopeWithKindImpl</a><span class="p">(</span>backingScope<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a><span class="p">, </span>backingKind<span class="o">: </span><a href="-ka-scope-kind/index.html">KaScopeKind</a><span class="p">)</span> : <a href="-ka-scope-with-kind/index.html">KaScopeWithKind</a>
</span></code></pre></div>
</div>

</div>
### [`KaSessionComponent`](-ka-session-component/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-session-component/index.html">KaSessionComponent</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

A component of a [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md).


</div>

</div>
### [`KaSignatureSubstitutor`](-ka-signature-substitutor/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-signature-substitutor/index.html">KaSignatureSubstitutor</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaSmartCastInfo`](-ka-smart-cast-info/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-smart-cast-info/index.html">KaSmartCastInfo</a> : <a href="../org.jetbrains.kotlin.analysis.api.dataflow/-ka-smart-cast-info/index.html">KaSmartCastInfo</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.dataflow.KaSmartCastInfo</strong>`](../org.jetbrains.kotlin.analysis.api.dataflow/-ka-smart-cast-info/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaSmartCastPossibility`](-ka-smart-cast-possibility/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-smart-cast-possibility/index.html">KaSmartCastPossibility</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a possible smart cast at a fixed context position.


</div>

</div>
### [`KaSmartCastSource`](-ka-smart-cast-source/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-smart-cast-source/index.html">KaSmartCastSource</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Either a symbol for which a smart cast is generated, or one of its receivers.


</div>

</div>
### [`KaSourceProvider`](-ka-source-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-source-provider/index.html">KaSourceProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaSubstitutorBuilder`](-ka-substitutor-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-substitutor-builder/index.html">KaSubstitutorBuilder</a><span class="p">(</span><span class="kd">val </span>token<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a><span class="p">)</span> : <a href="../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor-builder/index.html">KaSubstitutorBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.types.KaSubstitutorBuilder</strong>`](../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor-builder/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaSubstitutorProvider`](-ka-substitutor-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-substitutor-provider/index.html">KaSubstitutorProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaSubtypingErrorTypePolicy`](-ka-subtyping-error-type-policy/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.types.KaSubtypingErrorTypePolicy</strong>`](../org.jetbrains.kotlin.analysis.api.types/-ka-subtyping-error-type-policy/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaSymbolInformationProvider`](-ka-symbol-information-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-symbol-information-provider/index.html">KaSymbolInformationProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaSymbolRelationProvider`](-ka-symbol-relation-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-symbol-relation-provider/index.html">KaSymbolRelationProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaTypeBuilder`](-ka-type-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type-builder/index.html">KaTypeBuilder</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>

</div>
### [`KaTypeCreator`](-ka-type-creator/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type-creator/index.html">KaTypeCreator</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaTypeCreatorProvider`](-ka-type-creator-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type-creator-provider/index.html">KaTypeCreatorProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>


<div markdown>

Provides an instance of [`KaTypeCreator`](../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-type-creator/index.md) to create various [`types`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).


</div>

</div>
### [`KaTypeInformationProvider`](-ka-type-information-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type-information-provider/index.html">KaTypeInformationProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaTypeParameterTypeBuilder`](-ka-type-parameter-type-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type-parameter-type-builder/index.html">KaTypeParameterTypeBuilder</a> : <a href="-ka-type-builder/index.html">KaTypeBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

A builder for type parameter types.


</div>

</div>
### [`KaTypeProvider`](-ka-type-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type-provider/index.html">KaTypeProvider</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaTypeRelationChecker`](-ka-type-relation-checker/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type-relation-checker/index.html">KaTypeRelationChecker</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaUnificationSubstitutorPolicy`](-ka-unification-substitutor-policy/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-unification-substitutor-policy/index.html">KaUnificationSubstitutorPolicy</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-unification-substitutor-policy/index.html">KaUnificationSubstitutorPolicy</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.types.KaUnificationSubstitutorPolicy</strong>`](../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaUseSiteVisibilityChecker`](-ka-use-site-visibility-checker/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-use-site-visibility-checker/index.html">KaUseSiteVisibilityChecker</a> : <a href="../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html">KaUseSiteVisibilityChecker</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.visibility.KaUseSiteVisibilityChecker</strong>`](../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md)<strong> instead.</strong>


</div>

</div>
### [`KaVisibilityChecker`](-ka-visibility-checker/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-visibility-checker/index.html">KaVisibilityChecker</a> : <a href="-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>

</div>
### [`KaWhenMissingCase`](-ka-when-missing-case/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-when-missing-case/index.html">KaWhenMissingCase</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a missing case in a `when` expression.


</div>

</div>
### [`QualifierToShortenInfo`](-qualifier-to-shorten-info/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">class </span><a href="-qualifier-to-shorten-info/index.html">QualifierToShortenInfo</a><span class="p">(</span><span class="kd">val </span>qualifierToShorten<span class="o">: </span>SmartPsiElementPointer<span class="o"><</span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-dot-qualified-expression/index.html">KtDotQualifiedExpression</a><span class="o">></span><span class="p">, </span><span class="kd">val </span>shortenedReference<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

A class to keep a [`KtDotQualifiedExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-dot-qualified-expression/index.md) to shorten and what shape the shortened result has to be. [`shortenedReference`](-qualifier-to-shorten-info/index.md#shortenedreference) is the expected result of shortening in a string form. If [`shortenedReference`](-qualifier-to-shorten-info/index.md#shortenedreference) is null, it means the shortening will simply delete the qualifier. Note that currently the only usage of [`shortenedReference`](-qualifier-to-shorten-info/index.md#shortenedreference) is the case we have the import-alias. For example, [`shortenedReference`](-qualifier-to-shorten-info/index.md#shortenedreference) will be "bar" when we shorten:


</div>

</div>
### [`ShortenCommand`](-shorten-command/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-shorten-command/index.html">ShortenCommand</a>
</span></code></pre></div>
</div>

</div>
### [`ShortenOptions`](-shorten-options/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">class </span><a href="-shorten-options/index.html">ShortenOptions</a><span class="p">(</span>
    <span class="kd">val </span>removeThis<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span>
    <span class="kd">val </span>removeThisLabels<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span>
    <span class="kd">val </span>removeContextSensitiveResolutionQualifiers<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`ShortenStrategy`](-shorten-strategy/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-shorten-strategy/index.html">ShortenStrategy</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-shorten-strategy/index.html">ShortenStrategy</a><span class="o">> </span>
</span></code></pre></div>
</div>

</div>
### [`ThisLabelToShortenInfo`](-this-label-to-shorten-info/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">class </span><a href="-this-label-to-shorten-info/index.html">ThisLabelToShortenInfo</a><span class="p">(</span><span class="kd">val </span>labelToShorten<span class="o">: </span>SmartPsiElementPointer<span class="o"><</span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-this-expression/index.html">KtThisExpression</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

A class with a reference to [`KtThisExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-this-expression/index.md) with a label qualifier ([`KtThisExpression.labelQualifier`](../../psi-api/org.jetbrains.kotlin.psi/-kt-expression-with-label/label-qualifier.md)) that can be safely removed without changing the semantics of the code.


</div>

</div>
### [`TypeToShortenInfo`](-type-to-shorten-info/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">class </span><a href="-type-to-shorten-info/index.html">TypeToShortenInfo</a><span class="p">(</span><span class="kd">val </span>typeToShorten<span class="o">: </span>SmartPsiElementPointer<span class="o"><</span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-user-type/index.html">KtUserType</a><span class="o">></span><span class="p">, </span><span class="kd">val </span>shortenedReference<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

A class to keep a [`KtUserType`](../../psi-api/org.jetbrains.kotlin.psi/-kt-user-type/index.md) to shorten and what shape the shortened result has to be. [`shortenedReference`](-type-to-shorten-info/index.md#shortenedreference) is the expected result of shortening in a string form. If [`shortenedReference`](-type-to-shorten-info/index.md#shortenedreference) is null, it means the shortening will simply delete the qualifier. Note that currently the only usage of [`shortenedReference`](-type-to-shorten-info/index.md#shortenedreference) is the case we have the import-alias. For example, [`shortenedReference`](-type-to-shorten-info/index.md#shortenedreference) will be "AliasType" when we shorten:


</div>

</div>
## Properties
### [`importingScopeContext`](importing-scope-context.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="importing-scope-context.html">importingScopeContext</a><span class="o">: </span><a href="-ka-scope-context/index.html">KaScopeContext</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScopeContext`](-ka-scope-context/index.md) formed from all imports in the [`KtFile`](../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md).


</div>

</div>
## Functions
### [`asPsiType`](as-psi-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="as-psi-type.html"><span class="nf">asPsiType</span></a><span class="p">(</span>
    useSitePosition<span class="o">: </span>PsiElement<span class="p">, </span>
    allowErrorTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    mode<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type-mapping-mode/index.html">KaTypeMappingMode</a><span class="o"> = </span>KaTypeMappingMode.DEFAULT<span class="p">, </span>
    isAnnotationMethod<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span>
    suppressWildcards<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">?</span><span class="o"> = </span>null<span class="p">, </span>
    preserveAnnotations<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">, </span>
    allowNonJvmPlatforms<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span>
<span class="p">)</span><span class="o">: </span>PsiType<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a PsiType in the context of the [`useSitePosition`](as-psi-type.md).


</div>

</div>
### [`buildArrayType`](build-array-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="build-array-type.html"><span class="nf">buildArrayType</span></a><span class="p">(</span>elementType<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>init<span class="o">: </span><a href="-ka-array-type-builder/index.html">KaArrayTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a boxed / primitive (depending on the [`init`](build-array-type.md) block) array type from the given [`elementType`](build-array-type.md).


</div>

</div>
### [`buildClassType`](build-class-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="build-class-type.html"><span class="nf">buildClassType</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">, </span>init<span class="o">: </span><a href="-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a class type with the given class symbol.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="build-class-type.html"><span class="nf">buildClassType</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">, </span>init<span class="o">: </span><a href="-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a class type with the given class ID.


</div>

</div>
### [`buildStarTypeProjection`](build-star-type-projection.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="build-star-type-projection.html"><span class="nf">buildStarTypeProjection</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-star-type-projection/index.html">KaStarTypeProjection</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaStarTypeProjection`](../org.jetbrains.kotlin.analysis.api.types/-ka-star-type-projection/index.md) (`*`).


</div>

</div>
### [`buildTypeParameterType`](build-type-parameter-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="build-type-parameter-type.html"><span class="nf">buildTypeParameterType</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">, </span>init<span class="o">: </span><a href="-ka-type-parameter-type-builder/index.html">KaTypeParameterTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaTypeParameterType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.md) with the given type parameter symbol.


</div>

</div>
### [`buildVarargArrayType`](build-vararg-array-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="build-vararg-array-type.html"><span class="nf">buildVarargArrayType</span></a><span class="p">(</span>elementType<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds the underlying array type of [vararg](https://kotlinlang.org/docs/functions.html#variable-number-of-arguments-varargs) function parameter with the given [`elementType`](build-vararg-array-type.md).


</div>

</div>
### [`collectDiagnostics`](collect-diagnostics.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="collect-diagnostics.html"><span class="nf">collectDiagnostics</span></a><span class="p">(</span>filter<span class="o">: </span><a href="-ka-diagnostic-checker-filter/index.html">KaDiagnosticCheckerFilter</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic-with-psi/index.html">KaDiagnosticWithPsi</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Collects all diagnostics for the given file.


</div>

</div>
### [`collectPossibleReferenceShortenings`](collect-possible-reference-shortenings.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="collect-possible-reference-shortenings.html"><span class="nf">collectPossibleReferenceShortenings</span></a><span class="p">(</span>
    file<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>
    selection<span class="o">: </span>TextRange<span class="o"> = </span>file.textRange<span class="p">, </span>
    shortenOptions<span class="o">: </span><a href="-shorten-options/index.html">ShortenOptions</a><span class="o"> = </span>ShortenOptions.DEFAULT<span class="p">, </span>
    classShortenStrategy<span class="o">: </span><span class="p">(</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="-shorten-strategy/index.html">ShortenStrategy</a><span class="o"> = </span>defaultClassShortenStrategy<span class="p">, </span>
    callableShortenStrategy<span class="o">: </span><span class="p">(</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="-shorten-strategy/index.html">ShortenStrategy</a><span class="o"> = </span>defaultCallableShortenStrategy
<span class="p">)</span><span class="o">: </span><a href="-shorten-command/index.html">ShortenCommand</a>
</span></code></pre></div>
</div>


<div markdown>

Collects possible references to shorten.


</div>

</div>
### [`collectPossibleReferenceShorteningsInElement`](collect-possible-reference-shortenings-in-element.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="collect-possible-reference-shortenings-in-element.html"><span class="nf">collectPossibleReferenceShorteningsInElement</span></a><span class="p">(</span>
    element<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">, </span>
    shortenOptions<span class="o">: </span><a href="-shorten-options/index.html">ShortenOptions</a><span class="o"> = </span>ShortenOptions.DEFAULT<span class="p">, </span>
    classShortenStrategy<span class="o">: </span><span class="p">(</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="-shorten-strategy/index.html">ShortenStrategy</a><span class="o"> = </span>defaultClassShortenStrategy<span class="p">, </span>
    callableShortenStrategy<span class="o">: </span><span class="p">(</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="-shorten-strategy/index.html">ShortenStrategy</a><span class="o"> = </span>defaultCallableShortenStrategy
<span class="p">)</span><span class="o">: </span><a href="-shorten-command/index.html">ShortenCommand</a>
</span></code></pre></div>
</div>


<div markdown>

Collects possible references to shorten in [`element`](collect-possible-reference-shortenings-in-element.md)s text range.


</div>

</div>
### [`computeMissingCases`](compute-missing-cases.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-when-expression/index.html">KtWhenExpression</a><span class="p">.</span><a href="compute-missing-cases.html"><span class="nf">computeMissingCases</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-ka-when-missing-case/index.html">KaWhenMissingCase</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Computes the missing cases of the given [`KtWhenExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-when-expression/index.md).


</div>

</div>
### [`createExtensionCandidateChecker`](create-extension-candidate-checker.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="create-extension-candidate-checker.html"><span class="nf">createExtensionCandidateChecker</span></a><span class="p">(</span>
    originalFile<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>
    nameExpression<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">, </span>
    explicitReceiver<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="-ka-completion-extension-candidate-checker/index.html">KaCompletionExtensionCandidateChecker</a>
</span></code></pre></div>
</div>


<div markdown>

Returns an extension applicability checker for the given context [`nameExpression`](create-extension-candidate-checker.md). The function is meant to only be used for providing auto-completion for Kotlin in IntelliJ IDEA.


</div>

</div>
### [`resolveToCall`](resolve-to-call.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="resolve-to-call.html"><span class="nf">resolveToCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/index.html">KaCallInfo</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md) to a [`KaCallInfo`](../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/index.md) object. [`KaCallInfo`](../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/index.md) either contains a successfully resolved call or an error with a list of candidate calls and a diagnostic.


</div>

</div>
### [`resolveToCallCandidates`](resolve-to-call-candidates.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="resolve-to-call-candidates.html"><span class="nf">resolveToCallCandidates</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-candidate-info/index.html">KaCallCandidateInfo</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all candidates considered during [overload resolution](https://kotlinlang.org/spec/overload-resolution.html) for the call corresponding to this [`KtElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md).


</div>

</div>
### [`resolveToSymbol`](resolve-to-symbol.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.html">KtReference</a><span class="p">.</span><a href="resolve-to-symbol.html"><span class="nf">resolveToSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtReference`](../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.md) to a symbol.


</div>

</div>
### [`resolveToSymbols`](resolve-to-symbols.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.html">KtReference</a><span class="p">.</span><a href="resolve-to-symbols.html"><span class="nf">resolveToSymbols</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtReference`](../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.md) to symbols.


</div>

</div>
### [`scopeContext`](scope-context.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="scope-context.html"><span class="nf">scopeContext</span></a><span class="p">(</span>position<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="-ka-scope-context/index.html">KaScopeContext</a>
</span></code></pre></div>
</div>


<div markdown>

Computes the lexical scope context for a given [`position`](scope-context.md) in the [`KtFile`](../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md). The scope context includes all scopes that are relevant for the given position, together with all available implicit receivers.


</div>

</div>
