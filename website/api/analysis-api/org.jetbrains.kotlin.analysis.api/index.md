---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api"
---

# org.jetbrains.kotlin.analysis.api
## Types
### [`KaConstantInitializerValue`](-ka-constant-initializer-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-constant-initializer-value/index.html">KaConstantInitializerValue</a><span class="p">(</span><span class="kd">val </span>constant<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.base/-ka-constant-value/index.html">KaConstantValue</a><span class="p">, </span><span class="kd">val </span>initializerPsi<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span><span class="p">)</span> : <a href="-ka-initializer-value/index.html">KaInitializerValue</a>
</span></code></pre></div>
</div>


<div markdown>

An initializer value which can be evaluated to a [compile-time constant](https://kotlinlang.org/docs/properties.html#compile-time-constants), such as a string value, number, or `null` literal.


</div>

</div>
### [`KaConstantValueForAnnotation`](-ka-constant-value-for-annotation/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-constant-value-for-annotation/index.html">KaConstantValueForAnnotation</a><span class="p">(</span><span class="kd">val </span>annotationValue<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-value/index.html">KaAnnotationValue</a><span class="p">, </span><span class="kd">val </span>initializerPsi<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span><span class="p">)</span> : <a href="-ka-initializer-value/index.html">KaInitializerValue</a>
</span></code></pre></div>
</div>


<div markdown>

An initializer value of a property of an annotation, which cannot be represented as a [compile-time constant](https://kotlinlang.org/docs/properties.html#compile-time-constants), but can be represented as a [`KaAnnotationValue`](../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-value/index.md).


</div>

</div>
### [`KaContextParameterApi`](-ka-context-parameter-api/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"An API using the experimental 'context parameters' language feature."</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-ka-context-parameter-api/index.html">KaContextParameterApi</a>
</span></code></pre></div>
</div>


<div markdown>

Marks an API that uses context parameters, an experimental language feature. The API is intended for user consumption, but it's based on a non-stable language feature that may change or be removed in the future.


</div>

</div>
### [`KaExperimentalApi`](-ka-experimental-api/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html">AnnotationTarget.CLASS</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html">AnnotationTarget.CONSTRUCTOR</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html">AnnotationTarget.TYPEALIAS</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"Experimental API with no compatibility guarantees"</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-ka-experimental-api/index.html">KaExperimentalApi</a>
</span></code></pre></div>
</div>


<div markdown>

Marks an API as experimental. The API is intended for user consumption, but it's not stable and might change at any moment, or even be removed, without a deprecation cycle.


</div>

</div>
### [`KaIdeApi`](-ka-ide-api/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html">AnnotationTarget.CLASS</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html">AnnotationTarget.CONSTRUCTOR</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html">AnnotationTarget.TYPEALIAS</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"Internal API which is used only from the IntelliJ Kotlin plugin. Such an API should not be used in other places since it has no compatibility guarantees"</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-ka-ide-api/index.html">KaIdeApi</a>
</span></code></pre></div>
</div>


<div markdown>

Marks an API as designed for and internal to the Kotlin IntelliJ plugin. The API is not intended for public user consumption and does not have any compatibility guarantees.


</div>

</div>
### [`KaImplementationDetail`](-ka-implementation-detail/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html">AnnotationTarget.CLASS</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html">AnnotationTarget.CONSTRUCTOR</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html">AnnotationTarget.TYPEALIAS</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"Internal API which should not be used outside the Analysis API implementation modules as it does not have any compatibility guarantees"</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-ka-implementation-detail/index.html">KaImplementationDetail</a>
</span></code></pre></div>
</div>


<div markdown>

Marks an API as an implementation detail of the Analysis API. Such APIs are not intended to be used outside the implementation of the Analysis API and have no compatibility guarantees.


</div>

</div>
### [`KaInitializerValue`](-ka-initializer-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-initializer-value/index.html">KaInitializerValue</a>
</span></code></pre></div>
</div>


<div markdown>

A value of a property or variable initializer.


</div>

</div>
### [`KaNonConstantInitializerValue`](-ka-non-constant-initializer-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-non-constant-initializer-value/index.html">KaNonConstantInitializerValue</a><span class="p">(</span><span class="kd">val </span>initializerPsi<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span><span class="p">)</span> : <a href="-ka-initializer-value/index.html">KaInitializerValue</a>
</span></code></pre></div>
</div>


<div markdown>

An initializer value which cannot be represented as a [compile-time constant](https://kotlinlang.org/docs/properties.html#compile-time-constants).


</div>

</div>
### [`KaNonPublicApi`](-ka-non-public-api/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html">AnnotationTarget.CLASS</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html">AnnotationTarget.CONSTRUCTOR</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html">AnnotationTarget.TYPEALIAS</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"Internal API which is used in projects developed by JetBrains"</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-ka-non-public-api/index.html">KaNonPublicApi</a>
</span></code></pre></div>
</div>


<div markdown>

Marks an API as internal to projects developed by JetBrains. Such APIs are not intended for public user consumption and have less strict compatibility guarantees. For example, a change to the API might be implemented without a deprecation cycle.


</div>

</div>
### [`KaPlatformInterface`](-ka-platform-interface/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html">AnnotationTarget.CLASS</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html">AnnotationTarget.CONSTRUCTOR</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html">AnnotationTarget.TYPEALIAS</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"An API intended for Analysis API implementations and platforms. The API is neither stable nor intended for user consumption."</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-ka-platform-interface/index.html">KaPlatformInterface</a>
</span></code></pre></div>
</div>


<div markdown>

Marks an API intended for Analysis API implementations and platforms. The API is neither stable nor intended for user consumption.


</div>

</div>
### [`KaSession`](-ka-session/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-session/index.html">KaSession</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html">KaResolver</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html">KaSymbolRelationProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-diagnostic-provider/index.html">KaDiagnosticProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html">KaScopeProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-completion-candidate-checker/index.html">KaCompletionCandidateChecker</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.html">KaExpressionTypeProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html">KaTypeProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html">KaTypeInformationProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html">KaSymbolProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.html">KaJavaInteroperabilityComponent</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.html">KaSymbolInformationProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-type-relation-checker/index.html">KaTypeRelationChecker</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-expression-information-provider/index.html">KaExpressionInformationProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-evaluator/index.html">KaEvaluator</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-reference-shortener/index.html">KaReferenceShortener</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-renderer/index.html">KaRenderer</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-visibility-checker/index.html">KaVisibilityChecker</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.html">KaTypeCreator</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.html">KaTypeCreatorProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-analysis-scope-provider/index.html">KaAnalysisScopeProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html">KaSignatureSubstitutor</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-resolve-extension-info-provider/index.html">KaResolveExtensionInfoProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-plugin-generated-declarations-provider/index.html">KaCompilerPluginGeneratedDeclarationsProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-facility/index.html">KaCompilerFacility</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.html">KaSubstitutorProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-data-flow-provider/index.html">KaDataFlowProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-source-provider/index.html">KaSourceProvider</a>, <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-k-doc-provider/index.html">KaKDocProvider</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaSession`](-ka-session/index.md), also called an analysis session, is the entry point to all frontend-related work. It has the following contracts:


</div>

</div>
### [`KaSpiExtensionPoint`](-ka-spi-extension-point/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"An API designed for implementation only. Direct usage has no compatibility guarantees."</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-ka-spi-extension-point/index.html">KaSpiExtensionPoint</a>
</span></code></pre></div>
</div>


<div markdown>

Marks an API as a service provider interface extension point. Such APIs are designed to be implemented, not called directly. There are no compatibility guarantees for usage of these APIs, only for their implementation.


</div>

</div>
