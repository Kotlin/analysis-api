---
tags:
 - jvm
title: "org.jetbrains.kotlin.psi"
---

# org.jetbrains.kotlin.psi
## Types
### [`BuilderByPattern`](-builder-by-pattern/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-builder-by-pattern/index.html">BuilderByPattern</a><span class="o"><</span><a href="-builder-by-pattern/index.html">TElement</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A builder that assembles a [`createByPattern`](create-by-pattern.md) pattern step by step, appending fixed text, expressions, type references, names, and child ranges in order and tracking their placeholders automatically.


</div>

</div>
### [`FakeImplicitSpreadValueArgumentForCallableReference`](-fake-implicit-spread-value-argument-for-callable-reference/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-fake-implicit-spread-value-argument-for-callable-reference/index.html">FakeImplicitSpreadValueArgumentForCallableReference</a> : <a href="-value-argument/index.html">ValueArgument</a>
</span></code></pre></div>
</div>


<div markdown>

A synthetic spread [`ValueArgument`](-value-argument/index.md) used when modeling the implicit vararg spread of a callable reference.


</div>

</div>
### [`FakePositionalValueArgumentForCallableReference`](-fake-positional-value-argument-for-callable-reference/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-fake-positional-value-argument-for-callable-reference/index.html">FakePositionalValueArgumentForCallableReference</a> : <a href="-value-argument/index.html">ValueArgument</a>
</span></code></pre></div>
</div>


<div markdown>

A synthetic positional [`ValueArgument`](-value-argument/index.md) used when modeling the arguments of a callable reference, where arguments have no corresponding source PSI.


</div>

</div>
### [`IfNotParsed`](-if-not-parsed/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/annotation/Retention.html"><span class="se">Retention</span></a><span class="p">(</span>value<span class="o"> = </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/annotation/RetentionPolicy.html">RetentionPolicy.RUNTIME</a><span class="p">)</span>
<span class="se">@</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/annotation/Target.html"><span class="se">Target</span></a><span class="p">(</span>value<span class="o"> = </span><span class="p">[</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/annotation/ElementType.html">ElementType.METHOD</a><span class="p">]</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-if-not-parsed/index.html">IfNotParsed</a>
</span></code></pre></div>
</div>


<div markdown>

Comes along with @Nullable to indicate null is only possible if parsing error present

</div>

</div>
### [`KotlinCodeFragmentImportModificationListener`](-kotlin-code-fragment-import-modification-listener/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="kd">interface </span><a href="-kotlin-code-fragment-import-modification-listener/index.html">KotlinCodeFragmentImportModificationListener</a>
</span></code></pre></div>
</div>


<div markdown>

A listener notified when the imports of a [`KtCodeFragment`](-kt-code-fragment/index.md) are modified.


</div>

</div>
### [`KotlinDeclarationNavigationPolicy`](-kotlin-declaration-navigation-policy/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-declaration-navigation-policy/index.html">KotlinDeclarationNavigationPolicy</a>
</span></code></pre></div>
</div>


<div markdown>

A service that maps a [`KtDeclaration`](-kt-declaration/index.md) between its "original" and its "navigation" element.


</div>

</div>
### [`KotlinReferenceProvidersService`](-kotlin-reference-providers-service/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kotlin-reference-providers-service/index.html">KotlinReferenceProvidersService</a>
</span></code></pre></div>
</div>


<div markdown>

A project service that collects the PsiReferences contributed to a PSI element by the registered reference providers.


</div>

</div>
### [`KotlinStringLiteralTextEscaper`](-kotlin-string-literal-text-escaper/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-string-literal-text-escaper/index.html">KotlinStringLiteralTextEscaper</a><span class="p">(</span>host<span class="o">: </span><a href="-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="p">)</span> : LiteralTextEscaper<span class="o"><</span><a href="-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A LiteralTextEscaper for Kotlin string literals, enabling language injection into them.


</div>

</div>
### [`KtAnnotated`](-kt-annotated/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-annotated/index.html">KtAnnotated</a> : <a href="-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an element that owns annotations (the element may or may not be the parent for the annotations).

</div>

</div>
### [`KtAnnotatedExpression`](-kt-annotated-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-annotated-expression/index.html">KtAnnotatedExpression</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>, <a href="-kt-annotated/index.html">KtAnnotated</a>, <a href="-kt-annotations-container/index.html">KtAnnotationsContainer</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an expression with annotations applied to it.

</div>

</div>
### [`KtAnnotation`](-kt-annotation/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-annotation/index.html">KtAnnotation</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-annotation/index.html">KtAnnotation</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a bracketed group of annotation entries applied to the same use-site target, which avoids repeating the target for each entry.

</div>

</div>
### [`KtAnnotationEntry`](-kt-annotation-entry/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-annotation-entry/index.html">KtAnnotationEntry</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-annotation-entry-stub/index.html">KotlinAnnotationEntryStub</a><span class="o">> </span>, <a href="-kt-call-element/index.html">KtCallElement</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a single annotation applied to a declaration or expression.

</div>

</div>
### [`KtAnnotationsContainer`](-kt-annotations-container/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-annotations-container/index.html">KtAnnotationsContainer</a> : <a href="-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an element that may contain annotations (the container is the parent for them).

</div>

</div>
### [`KtAnnotationUseSiteTarget`](-kt-annotation-use-site-target/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-annotation-use-site-target/index.html">KtAnnotationUseSiteTarget</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-annotation-use-site-target-stub/index.html">KotlinAnnotationUseSiteTargetStub</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents an annotation use-site target that specifies where the annotation should be applied.


</div>

</div>
### [`KtAnonymousInitializer`](-kt-anonymous-initializer/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-kt-anonymous-initializer/index.html">KtAnonymousInitializer</a> : <a href="-kt-declaration/index.html">KtDeclaration</a>, <a href="-kt-statement-expression/index.html">KtStatementExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an anonymous initializer: a piece of code that runs during initialization without introducing a named declaration.


</div>

</div>
### [`KtArrayAccessExpression`](-kt-array-access-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-array-access-expression/index.html">KtArrayAccessExpression</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>, <a href="-kt-reference-expression/index.html">KtReferenceExpression</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an indexed access expression using square brackets.

</div>

</div>
### [`KtBackingField`](-kt-backing-field/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">open </span><span class="kd">class </span><a href="-kt-backing-field/index.html">KtBackingField</a> : <a href="-kt-declaration-stub/index.html">KtDeclarationStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-backing-field-stub/index.html">KotlinBackingFieldStub</a><span class="o">> </span>, <a href="-kt-modifier-list-owner/index.html">KtModifierListOwner</a>, <a href="-kt-declaration-with-initializer/index.html">KtDeclarationWithInitializer</a>, <a href="-kt-declaration-with-return-type/index.html">KtDeclarationWithReturnType</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an explicit backing field declaration for a property.


</div>

</div>
### [`KtBinaryExpression`](-kt-binary-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-binary-expression/index.html">KtBinaryExpression</a> : <a href="-kt-expression-impl-stub/index.html">KtExpressionImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-binary-expression/index.html">KtBinaryExpression</a><span class="o">></span><span class="o">> </span>, <a href="-kt-operation-expression/index.html">KtOperationExpression</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a binary expression with a left operand, operator, and right operand.

</div>

</div>
### [`KtBinaryExpressionWithTypeRHS`](-kt-binary-expression-with-type-r-h-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-binary-expression-with-type-r-h-s/index.html">KtBinaryExpressionWithTypeRHS</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>, <a href="-kt-operation-expression/index.html">KtOperationExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a type cast expression using `#!java as` or `#!java as?`.

</div>

</div>
### [`KtBlockCodeFragment`](-kt-block-code-fragment/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-block-code-fragment/index.html">KtBlockCodeFragment</a><span class="p">(</span>
    viewProvider<span class="o">: </span>FileViewProvider<span class="p">, </span>
    imports<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">, </span>
    context<span class="o">: </span>PsiElement<span class="o">?</span>
<span class="p">)</span> : <a href="-kt-code-fragment/index.html">KtCodeFragment</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KtCodeFragment`](-kt-code-fragment/index.md) whose content is a block of statements, as opposed to a single expression.


</div>

</div>
### [`KtBlockExpression`](-kt-block-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-block-expression/index.html">KtBlockExpression</a> : LazyParseablePsiElement, <a href="-kt-element/index.html">KtElement</a>, <a href="-kt-expression/index.html">KtExpression</a>, <a href="-kt-statement-expression/index.html">KtStatementExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a block of statements enclosed in curly braces.

</div>

</div>
### [`KtBlockStringTemplateEntry`](-kt-block-string-template-entry/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-block-string-template-entry/index.html">KtBlockStringTemplateEntry</a> : <a href="-kt-string-template-entry-with-expression/index.html">KtStringTemplateEntryWithExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a block interpolation in a string template using `#!java ${expression}`.

</div>

</div>
### [`KtBreakExpression`](-kt-break-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-break-expression/index.html">KtBreakExpression</a> : <a href="-kt-expression-with-label/index.html">KtExpressionWithLabel</a>, <a href="-kt-statement-expression/index.html">KtStatementExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java break` expression that terminates the enclosing loop.

</div>

</div>
### [`KtCallableDeclaration`](-kt-callable-declaration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-callable-declaration/index.html">KtCallableDeclaration</a> : <a href="-kt-named-declaration/index.html">KtNamedDeclaration</a>, <a href="-kt-declaration-with-return-type/index.html">KtDeclarationWithReturnType</a>, <a href="-kt-type-parameter-list-owner/index.html">KtTypeParameterListOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a declaration with the structure of a callable: it may declare value parameters, an extension receiver, type parameters (with constraints), and a return type.

