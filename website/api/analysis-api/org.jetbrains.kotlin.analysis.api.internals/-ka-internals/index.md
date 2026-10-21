---
tags:
 - jvm
title: "KaInternals"
---

# KaInternals

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaInternals</a>
</span></code></pre></div>An internal facade that aggregates the Analysis API implementation behind every public `context(session: KaSession)` endpoint.

Each capability is exposed as a dedicated `KaInternals<Xxx>` proxy, accessible through a property on this interface. Public endpoints never touch a session implementation directly; they delegate through this facade, for example `session.internals.typeRelationChecker.isSubtypeOf(...)`.

[`KaInternals`](index.md) is intentionally <strong>not</strong> a supertype of [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md): [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) stays a clean marker, while session implementations additionally implement [`KaInternals`](index.md). This is why the [`internals`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.internals/index.md) bridge can cast a [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) to [`KaInternals`](index.md).

This is an implementation detail with no compatibility guarantees and must not be used outside the Analysis API implementation modules.


</div>

## Properties
### analysisScopeProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#analysisscopeprovider">analysisScopeProvider</a><span class="o">: </span><a href="../-ka-internals-analysis-scope-provider/index.html">KaInternalsAnalysisScopeProvider</a>
</span></code></pre></div>
</div>

</div>
### compilerFacility

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#compilerfacility">compilerFacility</a><span class="o">: </span><a href="../-ka-internals-compiler-facility/index.html">KaInternalsCompilerFacility</a>
</span></code></pre></div>
</div>

</div>
### compilerPluginGeneratedDeclarationsProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#compilerplugingenerateddeclarationsprovider">compilerPluginGeneratedDeclarationsProvider</a><span class="o">: </span><a href="../-ka-internals-compiler-plugin-generated-declarations-provider/index.html">KaInternalsCompilerPluginGeneratedDeclarationsProvider</a>
</span></code></pre></div>
</div>

</div>
### completionCandidateChecker

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#completioncandidatechecker">completionCandidateChecker</a><span class="o">: </span><a href="../-ka-internals-completion-candidate-checker/index.html">KaInternalsCompletionCandidateChecker</a>
</span></code></pre></div>
</div>

</div>
### dataFlowProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#dataflowprovider">dataFlowProvider</a><span class="o">: </span><a href="../-ka-internals-data-flow-provider/index.html">KaInternalsDataFlowProvider</a>
</span></code></pre></div>
</div>

</div>
### diagnosticProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#diagnosticprovider">diagnosticProvider</a><span class="o">: </span><a href="../-ka-internals-diagnostic-provider/index.html">KaInternalsDiagnosticProvider</a>
</span></code></pre></div>
</div>

</div>
### evaluator

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#evaluator">evaluator</a><span class="o">: </span><a href="../-ka-internals-evaluator/index.html">KaInternalsEvaluator</a>
</span></code></pre></div>
</div>

</div>
### expressionInformationProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#expressioninformationprovider">expressionInformationProvider</a><span class="o">: </span><a href="../-ka-internals-expression-information-provider/index.html">KaInternalsExpressionInformationProvider</a>
</span></code></pre></div>
</div>

</div>
### expressionTypeProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#expressiontypeprovider">expressionTypeProvider</a><span class="o">: </span><a href="../-ka-internals-expression-type-provider/index.html">KaInternalsExpressionTypeProvider</a>
</span></code></pre></div>
</div>

</div>
### javaInteroperabilityComponent

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#javainteroperabilitycomponent">javaInteroperabilityComponent</a><span class="o">: </span><a href="../-ka-internals-java-interoperability-component/index.html">KaInternalsJavaInteroperabilityComponent</a>
</span></code></pre></div>
</div>

</div>
### kDocProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#kdocprovider">kDocProvider</a><span class="o">: </span><a href="../-ka-internals-k-doc-provider/index.html">KaInternalsKDocProvider</a>
</span></code></pre></div>
</div>

</div>
### legacyTypeCreator

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#legacytypecreator">legacyTypeCreator</a><span class="o">: </span><a href="../-ka-internals-type-creator/index.html">KaInternalsTypeCreator</a>
</span></code></pre></div>
</div>

