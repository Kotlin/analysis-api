---
tags:
 - jvm
title: "KaSessionComponent"
---

# KaSessionComponent

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaSessionComponent</a> : <a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>A component of a [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md).

Session components mix functions and properties into the session, which allows using them directly from an [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) block where a [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) is available as a receiver. As such, functions from session components define a large part of the Analysis API's surface, in addition to other [`lifetime owners`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.md) like [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md).

<strong>Important:</strong> Any public function or property in a "session component" is directly available in a [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) context. There is no need to first retrieve the session component in any way.

#### Example
```kotlin
// element: KtDeclaration
analyze(element) { // this: KaSession
    element.symbol
}
```

While [`symbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md#symbol) is actually a property from the [`KaSymbolProvider`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md) session component, it is usable directly in the [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) context because the property has been mixed into the session.

All public API components inherited from [`KaSessionComponent`](index.md) are expected to be direct children of [`KaSessionComponent`](index.md). That's required for the correctness of the Analysis API context parameter bridge checker, which ensures that each API endpoint from session components has a corresponding context parameter bridge in the same file.

#### Inheritors


 - [`KaAnalysisScopeProvider`](../-ka-analysis-scope-provider/index.md)
 - [`KaCompilerFacility`](../-ka-compiler-facility/index.md)
 - [`KaCompilerPluginGeneratedDeclarationsProvider`](../-ka-compiler-plugin-generated-declarations-provider/index.md)
 - [`KaCompletionCandidateChecker`](../-ka-completion-candidate-checker/index.md)
 - [`KaDataFlowProvider`](../-ka-data-flow-provider/index.md)
 - [`KaDiagnosticProvider`](../-ka-diagnostic-provider/index.md)
 - [`KaEvaluator`](../-ka-evaluator/index.md)
 - [`KaExpressionInformationProvider`](../-ka-expression-information-provider/index.md)
 - [`KaExpressionTypeProvider`](../-ka-expression-type-provider/index.md)
 - [`KaJavaInteroperabilityComponent`](../-ka-java-interoperability-component/index.md)
 - [`KaKDocProvider`](../-ka-k-doc-provider/index.md)
 - [`KaReferenceShortener`](../-ka-reference-shortener/index.md)
 - [`KaRenderer`](../-ka-renderer/index.md)
 - [`KaResolveExtensionInfoProvider`](../-ka-resolve-extension-info-provider/index.md)
 - [`KaResolver`](../-ka-resolver/index.md)
 - [`KaScopeProvider`](../-ka-scope-provider/index.md)
 - [`KaSignatureSubstitutor`](../-ka-signature-substitutor/index.md)
 - [`KaSourceProvider`](../-ka-source-provider/index.md)
 - [`KaSubstitutorProvider`](../-ka-substitutor-provider/index.md)
 - [`KaSymbolInformationProvider`](../-ka-symbol-information-provider/index.md)
 - [`KaSymbolRelationProvider`](../-ka-symbol-relation-provider/index.md)
 - [`KaTypeCreator`](../-ka-type-creator/index.md)
 - [`KaTypeCreatorProvider`](../-ka-type-creator-provider/index.md)
 - [`KaTypeInformationProvider`](../-ka-type-information-provider/index.md)
 - [`KaTypeProvider`](../-ka-type-provider/index.md)
 - [`KaTypeRelationChecker`](../-ka-type-relation-checker/index.md)
 - [`KaVisibilityChecker`](../-ka-visibility-checker/index.md)
 - [`KaSymbolProvider`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md)



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
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
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