</div>

</div>
### [`KtCallableReferenceExpression`](-kt-callable-reference-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-callable-reference-expression/index.html">KtCallableReferenceExpression</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>, <a href="-kt-double-colon-expression/index.html">KtDoubleColonExpression</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a callable reference expression using double colon syntax.

</div>

</div>
### [`KtCallElement`](-kt-call-element/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-call-element/index.html">KtCallElement</a> : <a href="-kt-element/index.html">KtElement</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an element with call syntax: a callee together with type arguments and value arguments.

</div>

</div>
### [`KtCallExpression`](-kt-call-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">open </span><span class="kd">class </span><a href="-kt-call-expression/index.html">KtCallExpression</a> : <a href="-kt-expression-impl-stub/index.html">KtExpressionImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-call-expression/index.html">KtCallExpression</a><span class="o">></span><span class="o">> </span>, <a href="-kt-call-element/index.html">KtCallElement</a>, <a href="-kt-reference-expression/index.html">KtReferenceExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a function call expression, including the callee and arguments.


</div>

</div>
### [`KtCatchClause`](-kt-catch-clause/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-catch-clause/index.html">KtCatchClause</a> : <a href="-kt-element-impl/index.html">KtElementImpl</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java catch` clause in a `#!java try` expression.

</div>

</div>
### [`KtClass`](-kt-class/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">open </span><span class="kd">class </span><a href="-kt-class/index.html">KtClass</a> : <a href="-kt-class-or-object/index.html">KtClassOrObject</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a class or interface declaration.


</div>

</div>
### [`KtClassBody`](-kt-class-body/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-class-body/index.html">KtClassBody</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-class-body/index.html">KtClassBody</a><span class="o">></span><span class="o">> </span>, <a href="-kt-declaration-container/index.html">KtDeclarationContainer</a>
</span></code></pre></div>
</div>


<div markdown>

Represents the body of a class or object declaration enclosed in curly braces.


</div>

</div>
### [`KtClassInitializer`](-kt-class-initializer/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-class-initializer/index.html">KtClassInitializer</a> : <a href="-kt-declaration-stub/index.html">KtDeclarationStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-class-initializer/index.html">KtClassInitializer</a><span class="o">></span><span class="o">> </span>, <a href="-kt-anonymous-initializer/index.html">KtAnonymousInitializer</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an init block in a class that executes during instance initialization.


</div>

</div>
### [`KtClassLikeDeclaration`](-kt-class-like-declaration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-kt-class-like-declaration/index.html">KtClassLikeDeclaration</a> : <a href="-kt-named-declaration/index.html">KtNamedDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a declaration that introduces a classifier referable by a ClassId, namely a class, interface, object, or type alias.


</div>

</div>
### [`KtClassLiteralExpression`](-kt-class-literal-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-class-literal-expression/index.html">KtClassLiteralExpression</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-class-literal-expression/index.html">KtClassLiteralExpression</a><span class="o">></span><span class="o">> </span>, <a href="-kt-double-colon-expression/index.html">KtDoubleColonExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a class literal expression that gets a class reference.

</div>

</div>
### [`KtClassOrObject`](-kt-class-or-object/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-kt-class-or-object/index.html">KtClassOrObject</a> : <a href="-kt-type-parameter-list-owner-stub/index.html">KtTypeParameterListOwnerStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-class-or-object-stub/index.html">KotlinClassOrObjectStub</a><span class="o"><</span><span class="kd">out </span><a href="-kt-class-or-object/index.html">KtClassOrObject</a><span class="o">></span><span class="o">> </span>, <a href="-kt-declaration-container/index.html">KtDeclarationContainer</a>, <a href="-kt-named-declaration/index.html">KtNamedDeclaration</a>, <a href="-kt-pure-class-or-object/index.html">KtPureClassOrObject</a>, <a href="-kt-class-like-declaration/index.html">KtClassLikeDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a class, interface, object, or enum entry declaration.


</div>

</div>
### [`KtCodeFragment`](-kt-code-fragment/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-kt-code-fragment/index.html">KtCodeFragment</a><span class="p">(</span>
    viewProvider<span class="o">: </span>FileViewProvider<span class="p">, </span>
    imports<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">, </span>
    elementType<span class="o">: </span>IElementType<span class="p">, </span>
    context<span class="o">: </span>PsiElement<span class="o">?</span>
<span class="p">)</span> : <a href="-kt-file/index.html">KtFile</a>, <a href="-kt-code-fragment-base/index.html">KtCodeFragmentBase</a>
</span></code></pre></div>
</div>


<div markdown>

A synthetic, in-memory Kotlin file that holds a standalone snippet of code together with a context.


</div>

</div>
### [`KtCodeFragmentBase`](-kt-code-fragment-base/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-code-fragment-base/index.html">KtCodeFragmentBase</a> : JavaCodeFragment
</span></code></pre></div>
</div>


<div markdown>

The Java-interop base for [`KtCodeFragment`](-kt-code-fragment/index.md), adapting the platform's JavaCodeFragment contract to Kotlin.


</div>

</div>
### [`KtCollectionLiteralExpression`](-kt-collection-literal-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-collection-literal-expression/index.html">KtCollectionLiteralExpression</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-collection-literal-expression-stub/index.html">KotlinCollectionLiteralExpressionStub</a><span class="o">> </span>, <a href="-kt-reference-expression/index.html">KtReferenceExpression</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a collection literal expression.

</div>

</div>
### [`KtCompanionBlock`](-kt-companion-block/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-companion-block/index.html">KtCompanionBlock</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-companion-block/index.html">KtCompanionBlock</a><span class="o">></span><span class="o">> </span>, <a href="-kt-declaration-container/index.html">KtDeclarationContainer</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a companion block.


</div>

</div>
### [`KtConstantExpression`](-kt-constant-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-constant-expression/index.html">KtConstantExpression</a> : <a href="-kt-expression-impl-stub/index.html">KtExpressionImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-constant-expression-stub/index.html">KotlinConstantExpressionStub</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a constant literal expression such as numbers, booleans, or characters.

</div>

</div>
### [`KtConstructor`](-kt-constructor/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-kt-constructor/index.html">KtConstructor</a><span class="o"><</span><a href="-kt-constructor/index.html">T</a><span class="o"> : </span><a href="-kt-constructor/index.html">KtConstructor</a><span class="o"><</span><a href="-kt-constructor/index.html">T</a><span class="o">></span><span class="o">></span> : <a href="-kt-declaration-stub/index.html">KtDeclarationStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-constructor-stub/index.html">KotlinConstructorStub</a><span class="o"><</span><a href="-kt-constructor/index.html">T</a><span class="o">></span><span class="o">> </span>, <a href="-kt-function/index.html">KtFunction</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a constructor of a class or object.


</div>

</div>
### [`KtConstructorCalleeExpression`](-kt-constructor-callee-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-constructor-callee-expression/index.html">KtConstructorCalleeExpression</a> : <a href="-kt-expression-impl-stub/index.html">KtExpressionImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-constructor-callee-expression/index.html">KtConstructorCalleeExpression</a><span class="o">></span><span class="o">> </span>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents the callee part in a constructor invocation, such as in annotations or super type calls.

</div>

</div>
### [`KtConstructorDelegationCall`](-kt-constructor-delegation-call/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a> : <a href="-kt-element-impl/index.html">KtElementImpl</a>, <a href="-kt-call-element/index.html">KtCallElement</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a constructor delegation call to `#!java this()` or `#!java super()`.

</div>

</div>
### [`KtConstructorDelegationReferenceExpression`](-kt-constructor-delegation-reference-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-constructor-delegation-reference-expression/index.html">KtConstructorDelegationReferenceExpression</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>, <a href="-kt-reference-expression/index.html">KtReferenceExpression</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents the `#!java this` or `#!java super` reference in a constructor delegation call.

</div>

</div>
### [`KtContainerNode`](-kt-container-node/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-container-node/index.html">KtContainerNode</a> : <a href="-kt-element-impl/index.html">KtElementImpl</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an auxiliary container node that wraps other PSI elements without adding semantic meaning.

</div>

</div>
### [`KtContainerNodeForControlStructureBody`](-kt-container-node-for-control-structure-body/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-container-node-for-control-structure-body/index.html">KtContainerNodeForControlStructureBody</a> : <a href="-kt-container-node/index.html">KtContainerNode</a>
</span></code></pre></div>
</div>


<div markdown>

A wrapper node that holds the body of a control structure, such as an `if`/`else` branch or a loop body.


</div>

</div>
### [`KtContextParameterList`](-kt-context-parameter-list/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-kt-context-parameter-list/index.html">KtContextParameterList</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-context-parameter-list/index.html">KtContextParameterList</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

The class representing a context parameter list in a declaration or functional type.


</div>

</div>
### [`KtContextReceiver`](-kt-context-receiver/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-context-receiver/index.html">KtContextReceiver</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-context-receiver-stub/index.html">KotlinContextReceiverStub</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a single context receiver in a context receiver list.


</div>

</div>
### [`KtContextReceiverList`](-kt-context-receiver-list/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-context-receiver-list/index.html">KtContextReceiverList</a> : <a href="-kt-context-parameter-list/index.html">KtContextParameterList</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a list of context receivers declared on a function, property, or class.


</div>

</div>
### [`KtContinueExpression`](-kt-continue-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-continue-expression/index.html">KtContinueExpression</a> : <a href="-kt-expression-with-label/index.html">KtExpressionWithLabel</a>, <a href="-kt-statement-expression/index.html">KtStatementExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java continue` expression that skips to the next iteration of the enclosing loop.

