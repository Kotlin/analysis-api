---
tags:
 - jvm
title: "KaCompilationOptionsBuilder"
---

# KaCompilationOptionsBuilder

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaCompilationOptionsBuilder</a> : <a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>A DSL builder for [`KaCompilationOptions`](../-ka-compilation-options/index.md).

Provides methods to configure the compilation target, language settings, JVM-specific options, error handling, and code fragment parameters. Instances are created internally by [`createCompilationOptions`](../create-compilation-options.md) and [`modify`](../../org.jetbrains.kotlin.analysis.api.components/-ka-compilation-options/index.md#modify).

#### See also


 - [`KaCompilationOptions`](../-ka-compilation-options/index.md)


#### Inheritors


 - [`KaCompilationOptionsBuilder`](../../org.jetbrains.kotlin.analysis.api.components/-ka-compilation-options-builder/index.md)



</div>

## Properties
### [`token`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#token)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#token">token</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaLifetimeToken`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md) which determines the lifetime of the lifetime owner.


</div>

</div>
## Functions
### allowedErrorFilter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#allowederrorfilter"><span class="nf">allowedErrorFilter</span></a><span class="p">(</span>value<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic/index.html">KaDiagnostic</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Sets a filter for allowed errors. Compilation will be aborted if there are errors that this filter rejects.

A filter returning `true` means the error is allowed and will not abort compilation. Defaults to rejecting all errors.


</div>

</div>
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### codeFragmentClassName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#codefragmentclassname"><span class="nf">codeFragmentClassName</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Sets the simple class name for the code fragment facade class. Only relevant when compiling [`KtCodeFragment`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-code-fragment/index.md) files.


</div>

</div>
### codeFragmentMethodName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#codefragmentmethodname"><span class="nf">codeFragmentMethodName</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Sets the entry point method name for the code fragment. Only relevant when compiling [`KtCodeFragment`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-code-fragment/index.md) files.


</div>

</div>
### disableCallAssertions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#disablecallassertions"><span class="nf">disableCallAssertions</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Disables null-check assertions on receiver and arguments of platform-typed calls.


</div>

</div>
### disableInline

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#disableinline"><span class="nf">disableInline</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Disables inlining of `inline` functions.


</div>

</div>
### disableOptimization

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#disableoptimization"><span class="nf">disableOptimization</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Disables optimizations in generated code.


</div>

</div>
### disableParameterAssertions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#disableparameterassertions"><span class="nf">disableParameterAssertions</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Disables null-check assertions on parameters.


</div>

</div>
### [`isValid`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#isvalid)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#isvalid"><span class="nf">isValid</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the lifetime owner is still valid, i.e. we are still in the scope of the lifetime owner's regular lifetime.


</div>

</div>
### jvmCompiledClassHandler

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compilation-options-builder/index.html#jvmcompiledclasshandler"><span class="nf">jvmCompiledClassHandler</span></a><span class="p">(</span>value<span class="o">: </span><a href="../-ka-compiled-class-handler/index.html">KaCompiledClassHandler</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Sets a handler which is called whenever a new class file is produced.

**See also**



 - [`KaCompiledClassHandler`](../-ka-compiled-class-handler/index.md)



</div>

</div>
### jvmExecutionStack

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#jvmexecutionstack"><span class="nf">jvmExecutionStack</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>PsiElement<span class="o">?</span><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Sets the execution stack for debugger code fragment compilation.

A sequence of PSI elements representing function calls or property accesses in the current execution stack, listed from the top to the bottom.


</div>

</div>
### jvmGenerateParameterMetadata

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#jvmgenerateparametermetadata"><span class="nf">jvmGenerateParameterMetadata</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Enables generation of parameter metadata (names and access flags) in class files.


</div>

</div>
### jvmOutputAsmListing

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#jvmoutputasmlisting"><span class="nf">jvmOutputAsmListing</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Enables output of ASM bytecode listing. When `true`, selects the test-mode class builder factory.


</div>

</div>
### jvmTarget

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#jvmtarget"><span class="nf">jvmTarget</span></a><span class="p">(</span>value<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-jvm-target/index.html">KaJvmTarget</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Sets the JVM bytecode target version.


</div>

</div>
### jvmUseInvokeDynamicForLambdas

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#jvmuseinvokedynamicforlambdas"><span class="nf">jvmUseInvokeDynamicForLambdas</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Uses `invokedynamic` for lambdas instead of generating anonymous classes.


</div>

</div>
### jvmUseInvokeDynamicForSamConversions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#jvmuseinvokedynamicforsamconversions"><span class="nf">jvmUseInvokeDynamicForSamConversions</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Uses `invokedynamic` for SAM conversions instead of generating anonymous classes.


</div>

</div>
### languageVersionSettings

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#languageversionsettings"><span class="nf">languageVersionSettings</span></a><span class="p">(</span>value<span class="o">: </span>LanguageVersionSettings<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Sets the language version settings used during compilation.


</div>

</div>
### moduleActualizer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compilation-options-builder/index.html#moduleactualizer"><span class="nf">moduleActualizer</span></a><span class="p">(</span>value<span class="o">: </span><a href="../-ka-compiler-facility-module-actualizer/index.html">KaCompilerFacilityModuleActualizer</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Sets a custom actualizer for common source modules in multiplatform projects.

**See also**



 - [`KaCompilerFacilityModuleActualizer`](../-ka-compiler-facility-module-actualizer/index.md)



</div>

</div>
### moduleName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#modulename"><span class="nf">moduleName</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Sets the module name used for the compiled output.


</div>

</div>
### stubUnboundIrSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#stubunboundirsymbols"><span class="nf">stubUnboundIrSymbols</span></a><span class="p">(</span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Whether unbound IR symbols should be stubbed instead of linked.

This should be enabled if the compiled file could refer to symbols defined in another file of the same module.


</div>

</div>
### target

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compilation-options-builder/index.html#target"><span class="nf">target</span></a><span class="p">(</span>value<span class="o">: </span><a href="../-ka-compilation-target/index.html">KaCompilationTarget</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Sets the target platform for compilation. Must be provided.


</div>

</div>
### [`withValidityAssertion`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion"><span class="nf">withValidityAssertion</span></a><span class="p">(</span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a>
</span></code></pre></div>
</div>


<div markdown>

Executes [`action`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion) only if the [`KaLifetimeOwner`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.md) is still [`valid`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md#isvalid) and [`accessible`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md#isaccessible). Otherwise, throws a validity exception based on the concrete violation.


</div>

</div>
