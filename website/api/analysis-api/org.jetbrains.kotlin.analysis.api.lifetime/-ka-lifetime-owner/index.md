---
tags:
 - jvm
title: "KaLifetimeOwner"
---

# KaLifetimeOwner

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaLifetimeOwner</a>
</span></code></pre></div>An Analysis API entity with a lifetime bound to the [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) where the entity was created.

The most common lifetime owners are [`symbols`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) and [`types`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md), but there are many additional kinds of lifetime owners created by the Analysis API which aren't symbols or types.

See the documentation for [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) to find out more about lifetime management.

#### Inheritors


 - [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)
 - [`KaAnnotation`](../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation/index.md)
 - [`KaAnnotationList`](../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-list/index.md)
 - [`KaAnnotationValue`](../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-value/index.md)
 - [`KaNamedAnnotationValue`](../../org.jetbrains.kotlin.analysis.api.annotations/-ka-named-annotation-value/index.md)
 - [`KaContextReceiver`](../../org.jetbrains.kotlin.analysis.api.base/-ka-context-receiver/index.md)
 - [`KaContextReceiversOwner`](../../org.jetbrains.kotlin.analysis.api.base/-ka-context-receivers-owner/index.md)
 - [`KaCompilationOptions`](../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-options/index.md)
 - [`KaCompilationOptionsBuilder`](../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compilation-options-builder/index.md)
 - [`KaCompilerPluginGeneratedDeclarations`](../../org.jetbrains.kotlin.analysis.api.compilerPlugins/-ka-compiler-plugin-generated-declarations/index.md)
 - [`KaCompletionExtensionCandidateChecker`](../../org.jetbrains.kotlin.analysis.api.components/-ka-completion-extension-candidate-checker/index.md)
 - [`KaExtensionApplicabilityResult`](../../org.jetbrains.kotlin.analysis.api.components/-ka-extension-applicability-result/index.md)
 - [`KaImplicitReceiverSmartCast`](../../org.jetbrains.kotlin.analysis.api.components/-ka-implicit-receiver-smart-cast/index.md)
 - [`KaScopeContext`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-context/index.md)
 - [`KaSmartCastPossibility`](../../org.jetbrains.kotlin.analysis.api.components/-ka-smart-cast-possibility/index.md)
 - [`KaSmartCastSource`](../../org.jetbrains.kotlin.analysis.api.components/-ka-smart-cast-source/index.md)
 - [`KaScopeImplicitValue`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-implicit-value/index.md)
 - [`KaScopeWithKind`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-with-kind/index.md)
 - [`KaSessionComponent`](../../org.jetbrains.kotlin.analysis.api.components/-ka-session-component/index.md)
 - [`KaTypeBuilder`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-builder/index.md)
 - [`KaContractBooleanExpression`](../../org.jetbrains.kotlin.analysis.api.contracts.description.booleans/-ka-contract-boolean-expression/index.md)
 - [`KaContractEffectDeclaration`](../../org.jetbrains.kotlin.analysis.api.contracts.description/-ka-contract-effect-declaration/index.md)
 - [`KaContractConstantValue`](../../org.jetbrains.kotlin.analysis.api.contracts.description/-ka-contract-constant-value/index.md)
 - [`KaContractParameterValue`](../../org.jetbrains.kotlin.analysis.api.contracts.description/-ka-contract-parameter-value/index.md)
 - [`KaImplicitReceiverSmartCast`](../../org.jetbrains.kotlin.analysis.api.dataflow/-ka-implicit-receiver-smart-cast/index.md)
 - [`KaSmartCastInfo`](../../org.jetbrains.kotlin.analysis.api.dataflow/-ka-smart-cast-info/index.md)
 - [`KaDiagnostic`](../../org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic/index.md)
 - [`KaDiagnostics`](../../org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostics/index.md)
 - [`Symbol`](../../org.jetbrains.kotlin.analysis.api.rendering/-ka-text-attribute/-symbol/index.md)
 - [`KaCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call/index.md)
 - [`KaCallCandidate`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-candidate/index.md)
 - [`KaCallCandidateInfo`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-candidate-info/index.md)
 - [`KaCallInfo`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/index.md)
 - [`KaCallResolutionAttempt`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-resolution-attempt/index.md)
 - [`KaSimpleOrMultiCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-or-multi-call/index.md)
 - [`KaCompoundOperation`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-compound-operation/index.md)
 - [`KaPartiallyAppliedSymbol`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-partially-applied-symbol/index.md)
 - [`KaReceiverValue`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-receiver-value/index.md)
 - [`KaSymbolResolutionAttempt`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-symbol-resolution-attempt/index.md)
 - [`KaScopeLike`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope-like/index.md)
 - [`KaCallableSignature`](../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.md)
 - [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md)
 - [`KaBuiltinTypes`](../../org.jetbrains.kotlin.analysis.api.types/-ka-builtin-types/index.md)
 - [`KaClassTypeQualifier`](../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type-qualifier/index.md)
 - [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md)
 - [`KaSubstitutorBuilder`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor-builder/index.md)
 - [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)
 - [`KaFunctionValueParameter`](../../org.jetbrains.kotlin.analysis.api.types/-ka-function-value-parameter/index.md)
 - [`KaTypeProjection`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type-projection/index.md)
 - [`KaTypeCreator`](../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-type-creator/index.md)
 - [`KaUseSiteVisibilityChecker`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md)



</div>

## Properties
### token

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#token">token</a><span class="o">: </span><a href="../-ka-lifetime-token/index.html">KaLifetimeToken</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaLifetimeToken`](../-ka-lifetime-token/index.md) which determines the lifetime of the lifetime owner.


</div>

</div>
## Functions
### assertIsValidAndAccessible

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

**See also**



 - [`withValidityAssertion`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../-ka-lifetime-token/index.html">KaLifetimeToken</a><span class="p">.</span><a href="../-ka-lifetime-token/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### isValid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#isvalid"><span class="nf">isValid</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the lifetime owner is still valid, i.e. we are still in the scope of the lifetime owner's regular lifetime.

[`isValid`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#isvalid) does not check whether the lifetime owner is [`accessible`](../-ka-lifetime-token/index.md#isaccessible).


</div>

</div>
### withValidityAssertion

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="o">> </span><a href="index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion"><span class="nf">withValidityAssertion</span></a><span class="p">(</span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a>
</span></code></pre></div>
</div>


<div markdown>

Executes [`action`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion) only if the [`KaLifetimeOwner`](index.md) is still [`valid`](../-ka-lifetime-token/index.md#isvalid) and [`accessible`](../-ka-lifetime-token/index.md#isaccessible). Otherwise, throws a validity exception based on the concrete violation.

All public endpoints of the Analysis API are protected by validity assertions to ensure that lifetime owners aren't misused outside the scope of their regular lifetime.


</div>

</div>