</div>

</div>
### [`KtContractEffect`](-kt-contract-effect/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-contract-effect/index.html">KtContractEffect</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-contract-effect/index.html">KtContractEffect</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a single effect declaration inside a contract block.


</div>

</div>
### [`KtContractEffectList`](-kt-contract-effect-list/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-contract-effect-list/index.html">KtContractEffectList</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-contract-effect-list/index.html">KtContractEffectList</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents the list of contract effects in a contract block.


</div>

</div>
### [`KtDeclaration`](-kt-declaration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-declaration/index.html">KtDeclaration</a> : <a href="-kt-expression/index.html">KtExpression</a>, <a href="-kt-modifier-list-owner/index.html">KtModifierListOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a Kotlin declaration: a construct that introduces a named or structural entity, such as a class, function, property, type alias, parameter, or type parameter.

</div>

</div>
### [`KtDeclarationContainer`](-kt-declaration-container/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-declaration-container/index.html">KtDeclarationContainer</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an element that contains a list of declarations, such as a file, a class or object body, or a script.

</div>

</div>
### [`KtDeclarationImpl`](-kt-declaration-impl/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-declaration-impl/index.html">KtDeclarationImpl</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>, <a href="-kt-declaration/index.html">KtDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Base implementation of [`KtDeclaration`](-kt-declaration/index.md) backed directly by the AST tree.

</div>

</div>
### [`KtDeclarationModifierList`](-kt-declaration-modifier-list/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-declaration-modifier-list/index.html">KtDeclarationModifierList</a> : <a href="-kt-modifier-list/index.html">KtModifierList</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a modifier list attached to a declaration.

</div>

</div>
### [`KtDeclarationStub`](-kt-declaration-stub/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-declaration-stub/index.html">KtDeclarationStub</a><span class="o"><</span><a href="-kt-declaration-stub/index.html">T</a><span class="o"> : </span>StubElement<span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span><span class="o">></span> : <a href="-kt-modifier-list-owner-stub/index.html">KtModifierListOwnerStub</a><span class="o"><</span><a href="-kt-declaration-stub/index.html">T</a><span class="o">> </span>, <a href="-kt-declaration/index.html">KtDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Base implementation of [`KtDeclaration`](-kt-declaration/index.md) that may be backed either by the AST tree or by a stub.

</div>

</div>
### [`KtDeclarationWithBody`](-kt-declaration-with-body/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-declaration-with-body/index.html">KtDeclarationWithBody</a> : <a href="-kt-declaration/index.html">KtDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a declaration that can have a body, such as a function, a property accessor, or an anonymous initializer.

</div>

</div>
### [`KtDeclarationWithInitializer`](-kt-declaration-with-initializer/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-declaration-with-initializer/index.html">KtDeclarationWithInitializer</a> : <a href="-kt-declaration/index.html">KtDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a declaration that can have an expression after `#!java =`, such as a property, a destructuring declaration, a named function, or a property accessor.

</div>

</div>
### [`KtDeclarationWithReturnType`](-kt-declaration-with-return-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-declaration-with-return-type/index.html">KtDeclarationWithReturnType</a> : <a href="-kt-declaration/index.html">KtDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a Kotlin declaration that semantically has a return type (ex.

</div>

</div>
### [`KtDelegatedSuperTypeEntry`](-kt-delegated-super-type-entry/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-delegated-super-type-entry/index.html">KtDelegatedSuperTypeEntry</a> : <a href="-kt-super-type-list-entry/index.html">KtSuperTypeListEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an interface delegation in the super type list using the `#!java by` keyword.

</div>

</div>
### [`KtDestructuringDeclaration`](-kt-destructuring-declaration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-destructuring-declaration/index.html">KtDestructuringDeclaration</a> : <a href="-kt-declaration-stub/index.html">KtDeclarationStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-destructuring-declaration-stub/index.html">KotlinDestructuringDeclarationStub</a><span class="o">> </span>, <a href="-kt-val-var-keyword-owner/index.html">KtValVarKeywordOwner</a>, <a href="-kt-declaration-with-initializer/index.html">KtDeclarationWithInitializer</a>, <a href="-kt-declaration-with-return-type/index.html">KtDeclarationWithReturnType</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a destructuring declaration that unpacks an object into multiple variables.

</div>

</div>
### [`KtDestructuringDeclarationEntry`](-kt-destructuring-declaration-entry/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a> : <a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-named-declaration-not-stubbed/index.html">KtNamedDeclarationNotStubbed</a>, <a href="-kt-variable-declaration/index.html">KtVariableDeclaration</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a single entry in a destructuring declaration.

</div>

</div>
### [`KtDotQualifiedExpression`](-kt-dot-qualified-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-dot-qualified-expression/index.html">KtDotQualifiedExpression</a> : <a href="-kt-expression-impl-stub/index.html">KtExpressionImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-dot-qualified-expression/index.html">KtDotQualifiedExpression</a><span class="o">></span><span class="o">> </span>, <a href="-kt-qualified-expression/index.html">KtQualifiedExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a dot-qualified expression for member/extension access.


</div>

</div>
### [`KtDoubleColonExpression`](-kt-double-colon-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-kt-double-colon-expression/index.html">KtDoubleColonExpression</a> : <a href="-kt-expression/index.html">KtExpression</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an expression that uses the `::` token, namely a callable reference or a class literal.


</div>

</div>
### [`KtDoWhileExpression`](-kt-do-while-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-do-while-expression/index.html">KtDoWhileExpression</a> : <a href="-kt-while-expression-base/index.html">KtWhileExpressionBase</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java do`-`#!java while` loop that executes its body at least once before checking the condition.

</div>

</div>
### [`KtDynamicType`](-kt-dynamic-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-dynamic-type/index.html">KtDynamicType</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-dynamic-type/index.html">KtDynamicType</a><span class="o">></span><span class="o">> </span>, <a href="-kt-type-element/index.html">KtTypeElement</a>
</span></code></pre></div>
</div>


<div markdown>

Represents the `#!java dynamic` type used in Kotlin/JS for interoperability.

</div>

</div>
### [`KtElement`](-kt-element/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-kt-element/index.html">KtElement</a> : NavigatablePsiElement, <a href="-kt-pure-element/index.html">KtPureElement</a>
</span></code></pre></div>
</div>


<div markdown>

The root interface of the Kotlin PSI (Program Structure Interface) hierarchy.


</div>

</div>
### [`KtElementImpl`](-kt-element-impl/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-element-impl/index.html">KtElementImpl</a> : ASTWrapperPsiElement, <a href="-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Base implementation of [`KtElement`](-kt-element/index.md) backed directly by the AST tree.

</div>

</div>
### [`KtElementImplStub`](-kt-element-impl-stub/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="-kt-element-impl-stub/index.html">T</a><span class="o"> : </span>StubElement<span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span><span class="o">></span> : StubBasedPsiElementBase<span class="o"><</span><a href="-kt-element-impl-stub/index.html">T</a><span class="o">> </span>, <a href="-kt-element/index.html">KtElement</a>, StubBasedPsiElement<span class="o"><</span><a href="-kt-element-impl-stub/index.html">T</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Base implementation of [`KtElement`](-kt-element/index.md) that may be backed either by the AST tree or by a stub.

</div>

</div>
### [`KtEnumEntry`](-kt-enum-entry/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-enum-entry/index.html">KtEnumEntry</a> : <a href="-kt-class/index.html">KtClass</a>, <a href="-kt-declaration-with-return-type/index.html">KtDeclarationWithReturnType</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an `#!java enum` entry within an `#!java enum` class.

</div>

</div>
### [`KtEnumEntrySuperclassReferenceExpression`](-kt-enum-entry-superclass-reference-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-enum-entry-superclass-reference-expression/index.html">KtEnumEntrySuperclassReferenceExpression</a> : <a href="-kt-expression-impl-stub/index.html">KtExpressionImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-enum-entry-superclass-reference-expression-stub/index.html">KotlinEnumEntrySuperclassReferenceExpressionStub</a><span class="o">> </span>, <a href="-kt-simple-name-expression/index.html">KtSimpleNameExpression</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a synthetic reference to the enum class constructor in an enum entry initializer.


</div>

</div>
### [`KtErrorSafeQualifiedExpression`](-kt-error-safe-qualified-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-kt-error-safe-qualified-expression/index.html">KtErrorSafeQualifiedExpression</a> : <a href="-kt-qualified-expression/index.html">KtQualifiedExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an error-safe-call expression using the `|.` operator.


</div>

</div>
### [`KtEscapeStringTemplateEntry`](-kt-escape-string-template-entry/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-escape-string-template-entry/index.html">KtEscapeStringTemplateEntry</a> : <a href="-kt-string-template-entry/index.html">KtStringTemplateEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an escape sequence in a string template.

</div>

</div>
### [`KtExperimentalApi`](-kt-experimental-api/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html">AnnotationTarget.CLASS</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html">AnnotationTarget.CONSTRUCTOR</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html">AnnotationTarget.TYPEALIAS</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"Experimental API with no compatibility guarantees"</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-kt-experimental-api/index.html">KtExperimentalApi</a>
</span></code></pre></div>
</div>


<div markdown>

Marks an API as experimental. The API is intended for user consumption, but it's not stable and might change at any moment, or even be removed, without a deprecation cycle.


</div>

</div>
### [`KtExpression`](-kt-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-expression/index.html">KtExpression</a> : <a href="-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a Kotlin expression: a piece of code that can be evaluated to a value, such as a literal, an operator application, a function call, or an `#!java if`/`#!java when` used as a value.

