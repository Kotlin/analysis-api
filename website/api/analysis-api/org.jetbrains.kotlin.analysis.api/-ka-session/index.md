---
tags:
 - jvm
title: "KaSession"
---

# KaSession

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaSession</a> : <a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html">KaResolver</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html">KaSymbolRelationProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-diagnostic-provider/index.html">KaDiagnosticProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html">KaScopeProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-completion-candidate-checker/index.html">KaCompletionCandidateChecker</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.html">KaExpressionTypeProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html">KaTypeProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html">KaTypeInformationProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html">KaSymbolProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.html">KaJavaInteroperabilityComponent</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.html">KaSymbolInformationProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-relation-checker/index.html">KaTypeRelationChecker</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-information-provider/index.html">KaExpressionInformationProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-evaluator/index.html">KaEvaluator</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-reference-shortener/index.html">KaReferenceShortener</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-renderer/index.html">KaRenderer</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-visibility-checker/index.html">KaVisibilityChecker</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.html">KaTypeCreator</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.html">KaTypeCreatorProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-analysis-scope-provider/index.html">KaAnalysisScopeProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html">KaSignatureSubstitutor</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolve-extension-info-provider/index.html">KaResolveExtensionInfoProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-plugin-generated-declarations-provider/index.html">KaCompilerPluginGeneratedDeclarationsProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-facility/index.html">KaCompilerFacility</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.html">KaSubstitutorProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-data-flow-provider/index.html">KaDataFlowProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-source-provider/index.html">KaSourceProvider</a>, <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-k-doc-provider/index.html">KaKDocProvider</a>
</span></code></pre></div>[`KaSession`](index.md), also called an analysis session, is the entry point to all frontend-related work. It has the following contracts:

 - It should not be accessed outside a [read action](https://plugins.jetbrains.com/docs/intellij/threading-model.html).


 - It should only be accessed in restricted analysis mode (see `KotlinRestrictedAnalysisService` in the platform interface) when restricted analysis is allowed by the Analysis API platform.


 - It should not be accessed from the event dispatch thread (EDT) or a write action unless explicitly allowed ([`allowAnalysisOnEdt`](../../org.jetbrains.kotlin.analysis.api.permissions/allow-analysis-on-edt.md), [`allowAnalysisFromWriteAction`](../../org.jetbrains.kotlin.analysis.api.permissions/allow-analysis-from-write-action.md)).


 - It should not be leaked outside the [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) call it was created in. To ensure that an analysis session isn't leaked, there are additional conventions, explained further below.


 - All [`lifetime owners`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.md)s retrieved from an analysis session should not be leaked outside the [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) call that spawned the analysis session.


To pass a lifetime owner from one `analyze` call to another, use a <strong>pointer</strong>:

 - [`KaSymbolProvider`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md) for [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md)s using [`KaSymbol.createPointer`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md#createpointer).


 - [`KaTypePointer`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type-pointer/index.md) for [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)s using [`KaType.createPointer`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md#createpointer).


To create a [`KaSession`](index.md), please use [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) or one of its siblings.

### Conventions to avoid leakage
It is crucial to avoid leaking the analysis session outside the read action it was created in, as the analysis session itself and all lifetime owners retrieved from it will become invalid. An analysis session also shouldn't be leaked from the [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) call it was created in.

It is forbidden to store an analysis session in a variable, parameter, or property. From the [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) block which provides the analysis session, the analysis session should be passed to functions via an context parameter. For example:

```kotlin
context(session: KaSession)
fun foo() { ... }
```

### PsiElement as input
Some API components accept PsiElements as input. For example, [`KaSymbolProvider.symbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md#symbol) takes a [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md) and returns a [`KaDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) for it.

In this case, the symbol may be created only for elements which are a part of the current [`KaSession`](index.md). And it means that [`KaAnalysisScopeProvider.canBeAnalysed`](../../org.jetbrains.kotlin.analysis.api.components/-ka-analysis-scope-provider/index.md#canbeanalysed) is <strong>true</strong> for such elements.

If this condition is not met, an exception will be thrown to prevent undefined behavior.

### Nested analysis
While [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) calls can be nested, it is currently not recommended to use [`lifetime owners`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.md) from the outer analysis context in the inner analysis context. This section illustrates the reasons behind this recommendation.

As there is one analysis session per use-site [`module`](../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md), in the best case, the analyzed element will be from the same module. Then the nested [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) call will simply perform the analysis in the same analysis session context. As such, it would be possible to use a symbol from the outer analysis context in the inner [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) call. But if it's the same use-site module, it's better to pass the analysis session down the call chain directly, instead of calling [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) again. In addition, relying on two elements having the same use-site module is an open invitation for bugs.

In more problematic cases, nested analysis may lead to various issues. First of all, a [`KaLifetimeOwner`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.md) can usually only be accessed in the session where it was created. Nesting [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) and starting analysis from a different use-site module will effectively change the current [`KaSession`](index.md) context. Any calls to symbols created in other sessions will result in an exception (unless the Analysis API platform defines different accessibility rules, such as the Standalone Analysis API).

Furthermore, even if such an access exception wasn't thrown, it is conceptually problematic to access a symbol in a different use-site context. Symbols are always viewed from a specific use-site context. It is unclear whether the symbol would even exist in the other use-site context. And even if the symbol is accessible, analyzing it may lead to different results due to differences in the use site's dependencies. For example, the supertypes of a class symbol may resolve to different declaration symbols.

In summary, using lifetime owners from an outer context in a nested [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) block will likely lead to an access exception given the accessibility rules of lifetime owners. And even if this wasn't the case, there's a conceptual problem with using a lifetime owner in the wrong session, as lifetime owners such as symbols are always viewed from a specific use-site context.

#### Example
```kotlin
// DO NOT DO THIS
analyze(element1) {
    val symbol1 = element1.symbol
    analyze(element2) {
         val type1 = symbol1.returnType // <-- error when `element1.module` != `element2.module`
    }
}
```


</div>

## Properties
### [`allOverriddenSymbols`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#alloverriddensymbols)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#alloverriddensymbols">allOverriddenSymbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

All explicitly declared (non-fake) callable symbols overridden by this callable symbol.


</div>

</div>
### [`allSupertypes`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#allsupertypes)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#allsupertypes">allSupertypes</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

All supertypes of the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md). The resulting sequence is ordered by a breadth-first traversal of the class hierarchy, without duplicates.


</div>

</div>
### [`analysisScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-analysis-scope-provider/index.md#analysisscope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-analysis-scope-provider/index.html#analysisscope">analysisScope</a><span class="o">: </span>GlobalSearchScope
</span></code></pre></div>
</div>


<div markdown>

A GlobalSearchScope which spans the files that can be analyzed by the current [`KaSession`](index.md).


</div>

</div>
### [`applicableAnnotationTargets`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.md#applicableannotationtargets)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.html#applicableannotationtargets">applicableAnnotationTargets</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-target/index.html">KaAnnotationTarget</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A set of applicable targets for an annotation class symbol, or `null` if the symbol is not an annotation class.


</div>

</div>
### [`arrayElementType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#arrayelementtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#arrayelementtype">arrayElementType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The array type's element type if the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a primitive type array or [`Array`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html), and `null` otherwise.


</div>

</div>
### [`augmentedByWarningLevelAnnotations`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#augmentedbywarninglevelannotations)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#augmentedbywarninglevelannotations">augmentedByWarningLevelAnnotations</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) derived from the given type by enforcing warning-level nullability annotations. If the derived type doesn't differ from the original type, the original type is used.


</div>

</div>
### [`builtinFunctionTypeFamilies`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#builtinfunctiontypefamilies)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#builtinfunctiontypefamilies">builtinFunctionTypeFamilies</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-builtin-function-type-families/index.html">KaBuiltinFunctionTypeFamilies</a>
</span></code></pre></div>
</div>


<div markdown>

Provides access to the built-in [`function type families`](../../org.jetbrains.kotlin.analysis.api.components/-ka-function-type-family/index.md).


</div>

</div>
### [`builtinTypes`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#builtintypes)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#builtintypes">builtinTypes</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-builtin-types/index.html">KaBuiltinTypes</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) instances for built-in types.


</div>

</div>
### [`callableSymbol`](../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.md#callablesymbol)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span>PsiMember<span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.html#callablesymbol">callableSymbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) for the given PsiMember method or field, or `null` for local declarations and Kotlin light classes.


</div>

</div>
### [`canBeOperator`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.md#canbeoperator)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.html#canbeoperator">canBeOperator</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the function symbol meets all the requirements to be declared as an [operator function](https://kotlinlang.org/docs/operator-overloading.html).


</div>

</div>
### [`classSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md#classsymbol)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#classsymbol">classSymbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaClassSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) for the given [`KtClassOrObject`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.md), or `null` for [`KtEnumEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry/index.md) declarations.


</div>

</div>
### [`combinedDeclaredMemberScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#combineddeclaredmemberscope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#combineddeclaredmemberscope">combinedDeclaredMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing all members explicitly declared in the given [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md).


</div>

</div>
### [`combinedMemberScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#combinedmemberscope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#combinedmemberscope">combinedMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing all members from [`memberScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#memberscope) and [`staticMemberScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#staticmemberscope).


</div>

</div>
### [`commonSupertype`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#commonsupertype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#commonsupertype">commonSupertype</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The common supertype of the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)s.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/index.html">Iterable</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#commonsupertype">commonSupertype</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The common supertype of the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)s.


</div>

</div>
### [`compilerPluginGeneratedDeclarations`](../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-plugin-generated-declarations-provider/index.md#compilerplugingenerateddeclarations)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-plugin-generated-declarations-provider/index.html#compilerplugingenerateddeclarations">compilerPluginGeneratedDeclarations</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-plugin-generated-declarations/index.html">KaCompilerPluginGeneratedDeclarations</a>
</span></code></pre></div>
</div>


<div markdown>

[`Declarations`](../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-plugin-generated-declarations/index.md) generated by compiler plugins for [`this`](../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md) module, not including the generated declarations for dependencies of this module.


</div>

</div>
### [`containingDeclaration`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#containingdeclaration)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#containingdeclaration">containingDeclaration</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`KaDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) which contains this symbol, or `null` if there is no containing declaration:


</div>

</div>
### [`containingFile`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#containingfile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#containingfile">containingFile</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`KaFileSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md) which contains this symbol, or `null` if this symbol is already a [`KaFileSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md), since it has no containing file. Also `null` for Java and library declarations.


</div>

</div>
### [`containingFileAnnotations`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.md#containingfileannotations)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.html#containingfileannotations">containingFileAnnotations</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-list/index.html">KaAnnotationList</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

File-level annotations (`@file:SomeAnnotation`) of the source file this top-level [`KaDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) was defined in, or `null` for a nested declaration.


</div>

</div>
### [`containingJvmClassName`](../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.md#containingjvmclassname)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.html#containingjvmclassname">containingJvmClassName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The containing JVM class name for the given [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md).


</div>

</div>
### [`containingModule`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#containingmodule)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#containingmodule">containingModule</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaModule`](../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md) which contains this symbol.


</div>

</div>
### [`containingSymbol`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#containingsymbol)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#containingsymbol">containingSymbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) which contains this symbol, or `null` if there is no containing declaration:


</div>

</div>
### [`contextSensitiveResolutionStatus`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#contextsensitiveresolutionstatus)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#contextsensitiveresolutionstatus">contextSensitiveResolutionStatus</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-context-sensitive-resolution-status/index.html">KaContextSensitiveResolutionStatus</a>
</span></code></pre></div>
</div>


<div markdown>

The [context-sensitive resolution](https://github.com/Kotlin/KEEP/issues/379) status of the [`KtSimpleNameExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.md): whether the name is already resolved through context-sensitive resolution, and whether a redundant explicit qualifier or import could be removed in favor of it.


</div>

</div>
### [`declarationScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#declarationscope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.html">KaTypeScope</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#declarationscope">declarationScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing unsubstituted declarations from the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)'s underlying declaration.


</div>

</div>
### [`declaredMemberScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#declaredmemberscope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#declaredmemberscope">declaredMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing the non-static callables (functions, properties, and constructors) and inner classes explicitly declared in the given [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md).


</div>

</div>
### [`defaultAnnotationTargets`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.md#defaultannotationtargets)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.html#defaultannotationtargets">defaultAnnotationTargets</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-target/index.html">KaAnnotationTarget</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A set of annotation targets matching for the given symbol, or `null` if the symbol cannot be annotated. Annotations with one of targets from the returned set can be placed on the [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) without an explicit use-site target.


</div>

</div>
### [`defaultInitializer`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#defaultinitializer)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#defaultinitializer">defaultInitializer</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The default initializer for the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md), or `null` if the type is neither nullable, a primitive, nor a string.


</div>

</div>
### [`defaultType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#defaulttype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#defaulttype">defaultType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The representation of [`this`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) in terms of [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).


</div>

</div>
### [`defaultTypeWithStarProjections`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#defaulttypewithstarprojections)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#defaulttypewithstarprojections">defaultTypeWithStarProjections</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The representation of [`this`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) in terms of [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).


</div>

</div>
### [`delegatedMemberScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#delegatedmemberscope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#delegatedmemberscope">delegatedMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing synthetic callables (functions and properties) created by interface delegation.


</div>

</div>
### [`deprecation`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.md#deprecation)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.html#deprecation">deprecation</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-deprecation/index.html">KaDeprecation</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The deprecation status of the given symbol, or `null` if the symbol is not deprecated.


</div>

</div>
### [`directlyOverriddenSymbols`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#directlyoverriddensymbols)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#directlyoverriddensymbols">directlyOverriddenSymbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Explicitly declared (non-fake) callable symbols that are directly overridden by this callable symbol.


</div>

</div>
### [`directSupertypes`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#directsupertypes)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#directsupertypes">directSupertypes</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The direct supertypes of the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).


</div>

</div>
### [`expandedSymbol`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#expandedsymbol)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#expandedsymbol">expandedSymbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The class symbol backing the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md), if available.


</div>

</div>
### [`expectedType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.md#expectedtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.html#expectedtype">expectedType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The expected [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) for the given PsiElement if it is an expression, or `null` if the element does not have an expected type. The expected type represents the type that is expected for an expression at a specific location in the code.


</div>

</div>
### [`expressionType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.md#expressiontype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.html#expressiontype">expressionType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The type of the given [`KtExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md), or `null` if it does not have a type.


</div>

</div>
### [`fakeOverrideOriginal`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#fakeoverrideoriginal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#fakeoverrideoriginal">fakeOverrideOriginal</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

The original declared symbol for this callable symbol, after unwrapping fake override [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md)s if needed.


</div>

</div>
### [`fileScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#filescope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#filescope">fileScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing the top-level declarations (such as classes, functions and properties) in the given [`KaFileSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md).


</div>

</div>
### [`fullyExpandedType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#fullyexpandedtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#fullyexpandedtype">fullyExpandedType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The type that corresponds to the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) with fully expanded type aliases.


</div>

</div>
### [`functionalInterface`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#functionalinterface)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-sam-constructor-symbol/index.html">KaSamConstructorSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#functionalinterface">functionalInterface</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaClassLikeSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.md) of the corresponding [functional (SAM) interface](https://kotlinlang.org/docs/fun-interfaces.html).


</div>

</div>
### [`functionalInterfaceFunction`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#functionalinterfacefunction)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#functionalinterfacefunction">functionalInterfaceFunction</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The single abstract function of a [functional interface](https://kotlinlang.org/docs/fun-interfaces.html), or `null` if this class is not a functional interface.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-sam-constructor-symbol/index.html">KaSamConstructorSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#functionalinterfacefunction">functionalInterfaceFunction</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

The single abstract function of the [`functional interface`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#functionalinterface) that this SAM constructor creates.


</div>

</div>
### [`functionType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.md#functiontype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-function/index.html">KtFunction</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.html#functiontype">functionType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The function type of the given [`KtFunction`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-function/index.md).


</div>

</div>
### [`functionTypeFamily`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#functiontypefamily)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#functiontypefamily">functionTypeFamily</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-function-type-family/index.html">KaFunctionTypeFamily</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`function type family`](../../org.jetbrains.kotlin.analysis.api.components/-ka-function-type-family/index.md) of the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md), or `null` if the type is not a function type.


</div>

</div>
### [`hasFlexibleNullability`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#hasflexiblenullability)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#hasflexiblenullability">hasFlexibleNullability</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`org.jetbrains.kotlin.analysis.api.types.KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md) / [`org.jetbrains.kotlin.analysis.api.types.KaDynamicType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.md) with flexible nullability or [`org.jetbrains.kotlin.analysis.api.types.KaErrorType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-error-type/index.md) with unknown nullability. Both safe and ordinary calls are valid on such types.


</div>

</div>
### [`implicitReceiverSmartCasts`](../../org.jetbrains.kotlin.analysis.api.components/-ka-data-flow-provider/index.md#implicitreceiversmartcasts)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-data-flow-provider/index.html#implicitreceiversmartcasts">implicitReceiverSmartCasts</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-implicit-receiver-smart-cast/index.html">KaImplicitReceiverSmartCast</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The list of [`implicit receiver smart casts`](../../org.jetbrains.kotlin.analysis.api.components/-ka-implicit-receiver-smart-cast/index.md) which have refined the expression's implicit receivers to a more specific type. These smart casts are required for the expression to be evaluated. The list does not include smart casts for explicit receivers.


</div>

</div>
### [`importableFqName`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.md#importablefqname)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.html#importablefqname">importableFqName</a><span class="o">: </span>FqName<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A FqName which can be used to import the given symbol, or `null` if the symbol cannot be imported.


</div>

</div>
### [`importingScopeContext`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#importingscopecontext)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#importingscopecontext">importingScopeContext</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-context/index.html">KaScopeContext</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScopeContext`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-context/index.md) formed from all imports in the [`KtFile`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md).


</div>

</div>
### [`intersectionOverriddenSymbols`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#intersectionoverriddensymbols)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#intersectionoverriddensymbols">intersectionOverriddenSymbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

All callable symbols overridden by this callable symbol if it is an intersection override, or an empty list otherwise.


</div>

</div>
### [`isAnyType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isanytype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isanytype">isAnyType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is an [`Any`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html) type.


</div>

</div>
### [`isArrayOrPrimitiveArray`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isarrayorprimitivearray)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isarrayorprimitivearray">isArrayOrPrimitiveArray</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is an array or a primitive array type.


</div>

</div>
### [`isBooleanType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isbooleantype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isbooleantype">isBooleanType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Boolean`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) type.


</div>

</div>
### [`isByteType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isbytetype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isbytetype">isByteType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Byte`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte/index.html) type.


</div>

</div>
### [`isCharSequenceType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#ischarsequencetype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#ischarsequencetype">isCharSequenceType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`CharSequence`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/index.html) type.


</div>

</div>
### [`isCharType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#ischartype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#ischartype">isCharType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Char`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char/index.html) type.


</div>

</div>
### [`isDefinitelyNotNull`](../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.md#isdefinitelynotnull)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.html#isdefinitelynotnull">isDefinitelyNotNull</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether this expression is definitely not null.


</div>

</div>
### [`isDefinitelyNull`](../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.md#isdefinitelynull)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.html#isdefinitelynull">isDefinitelyNull</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether this expression is definitely null, based on the declared nullability and smart cast types derived from data-flow analysis facts.


</div>

</div>
### [`isDenotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isdenotable">isDenotable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is denotable. A [denotable type](https://kotlinlang.org/spec/type-system.html#type-kinds) can be expressed in Kotlin code, as opposed to being only constructible via compiler type operations (such as type inference).


</div>

</div>
### [`isDeprecated`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.md#isdeprecated)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.html#isdeprecated">isDeprecated</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the symbol is deprecated at any level.


</div>

</div>
### [`isDoubleType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdoubletype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isdoubletype">isDoubleType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Double`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html) type.


</div>

</div>
### [`isFloatType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isfloattype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isfloattype">isFloatType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Float`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html) type.


</div>

</div>
### [`isFromResolveExtension`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolve-extension-info-provider/index.md#isfromresolveextension)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolve-extension-info-provider/index.html#isfromresolveextension">isFromResolveExtension</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the given [`KtElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md) is provided by a [`KaResolveExtension`](../../org.jetbrains.kotlin.analysis.api.resolve.extensions/-ka-resolve-extension/index.md).


</div>

</div>
### [`isFunctionalInterface`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isfunctionalinterface)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isfunctionalinterface">isFunctionalInterface</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [functional interface type](https://kotlinlang.org/docs/fun-interfaces.html), such as [`Runnable`](https://docs.oracle.com/javase/8/docs/api/java/lang/Runnable.html). Such types are also known as SAM types.


</div>

</div>
### [`isFunctionType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isfunctiontype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isfunctiontype">isFunctionType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`kotlin.Function`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-function/index.html) type.


</div>

</div>
### [`isImplicitReferenceToCompanion`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#isimplicitreferencetocompanion)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#isimplicitreferencetocompanion">isImplicitReferenceToCompanion</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks if the [`KtSimpleNameExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.md) is an implicit reference to a companion object via the containing class.


</div>

</div>
### [`isInline`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.md#isinline)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-kotlin-property-symbol/index.html">KaKotlinPropertySymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.html#isinline">isInline</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the property is an [inline property](https://kotlinlang.org/docs/inline-functions.html#inline-properties). A property is considered `inline` when both of its accessors are `inline` or when it has the `inline` keyword. The `inline` keyword on a property is syntactic sugar for marking both accessors as `inline`.


</div>

</div>
### [`isIntType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isinttype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isinttype">isIntType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is an [`Int`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) type.


</div>

</div>
### [`isKFunctionType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#iskfunctiontype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#iskfunctiontype">isKFunctionType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`kotlin.reflect.KFunction`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/-k-function/index.html) type.


</div>

</div>
### [`isKSuspendFunctionType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isksuspendfunctiontype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isksuspendfunctiontype">isKSuspendFunctionType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a `KSuspendFunction` type.


</div>

</div>
### [`isLongType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#islongtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#islongtype">isLongType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Long`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html) type.


</div>

</div>
### [`isMarkedNullable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#ismarkednullable)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#ismarkednullable">isMarkedNullable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is explicitly marked as nullable, i.e., is represented as `T?`.


</div>

</div>
### [`isNestedArray`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isnestedarray)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isnestedarray">isNestedArray</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is an array or a primitive array type, and its element is also an array type.


</div>

</div>
### [`isNothingType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isnothingtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isnothingtype">isNothingType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Nothing`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-nothing/index.html) type.


</div>

</div>
### [`isNullable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isnullable)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isnullable">isNullable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether a public value of the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) can potentially be `null`.


</div>

</div>
### [`isPrimitive`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isprimitive)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isprimitive">isPrimitive</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a primitive type.


</div>

</div>
### [`isPrimitiveBacked`](../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.md#isprimitivebacked)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.html#isprimitivebacked">isPrimitiveBacked</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is backed by a single JVM primitive type.


</div>

</div>
### [`isResolveExtensionFile`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolve-extension-info-provider/index.md#isresolveextensionfile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span>VirtualFile<span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolve-extension-info-provider/index.html#isresolveextensionfile">isResolveExtensionFile</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the given VirtualFile is provided by a [`KaResolveExtension`](../../org.jetbrains.kotlin.analysis.api.resolve.extensions/-ka-resolve-extension/index.md).


</div>

</div>
### [`isShortType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isshorttype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isshorttype">isShortType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Short`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/index.html) type.


</div>

</div>
### [`isStableForSmartCasting`](../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-information-provider/index.md#isstableforsmartcasting)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-information-provider/index.html#isstableforsmartcasting">isStableForSmartCasting</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether this expression can be used as a stable smart-cast sink at the current program point.


</div>

</div>
### [`isStringType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isstringtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isstringtype">isStringType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`String`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) type.


</div>

</div>
### [`isSuspendFunctionType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#issuspendfunctiontype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#issuspendfunctiontype">isSuspendFunctionType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [suspend function](https://kotlinlang.org/spec/asynchronous-programming-with-coroutines.html#suspending-functions) type.


</div>

</div>
### [`isUByteType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isubytetype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isubytetype">isUByteType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`UByte`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-byte/index.html) type.


</div>

</div>
### [`isUIntType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isuinttype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isuinttype">isUIntType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`UInt`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-int/index.html) type.


</div>

</div>
### [`isULongType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isulongtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isulongtype">isULongType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`ULong`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-long/index.html) type.


</div>

</div>
### [`isUnitType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isunittype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isunittype">isUnitType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Unit`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html) type.


</div>

</div>
### [`isUsedAsExpression`](../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-information-provider/index.md#isusedasexpression)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-information-provider/index.html#isusedasexpression">isUsedAsExpression</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the value of the given [`KtExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md) is used. In other words, `true` if the value of the expression is not safe to discard.


</div>

</div>
### [`isUsedAsResultOfLambda`](../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-information-provider/index.md#isusedasresultoflambda)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-information-provider/index.html#isusedasresultoflambda">isUsedAsResultOfLambda</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the value of the given [`KtExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md) is used as the resulting expression of some lambda block.


</div>

</div>
### [`isUShortType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isushorttype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.html#isushorttype">isUShortType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`UShort`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-short/index.html) type.


</div>

</div>
### [`klibSourceFileName`](../../org.jetbrains.kotlin.analysis.api.components/-ka-source-provider/index.md#klibsourcefilename)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-source-provider/index.html#klibsourcefilename">klibSourceFileName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The source file name for the given [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md) located in a Kotlin library (klib), or `null` if the declaration is not located in a klib, or when the source file name is not available.


</div>

</div>
### [`memberScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#memberscope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#memberscope">memberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing non-static callable members (functions, properties, and constructors) and all classifier members (classes and objects) of the given [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md). The scope includes members inherited from the symbol's supertypes, in addition to members which are declared explicitly inside the symbol's body.


</div>

</div>
### [`namedClassSymbol`](../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.md#namedclasssymbol)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span>PsiClass<span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.html#namedclasssymbol">namedClassSymbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaNamedClassSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.md) for the given PsiClass, or `null` for anonymous classes, local classes, type parameters (which are also PsiClasses), and Kotlin light classes.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#namedclasssymbol">namedClassSymbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaNamedClassSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.md) for the given named [`KtClassOrObject`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.md), or `null` for [`KtEnumEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry/index.md) declarations and object literals.


</div>

</div>
### [`originalConstructorIfTypeAliased`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#originalconstructoriftypealiased)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#originalconstructoriftypealiased">originalConstructorIfTypeAliased</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The original [`KaConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) for a [`type-aliased constructor`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-origin/-t-y-p-e-a-l-i-a-s-e-d_-c-o-n-s-t-r-u-c-t-o-r/index.md), or `null` otherwise.


</div>

</div>
### [`packageScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#packagescope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-package-symbol/index.html">KaPackageSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#packagescope">packageScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing all members of the package represented by the given [`KaPackageSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-package-symbol/index.md), not including members of subpackages.


</div>

</div>
### [`receiverType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#receivertype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-double-colon-expression/index.html">KtDoubleColonExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#receivertype">receiverType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtDoubleColonExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-double-colon-expression/index.md) to the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) of its receiver.


</div>

</div>
### [`resolveExtensionNavigationElements`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolve-extension-info-provider/index.md#resolveextensionnavigationelements)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolve-extension-info-provider/index.html#resolveextensionnavigationelements">resolveExtensionNavigationElements</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of PsiElements which are used as navigation targets in place of this [`KtElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md) provided by a [`KaResolveExtension`](../../org.jetbrains.kotlin.analysis.api.resolve.extensions/-ka-resolve-extension/index.md).


</div>

</div>
### [`resolveExtensionScopeWithTopLevelDeclarations`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolve-extension-info-provider/index.md#resolveextensionscopewithtopleveldeclarations)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolve-extension-info-provider/index.html#resolveextensionscopewithtopleveldeclarations">resolveExtensionScopeWithTopLevelDeclarations</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing top-level callable declarations generated by [`KaResolveExtension`](../../org.jetbrains.kotlin.analysis.api.resolve.extensions/-ka-resolve-extension/index.md)s.


</div>

</div>
### [`returnType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.md#returntype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration-with-return-type/index.html">KtDeclarationWithReturnType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.html#returntype">returnType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The return type of the given [`KtDeclarationWithReturnType`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration-with-return-type/index.md).


</div>

</div>
### [`returnValueStatus`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.md#returnvaluestatus)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-information-provider/index.html#returnvaluestatus">returnValueStatus</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-return-value-status/index.html">KaReturnValueStatus</a>
</span></code></pre></div>
</div>


<div markdown>

The return value status of the function (should it be used, or can it be ignored). See the [KEEP](https://github.com/Kotlin/KEEP/blob/main/proposals/KEEP-0412-unused-return-value-checker.md) for details.


</div>

</div>
### [`rootPackageSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md#rootpackagesymbol)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#rootpackagesymbol">rootPackageSymbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-package-symbol/index.html">KaPackageSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaPackageSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-package-symbol/index.md) for the root package, which is the special package with an empty fully-qualified name.


</div>

</div>
### [`samConstructor`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#samconstructor)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#samconstructor">samConstructor</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-sam-constructor-symbol/index.html">KaSamConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The associated [`KaSamConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-sam-constructor-symbol/index.md) if this [`KaClassLikeSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.md) is a [functional interface type (SAM)](https://kotlinlang.org/docs/fun-interfaces.html).


</div>

</div>
### [`scope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#scope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#scope">scope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.html">KaTypeScope</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.md) for the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md), or `null` if the type is [`erroneous`](../../org.jetbrains.kotlin.analysis.api.types/-ka-error-type/index.md). The scope includes all members which are callable on a given type. It also includes [synthetic Java properties](https://kotlinlang.org/docs/java-interop.html#getters-and-setters).


</div>

</div>
### [`sealedClassInheritors`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#sealedclassinheritors)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#sealedclassinheritors">sealedClassInheritors</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The inheritors of the given sealed class.


</div>

</div>
### [`smartCastInfo`](../../org.jetbrains.kotlin.analysis.api.components/-ka-data-flow-provider/index.md#smartcastinfo)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-data-flow-provider/index.html#smartcastinfo">smartCastInfo</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-smart-cast-info/index.html">KaSmartCastInfo</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

[`Smart cast information`](../../org.jetbrains.kotlin.analysis.api.components/-ka-smart-cast-info/index.md) for the given [`KtExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md), or `null` if smart casts are not applied to it.


</div>

</div>
### [`staticDeclaredMemberScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#staticdeclaredmemberscope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#staticdeclaredmemberscope">staticDeclaredMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing the static callables (functions and properties) and all classifiers (classes and objects) explicitly declared in the given [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md).


</div>

</div>
### [`staticMemberScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#staticmemberscope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#staticmemberscope">staticMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing the static members of the given [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md).


</div>

</div>
### [`symbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md#symbol)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-backing-field/index.html">KtBackingField</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-backing-field-symbol/index.html">KaBackingFieldSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaBackingFieldSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-backing-field-symbol/index.md) for the given [`KtBackingField`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-backing-field/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-initializer/index.html">KtClassInitializer</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-initializer-symbol/index.html">KaClassInitializerSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaClassInitializerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-initializer-symbol/index.md) for the given [`KtClassInitializer`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-initializer/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor/index.html">KtConstructor</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) for the given [`KtConstructor`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-context-receiver/index.html">KtContextReceiver</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-context-parameter-symbol/index.html">KaContextParameterSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

Represents [`KtContextReceiver`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-context-receiver/index.md) as a [`KaContextParameterSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-context-parameter-symbol/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) for the given [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration/index.html">KtDestructuringDeclaration</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-destructuring-declaration-symbol/index.html">KaDestructuringDeclarationSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaDestructuringDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-destructuring-declaration-symbol/index.md) for the given [`KtDestructuringDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaVariableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.md) that corresponds to the local variable introduced by the given [`KtDestructuringDeclarationEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry/index.html">KtEnumEntry</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-enum-entry-symbol/index.html">KaEnumEntrySymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaEnumEntrySymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-enum-entry-symbol/index.md) for the given [`KtEnumEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaFileSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md) for a [`KtFile`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-function-literal/index.html">KtFunctionLiteral</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-anonymous-function-symbol/index.html">KaAnonymousFunctionSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaAnonymousFunctionSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-anonymous-function-symbol/index.md) for the given [`KtFunctionLiteral`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-function-literal/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-named-function/index.html">KtNamedFunction</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaFunctionSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md) for the given [`KtNamedFunction`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-named-function/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-object-declaration/index.html">KtObjectDeclaration</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaClassSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) for the given [`KtObjectDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-object-declaration/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-object-literal-expression/index.html">KtObjectLiteralExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-anonymous-object-symbol/index.html">KaAnonymousObjectSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaAnonymousObjectSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-anonymous-object-symbol/index.md) for the given [`KtObjectLiteralExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-object-literal-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-parameter/index.html">KtParameter</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaVariableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.md) for the given [`KtParameter`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-parameter/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-property/index.html">KtProperty</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaVariableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.md) for the given [`KtProperty`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-property/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-accessor/index.html">KtPropertyAccessor</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-property-accessor-symbol/index.html">KaPropertyAccessorSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaPropertyAccessorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-property-accessor-symbol/index.md) for the given [`KtPropertyAccessor`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-accessor/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-script/index.html">KtScript</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-script-symbol/index.html">KaScriptSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScriptSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-script-symbol/index.md) for a [`KtScript`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-script/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-alias/index.html">KtTypeAlias</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-alias-symbol/index.html">KaTypeAliasSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeAliasSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-alias-symbol/index.md) for the given [`KtTypeAlias`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-alias/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-parameter/index.html">KtTypeParameter</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeParameterSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.md) for the given [`KtTypeParameter`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-parameter/index.md).


</div>

</div>
### [`syntheticJavaPropertiesScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#syntheticjavapropertiesscope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#syntheticjavapropertiesscope">syntheticJavaPropertiesScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.html">KaTypeScope</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.md) containing the [synthetic Java properties](https://kotlinlang.org/docs/java-interop.html#getters-and-setters) created for a given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).


</div>

</div>
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
### [`type`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#type)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.html">KtTypeReference</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#type">type</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtTypeReference`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.md) to its corresponding [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).


</div>

</div>
### [`typeCreator`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.md#typecreator)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.html#typecreator">typeCreator</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-type-creator/index.html">KaTypeCreator</a>
</span></code></pre></div>
</div>


<div markdown>

A single entry point for the type building infrastructure.


</div>

</div>
### useSiteModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#usesitemodule">useSiteModule</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaModule`](../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md) from whose perspective the analysis is performed. The use-site module defines the resolution scope of the [`KaSession`](index.md), which signifies where symbols are located (such as sources, dependencies, and so on) and which symbols can be found in the first place.


</div>

</div>
### useSiteSession

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="index.html#usesitesession">useSiteSession</a><span class="o">: </span><a href="index.html">KaSession</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaSession`](index.md) of the current analysis context.


</div>

</div>
### [`varargArrayType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#varargarraytype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.html">KaValueParameterSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#varargarraytype">varargArrayType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The array type that represents the list of arguments passed to this parameter if [`this`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.md) is a [vararg](https://kotlinlang.org/docs/functions.html#variable-number-of-arguments-varargs) parameter.


</div>

</div>
## Functions
### [`allSupertypes`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#allsupertypes)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#allsupertypes"><span class="nf">allSupertypes</span></a><span class="p">(</span>shouldApproximate<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all supertypes of the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md). The resulting sequence is ordered by a breadth-first traversal of the class hierarchy, without duplicates.


</div>

</div>
### [`approximateToDenotableSubtype`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#approximatetodenotablesubtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#approximatetodenotablesubtype"><span class="nf">approximateToDenotableSubtype</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a [`denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) subtype.


</div>

</div>
### [`approximateToDenotableSubtypeOrSelf`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#approximatetodenotablesubtypeorself)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#approximatetodenotablesubtypeorself"><span class="nf">approximateToDenotableSubtypeOrSelf</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a [`denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) subtype, or returns the given type itself if it is already denotable.


</div>

</div>
### [`approximateToDenotableSupertype`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#approximatetodenotablesupertype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#approximatetodenotablesupertype"><span class="nf">approximateToDenotableSupertype</span></a><span class="p">(</span>allowLocalDenotableTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a [`denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) supertype.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#approximatetodenotablesupertype"><span class="nf">approximateToDenotableSupertype</span></a><span class="p">(</span>position<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a [`denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) supertype based on the given [`position`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#approximatetodenotablesupertype).


</div>

</div>
### [`approximateToDenotableSupertypeOrSelf`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#approximatetodenotablesupertypeorself)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#approximatetodenotablesupertypeorself"><span class="nf">approximateToDenotableSupertypeOrSelf</span></a><span class="p">(</span>allowLocalDenotableTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a [`denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) supertype, or returns the given type itself if it is already denotable.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#approximatetodenotablesupertypeorself"><span class="nf">approximateToDenotableSupertypeOrSelf</span></a><span class="p">(</span>position<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a [`denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) subtype based on the given [`position`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#approximatetodenotablesupertypeorself), or returns the given type itself if it is already denotable.


</div>

</div>
### [`asCompositeScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#ascompositescope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a><span class="o">></span><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#ascompositescope"><span class="nf">asCompositeScope</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

Combines a list of [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md)s into a single composite [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md). The resulting scope contains all members of its constituent scopes.


</div>

</div>
### [`asKaType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.md#askatype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span>PsiType<span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.html#askatype"><span class="nf">asKaType</span></a><span class="p">(</span>useSitePosition<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given PsiType to a [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) in the context of the [`useSitePosition`](../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.md#askatype).


</div>

</div>
### [`asPsiType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.md#aspsitype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.html#aspsitype"><span class="nf">asPsiType</span></a><span class="p">(</span>
    useSitePosition<span class="o">: </span>PsiElement<span class="p">, </span>
    allowErrorTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    mode<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-mapping-mode/index.html">KaTypeMappingMode</a><span class="o"> = </span>KaTypeMappingMode.DEFAULT<span class="p">, </span>
    isAnnotationMethod<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span>
    suppressWildcards<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">?</span><span class="o"> = </span>null<span class="p">, </span>
    preserveAnnotations<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">, </span>
    allowNonJvmPlatforms<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span>
<span class="p">)</span><span class="o">: </span>PsiType<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a PsiType in the context of the [`useSitePosition`](../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.md#aspsitype).


</div>

</div>
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`asSignature`](../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.md#assignature)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#assignature">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#assignature">S</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#assignature"><span class="nf">asSignature</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#assignature">S</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Creates a new [`KaCallableSignature`](../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.md) for the given symbol and leaves all types unsubstituted.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#assignature">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#assignature">S</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#assignature"><span class="nf">asSignature</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-function-signature/index.html">KaFunctionSignature</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#assignature">S</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Creates a new [`KaFunctionSignature`](../../org.jetbrains.kotlin.analysis.api.signatures/-ka-function-signature/index.md) for the given symbol and leaves all types unsubstituted.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#assignature">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#assignature">S</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#assignature"><span class="nf">asSignature</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-variable-signature/index.html">KaVariableSignature</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#assignature">S</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Creates a new [`KaVariableSignature`](../../org.jetbrains.kotlin.analysis.api.signatures/-ka-variable-signature/index.md) for the given symbol and leaves all types unsubstituted.


</div>

</div>
### [`buildArrayType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.md#buildarraytype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.html#buildarraytype"><span class="nf">buildArrayType</span></a><span class="p">(</span>elementType<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-array-type-builder/index.html">KaArrayTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a boxed / primitive (depending on the [`init`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.md#buildarraytype) block) array type from the given [`elementType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.md#buildarraytype).


</div>

</div>
### [`buildClassType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.md#buildclasstype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.html#buildclasstype"><span class="nf">buildClassType</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">, </span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a class type with the given class symbol.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.html#buildclasstype"><span class="nf">buildClassType</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">, </span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a class type with the given class ID.


</div>

</div>
### [`buildStarTypeProjection`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.md#buildstartypeprojection)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.html#buildstartypeprojection"><span class="nf">buildStarTypeProjection</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-star-type-projection/index.html">KaStarTypeProjection</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaStarTypeProjection`](../../org.jetbrains.kotlin.analysis.api.types/-ka-star-type-projection/index.md) (`*`).


</div>

</div>
### [`buildTypeParameterType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.md#buildtypeparametertype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.html#buildtypeparametertype"><span class="nf">buildTypeParameterType</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">, </span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-parameter-type-builder/index.html">KaTypeParameterTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaTypeParameterType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.md) with the given type parameter symbol.


</div>

</div>
### [`buildVarargArrayType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.md#buildvarargarraytype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.html#buildvarargarraytype"><span class="nf">buildVarargArrayType</span></a><span class="p">(</span>elementType<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds the underlying array type of [vararg](https://kotlinlang.org/docs/functions.html#variable-number-of-arguments-varargs) function parameter with the given [`elementType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator/index.md#buildvarargarraytype).


</div>

</div>
### [`canBeAnalysed`](../../org.jetbrains.kotlin.analysis.api.components/-ka-analysis-scope-provider/index.md#canbeanalysed)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-analysis-scope-provider/index.html#canbeanalysed"><span class="nf">canBeAnalysed</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether the PsiElement is inside the [`analysisScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-analysis-scope-provider/index.md#analysisscope).


</div>

</div>
### [`collectCallCandidates`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#collectcallcandidates)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#collectcallcandidates"><span class="nf">collectCallCandidates</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-candidate/index.html">KaCallCandidate</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all candidates considered during [overload resolution](https://kotlinlang.org/spec/overload-resolution.html) for the call corresponding to the given [`KtResolvableCall`](../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md).


</div>

</div>
### [`collectDiagnostics`](../../org.jetbrains.kotlin.analysis.api.components/-ka-diagnostic-provider/index.md#collectdiagnostics)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-diagnostic-provider/index.html#collectdiagnostics"><span class="nf">collectDiagnostics</span></a><span class="p">(</span>filter<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-diagnostic-checker-filter/index.html">KaDiagnosticCheckerFilter</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic-with-psi/index.html">KaDiagnosticWithPsi</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Collects all diagnostics for the given file.


</div>

</div>
### [`collectPossibleReferenceShortenings`](../../org.jetbrains.kotlin.analysis.api.components/-ka-reference-shortener/index.md#collectpossiblereferenceshortenings)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-reference-shortener/index.html#collectpossiblereferenceshortenings"><span class="nf">collectPossibleReferenceShortenings</span></a><span class="p">(</span>
    file<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>
    selection<span class="o">: </span>TextRange<span class="o"> = </span>file.textRange<span class="p">, </span>
    shortenOptions<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-options/index.html">ShortenOptions</a><span class="o"> = </span>ShortenOptions.DEFAULT<span class="p">, </span>
    classShortenStrategy<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-strategy/index.html">ShortenStrategy</a><span class="o"> = </span>defaultClassShortenStrategy<span class="p">, </span>
    callableShortenStrategy<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-strategy/index.html">ShortenStrategy</a><span class="o"> = </span>defaultCallableShortenStrategy
<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-command/index.html">ShortenCommand</a>
</span></code></pre></div>
</div>


<div markdown>

Collects possible references to shorten.


</div>

</div>
### [`collectPossibleReferenceShorteningsInElement`](../../org.jetbrains.kotlin.analysis.api.components/-ka-reference-shortener/index.md#collectpossiblereferenceshorteningsinelement)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-reference-shortener/index.html#collectpossiblereferenceshorteningsinelement"><span class="nf">collectPossibleReferenceShorteningsInElement</span></a><span class="p">(</span>
    element<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">, </span>
    shortenOptions<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-options/index.html">ShortenOptions</a><span class="o"> = </span>ShortenOptions.DEFAULT<span class="p">, </span>
    classShortenStrategy<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-strategy/index.html">ShortenStrategy</a><span class="o"> = </span>defaultClassShortenStrategy<span class="p">, </span>
    callableShortenStrategy<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-strategy/index.html">ShortenStrategy</a><span class="o"> = </span>defaultCallableShortenStrategy
<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-command/index.html">ShortenCommand</a>
</span></code></pre></div>
</div>


<div markdown>

Collects possible references to shorten in [`element`](../../org.jetbrains.kotlin.analysis.api.components/-ka-reference-shortener/index.md#collectpossiblereferenceshorteningsinelement)s text range.


</div>

</div>
### [`compile`](../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-facility/index.md#compile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-facility/index.html#compile"><span class="nf">compile</span></a><span class="p">(</span>file<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>options<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compilation-options/index.html">KaCompilationOptions</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compilation-result/index.html">KaCompilationResult</a>
</span></code></pre></div>
</div>


<div markdown>

Compiles the given [`file`](../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-facility/index.md#compile) in-memory using the specified [`options`](../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-facility/index.md#compile).


</div>

</div>
### [`compositeScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#compositescope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-context/index.html">KaScopeContext</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#compositescope"><span class="nf">compositeScope</span></a><span class="p">(</span>filter<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-kind/index.html">KaScopeKind</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a single [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) that contains declarations from all scopes that satisfy [`filter`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#compositescope).


</div>

</div>
### [`computeExitPointSnapshot`](../../org.jetbrains.kotlin.analysis.api.components/-ka-data-flow-provider/index.md#computeexitpointsnapshot)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-data-flow-provider/index.html#computeexitpointsnapshot"><span class="nf">computeExitPointSnapshot</span></a><span class="p">(</span>statements<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-data-flow-exit-point-snapshot/index.html">KaDataFlowExitPointSnapshot</a>
</span></code></pre></div>
</div>

</div>
### [`computeMissingCases`](../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-information-provider/index.md#computemissingcases)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-expression/index.html">KtWhenExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-information-provider/index.html#computemissingcases"><span class="nf">computeMissingCases</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-when-missing-case/index.html">KaWhenMissingCase</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Computes the missing cases of the given [`KtWhenExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-expression/index.md).


</div>

</div>
### [`copy`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.md#copy)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.html#copy">T</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.html">KaClassType</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.html#copy">T</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.html#copy"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.html">KaClassType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaClassType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.md) with modifications applied via the [`init`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.md#copy) block.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.html">KaFunctionType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.html#copy"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-function-type-builder/index.html">KaFunctionTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.html">KaFunctionType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaFunctionType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.md) with modifications applied via the [`init`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.md#copy) block.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.html#copy"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-type-parameter-type-builder/index.html">KaTypeParameterTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaTypeParameterType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.md) with modifications applied via the [`init`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.md#copy) block.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/index.html">KaUsualClassType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.html#copy"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/index.html">KaUsualClassType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaUsualClassType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/index.md) with modifications applied via the [`init`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-creator-provider/index.md#copy) block.


</div>

</div>
### [`createCompilationOptions`](../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-facility/index.md#createcompilationoptions)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-facility/index.html#createcompilationoptions"><span class="nf">createCompilationOptions</span></a><span class="p">(</span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compilation-options-builder/index.html">KaCompilationOptionsBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compilation-options/index.html">KaCompilationOptions</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a new [`KaCompilationOptions`](../../org.jetbrains.kotlin.analysis.api.components/-ka-compilation-options/index.md) instance using the given DSL [`init`](../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-facility/index.md#createcompilationoptions) block.


</div>

</div>
### [`createExtensionCandidateChecker`](../../org.jetbrains.kotlin.analysis.api.components/-ka-completion-candidate-checker/index.md#createextensioncandidatechecker)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-completion-candidate-checker/index.html#createextensioncandidatechecker"><span class="nf">createExtensionCandidateChecker</span></a><span class="p">(</span>
    originalFile<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>
    nameExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">, </span>
    explicitReceiver<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-completion-extension-candidate-checker/index.html">KaCompletionExtensionCandidateChecker</a>
</span></code></pre></div>
</div>


<div markdown>

Returns an extension applicability checker for the given context [`nameExpression`](../../org.jetbrains.kotlin.analysis.api.components/-ka-completion-candidate-checker/index.md#createextensioncandidatechecker). The function is meant to only be used for providing auto-completion for Kotlin in IntelliJ IDEA.


</div>

</div>
### [`createInheritanceTypeSubstitutor`](../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.md#createinheritancetypesubstitutor)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.html#createinheritancetypesubstitutor"><span class="nf">createInheritanceTypeSubstitutor</span></a><span class="p">(</span>subClass<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">, </span>superClass<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md) based on the inheritance relationship between [`subClass`](../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.md#createinheritancetypesubstitutor) and [`superClass`](../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.md#createinheritancetypesubstitutor). [`subClass`](../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.md#createinheritancetypesubstitutor) must inherit from [`superClass`](../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.md#createinheritancetypesubstitutor) and there may not be any error types in the inheritance path. Otherwise, `null` is returned.


</div>

</div>
### [`createSubstitutor`](../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.md#createsubstitutor)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.html#createsubstitutor"><span class="nf">createSubstitutor</span></a><span class="p">(</span>mappings<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md) based on the given [`mappings`](../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.md#createsubstitutor).


</div>

</div>
### [`createSubtypingUnificationSubstitutor`](../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.md#createsubtypingunificationsubstitutor)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.html#createsubtypingunificationsubstitutor"><span class="nf">createSubtypingUnificationSubstitutor</span></a><span class="p">(</span>leftTypesToRightTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/index.html">Pair</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span><span class="o">></span><span class="p">, </span>isFreeTypeParameter<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md) which assigns type arguments such that, for each pair in [`leftTypesToRightTypes`](../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.md#createsubtypingunificationsubstitutor), the substituted left type is a subtype of the substituted right type. Returns `null` if such an assignment is not possible.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.html#createsubtypingunificationsubstitutor"><span class="nf">createSubtypingUnificationSubstitutor</span></a><span class="p">(</span>leftTypesToRightTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/index.html">Pair</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span><span class="o">></span><span class="p">, </span>constructionPolicy<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-unification-substitutor-policy/index.html">KaUnificationSubstitutorPolicy</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md) which assigns type arguments such that, for each pair in [`leftTypesToRightTypes`](../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.md#createsubtypingunificationsubstitutor), the substituted left type is a subtype of the substituted right type. Returns `null` if such an assignment is not possible.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.html#createsubtypingunificationsubstitutor"><span class="nf">createSubtypingUnificationSubstitutor</span></a><span class="p">(</span>
    leftType<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    rightType<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    constructionPolicy<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-unification-substitutor-policy/index.html">KaUnificationSubstitutorPolicy</a>
<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md) which assigns type arguments such that the substituted [`leftType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.md#createsubtypingunificationsubstitutor) is a subtype of the substituted [`rightType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-substitutor-provider/index.md#createsubtypingunificationsubstitutor). Returns `null` if such an assignment is not possible.


</div>

</div>
### [`createUseSiteVisibilityChecker`](../../org.jetbrains.kotlin.analysis.api.components/-ka-visibility-checker/index.md#createusesitevisibilitychecker)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-visibility-checker/index.html#createusesitevisibilitychecker"><span class="nf">createUseSiteVisibilityChecker</span></a><span class="p">(</span>
    useSiteFile<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="p">, </span>
    receiverExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span><span class="o"> = </span>null<span class="p">, </span>
    position<span class="o">: </span>PsiElement
<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-use-site-visibility-checker/index.html">KaUseSiteVisibilityChecker</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a visibility checker for the given use-site position.


</div>

</div>
### [`directSupertypes`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#directsupertypes)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#directsupertypes"><span class="nf">directSupertypes</span></a><span class="p">(</span>shouldApproximate<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the direct supertypes of the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).


</div>

</div>
### [`evaluate`](../../org.jetbrains.kotlin.analysis.api.components/-ka-evaluator/index.md#evaluate)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-evaluator/index.html#evaluate"><span class="nf">evaluate</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.base/-ka-constant-value/index.html">KaConstantValue</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to evaluate the given [`KtExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md) to a [`compile-time constant value`](../../org.jetbrains.kotlin.analysis.api.base/-ka-constant-value/index.md), or returns `null` if this is not possible.


</div>

</div>
### [`evaluateAsAnnotationValue`](../../org.jetbrains.kotlin.analysis.api.components/-ka-evaluator/index.md#evaluateasannotationvalue)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-evaluator/index.html#evaluateasannotationvalue"><span class="nf">evaluateAsAnnotationValue</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-value/index.html">KaAnnotationValue</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to evaluate the given [`KtExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md) to an [`annotation value`](../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-value/index.md) (a constant value which can be used as an annotation argument), or returns `null` if this is not possible.


</div>

</div>
### [`findClass`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md#findclass)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#findclass"><span class="nf">findClass</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaClassSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) for the specified ClassId, or `null` if such a symbol cannot be found.


</div>

</div>
### [`findClassLike`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md#findclasslike)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#findclasslike"><span class="nf">findClassLike</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaClassLikeSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.md) for the specified ClassId, or `null` if such a symbol cannot be found.


</div>

</div>
### [`findKDoc`](../../org.jetbrains.kotlin.analysis.api.components/-ka-k-doc-provider/index.md#findkdoc)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-k-doc-provider/index.html#findkdoc"><span class="nf">findKDoc</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.kdoc.psi.api/-k-doc-comment-descriptor/index.html">KDocCommentDescriptor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves KDoc for this [`KaDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-k-doc-provider/index.html#findkdoc"><span class="nf">findKDoc</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.kdoc.psi.api/-k-doc-comment-descriptor/index.html">KDocCommentDescriptor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves KDoc for this [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md).


</div>

</div>
### [`findPackage`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md#findpackage)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#findpackage"><span class="nf">findPackage</span></a><span class="p">(</span>fqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-package-symbol/index.html">KaPackageSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaPackageSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-package-symbol/index.md) corresponding to the given [`fqName`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md#findpackage) if that package exists and is visible from the current use site, or `null` otherwise.


</div>

</div>
### [`findTopLevelCallables`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md#findtoplevelcallables)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#findtoplevelcallables"><span class="nf">findTopLevelCallables</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">, </span>name<span class="o">: </span>Name<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Finds top-level functions and properties called [`name`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md#findtoplevelcallables) in the package called [`packageFqName`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md#findtoplevelcallables). Returns only symbols that are visible from the current use-site module.


</div>

</div>
### [`findTypeAlias`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.md#findtypealias)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-provider/index.html#findtypealias"><span class="nf">findTypeAlias</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-alias-symbol/index.html">KaTypeAliasSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaTypeAliasSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-alias-symbol/index.md) for the specified ClassId, or `null` if such a symbol cannot be found.


</div>

</div>
### [`getExpectsForActual`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#getexpectsforactual)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#getexpectsforactual"><span class="nf">getExpectsForActual</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an `expect` symbol for the given `actual` symbol, if it is available. The function may return multiple `expect` symbols in case of ambiguity errors.


</div>

</div>
### [`hasCommonSubtypeWith`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#hascommonsubtypewith)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#hascommonsubtypewith"><span class="nf">hasCommonSubtypeWith</span></a><span class="p">(</span>that<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether this [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is compatible with [`that`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#hascommonsubtypewith) other type. If they are compatible, the types can have a common subtype.


</div>

</div>
### [`hasConflictingSignatureWith`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#hasconflictingsignaturewith)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#hasconflictingsignaturewith"><span class="nf">hasConflictingSignatureWith</span></a><span class="p">(</span>other<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="p">, </span>targetPlatform<span class="o">: </span>TargetPlatform<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether [`this`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md) declaration has a conflicting signature with [`other`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#hasconflictingsignaturewith) based on platform-specific checks from [`targetPlatform`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#hasconflictingsignaturewith).


</div>

</div>
### [`implementationState`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#implementationstate)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#implementationstate"><span class="nf">implementationState</span></a><span class="p">(</span>implementerClassSymbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-callable-implementation-state/index.html">KaCallableImplementationState</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KaCallableImplementationState`](../../org.jetbrains.kotlin.analysis.api.components/-ka-callable-implementation-state/index.md) of the given [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) in the context of [`implementerClassSymbol`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#implementationstate).


</div>

</div>
### [`isDirectSubClassOf`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#isdirectsubclassof)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#isdirectsubclassof"><span class="nf">isDirectSubClassOf</span></a><span class="p">(</span>superClass<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks if [`this`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) class has [`superClass`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#isdirectsubclassof) listed as its direct superclass.


</div>

</div>
### [`isPublicApi`](../../org.jetbrains.kotlin.analysis.api.components/-ka-visibility-checker/index.md#ispublicapi)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-visibility-checker/index.html#ispublicapi"><span class="nf">isPublicApi</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the symbol is effectively public, including internal declarations with the [`PublishedApi`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-published-api/index.html) annotation.


</div>

</div>
### [`isSubClassOf`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#issubclassof)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.html#issubclassof"><span class="nf">isSubClassOf</span></a><span class="p">(</span>superClass<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks if [`this`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) class has [`superClass`](../../org.jetbrains.kotlin.analysis.api.components/-ka-symbol-relation-provider/index.md#issubclassof) as its superclass somewhere in the inheritance hierarchy.


</div>

</div>
### [`isSubtypeOf`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-relation-checker/index.md#issubtypeof)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-relation-checker/index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">, </span>errorTypePolicy<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a><span class="o"> = </span>KaSubtypingErrorTypePolicy.STRICT<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a subtype of a class represented by [`symbol`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-relation-checker/index.md#issubtypeof).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-relation-checker/index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>supertype<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>errorTypePolicy<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a><span class="o"> = </span>KaSubtypingErrorTypePolicy.STRICT<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a subtype of [`supertype`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-relation-checker/index.md#issubtypeof). The relation is non-strict, i.e. any type `t` is a subtype of itself.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-relation-checker/index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">, </span>errorTypePolicy<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a><span class="o"> = </span>KaSubtypingErrorTypePolicy.STRICT<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a subtype of a class called [`classId`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-relation-checker/index.md#issubtypeof).


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
### [`isVisibleInClass`](../../org.jetbrains.kotlin.analysis.api.components/-ka-visibility-checker/index.md#isvisibleinclass)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-visibility-checker/index.html#isvisibleinclass"><span class="nf">isVisibleInClass</span></a><span class="p">(</span>classSymbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether the given [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) (possibly inherited from a superclass) is visible in the given [`classSymbol`](../../org.jetbrains.kotlin.analysis.api.components/-ka-visibility-checker/index.md#isvisibleinclass).


</div>

</div>
### [`lowerBoundIfFlexible`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#lowerboundifflexible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#lowerboundifflexible"><span class="nf">lowerBoundIfFlexible</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md)'s lower bound, or the type itself if it is not flexible.


</div>

</div>
### [`mapToJvmTypeDescriptor`](../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.md#maptojvmtypedescriptor)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.html#maptojvmtypedescriptor"><span class="nf">mapToJvmTypeDescriptor</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Convert the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a JVM type descriptor with the [`KaTypeMappingMode.DEFAULT`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type-mapping-mode/-d-e-f-a-u-l-t/index.md). To learn more about JVM descriptors, check out the [JVM specification](https://docs.oracle.com/javase/specs/jvms/se24/html/jvms-4.html#jvms-4.3).


</div>

</div>
### [`modify`](../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-facility/index.md#modify)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compilation-options/index.html">KaCompilationOptions</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-facility/index.html#modify"><span class="nf">modify</span></a><span class="p">(</span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compilation-options-builder/index.html">KaCompilationOptionsBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-compilation-options/index.html">KaCompilationOptions</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of these [`KaCompilationOptions`](../../org.jetbrains.kotlin.analysis.api.components/-ka-compilation-options/index.md), applying the given [`init`](../../org.jetbrains.kotlin.analysis.api.components/-ka-compiler-facility/index.md#modify) modifications.


</div>

</div>
### [`render`](../../org.jetbrains.kotlin.analysis.api.components/-ka-renderer/index.md#render)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-renderer/index.html#render"><span class="nf">render</span></a><span class="p">(</span>renderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="o"> = </span>KaDeclarationRendererForSource.WITH_QUALIFIED_NAMES<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Renders the given [`KaDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) to a string. The particular rendering strategy is defined by the [`renderer`](../../org.jetbrains.kotlin.analysis.api.components/-ka-renderer/index.md#render).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-renderer/index.html#render"><span class="nf">render</span></a><span class="p">(</span>renderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.types/-ka-type-renderer/index.html">KaTypeRenderer</a><span class="o"> = </span>KaTypeRendererForSource.WITH_QUALIFIED_NAMES<span class="p">, </span>position<span class="o">: </span>Variance<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Renders the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) into a string. The particular rendering strategy is defined by the [`renderer`](../../org.jetbrains.kotlin.analysis.api.components/-ka-renderer/index.md#render).


</div>

</div>
### [`resolveCall`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#resolvecall)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-annotation-call/index.html">KaAnnotationCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtAnnotationEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.md) to an annotation constructor call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.html">KtArrayAccessExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtArrayAccessExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.md) to a simple function call representing `get`/`set` operator invocation.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.html">KtCallElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtCallElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.md) to a function call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.html">KtCallableReferenceExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-callable-reference-call/index.html">KaCallableReferenceCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtCallableReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.md) to a callable member call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.html">KtCollectionLiteralExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtCollectionLiteralExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.md) to a simple function call representing the corresponding array factory invocation.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.html">KtConstructorCalleeExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtConstructorCalleeExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.md) to a constructor call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtConstructorDelegationCall`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.md) to a delegated constructor call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.html">KtConstructorDelegationReferenceExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtConstructorDelegationReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.md) to a delegated constructor call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtDestructuringDeclarationEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.md) to a call representing the `componentN` invocation (for positional destructuring) or the property access (for name-based destructuring).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.html">KtEnumEntrySuperclassReferenceExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtEnumEntrySuperclassReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md) to a delegated constructor call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.html">KtForExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-for-loop-call/index.html">KaForLoopCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtForExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.md) to a [`KaForLoopCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-for-loop-call/index.md) representing the desugared `for` loop.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.html">KtNameReferenceExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtNameReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md) to a call representing the referenced declaration.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.html">KtPropertyDelegate</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-property-call/index.html">KaDelegatedPropertyCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtPropertyDelegate`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.md) to a [`KaDelegatedPropertyCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-property-call/index.md) representing the desugared delegated property.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtQualifiedExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.md) to a call representing the member or extension access.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.html">KtSuperTypeCallEntry</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtSuperTypeCallEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.md) to a constructor call of the referenced supertype.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.html">KtWhenConditionInRange</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtWhenConditionInRange`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.md) to a simple function call representing the corresponding `contains` operator invocation used by the `in`/`!in` branch condition.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the call for the given [`KtResolvableCall`](../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md).


</div>

</div>
### [`resolveSymbol`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#resolvesymbol)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol of the annotation referenced by the given [`KtAnnotationEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.html">KtArrayAccessExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the operator function symbol targeted by the given [`KtArrayAccessExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.html">KtCallElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the function symbol targeted by the given [`KtCallElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.html">KtCallableReferenceExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the callable symbol targeted by the given [`KtCallableReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-literal-expression/index.html">KtClassLiteralExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtClassLiteralExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-literal-expression/index.md) (`Foo::class`).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.html">KtCollectionLiteralExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the function symbol targeted by the given [`KtCollectionLiteralExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.html">KtConstructorCalleeExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol referenced by the given [`KtConstructorCalleeExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol referenced by the given [`KtConstructorDelegationCall`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.html">KtConstructorDelegationReferenceExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol referenced by the given [`KtConstructorDelegationReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-delegated-super-type-entry/index.html">KtDelegatedSuperTypeEntry</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtDelegatedSuperTypeEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-delegated-super-type-entry/index.md) (`class Foo : Bar by baz`).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the callable symbol targeted by the given [`KtDestructuringDeclarationEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.html">KtEnumEntrySuperclassReferenceExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the enum class symbol referenced by the given [`KtEnumEntrySuperclassReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-function-type/index.html">KtFunctionType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the synthetic function class symbol referenced by the given [`KtFunctionType`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-function-type/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-instance-expression-with-label/index.html">KtInstanceExpressionWithLabel</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the declaration symbol referenced by the given [`KtInstanceExpressionWithLabel`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-instance-expression-with-label/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-label-reference-expression/index.html">KtLabelReferenceExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the declaration symbol targeted by the given [`KtLabelReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-label-reference-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-nullable-type/index.html">KtNullableType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtNullableType`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-nullable-type/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the callable symbol targeted by the given [`KtQualifiedExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-return-expression/index.html">KtReturnExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the function symbol targeted by the given [`KtReturnExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-return-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.html">KtSuperTypeCallEntry</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol by the given [`KtSuperTypeCallEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-entry/index.html">KtSuperTypeEntry</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtSuperTypeEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-entry/index.md) (the no-parens form `class Foo : Bar`).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.html">KtTypeReference</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtTypeReference`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.html">KtWhenConditionInRange</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the operator function symbol targeted by the given [`KtWhenConditionInRange`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves a single symbol for the given [`KtResolvable`](../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md).


</div>

</div>
### [`resolveSymbols`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#resolvesymbols)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvesymbols"><span class="nf">resolveSymbols</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Resolves symbols for the given [`KtResolvable`](../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md).


</div>

</div>
### [`resolveToCall`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#resolvetocall)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvetocall"><span class="nf">resolveToCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/index.html">KaCallInfo</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md) to a [`KaCallInfo`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/index.md) object. [`KaCallInfo`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/index.md) either contains a successfully resolved call or an error with a list of candidate calls and a diagnostic.


</div>

</div>
### [`resolveToCallCandidates`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#resolvetocallcandidates)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvetocallcandidates"><span class="nf">resolveToCallCandidates</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-candidate-info/index.html">KaCallCandidateInfo</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all candidates considered during [overload resolution](https://kotlinlang.org/spec/overload-resolution.html) for the call corresponding to this [`KtElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md).


</div>

</div>
### [`resolveToSymbol`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#resolvetosymbol)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.html">KtReference</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvetosymbol"><span class="nf">resolveToSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtReference`](../../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.md) to a symbol.


</div>

</div>
### [`resolveToSymbols`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#resolvetosymbols)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.html">KtReference</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#resolvetosymbols"><span class="nf">resolveToSymbols</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtReference`](../../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.md) to symbols.


</div>

</div>
### restore

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#restore">T</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-pointer/index.html">KaTypePointer</a><span class="o"><</span><a href="index.html#restore">T</a><span class="o">></span><span class="p">.</span><a href="index.html#restore"><span class="nf">restore</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="index.html#restore">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the restored [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) (possibly a new type instance) if the pointer is still valid, or `null` otherwise.


</div>

</div>
### restoreSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#restoresymbol">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.pointers/-ka-symbol-pointer/index.html">KaSymbolPointer</a><span class="o"><</span><a href="index.html#restoresymbol">S</a><span class="o">></span><span class="p">.</span><a href="index.html#restoresymbol"><span class="nf">restoreSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="index.html#restoresymbol">S</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the restored [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) (possibly a new symbol instance) if the pointer is still valid, or `null` otherwise.


</div>

</div>
### [`scopeContext`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#scopecontext)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.html#scopecontext"><span class="nf">scopeContext</span></a><span class="p">(</span>position<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-context/index.html">KaScopeContext</a>
</span></code></pre></div>
</div>


<div markdown>

Computes the lexical scope context for a given [`position`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#scopecontext) in the [`KtFile`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md). The scope context includes all scopes that are relevant for the given position, together with all available implicit receivers.


</div>

</div>
### [`semanticallyEquals`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-relation-checker/index.md#semanticallyequals)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-relation-checker/index.html#semanticallyequals"><span class="nf">semanticallyEquals</span></a><span class="p">(</span>other<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>errorTypePolicy<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a><span class="o"> = </span>KaSubtypingErrorTypePolicy.STRICT<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is semantically equal to [`other`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-relation-checker/index.md#semanticallyequals).


</div>

</div>
### [`substitute`](../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.md#substitute)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#substitute">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#substitute">S</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#substitute"><span class="nf">substitute</span></a><span class="p">(</span>substitutor<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#substitute">S</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Applies a [`substitutor`](../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.md#substitute) to the given symbol and returns a [`KaCallableSignature`](../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.md) with substituted types.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#substitute">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#substitute">S</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#substitute"><span class="nf">substitute</span></a><span class="p">(</span>substitutor<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-function-signature/index.html">KaFunctionSignature</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#substitute">S</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Applies a [`substitutor`](../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.md#substitute) to the given symbol and returns a [`KaFunctionSignature`](../../org.jetbrains.kotlin.analysis.api.signatures/-ka-function-signature/index.md) with substituted types.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#substitute">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#substitute">S</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#substitute"><span class="nf">substitute</span></a><span class="p">(</span>substitutor<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-variable-signature/index.html">KaVariableSignature</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.html#substitute">S</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Applies a [`substitutor`](../../org.jetbrains.kotlin.analysis.api.components/-ka-signature-substitutor/index.md#substitute) to the given symbol and returns a [`KaVariableSignature`](../../org.jetbrains.kotlin.analysis.api.signatures/-ka-variable-signature/index.md) with substituted types.


</div>

</div>
### [`tryResolveCall`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#tryresolvecall)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.html">KtForExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#tryresolvecall"><span class="nf">tryResolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-for-loop-call-resolution-attempt/index.html">KaForLoopCallResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve the given [`KtForExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.md) to a [`KaForLoopCallResolutionAttempt`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-for-loop-call-resolution-attempt/index.md) containing the individual resolution results for each desugared operator call (`iterator`, `hasNext`, `next`).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.html">KtPropertyDelegate</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#tryresolvecall"><span class="nf">tryResolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-property-call-resolution-attempt/index.html">KaDelegatedPropertyCallResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve the given [`KtPropertyDelegate`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.md) to a [`KaDelegatedPropertyCallResolutionAttempt`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-property-call-resolution-attempt/index.md) containing the individual resolution results for each desugared operator call (`getValue`, `setValue`, `provideDelegate`).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#tryresolvecall"><span class="nf">tryResolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve the call for the given [`KtResolvableCall`](../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md).


</div>

</div>
### [`tryResolveSymbols`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#tryresolvesymbols)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.html#tryresolvesymbols"><span class="nf">tryResolveSymbols</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve a symbol for the given [`KtResolvable`](../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md).


</div>

</div>
### [`upperBoundIfFlexible`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#upperboundifflexible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#upperboundifflexible"><span class="nf">upperBoundIfFlexible</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md)'s upper bound, or the type itself if it is not flexible.


</div>

</div>
### [`withNullability`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#withnullability)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.html#withnullability"><span class="nf">withNullability</span></a><span class="p">(</span>isMarkedNullable<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a new [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) based on the given type with the updated nullability specified by [`isMarkedNullable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-provider/index.md#withnullability).


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