</div>
### referenceShortener

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#referenceshortener">referenceShortener</a><span class="o">: </span><a href="../-ka-internals-reference-shortener/index.html">KaInternalsReferenceShortener</a>
</span></code></pre></div>
</div>

</div>
### renderer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#renderer">renderer</a><span class="o">: </span><a href="../-ka-internals-renderer/index.html">KaInternalsRenderer</a>
</span></code></pre></div>
</div>

</div>
### resolveExtensionInfoProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#resolveextensioninfoprovider">resolveExtensionInfoProvider</a><span class="o">: </span><a href="../-ka-internals-resolve-extension-info-provider/index.html">KaInternalsResolveExtensionInfoProvider</a>
</span></code></pre></div>
</div>

</div>
### resolver

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#resolver">resolver</a><span class="o">: </span><a href="../-ka-internals-resolver/index.html">KaInternalsResolver</a>
</span></code></pre></div>
</div>

</div>
### scopeProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#scopeprovider">scopeProvider</a><span class="o">: </span><a href="../-ka-internals-scope-provider/index.html">KaInternalsScopeProvider</a>
</span></code></pre></div>
</div>

</div>
### signatureSubstitutor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#signaturesubstitutor">signatureSubstitutor</a><span class="o">: </span><a href="../-ka-internals-signature-substitutor/index.html">KaInternalsSignatureSubstitutor</a>
</span></code></pre></div>
</div>

</div>
### sourceProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#sourceprovider">sourceProvider</a><span class="o">: </span><a href="../-ka-internals-source-provider/index.html">KaInternalsSourceProvider</a>
</span></code></pre></div>
</div>

</div>
### substitutorProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#substitutorprovider">substitutorProvider</a><span class="o">: </span><a href="../-ka-internals-substitutor-provider/index.html">KaInternalsSubstitutorProvider</a>
</span></code></pre></div>
</div>

</div>
### symbolInformationProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#symbolinformationprovider">symbolInformationProvider</a><span class="o">: </span><a href="../-ka-internals-symbol-information-provider/index.html">KaInternalsSymbolInformationProvider</a>
</span></code></pre></div>
</div>

</div>
### symbolProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#symbolprovider">symbolProvider</a><span class="o">: </span><a href="../-ka-internals-symbol-provider/index.html">KaInternalsSymbolProvider</a>
</span></code></pre></div>
</div>

</div>
### symbolRelationProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#symbolrelationprovider">symbolRelationProvider</a><span class="o">: </span><a href="../-ka-internals-symbol-relation-provider/index.html">KaInternalsSymbolRelationProvider</a>
</span></code></pre></div>
</div>

</div>
### typeCreatorProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#typecreatorprovider">typeCreatorProvider</a><span class="o">: </span><a href="../-ka-internals-type-creator-provider/index.html">KaInternalsTypeCreatorProvider</a>
</span></code></pre></div>
</div>

</div>
### typeInformationProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#typeinformationprovider">typeInformationProvider</a><span class="o">: </span><a href="../-ka-internals-type-information-provider/index.html">KaInternalsTypeInformationProvider</a>
</span></code></pre></div>
</div>

</div>
### typeProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#typeprovider">typeProvider</a><span class="o">: </span><a href="../-ka-internals-type-provider/index.html">KaInternalsTypeProvider</a>
</span></code></pre></div>
</div>

</div>
### typeRelationChecker

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#typerelationchecker">typeRelationChecker</a><span class="o">: </span><a href="../-ka-internals-type-relation-checker/index.html">KaInternalsTypeRelationChecker</a>
</span></code></pre></div>
</div>

</div>
### useSiteModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#usesitemodule">useSiteModule</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>

</div>
### visibilityChecker

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#visibilitychecker">visibilityChecker</a><span class="o">: </span><a href="../-ka-internals-visibility-checker/index.html">KaInternalsVisibilityChecker</a>
</span></code></pre></div>
</div>

</div>