</div>

</div>
### [`KtExpressionCodeFragment`](-kt-expression-code-fragment/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-expression-code-fragment/index.html">KtExpressionCodeFragment</a><span class="p">(</span>
    project<span class="o">: </span>Project<span class="p">, </span>
    name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/index.html">CharSequence</a><span class="p">, </span>
    imports<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">, </span>
    context<span class="o">: </span>PsiElement<span class="o">?</span>
<span class="p">)</span> : <a href="-kt-code-fragment/index.html">KtCodeFragment</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KtCodeFragment`](-kt-code-fragment/index.md) whose content is a single expression.


</div>

</div>
### [`KtExpressionImpl`](-kt-expression-impl/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-kt-expression-impl/index.html">KtExpressionImpl</a> : <a href="-kt-element-impl/index.html">KtElementImpl</a>, <a href="-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Base implementation of [`KtExpression`](-kt-expression/index.md) backed directly by the AST tree.


</div>

</div>
### [`KtExpressionImplStub`](-kt-expression-impl-stub/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-expression-impl-stub/index.html">KtExpressionImplStub</a><span class="o"><</span><a href="-kt-expression-impl-stub/index.html">T</a><span class="o"> : </span>StubElement<span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span><span class="o">></span> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="-kt-expression-impl-stub/index.html">T</a><span class="o">> </span>, <a href="-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Base implementation of [`KtExpression`](-kt-expression/index.md) that may be backed either by the AST tree or by a stub.

</div>

</div>
### [`KtExpressionWithLabel`](-kt-expression-with-label/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">open </span><span class="kd">class </span><a href="-kt-expression-with-label/index.html">KtExpressionWithLabel</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an expression that may contain a label qualifier. A [`KtLabeledExpression`](-kt-labeled-expression/index.md) declares a label with `label@`, while labeled `break`/`continue`, qualified `return`, and qualified `this`/`super` expressions reference one with `@label`.


</div>

</div>
### [`KtFile`](-kt-file/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">open </span><span class="kd">class </span><a href="-kt-file/index.html">KtFile</a><span class="p">(</span>viewProvider<span class="o">: </span>FileViewProvider<span class="p">, </span>isCompiled<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span> : <a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-common-file/index.html">KtCommonFile</a>, PsiClassOwner
</span></code></pre></div>
</div>


<div markdown>

The root of the PSI tree for a Kotlin source or script file.


</div>

</div>
### [`KtFileAnnotationList`](-kt-file-annotation-list/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-file-annotation-list/index.html">KtFileAnnotationList</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-file-annotation-list/index.html">KtFileAnnotationList</a><span class="o">></span><span class="o">> </span>, <a href="-kt-annotations-container/index.html">KtAnnotationsContainer</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a list of file-level annotations at the beginning of a Kotlin file.

</div>

</div>
### [`KtFileClassProvider`](-kt-file-class-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-file-class-provider/index.html">KtFileClassProvider</a>
</span></code></pre></div>
</div>


<div markdown>

A service that computes the Java light classes exposed by a [`KtFile`](-kt-file/index.md) (its file facade class and top-level class declarations).


</div>

</div>
### [`KtFinallySection`](-kt-finally-section/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-finally-section/index.html">KtFinallySection</a> : <a href="-kt-element-impl/index.html">KtElementImpl</a>, <a href="-kt-statement-expression/index.html">KtStatementExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java finally` block in a `#!java try` expression.

</div>

</div>
### [`KtForExpression`](-kt-for-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-for-expression/index.html">KtForExpression</a> : <a href="-kt-loop-expression/index.html">KtLoopExpression</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java for` loop.

</div>

</div>
### [`KtFunction`](-kt-function/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-function/index.html">KtFunction</a> : <a href="-kt-declaration-with-body/index.html">KtDeclarationWithBody</a>, <a href="-kt-callable-declaration/index.html">KtCallableDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a function: a named function, a function literal (lambda or anonymous function), or a constructor.

</div>

</div>
### [`KtFunctionLiteral`](-kt-function-literal/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-function-literal/index.html">KtFunctionLiteral</a> : <a href="-kt-function-not-stubbed/index.html">KtFunctionNotStubbed</a>
</span></code></pre></div>
</div>


<div markdown>

Represents the body of a lambda expression, containing parameters and the function body.

</div>

</div>
### [`KtFunctionNotStubbed`](-kt-function-not-stubbed/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-function-not-stubbed/index.html">KtFunctionNotStubbed</a> : <a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-type-parameter-list-owner-not-stubbed/index.html">KtTypeParameterListOwnerNotStubbed</a>, <a href="-kt-function/index.html">KtFunction</a>
</span></code></pre></div>
</div>


<div markdown>

Base implementation of [`KtFunction`](-kt-function/index.md) for functions that are never backed by a stub, such as function literals and anonymous functions.

</div>

</div>
### [`KtFunctionType`](-kt-function-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-function-type/index.html">KtFunctionType</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-function-type-stub/index.html">KotlinFunctionTypeStub</a><span class="o">> </span>, <a href="-kt-type-element/index.html">KtTypeElement</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a function type with parameters and return type.

</div>

</div>
### [`KtFunctionTypeReceiver`](-kt-function-type-receiver/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-function-type-receiver/index.html">KtFunctionTypeReceiver</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-function-type-receiver/index.html">KtFunctionTypeReceiver</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents the receiver type in a function type with receiver.

</div>

</div>
### [`KtIdeApi`](-kt-ide-api/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html">AnnotationTarget.CLASS</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html">AnnotationTarget.CONSTRUCTOR</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html">AnnotationTarget.TYPEALIAS</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"Internal API which is used only from the IntelliJ Kotlin plugin. Such an API should not be used in other places since it has no compatibility guarantees"</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-kt-ide-api/index.html">KtIdeApi</a>
</span></code></pre></div>
</div>


<div markdown>

Marks an API as designed for and internal to the Kotlin IntelliJ plugin. The API is not intended for public user consumption and does not have any compatibility guarantees.


</div>

</div>
### [`KtIfExpression`](-kt-if-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-if-expression/index.html">KtIfExpression</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an `#!java if` expression with condition, then branch, and optional `#!java else` branch.

</div>

</div>
### [`KtImplementationDetail`](-kt-implementation-detail/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"Internal API which should not be used outside the Kotlin PSI API implementation modules as it does not have any compatibility guarantees"</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-kt-implementation-detail/index.html">KtImplementationDetail</a>
</span></code></pre></div>
</div>


<div markdown>

Marks an API as an implementation detail of the Kotlin PSI API. Such APIs are not intended to be used outside the implementation of the PSI API and have no compatibility guarantees.


</div>

</div>
### [`KtImportAlias`](-kt-import-alias/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-import-alias/index.html">KtImportAlias</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-import-alias-stub/index.html">KotlinImportAliasStub</a><span class="o">> </span>, PsiNameIdentifierOwner
</span></code></pre></div>
</div>


<div markdown>

Represents an import alias that provides an alternative name for an imported declaration.


</div>

</div>
### [`KtImportDirective`](-kt-import-directive/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-import-directive/index.html">KtImportDirective</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-import-directive-stub/index.html">KotlinImportDirectiveStub</a><span class="o">> </span>, <a href="-kt-import-info/index.html">KtImportInfo</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a single `#!java import` directive.

</div>

</div>
### [`KtImportInfo`](-kt-import-info/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-import-info/index.html">KtImportInfo</a>
</span></code></pre></div>
</div>


<div markdown>

A representation-agnostic view of a single import statement.


</div>

</div>
### [`KtImportList`](-kt-import-list/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-import-list/index.html">KtImportList</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-import-list/index.html">KtImportList</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents the list of `#!java import` directives in a Kotlin file.

</div>

</div>
### [`KtInitializerList`](-kt-initializer-list/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-initializer-list/index.html">KtInitializerList</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-initializer-list/index.html">KtInitializerList</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents the initializer list for an `#!java enum` entry with constructor arguments.

</div>

</div>
### [`KtInstanceExpressionWithLabel`](-kt-instance-expression-with-label/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-instance-expression-with-label/index.html">KtInstanceExpressionWithLabel</a> : <a href="-kt-expression-with-label/index.html">KtExpressionWithLabel</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a>
</span></code></pre></div>
</div>


<div markdown>

A common base class for `#!java this` and `#!java super` expressions, both of which refer to an instance receiver and may have an optional label qualifier.

</div>

</div>
### [`KtIntersectionType`](-kt-intersection-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-intersection-type/index.html">KtIntersectionType</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-intersection-type/index.html">KtIntersectionType</a><span class="o">></span><span class="o">> </span>, <a href="-kt-type-element/index.html">KtTypeElement</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an intersection type combining two types with {@code &}.


</div>

</div>
### [`KtIsExpression`](-kt-is-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-is-expression/index.html">KtIsExpression</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>, <a href="-kt-operation-expression/index.html">KtOperationExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a type check expression using `#!java is` or `#!java !is`.

</div>

</div>
### [`KtLabeledExpression`](-kt-labeled-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-labeled-expression/index.html">KtLabeledExpression</a> : <a href="-kt-expression-with-label/index.html">KtExpressionWithLabel</a>, PsiNameIdentifierOwner
</span></code></pre></div>
</div>


<div markdown>

Represents a labeled expression with a label prefix.


</div>

</div>
### [`KtLabelReferenceExpression`](-kt-label-reference-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-label-reference-expression/index.html">KtLabelReferenceExpression</a> : <a href="-kt-simple-name-expression-impl/index.html">KtSimpleNameExpressionImpl</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a reference to a label in a labeled expression, such as `@main` in `return@main`.


