---
tags:
 - jvm
title: "KaInternalsResolver"
---

# KaInternalsResolver

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaInternalsResolver</a>
</span></code></pre></div>
</div>

## Functions
### collectCallCandidates

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#collectcallcandidates"><span class="nf">collectCallCandidates</span></a><span class="p">(</span>resolvableCall<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-candidate/index.html">KaCallCandidate</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### contextSensitiveResolutionStatus

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#contextsensitiveresolutionstatus"><span class="nf">contextSensitiveResolutionStatus</span></a><span class="p">(</span>simpleNameExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-context-sensitive-resolution-status/index.html">KaContextSensitiveResolutionStatus</a>
</span></code></pre></div>
</div>

</div>
### isImplicitReferenceToCompanion

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#isimplicitreferencetocompanion"><span class="nf">isImplicitReferenceToCompanion</span></a><span class="p">(</span>simpleNameExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#isimplicitreferencetocompanion"><span class="nf">isImplicitReferenceToCompanion</span></a><span class="p">(</span>reference<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.html">KtReference</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### resolveSuccessfulCall

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>resolvableCall<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>annotationEntry<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-annotation-call/index.html">KaAnnotationCall</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>superTypeCallEntry<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.html">KtSuperTypeCallEntry</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>constructorDelegationCall<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>constructorDelegationReferenceExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.html">KtConstructorDelegationReferenceExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>callElement<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.html">KtCallElement</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>callableReferenceExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.html">KtCallableReferenceExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-callable-reference-call/index.html">KaCallableReferenceCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>arrayAccessExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.html">KtArrayAccessExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>collectionLiteralExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.html">KtCollectionLiteralExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>enumEntrySuperclassReferenceExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.html">KtEnumEntrySuperclassReferenceExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>whenConditionInRange<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.html">KtWhenConditionInRange</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>destructuringDeclarationEntry<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>qualifiedExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>forExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.html">KtForExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-for-loop-call/index.html">KaForLoopCall</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>propertyDelegate<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.html">KtPropertyDelegate</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-property-call/index.html">KaDelegatedPropertyCall</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>constructorCalleeExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.html">KtConstructorCalleeExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulcall"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span>nameReferenceExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.html">KtNameReferenceExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### resolveSuccessfulSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>resolvable<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>annotationEntry<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>superTypeCallEntry<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.html">KtSuperTypeCallEntry</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>constructorDelegationCall<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>constructorDelegationReferenceExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.html">KtConstructorDelegationReferenceExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>callElement<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.html">KtCallElement</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>callableReferenceExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.html">KtCallableReferenceExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>arrayAccessExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.html">KtArrayAccessExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>collectionLiteralExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.html">KtCollectionLiteralExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>enumEntrySuperclassReferenceExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.html">KtEnumEntrySuperclassReferenceExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>labelReferenceExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-label-reference-expression/index.html">KtLabelReferenceExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>returnExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-return-expression/index.html">KtReturnExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>whenConditionInRange<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.html">KtWhenConditionInRange</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>destructuringDeclarationEntry<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>qualifiedExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>constructorCalleeExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.html">KtConstructorCalleeExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>instanceExpressionWithLabel<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-instance-expression-with-label/index.html">KtInstanceExpressionWithLabel</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>nullableType<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-nullable-type/index.html">KtNullableType</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>functionType<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-function-type/index.html">KtFunctionType</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>typeReference<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.html">KtTypeReference</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>classLiteralExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-literal-expression/index.html">KtClassLiteralExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>superTypeEntry<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-entry/index.html">KtSuperTypeEntry</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbol"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span>delegatedSuperTypeEntry<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-delegated-super-type-entry/index.html">KtDelegatedSuperTypeEntry</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### resolveSuccessfulSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvesuccessfulsymbols"><span class="nf">resolveSuccessfulSymbols</span></a><span class="p">(</span>resolvable<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### resolveToCall

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvetocall"><span class="nf">resolveToCall</span></a><span class="p">(</span>element<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/index.html">KaCallInfo</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### resolveToCallCandidates

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvetocallcandidates"><span class="nf">resolveToCallCandidates</span></a><span class="p">(</span>element<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-candidate-info/index.html">KaCallCandidateInfo</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### resolveToSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvetosymbol"><span class="nf">resolveToSymbol</span></a><span class="p">(</span>reference<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.html">KtReference</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### resolveToSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvetosymbols"><span class="nf">resolveToSymbols</span></a><span class="p">(</span>reference<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.html">KtReference</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### tryResolveCall

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#tryresolvecall"><span class="nf">tryResolveCall</span></a><span class="p">(</span>resolvableCall<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#tryresolvecall"><span class="nf">tryResolveCall</span></a><span class="p">(</span>forExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.html">KtForExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-for-loop-call-resolution-attempt/index.html">KaForLoopCallResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#tryresolvecall"><span class="nf">tryResolveCall</span></a><span class="p">(</span>propertyDelegate<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.html">KtPropertyDelegate</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-property-call-resolution-attempt/index.html">KaDelegatedPropertyCallResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### tryResolveSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#tryresolvesymbols"><span class="nf">tryResolveSymbols</span></a><span class="p">(</span>resolvable<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### usesContextSensitiveResolution

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#usescontextsensitiveresolution"><span class="nf">usesContextSensitiveResolution</span></a><span class="p">(</span>reference<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.html">KtReference</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#usescontextsensitiveresolution"><span class="nf">usesContextSensitiveResolution</span></a><span class="p">(</span>simpleNameExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