</div>

</div>
### [`KtLambdaArgument`](-kt-lambda-argument/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-lambda-argument/index.html">KtLambdaArgument</a> : <a href="-kt-value-argument/index.html">KtValueArgument</a>, <a href="-lambda-argument/index.html">LambdaArgument</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a trailing lambda argument passed outside of parentheses.


</div>

</div>
### [`KtLambdaExpression`](-kt-lambda-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-lambda-expression/index.html">KtLambdaExpression</a> : LazyParseablePsiElement, <a href="-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a lambda expression with optional parameters and a body.

</div>

</div>
### [`KtLiteralStringTemplateEntry`](-kt-literal-string-template-entry/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-literal-string-template-entry/index.html">KtLiteralStringTemplateEntry</a> : <a href="-kt-string-template-entry/index.html">KtStringTemplateEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a literal text segment in a string template without any interpolation.

</div>

</div>
### [`KtLoopExpression`](-kt-loop-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-loop-expression/index.html">KtLoopExpression</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>, <a href="-kt-statement-expression/index.html">KtStatementExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a loop expression: a `#!java for`, `#!java while`, or `#!java do`-`#!java while` loop.

</div>

</div>
### [`KtModifierList`](-kt-modifier-list/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-modifier-list/index.html">KtModifierList</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-modifier-list-stub/index.html">KotlinModifierListStub</a><span class="o">> </span>, <a href="-kt-annotations-container/index.html">KtAnnotationsContainer</a>
</span></code></pre></div>
</div>


<div markdown>

Represents the list of modifiers and annotations that precede a declaration or other [`KtModifierListOwner`](-kt-modifier-list-owner/index.md).

</div>

</div>
### [`KtModifierListOwner`](-kt-modifier-list-owner/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-modifier-list-owner/index.html">KtModifierListOwner</a> : PsiElement, <a href="-kt-annotated/index.html">KtAnnotated</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an element that may own a [`KtModifierList`](-kt-modifier-list/index.md), that is, a sequence of modifiers (such as `#!java public`, `#!java inline`, `#!java suspend`) and annotations.

</div>

</div>
### [`KtModifierListOwnerStub`](-kt-modifier-list-owner-stub/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-modifier-list-owner-stub/index.html">KtModifierListOwnerStub</a><span class="o"><</span><a href="-kt-modifier-list-owner-stub/index.html">T</a><span class="o"> : </span>StubElement<span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span><span class="o">></span> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="-kt-modifier-list-owner-stub/index.html">T</a><span class="o">> </span>, <a href="-kt-modifier-list-owner/index.html">KtModifierListOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Base implementation of [`KtModifierListOwner`](-kt-modifier-list-owner/index.md) that may be backed either by the AST tree or by a stub.

</div>

</div>
### [`KtNamed`](-kt-named/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-named/index.html">KtNamed</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an element that carries a Kotlin Name, such as a named declaration or a label.

</div>

</div>
### [`KtNamedDeclaration`](-kt-named-declaration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-named-declaration/index.html">KtNamedDeclaration</a> : <a href="-kt-declaration/index.html">KtDeclaration</a>, PsiNameIdentifierOwner, <a href="-kt-statement-expression/index.html">KtStatementExpression</a>, <a href="-kt-named/index.html">KtNamed</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`KtDeclaration`](-kt-declaration/index.md) that introduces a name, such as a class, function, property, or type alias.

</div>

</div>
### [`KtNamedDeclarationStub`](-kt-named-declaration-stub/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-named-declaration-stub/index.html">KtNamedDeclarationStub</a><span class="o"><</span><a href="-kt-named-declaration-stub/index.html">T</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-stub-with-fq-name/index.html">KotlinStubWithFqName</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span><span class="o">></span> : <a href="-kt-declaration-stub/index.html">KtDeclarationStub</a><span class="o"><</span><a href="-kt-named-declaration-stub/index.html">T</a><span class="o">> </span>, <a href="-kt-named-declaration/index.html">KtNamedDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Base implementation of [`KtNamedDeclaration`](-kt-named-declaration/index.md) that may be backed either by the AST tree or by a stub.

</div>

</div>
### [`KtNamedDeclarationUtil`](-kt-named-declaration-util/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-named-declaration-util/index.html">KtNamedDeclarationUtil</a>
</span></code></pre></div>
</div>


<div markdown>

Static helpers for computing fully qualified names of [`KtNamedDeclaration`](-kt-named-declaration/index.md)s from their PSI structure.

</div>

</div>
### [`KtNamedFunction`](-kt-named-function/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">open </span><span class="kd">class </span><a href="-kt-named-function/index.html">KtNamedFunction</a> : <a href="-kt-type-parameter-list-owner-stub/index.html">KtTypeParameterListOwnerStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-function-stub/index.html">KotlinFunctionStub</a><span class="o">> </span>, <a href="-kt-function/index.html">KtFunction</a>, <a href="-kt-declaration-with-initializer/index.html">KtDeclarationWithInitializer</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a named function declaration.


</div>

</div>
### [`KtNameReferenceExpression`](-kt-name-reference-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-name-reference-expression/index.html">KtNameReferenceExpression</a> : <a href="-kt-expression-impl-stub/index.html">KtExpressionImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-name-reference-expression-stub/index.html">KotlinNameReferenceExpressionStub</a><span class="o">> </span>, <a href="-kt-simple-name-expression/index.html">KtSimpleNameExpression</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a simple name reference to a variable, function, or type.


</div>

</div>
### [`KtNonPublicApi`](-kt-non-public-api/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html">AnnotationTarget.CLASS</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html">AnnotationTarget.CONSTRUCTOR</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html">AnnotationTarget.TYPEALIAS</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"Internal API which is used in projects developed by JetBrains"</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-kt-non-public-api/index.html">KtNonPublicApi</a>
</span></code></pre></div>
</div>


<div markdown>

Marks an API as internal to projects developed by JetBrains. Such APIs are not intended for public user consumption and have less strict compatibility guarantees. For example, a change to the API might be implemented without a deprecation cycle.


</div>

</div>
### [`KtNullableType`](-kt-nullable-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-nullable-type/index.html">KtNullableType</a> : <a href="-kt-modifier-list-owner-stub/index.html">KtModifierListOwnerStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-nullable-type/index.html">KtNullableType</a><span class="o">></span><span class="o">> </span>, <a href="-kt-type-element/index.html">KtTypeElement</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a nullable type marked with a question mark.

</div>

</div>
### [`KtObjectDeclaration`](-kt-object-declaration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-object-declaration/index.html">KtObjectDeclaration</a> : <a href="-kt-class-or-object/index.html">KtClassOrObject</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an object declaration, including companion objects and named objects.


</div>

</div>
### [`KtObjectLiteralExpression`](-kt-object-literal-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-object-literal-expression/index.html">KtObjectLiteralExpression</a> : <a href="-kt-expression-impl-stub/index.html">KtExpressionImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-object-literal-expression/index.html">KtObjectLiteralExpression</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents an `#!java object` literal expression that creates an anonymous object.

</div>

</div>
### [`KtOperationExpression`](-kt-operation-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-operation-expression/index.html">KtOperationExpression</a> : <a href="-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an expression built around an operation sign, such as a unary, binary, or "is"/"as" expression.

</div>

</div>
### [`KtOperationReferenceExpression`](-kt-operation-reference-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-operation-reference-expression/index.html">KtOperationReferenceExpression</a> : <a href="-kt-expression-impl-stub/index.html">KtExpressionImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-operation-reference-expression-stub/index.html">KotlinOperationReferenceExpressionStub</a><span class="o">> </span>, <a href="-kt-simple-name-expression/index.html">KtSimpleNameExpression</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an operator symbol in an expression.


</div>

</div>
### [`KtPackageDirective`](-kt-package-directive/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-package-directive/index.html">KtPackageDirective</a> : <a href="-kt-modifier-list-owner-stub/index.html">KtModifierListOwnerStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-package-directive/index.html">KtPackageDirective</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java package` directive that declares the package of a Kotlin file.

</div>

</div>
### [`KtParameter`](-kt-parameter/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-parameter/index.html">KtParameter</a> : <a href="-kt-named-declaration-stub/index.html">KtNamedDeclarationStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-parameter-stub/index.html">KotlinParameterStub</a><span class="o">> </span>, <a href="-kt-callable-declaration/index.html">KtCallableDeclaration</a>, <a href="-kt-val-var-keyword-owner/index.html">KtValVarKeywordOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a parameter declaration in various contexts.

</div>

</div>
### [`KtParameterList`](-kt-parameter-list/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-parameter-list/index.html">KtParameterList</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-parameter-list/index.html">KtParameterList</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a list of parameters in various contexts.

</div>

</div>
### [`KtParenthesizedExpression`](-kt-parenthesized-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-parenthesized-expression/index.html">KtParenthesizedExpression</a> : <a href="-kt-expression-impl-stub/index.html">KtExpressionImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-parenthesized-expression/index.html">KtParenthesizedExpression</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents an expression enclosed in parentheses.

</div>

</div>
### [`KtPlatformInterface`](-kt-platform-interface/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html">AnnotationTarget.CLASS</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html">AnnotationTarget.CONSTRUCTOR</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html">AnnotationTarget.TYPEALIAS</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"An API intended for the Analysis API engine and its platform implementations. The API is neither stable nor intended for consumption by PSI users."</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-kt-platform-interface/index.html">KtPlatformInterface</a>
</span></code></pre></div>
</div>


<div markdown>

Marks an API intended for the Analysis API engine and its platform implementations.


</div>

</div>
### [`KtPostfixExpression`](-kt-postfix-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-postfix-expression/index.html">KtPostfixExpression</a> : <a href="-kt-unary-expression/index.html">KtUnaryExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a postfix unary expression where the operator follows the operand.

</div>

</div>
### [`KtPrefixExpression`](-kt-prefix-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-prefix-expression/index.html">KtPrefixExpression</a> : <a href="-kt-unary-expression/index.html">KtUnaryExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a prefix unary expression where the operator precedes the operand.

</div>

</div>
### [`KtPrimaryConstructor`](-kt-primary-constructor/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-primary-constructor/index.html">KtPrimaryConstructor</a> : <a href="-kt-constructor/index.html">KtConstructor</a><span class="o"><</span><a href="-kt-primary-constructor/index.html">KtPrimaryConstructor</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a primary constructor explicitly declared in a class header.


</div>

</div>
### [`KtProjectionKind`](-kt-projection-kind/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-kt-projection-kind/index.html">KtProjectionKind</a>
</span></code></pre></div>
</div>


<div markdown>

The kind of variance projection applied to a type argument in a [`KtTypeProjection`](-kt-type-projection/index.md).

</div>

</div>
### [`KtProperty`](-kt-property/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-property/index.html">KtProperty</a> : <a href="-kt-type-parameter-list-owner-stub/index.html">KtTypeParameterListOwnerStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-property-stub/index.html">KotlinPropertyStub</a><span class="o">> </span>, <a href="-kt-variable-declaration/index.html">KtVariableDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a property declaration with an optional getter and setter.

</div>

</div>
### [`KtPropertyAccessor`](-kt-property-accessor/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">open </span><span class="kd">class </span><a href="-kt-property-accessor/index.html">KtPropertyAccessor</a> : <a href="-kt-declaration-stub/index.html">KtDeclarationStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-property-accessor-stub/index.html">KotlinPropertyAccessorStub</a><span class="o">> </span>, <a href="-kt-declaration-with-body/index.html">KtDeclarationWithBody</a>, <a href="-kt-modifier-list-owner/index.html">KtModifierListOwner</a>, <a href="-kt-declaration-with-initializer/index.html">KtDeclarationWithInitializer</a>, <a href="-kt-declaration-with-return-type/index.html">KtDeclarationWithReturnType</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a property getter or setter accessor.


</div>

</div>
### [`KtPropertyDelegate`](-kt-property-delegate/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-property-delegate/index.html">KtPropertyDelegate</a> : <a href="-kt-element-impl/index.html">KtElementImpl</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a property delegate expression that provides the implementation for property accessors.

</div>

</div>
### [`KtPsiFactory`](-kt-psi-factory/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-psi-factory/index.html">KtPsiFactory</a>
</span></code></pre></div>
</div>


<div markdown>

A factory for creating Kotlin PSI elements programmatically, usually by parsing a snippet of source text.


</div>

</div>
### [`KtPsiInconsistencyHandling`](-kt-psi-inconsistency-handling/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a>
<span class="kd">annotation class </span><a href="-kt-psi-inconsistency-handling/index.html">KtPsiInconsistencyHandling</a>
</span></code></pre></div>
</div>


<div markdown>

Functions and classes annotated with [`KtPsiInconsistencyHandling`](-kt-psi-inconsistency-handling/index.md) are not intended for general-purpose use, but for working with possibly inconsistent PSI. The specific circumstances need to be described in the documentation of the annotated function/class.


</div>

</div>
### [`KtPsiMutationService`](-kt-psi-mutation-service/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-psi-mutation-service/index.html">KtPsiMutationService</a>
</span></code></pre></div>
</div>


<div markdown>

Service responsible for Kotlin PSI mutation operations whose implementation is provided by the Kotlin plugin environment.


</div>

</div>
### [`KtPsiUtil`](-kt-psi-util/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-psi-util/index.html">KtPsiUtil</a>
</span></code></pre></div>
</div>


<div markdown>

A collection of static helper methods for working with the Kotlin PSI.

</div>

</div>
### [`KtPureClassOrObject`](-kt-pure-class-or-object/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-pure-class-or-object/index.html">KtPureClassOrObject</a> : <a href="-kt-pure-element/index.html">KtPureElement</a>, <a href="-kt-declaration-container/index.html">KtDeclarationContainer</a>
</span></code></pre></div>
</div>


<div markdown>

A minimal interface that [`KtClassOrObject`](-kt-class-or-object/index.md) implements for the purpose of code-generation that does not need the full power of PSI.

</div>

</div>
### [`KtPureElement`](-kt-pure-element/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-pure-element/index.html">KtPureElement</a>
</span></code></pre></div>
</div>


<div markdown>

A minimal interface that [`KtElement`](-kt-element/index.md) implements for the purpose of code-generation that does not need the full power of PSI.

</div>

</div>
### [`KtQualifiedExpression`](-kt-qualified-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-kt-qualified-expression/index.html">KtQualifiedExpression</a> : <a href="-kt-expression/index.html">KtExpression</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a qualified expression, which accesses a member or extension on a receiver using the `.`, `?.`, or `|.` operator.


</div>

</div>
### [`KtReferenceExpression`](-kt-reference-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-reference-expression/index.html">KtReferenceExpression</a> : <a href="-kt-expression/index.html">KtExpression</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an expression that references a declaration and can therefore be resolved to it, such as a name reference, an array access, or a call expression.

</div>

</div>
### [`KtReturnExpression`](-kt-return-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-return-expression/index.html">KtReturnExpression</a> : <a href="-kt-expression-with-label/index.html">KtExpressionWithLabel</a>, <a href="-kt-statement-expression/index.html">KtStatementExpression</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java return` expression that returns a value from a function or lambda.

</div>

</div>
### [`KtSafeQualifiedExpression`](-kt-safe-qualified-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-safe-qualified-expression/index.html">KtSafeQualifiedExpression</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>, <a href="-kt-qualified-expression/index.html">KtQualifiedExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a safe-call expression using the `?.` operator.


</div>

</div>
### [`KtScript`](-kt-script/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">open </span><span class="kd">class </span><a href="-kt-script/index.html">KtScript</a> : <a href="-kt-named-declaration-stub/index.html">KtNamedDeclarationStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-script-stub/index.html">KotlinScriptStub</a><span class="o">> </span>, <a href="-kt-declaration-container/index.html">KtDeclarationContainer</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a Kotlin script file containing top-level statements and declarations.


</div>

</div>
### [`KtScriptInitializer`](-kt-script-initializer/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-script-initializer/index.html">KtScriptInitializer</a> : <a href="-kt-declaration-stub/index.html">KtDeclarationStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-script-initializer/index.html">KtScriptInitializer</a><span class="o">></span><span class="o">> </span>, <a href="-kt-anonymous-initializer/index.html">KtAnonymousInitializer</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an initializer expression in a script. Effectively, it is a wrapper for top-level expressions


</div>

</div>
### [`KtSecondaryConstructor`](-kt-secondary-constructor/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-secondary-constructor/index.html">KtSecondaryConstructor</a> : <a href="-kt-constructor/index.html">KtConstructor</a><span class="o"><</span><a href="-kt-secondary-constructor/index.html">KtSecondaryConstructor</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a secondary constructor declared in the class body.


</div>

</div>
### [`KtSimpleNameExpression`](-kt-simple-name-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-kt-simple-name-expression/index.html">KtSimpleNameExpression</a> : <a href="-kt-reference-expression/index.html">KtReferenceExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a simple name reference: an unqualified reference to a declaration by its name, or an operation sign that references a declaration (for example, the `+` of a binary expression).


</div>

</div>
### [`KtSimpleNameExpressionImpl`](-kt-simple-name-expression-impl/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-kt-simple-name-expression-impl/index.html">KtSimpleNameExpressionImpl</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>, <a href="-kt-simple-name-expression/index.html">KtSimpleNameExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Base implementation of [`KtSimpleNameExpression`](-kt-simple-name-expression/index.md) shared by its stub-based and AST-based variants.


</div>

</div>
### [`KtSimpleNameStringTemplateEntry`](-kt-simple-name-string-template-entry/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-simple-name-string-template-entry/index.html">KtSimpleNameStringTemplateEntry</a> : <a href="-kt-string-template-entry-with-expression/index.html">KtStringTemplateEntryWithExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a simple variable interpolation in a string template using `#!java $name`.

</div>

</div>
### [`KtSpiExtensionPoint`](-kt-spi-extension-point/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"An API designed for implementation only. Direct usage has no compatibility guarantees."</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-kt-spi-extension-point/index.html">KtSpiExtensionPoint</a>
</span></code></pre></div>
</div>


<div markdown>

Marks an API as a service provider interface extension point. Such APIs are designed to be implemented, not called directly. There are no compatibility guarantees for usage of these APIs, only for their implementation.


</div>

</div>
### [`KtStatementExpression`](-kt-statement-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-statement-expression/index.html">KtStatementExpression</a>
</span></code></pre></div>
</div>


<div markdown>

This is an interface to show that [`KtExpression`](-kt-expression/index.md) is not actually an expression (in the sense that this expression can be placed after "val x = ").

</div>

</div>
### [`KtStringInterpolationPrefix`](-kt-string-interpolation-prefix/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-string-interpolation-prefix/index.html">KtStringInterpolationPrefix</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-string-interpolation-prefix-stub/index.html">KotlinStringInterpolationPrefixStub</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents the multi-dollar interpolation prefix for string templates.


</div>

</div>
### [`KtStringTemplateEntry`](-kt-string-template-entry/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-string-template-entry/index.html">KtStringTemplateEntry</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-with-text-stub/index.html">KotlinPlaceHolderWithTextStub</a><span class="o"><</span><span class="kd">out </span><a href="-kt-string-template-entry/index.html">KtStringTemplateEntry</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a single entry of a [`KtStringTemplateExpression`](-kt-string-template-expression/index.md), that is, one segment of a string literal.

</div>

</div>
### [`KtStringTemplateEntryWithExpression`](-kt-string-template-entry-with-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-string-template-entry-with-expression/index.html">KtStringTemplateEntryWithExpression</a> : <a href="-kt-string-template-entry/index.html">KtStringTemplateEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a string template entry that interpolates an expression, using either the `#!java $name` or the `#!java ${...}` syntax.

</div>

</div>
### [`KtStringTemplateExpression`](-kt-string-template-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-string-template-expression/index.html">KtStringTemplateExpression</a> : <a href="-kt-expression-impl-stub/index.html">KtExpressionImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="o">></span><span class="o">> </span>, PsiLanguageInjectionHost, ContributedReferenceHost
</span></code></pre></div>
</div>


<div markdown>

Represents a string literal, including simple strings and string templates with interpolation.

</div>

</div>
### [`KtStubbedPsiUtil`](-kt-stubbed-psi-util/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-stubbed-psi-util/index.html">KtStubbedPsiUtil</a>
</span></code></pre></div>
</div>


<div markdown>

Static helpers for navigating the Kotlin PSI in a way that also works over stubs.

</div>

</div>
### [`KtSuperExpression`](-kt-super-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-super-expression/index.html">KtSuperExpression</a> : <a href="-kt-instance-expression-with-label/index.html">KtInstanceExpressionWithLabel</a>, <a href="-kt-statement-expression/index.html">KtStatementExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java super` expression that refers to the superclass implementation.

</div>

</div>
### [`KtSuperTypeCallEntry`](-kt-super-type-call-entry/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-super-type-call-entry/index.html">KtSuperTypeCallEntry</a> : <a href="-kt-super-type-list-entry/index.html">KtSuperTypeListEntry</a>, <a href="-kt-call-element/index.html">KtCallElement</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a superclass constructor call in the super type list.

</div>

</div>
### [`KtSuperTypeEntry`](-kt-super-type-entry/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-super-type-entry/index.html">KtSuperTypeEntry</a> : <a href="-kt-super-type-list-entry/index.html">KtSuperTypeListEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an interface type in the super type list (without a constructor call).

</div>

</div>
### [`KtSuperTypeList`](-kt-super-type-list/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-super-type-list/index.html">KtSuperTypeList</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-super-type-list/index.html">KtSuperTypeList</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents the list of super types after the colon in a class header.

</div>

</div>
### [`KtSuperTypeListEntry`](-kt-super-type-list-entry/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-super-type-list-entry/index.html">KtSuperTypeListEntry</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><span class="kd">out </span><a href="-kt-super-type-list-entry/index.html">KtSuperTypeListEntry</a><span class="o">></span><span class="o">> </span>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a single entry in a super type list.

</div>

</div>
### [`KtThisExpression`](-kt-this-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-this-expression/index.html">KtThisExpression</a> : <a href="-kt-instance-expression-with-label/index.html">KtInstanceExpressionWithLabel</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java this` expression that refers to the current receiver.

</div>

</div>
### [`KtThrowExpression`](-kt-throw-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-throw-expression/index.html">KtThrowExpression</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>, <a href="-kt-statement-expression/index.html">KtStatementExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java throw` expression that throws an exception.

</div>

</div>
### [`KtTreeVisitor`](-kt-tree-visitor/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-tree-visitor/index.html">KtTreeVisitor</a><span class="o"><</span><a href="-kt-tree-visitor/index.html">D</a><span class="o">></span> : <a href="-kt-visitor/index.html">KtVisitor</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a><span class="p">, </span><a href="-kt-tree-visitor/index.html">D</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A [`KtVisitor`](-kt-visitor/index.md) that recursively traverses the whole PSI subtree.

</div>

</div>
### [`KtTreeVisitorVoid`](-kt-tree-visitor-void/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-tree-visitor-void/index.html">KtTreeVisitorVoid</a> : <a href="-kt-visitor-void/index.html">KtVisitorVoid</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KtVisitorVoid`](-kt-visitor-void/index.md) that recursively traverses the whole PSI subtree.

</div>

</div>
### [`KtTryExpression`](-kt-try-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-try-expression/index.html">KtTryExpression</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java try` expression with `#!java catch` clauses and optional `#!java finally` block.

</div>

</div>
### [`KtTypeAlias`](-kt-type-alias/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-type-alias/index.html">KtTypeAlias</a> : <a href="-kt-type-parameter-list-owner-stub/index.html">KtTypeParameterListOwnerStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-type-alias-stub/index.html">KotlinTypeAliasStub</a><span class="o">> </span>, <a href="-kt-named-declaration/index.html">KtNamedDeclaration</a>, <a href="-kt-class-like-declaration/index.html">KtClassLikeDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a type alias declaration.


</div>

</div>
### [`KtTypeArgumentList`](-kt-type-argument-list/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-type-argument-list/index.html">KtTypeArgumentList</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-type-argument-list/index.html">KtTypeArgumentList</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a list of type arguments in angle brackets.

</div>

</div>
### [`KtTypeCodeFragment`](-kt-type-code-fragment/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-type-code-fragment/index.html">KtTypeCodeFragment</a><span class="p">(</span>
    project<span class="o">: </span>Project<span class="p">, </span>
    name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/index.html">CharSequence</a><span class="p">, </span>
    context<span class="o">: </span>PsiElement<span class="o">?</span>
<span class="p">)</span> : <a href="-kt-code-fragment/index.html">KtCodeFragment</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KtCodeFragment`](-kt-code-fragment/index.md) whose content is a type reference.


</div>

</div>
### [`KtTypeConstraint`](-kt-type-constraint/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-type-constraint/index.html">KtTypeConstraint</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-type-constraint/index.html">KtTypeConstraint</a><span class="o">></span><span class="o">> </span>, <a href="-kt-annotated/index.html">KtAnnotated</a>, <a href="-kt-annotations-container/index.html">KtAnnotationsContainer</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a single type constraint in a `#!java where` clause.

</div>

</div>
### [`KtTypeConstraintList`](-kt-type-constraint-list/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-type-constraint-list/index.html">KtTypeConstraintList</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-type-constraint-list/index.html">KtTypeConstraintList</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java where` clause containing type constraints.

</div>

</div>
### [`KtTypeElement`](-kt-type-element/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-type-element/index.html">KtTypeElement</a> : <a href="-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Represents the actual type syntax inside a [`KtTypeReference`](-kt-type-reference/index.md), stripped of any leading annotations and modifiers.

</div>

</div>
### [`KtTypeParameter`](-kt-type-parameter/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-type-parameter/index.html">KtTypeParameter</a> : <a href="-kt-named-declaration-stub/index.html">KtNamedDeclarationStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-type-parameter-stub/index.html">KotlinTypeParameterStub</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a type parameter in a generic declaration.

</div>

</div>
### [`KtTypeParameterList`](-kt-type-parameter-list/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-type-parameter-list/index.html">KtTypeParameterList</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-type-parameter-list/index.html">KtTypeParameterList</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a list of type parameters in angle brackets.

</div>

</div>
### [`KtTypeParameterListOwner`](-kt-type-parameter-list-owner/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-type-parameter-list-owner/index.html">KtTypeParameterListOwner</a> : <a href="-kt-named-declaration/index.html">KtNamedDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a declaration that may declare type parameters, such as a class, function, or type alias.

</div>

</div>
### [`KtTypeParameterListOwnerStub`](-kt-type-parameter-list-owner-stub/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-type-parameter-list-owner-stub/index.html">KtTypeParameterListOwnerStub</a><span class="o"><</span><a href="-kt-type-parameter-list-owner-stub/index.html">T</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-stub-with-fq-name/index.html">KotlinStubWithFqName</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span><span class="o">></span> : <a href="-kt-named-declaration-stub/index.html">KtNamedDeclarationStub</a><span class="o"><</span><a href="-kt-type-parameter-list-owner-stub/index.html">T</a><span class="o">> </span>, <a href="-kt-type-parameter-list-owner/index.html">KtTypeParameterListOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Base implementation of [`KtTypeParameterListOwner`](-kt-type-parameter-list-owner/index.md) that may be backed either by the AST tree or by a stub.

</div>

</div>
### [`KtTypeProjection`](-kt-type-projection/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-type-projection/index.html">KtTypeProjection</a> : <a href="-kt-modifier-list-owner-stub/index.html">KtModifierListOwnerStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-type-projection-stub/index.html">KotlinTypeProjectionStub</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a type projection in a type argument, including variance modifiers or star projection.

</div>

</div>
### [`KtTypeReference`](-kt-type-reference/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-type-reference/index.html">KtTypeReference</a> : <a href="-kt-modifier-list-owner-stub/index.html">KtModifierListOwnerStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-type-reference/index.html">KtTypeReference</a><span class="o">></span><span class="o">> </span>, <a href="-kt-annotated/index.html">KtAnnotated</a>, <a href="-kt-annotations-container/index.html">KtAnnotationsContainer</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a type reference.


</div>

</div>
### [`KtUnaryExpression`](-kt-unary-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-unary-expression/index.html">KtUnaryExpression</a> : <a href="-kt-expression-impl-stub/index.html">KtExpressionImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><span class="kd">out </span><a href="-kt-unary-expression/index.html">KtUnaryExpression</a><span class="o">></span><span class="o">> </span>, <a href="-kt-operation-expression/index.html">KtOperationExpression</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a unary expression with an operator and a single operand.

</div>

</div>
### [`KtUnionType`](-kt-union-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-kt-union-type/index.html">KtUnionType</a> : <a href="-kt-type-element/index.html">KtTypeElement</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an union type combining two types with {@code |}.


</div>

</div>
### [`KtUserType`](-kt-user-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-user-type/index.html">KtUserType</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-user-type-stub/index.html">KotlinUserTypeStub</a><span class="o">> </span>, <a href="-kt-type-element/index.html">KtTypeElement</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a simple type, optionally with type arguments.

</div>

</div>
### [`KtValueArgument`](-kt-value-argument/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-value-argument/index.html">KtValueArgument</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-value-argument-stub/index.html">KotlinValueArgumentStub</a><span class="o"><</span><span class="kd">out </span><a href="-kt-value-argument/index.html">KtValueArgument</a><span class="o">></span><span class="o">> </span>, <a href="-value-argument/index.html">ValueArgument</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a value argument in a function call.

</div>

</div>
### [`KtValueArgumentList`](-kt-value-argument-list/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-value-argument-list/index.html">KtValueArgumentList</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-value-argument-list/index.html">KtValueArgumentList</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents a parenthesized list of value arguments in a call.

</div>

</div>
### [`KtValueArgumentName`](-kt-value-argument-name/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-value-argument-name/index.html">KtValueArgumentName</a> : <a href="-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="-kt-value-argument-name/index.html">KtValueArgumentName</a><span class="o">></span><span class="o">> </span>, <a href="-value-argument-name/index.html">ValueArgumentName</a>
</span></code></pre></div>
</div>


<div markdown>

Represents the name part of a named argument.

</div>

</div>
### [`KtValVarKeywordOwner`](-kt-val-var-keyword-owner/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-val-var-keyword-owner/index.html">KtValVarKeywordOwner</a> : PsiElement
</span></code></pre></div>
</div>


<div markdown>

Represents an element that may be introduced by a `#!java val` or `#!java var` keyword, such as a property, a destructuring entry, or a constructor value parameter.

</div>

</div>
### [`KtVariableDeclaration`](-kt-variable-declaration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-variable-declaration/index.html">KtVariableDeclaration</a> : <a href="-kt-callable-declaration/index.html">KtCallableDeclaration</a>, <a href="-kt-declaration-with-initializer/index.html">KtDeclarationWithInitializer</a>, <a href="-kt-val-var-keyword-owner/index.html">KtValVarKeywordOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a variable declaration introduced by `#!java val` or `#!java var`: a property, a local variable, or an entry of a destructuring declaration.

</div>

</div>
### [`KtVisitor`](-kt-visitor/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-visitor/index.html">KtVisitor</a><span class="o"><</span><a href="-kt-visitor/index.html">R</a><span class="p">, </span><a href="-kt-visitor/index.html">D</a><span class="o">></span> : PsiElementVisitor
</span></code></pre></div>
</div>


<div markdown>

The base visitor over the Kotlin PSI, implementing the visitor pattern for [`KtElement`](-kt-element/index.md)s.

</div>

</div>
### [`KtVisitorVoid`](-kt-visitor-void/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-visitor-void/index.html">KtVisitorVoid</a> : <a href="-kt-visitor/index.html">KtVisitor</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a><span class="p">, </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A convenience [`KtVisitor`](-kt-visitor/index.md) for the common case of a visitor that returns nothing and needs no extra data.

</div>

</div>
### [`KtVisitorVoidWithParameter`](-kt-visitor-void-with-parameter/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-visitor-void-with-parameter/index.html">KtVisitorVoidWithParameter</a><span class="o"><</span><a href="-kt-visitor-void-with-parameter/index.html">P</a><span class="o">></span> : <a href="-kt-visitor/index.html">KtVisitor</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a><span class="p">, </span><a href="-kt-visitor-void-with-parameter/index.html">P</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A convenience [`KtVisitor`](-kt-visitor/index.md) for visitors that return nothing but still thread a data parameter through the traversal.

</div>

</div>
### [`KtWhenCondition`](-kt-when-condition/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-when-condition/index.html">KtWhenCondition</a> : <a href="-kt-element-impl/index.html">KtElementImpl</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a single condition of a [`KtWhenEntry`](-kt-when-entry/index.md) in a `#!java when` expression.

</div>

</div>
### [`KtWhenConditionInRange`](-kt-when-condition-in-range/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-when-condition-in-range/index.html">KtWhenConditionInRange</a> : <a href="-kt-when-condition/index.html">KtWhenCondition</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java when` condition that checks membership using `#!java in` or `#!java !in`.

</div>

</div>
### [`KtWhenConditionIsPattern`](-kt-when-condition-is-pattern/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-when-condition-is-pattern/index.html">KtWhenConditionIsPattern</a> : <a href="-kt-when-condition/index.html">KtWhenCondition</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java when` condition that performs a type check using `#!java is` or `#!java !is`.

</div>

</div>
### [`KtWhenConditionWithExpression`](-kt-when-condition-with-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-when-condition-with-expression/index.html">KtWhenConditionWithExpression</a> : <a href="-kt-when-condition/index.html">KtWhenCondition</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java when` condition that matches against an expression value.

</div>

</div>
### [`KtWhenEntry`](-kt-when-entry/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-when-entry/index.html">KtWhenEntry</a> : <a href="-kt-element-impl/index.html">KtElementImpl</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a single branch in a `#!java when` expression.

</div>

</div>
### [`KtWhenEntryGuard`](-kt-when-entry-guard/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-when-entry-guard/index.html">KtWhenEntryGuard</a> : <a href="-kt-element-impl/index.html">KtElementImpl</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a guard condition in a `when` entry using the `if` keyword.


</div>

</div>
### [`KtWhenExpression`](-kt-when-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-when-expression/index.html">KtWhenExpression</a> : <a href="-kt-expression-impl/index.html">KtExpressionImpl</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java when` expression with an optional subject and multiple branches.

</div>

</div>
### [`KtWhileExpression`](-kt-while-expression/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-while-expression/index.html">KtWhileExpression</a> : <a href="-kt-while-expression-base/index.html">KtWhileExpressionBase</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `#!java while` loop that executes its body while the condition is true.

</div>

</div>
### [`KtWhileExpressionBase`](-kt-while-expression-base/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-while-expression-base/index.html">KtWhileExpressionBase</a> : <a href="-kt-loop-expression/index.html">KtLoopExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a condition-driven loop: a `#!java while` or `#!java do`-`#!java while` loop.

</div>

</div>
### [`LambdaArgument`](-lambda-argument/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-lambda-argument/index.html">LambdaArgument</a> : <a href="-value-argument/index.html">ValueArgument</a>
</span></code></pre></div>
</div>


<div markdown>

A [`ValueArgument`](-value-argument/index.md) that is a trailing lambda passed outside the call parentheses, as in `list.forEach { ... }`.


</div>

</div>
### [`UserDataProperty`](-user-data-property/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-user-data-property/index.html">UserDataProperty</a><span class="o"><</span><span class="kd">in </span><a href="-user-data-property/index.html">R</a><span class="o"> : </span>UserDataHolder<span class="p">, </span><a href="-user-data-property/index.html">T</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">(</span><span class="kd">val </span>key<span class="o">: </span>Key<span class="o"><</span><a href="-user-data-property/index.html">T</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

A property delegate that reads and writes a value stored in a UserDataHolder under the given [`key`](-user-data-property/index.md#key).


</div>

</div>
### [`ValueArgument`](-value-argument/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-value-argument/index.html">ValueArgument</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a single argument passed in a call, such as `foo(1, message = "hi", *array)`.


</div>

</div>
### [`ValueArgumentName`](-value-argument-name/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-value-argument-name/index.html">ValueArgumentName</a>
</span></code></pre></div>
</div>


<div markdown>

The name of a named [`ValueArgument`](-value-argument/index.md) (the `name` in `name = value`).


</div>

</div>
## Properties
## Functions
### [`buildByPattern`](build-by-pattern.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="build-by-pattern.html">TElement</a><span class="o">> </span><a href="build-by-pattern.html"><span class="nf">buildByPattern</span></a><span class="p">(</span>factory<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span><a href="build-by-pattern.html">TElement</a><span class="p">, </span>build<span class="o">: </span><a href="-builder-by-pattern/index.html">BuilderByPattern</a><span class="o"><</span><a href="build-by-pattern.html">TElement</a><span class="o">></span><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="build-by-pattern.html">TElement</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`BuilderByPattern`](-builder-by-pattern/index.md), runs [`build`](build-by-pattern.md) on it, and produces the element via [`factory`](build-by-pattern.md). Backs the `KtPsiFactory.build*` entry points.


</div>

</div>
### [`createByPattern`](create-by-pattern.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="create-by-pattern.html">TElement</a><span class="o"> : </span><a href="-kt-element/index.html">KtElement</a><span class="o">> </span><a href="create-by-pattern.html"><span class="nf">createByPattern</span></a><span class="p">(</span>
    pattern<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    <span class="kd">vararg </span>args<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span>
    reformat<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">, </span>
    factory<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o"> -> </span><a href="create-by-pattern.html">TElement</a>
<span class="p">)</span><span class="o">: </span><a href="create-by-pattern.html">TElement</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a PSI element from a textual [`pattern`](create-by-pattern.md) with `$0`, `$1`, … placeholders replaced by the corresponding [`args`](create-by-pattern.md).


</div>

</div>
