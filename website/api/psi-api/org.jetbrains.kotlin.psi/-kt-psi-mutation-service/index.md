---
tags:
 - jvm
title: "KtPsiMutationService"
---

# KtPsiMutationService

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KtPsiMutationService</a>
</span></code></pre></div>Service responsible for Kotlin PSI mutation operations whose implementation is provided by the Kotlin plugin environment.

Avoid using this service directly if possible: instead, use the helper extension functions from `org.jetbrains.kotlin.idea.base.psi.KotlinPsiModificationUtils`.

When the service is not registered (e.g., when the Kotlin PSI is used outside the IntelliJ Kotlin plugin), Kotlin PSI overrides of platform mutation methods, such as [`PsiElement.delete`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#delete), [`PsiElement.replace`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#replace), [`com.intellij.psi.PsiNamedElement.setName`](../-kt-class-like-declaration/index.md#setname) and PsiLanguageInjectionHost.updateText, fall back to plain operations without Kotlin-specific adjustments like removing dangling separators or adding parentheses. However, Kotlin-specific mutation methods still require the service.


</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Functions
### addAnnotation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#addannotation"><span class="nf">addAnnotation</span></a><span class="p">(</span>owner<span class="o">: </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">, </span>annotationEntry<span class="o">: </span><a href="../-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">)</span><span class="o">: </span><a href="../-kt-annotation-entry/index.html">KtAnnotationEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`annotationEntry`](index.md#addannotation) to [`owner`](index.md#addannotation).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#addannotation"><span class="nf">addAnnotation</span></a><span class="p">(</span>constructor<span class="o">: </span><a href="../-kt-primary-constructor/index.html">KtPrimaryConstructor</a><span class="p">, </span>annotationEntry<span class="o">: </span><a href="../-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">)</span><span class="o">: </span><a href="../-kt-annotation-entry/index.html">KtAnnotationEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`annotationEntry`](index.md#addannotation) to [`constructor`](index.md#addannotation) using primary-constructor-specific behavior.


</div>

</div>
### addEnumEntrySemicolon

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#addenumentrysemicolon"><span class="nf">addEnumEntrySemicolon</span></a><span class="p">(</span>enumEntry<span class="o">: </span><a href="../-kt-enum-entry/index.html">KtEnumEntry</a><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Adds a semicolon to [`enumEntry`](index.md#addenumentrysemicolon), reusing an existing sibling semicolon when possible.


</div>

</div>
### addMemberDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#addmemberdeclaration">T</a><span class="o"> : </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="o">> </span><a href="index.html#addmemberdeclaration"><span class="nf">addMemberDeclaration</span></a><span class="p">(</span>classOrObject<span class="o">: </span><a href="../-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">, </span>declaration<span class="o">: </span><a href="index.html#addmemberdeclaration">T</a><span class="p">)</span><span class="o">: </span><a href="index.html#addmemberdeclaration">T</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`declaration`](index.md#addmemberdeclaration) to [`classOrObject`](index.md#addmemberdeclaration), creating a body when needed.


</div>

</div>
### addMemberDeclarationAfter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#addmemberdeclarationafter">T</a><span class="o"> : </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="o">> </span><a href="index.html#addmemberdeclarationafter"><span class="nf">addMemberDeclarationAfter</span></a><span class="p">(</span>
    classOrObject<span class="o">: </span><a href="../-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">, </span>
    declaration<span class="o">: </span><a href="index.html#addmemberdeclarationafter">T</a><span class="p">, </span>
    anchor<span class="o">: </span>PsiElement<span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="index.html#addmemberdeclarationafter">T</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`declaration`](index.md#addmemberdeclarationafter) after [`anchor`](index.md#addmemberdeclarationafter) in [`classOrObject`](index.md#addmemberdeclarationafter), or appends it when [`anchor`](index.md#addmemberdeclarationafter) is `null`.


</div>

</div>
### addMemberDeclarationBefore

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#addmemberdeclarationbefore">T</a><span class="o"> : </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="o">> </span><a href="index.html#addmemberdeclarationbefore"><span class="nf">addMemberDeclarationBefore</span></a><span class="p">(</span>
    classOrObject<span class="o">: </span><a href="../-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">, </span>
    declaration<span class="o">: </span><a href="index.html#addmemberdeclarationbefore">T</a><span class="p">, </span>
    anchor<span class="o">: </span>PsiElement<span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="index.html#addmemberdeclarationbefore">T</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`declaration`](index.md#addmemberdeclarationbefore) before [`anchor`](index.md#addmemberdeclarationbefore) in [`classOrObject`](index.md#addmemberdeclarationbefore), or prepends it when [`anchor`](index.md#addmemberdeclarationbefore) is `null`.


</div>

</div>
### addModifierKeyword

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#addmodifierkeyword"><span class="nf">addModifierKeyword</span></a><span class="p">(</span>owner<span class="o">: </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">, </span>modifier<span class="o">: </span><a href="../../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Adds [`modifier`](index.md#addmodifierkeyword) to [`owner`](index.md#addmodifierkeyword).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#addmodifierkeyword"><span class="nf">addModifierKeyword</span></a><span class="p">(</span>constructor<span class="o">: </span><a href="../-kt-primary-constructor/index.html">KtPrimaryConstructor</a><span class="p">, </span>modifier<span class="o">: </span><a href="../../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Adds [`modifier`](index.md#addmodifierkeyword) to [`constructor`](index.md#addmodifierkeyword) using primary-constructor-specific behavior.


</div>

</div>
### addSuperType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#addsupertype"><span class="nf">addSuperType</span></a><span class="p">(</span>declaration<span class="o">: </span><a href="../-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">, </span>superTypeListEntry<span class="o">: </span><a href="../-kt-super-type-list-entry/index.html">KtSuperTypeListEntry</a><span class="p">)</span><span class="o">: </span><a href="../-kt-super-type-list-entry/index.html">KtSuperTypeListEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`superTypeListEntry`](index.md#addsupertype) to [`declaration`](index.md#addsupertype).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#addsupertype"><span class="nf">addSuperType</span></a><span class="p">(</span>superTypeList<span class="o">: </span><a href="../-kt-super-type-list/index.html">KtSuperTypeList</a><span class="p">, </span>superTypeListEntry<span class="o">: </span><a href="../-kt-super-type-list-entry/index.html">KtSuperTypeListEntry</a><span class="p">)</span><span class="o">: </span><a href="../-kt-super-type-list-entry/index.html">KtSuperTypeListEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`superTypeListEntry`](index.md#addsupertype) to [`superTypeList`](index.md#addsupertype).


</div>

</div>
### appendParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#appendparameter"><span class="nf">appendParameter</span></a><span class="p">(</span>parameterList<span class="o">: </span><a href="../-kt-parameter-list/index.html">KtParameterList</a><span class="p">, </span>parameter<span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a><span class="p">)</span><span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`parameter`](index.md#appendparameter) to [`parameterList`](index.md#appendparameter).


</div>

</div>
### appendTypeArgument

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#appendtypeargument"><span class="nf">appendTypeArgument</span></a><span class="p">(</span>typeArgumentList<span class="o">: </span><a href="../-kt-type-argument-list/index.html">KtTypeArgumentList</a><span class="p">, </span>typeArgument<span class="o">: </span><a href="../-kt-type-projection/index.html">KtTypeProjection</a><span class="p">)</span><span class="o">: </span><a href="../-kt-type-projection/index.html">KtTypeProjection</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`typeArgument`](index.md#appendtypeargument) to [`typeArgumentList`](index.md#appendtypeargument).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#appendtypeargument"><span class="nf">appendTypeArgument</span></a><span class="p">(</span>callExpression<span class="o">: </span><a href="../-kt-call-expression/index.html">KtCallExpression</a><span class="p">, </span>typeArgument<span class="o">: </span><a href="../-kt-type-projection/index.html">KtTypeProjection</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Adds [`typeArgument`](index.md#appendtypeargument) to [`callExpression`](index.md#appendtypeargument), creating the type argument list if needed.


</div>

</div>
### appendTypeParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#appendtypeparameter"><span class="nf">appendTypeParameter</span></a><span class="p">(</span>typeParameterList<span class="o">: </span><a href="../-kt-type-parameter-list/index.html">KtTypeParameterList</a><span class="p">, </span>typeParameter<span class="o">: </span><a href="../-kt-type-parameter/index.html">KtTypeParameter</a><span class="p">)</span><span class="o">: </span><a href="../-kt-type-parameter/index.html">KtTypeParameter</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`typeParameter`](index.md#appendtypeparameter) to [`typeParameterList`](index.md#appendtypeparameter).


</div>

</div>
### appendValueArgument

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#appendvalueargument"><span class="nf">appendValueArgument</span></a><span class="p">(</span>argumentList<span class="o">: </span><a href="../-kt-value-argument-list/index.html">KtValueArgumentList</a><span class="p">, </span>argument<span class="o">: </span><a href="../-kt-value-argument/index.html">KtValueArgument</a><span class="p">)</span><span class="o">: </span><a href="../-kt-value-argument/index.html">KtValueArgument</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`argument`](index.md#appendvalueargument) to [`argumentList`](index.md#appendvalueargument).


</div>

</div>
### astReplace

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#astreplace"><span class="nf">astReplace</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">, </span>newElement<span class="o">: </span>PsiElement<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces [`element`](index.md#astreplace) with [`newElement`](index.md#astreplace) on the AST level.


</div>

</div>
### convertImplicitDelegationCallToExplicit

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#convertimplicitdelegationcalltoexplicit"><span class="nf">convertImplicitDelegationCallToExplicit</span></a><span class="p">(</span>constructor<span class="o">: </span><a href="../-kt-secondary-constructor/index.html">KtSecondaryConstructor</a><span class="p">, </span>isThis<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a>
</span></code></pre></div>
</div>


<div markdown>

Replaces the implicit delegation call in [`constructor`](index.md#convertimplicitdelegationcalltoexplicit) with an explicit `this()` or `super()` call.


</div>

</div>
### deleteBlockExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#deleteblockexpression"><span class="nf">deleteBlockExpression</span></a><span class="p">(</span>blockExpression<span class="o">: </span><a href="../-kt-block-expression/index.html">KtBlockExpression</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Performs smart deletion of [`blockExpression`](index.md#deleteblockexpression).


</div>

</div>
### deleteClassOrObject

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#deleteclassorobject"><span class="nf">deleteClassOrObject</span></a><span class="p">(</span>declaration<span class="o">: </span><a href="../-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Performs smart deletion of [`declaration`](index.md#deleteclassorobject).


</div>

</div>
### deleteElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#deleteelement"><span class="nf">deleteElement</span></a><span class="p">(</span>element<span class="o">: </span><a href="../-kt-element/index.html">KtElement</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Performs smart deletion of [`element`](index.md#deleteelement).


</div>

</div>
### deleteEnumEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#deleteenumentry"><span class="nf">deleteEnumEntry</span></a><span class="p">(</span>enumEntry<span class="o">: </span><a href="../-kt-enum-entry/index.html">KtEnumEntry</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Performs smart deletion of [`enumEntry`](index.md#deleteenumentry).


</div>

</div>
### deleteParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#deleteparameter"><span class="nf">deleteParameter</span></a><span class="p">(</span>parameterList<span class="o">: </span><a href="../-kt-parameter-list/index.html">KtParameterList</a><span class="p">, </span>parameter<span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Removes [`parameter`](index.md#deleteparameter) from [`parameterList`](index.md#deleteparameter).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#deleteparameter"><span class="nf">deleteParameter</span></a><span class="p">(</span>parameterList<span class="o">: </span><a href="../-kt-parameter-list/index.html">KtParameterList</a><span class="p">, </span>index<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Removes a parameter at [`index`](index.md#deleteparameter) from [`parameterList`](index.md#deleteparameter).


</div>

</div>
### deleteSuperTypeList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#deletesupertypelist"><span class="nf">deleteSuperTypeList</span></a><span class="p">(</span>superTypeList<span class="o">: </span><a href="../-kt-super-type-list/index.html">KtSuperTypeList</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Deletes [`superTypeList`](index.md#deletesupertypelist), removing the preceding colon when needed.


</div>

</div>
### deleteValueArgument

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#deletevalueargument"><span class="nf">deleteValueArgument</span></a><span class="p">(</span>argumentList<span class="o">: </span><a href="../-kt-value-argument-list/index.html">KtValueArgumentList</a><span class="p">, </span>argument<span class="o">: </span><a href="../-kt-value-argument/index.html">KtValueArgument</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Removes [`argument`](index.md#deletevalueargument) from [`argumentList`](index.md#deletevalueargument).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#deletevalueargument"><span class="nf">deleteValueArgument</span></a><span class="p">(</span>argumentList<span class="o">: </span><a href="../-kt-value-argument-list/index.html">KtValueArgumentList</a><span class="p">, </span>index<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Removes an argument at [`index`](index.md#deletevalueargument) from [`argumentList`](index.md#deletevalueargument).


</div>

</div>
### getOrCreateCallValueArgumentList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getorcreatecallvalueargumentlist"><span class="nf">getOrCreateCallValueArgumentList</span></a><span class="p">(</span>callExpression<span class="o">: </span><a href="../-kt-call-expression/index.html">KtCallExpression</a><span class="p">)</span><span class="o">: </span><a href="../-kt-value-argument-list/index.html">KtValueArgumentList</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the existing value argument list for [`callExpression`](index.md#getorcreatecallvalueargumentlist), or creates an empty one.


</div>

</div>
### getOrCreateClassBody

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getorcreateclassbody"><span class="nf">getOrCreateClassBody</span></a><span class="p">(</span>classOrObject<span class="o">: </span><a href="../-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">)</span><span class="o">: </span><a href="../-kt-class-body/index.html">KtClassBody</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the existing body for [`classOrObject`](index.md#getorcreateclassbody), or creates one if missing.


</div>

</div>
### getOrCreateFunctionLiteralParameterList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getorcreatefunctionliteralparameterlist"><span class="nf">getOrCreateFunctionLiteralParameterList</span></a><span class="p">(</span>functionLiteral<span class="o">: </span><a href="../-kt-function-literal/index.html">KtFunctionLiteral</a><span class="p">)</span><span class="o">: </span><a href="../-kt-parameter-list/index.html">KtParameterList</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the existing value parameter list for [`functionLiteral`](index.md#getorcreatefunctionliteralparameterlist), or creates an empty one together with the arrow token.


</div>

</div>
### getOrCreatePrimaryConstructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getorcreateprimaryconstructor"><span class="nf">getOrCreatePrimaryConstructor</span></a><span class="p">(</span>klass<span class="o">: </span><a href="../-kt-class/index.html">KtClass</a><span class="p">)</span><span class="o">: </span><a href="../-kt-primary-constructor/index.html">KtPrimaryConstructor</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the existing primary constructor for [`klass`](index.md#getorcreateprimaryconstructor), or creates one if missing.


</div>

</div>
### getOrCreatePrimaryConstructorParameterList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getorcreateprimaryconstructorparameterlist"><span class="nf">getOrCreatePrimaryConstructorParameterList</span></a><span class="p">(</span>klass<span class="o">: </span><a href="../-kt-class/index.html">KtClass</a><span class="p">)</span><span class="o">: </span><a href="../-kt-parameter-list/index.html">KtParameterList</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the existing primary constructor parameter list for [`klass`](index.md#getorcreateprimaryconstructorparameterlist), or creates one if missing.


</div>

</div>
### insertParameterAfter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#insertparameterafter"><span class="nf">insertParameterAfter</span></a><span class="p">(</span>
    parameterList<span class="o">: </span><a href="../-kt-parameter-list/index.html">KtParameterList</a><span class="p">, </span>
    parameter<span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a><span class="p">, </span>
    anchor<span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a><span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`parameter`](index.md#insertparameterafter) to [`parameterList`](index.md#insertparameterafter) after [`anchor`](index.md#insertparameterafter).


</div>

</div>
### insertParameterBefore

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#insertparameterbefore"><span class="nf">insertParameterBefore</span></a><span class="p">(</span>
    parameterList<span class="o">: </span><a href="../-kt-parameter-list/index.html">KtParameterList</a><span class="p">, </span>
    parameter<span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a><span class="p">, </span>
    anchor<span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a><span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`parameter`](index.md#insertparameterbefore) to [`parameterList`](index.md#insertparameterbefore) before [`anchor`](index.md#insertparameterbefore).


</div>

</div>
### insertValueArgumentAfter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#insertvalueargumentafter"><span class="nf">insertValueArgumentAfter</span></a><span class="p">(</span>
    argumentList<span class="o">: </span><a href="../-kt-value-argument-list/index.html">KtValueArgumentList</a><span class="p">, </span>
    argument<span class="o">: </span><a href="../-kt-value-argument/index.html">KtValueArgument</a><span class="p">, </span>
    anchor<span class="o">: </span><a href="../-kt-value-argument/index.html">KtValueArgument</a><span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="../-kt-value-argument/index.html">KtValueArgument</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`argument`](index.md#insertvalueargumentafter) to [`argumentList`](index.md#insertvalueargumentafter) after [`anchor`](index.md#insertvalueargumentafter).


</div>

</div>
### insertValueArgumentBefore

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#insertvalueargumentbefore"><span class="nf">insertValueArgumentBefore</span></a><span class="p">(</span>
    argumentList<span class="o">: </span><a href="../-kt-value-argument-list/index.html">KtValueArgumentList</a><span class="p">, </span>
    argument<span class="o">: </span><a href="../-kt-value-argument/index.html">KtValueArgument</a><span class="p">, </span>
    anchor<span class="o">: </span><a href="../-kt-value-argument/index.html">KtValueArgument</a><span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="../-kt-value-argument/index.html">KtValueArgument</a>
</span></code></pre></div>
</div>


<div markdown>

Adds [`argument`](index.md#insertvalueargumentbefore) to [`argumentList`](index.md#insertvalueargumentbefore) before [`anchor`](index.md#insertvalueargumentbefore).


</div>

</div>
### removeAnnotationEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#removeannotationentry"><span class="nf">removeAnnotationEntry</span></a><span class="p">(</span>annotation<span class="o">: </span><a href="../-kt-annotation/index.html">KtAnnotation</a><span class="p">, </span>entry<span class="o">: </span><a href="../-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Removes [`entry`](index.md#removeannotationentry) from [`annotation`](index.md#removeannotationentry), deleting the annotation when it becomes empty.


</div>

</div>
### removeModifierKeyword

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#removemodifierkeyword"><span class="nf">removeModifierKeyword</span></a><span class="p">(</span>owner<span class="o">: </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">, </span>modifier<span class="o">: </span><a href="../../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Removes [`modifier`](index.md#removemodifierkeyword) from [`owner`](index.md#removemodifierkeyword).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#removemodifierkeyword"><span class="nf">removeModifierKeyword</span></a><span class="p">(</span>constructor<span class="o">: </span><a href="../-kt-primary-constructor/index.html">KtPrimaryConstructor</a><span class="p">, </span>modifier<span class="o">: </span><a href="../../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Removes [`modifier`](index.md#removemodifierkeyword) from [`constructor`](index.md#removemodifierkeyword) using primary-constructor-specific behavior.


</div>

</div>
### removeQualifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#removequalifier"><span class="nf">removeQualifier</span></a><span class="p">(</span>userType<span class="o">: </span><a href="../-kt-user-type/index.html">KtUserType</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Removes the qualifier of [`userType`](index.md#removequalifier), keeping the referenced name intact.


</div>

</div>
### removeRedundantConstructorKeyword

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#removeredundantconstructorkeyword"><span class="nf">removeRedundantConstructorKeyword</span></a><span class="p">(</span>constructor<span class="o">: </span><a href="../-kt-primary-constructor/index.html">KtPrimaryConstructor</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Removes the redundant `constructor` keyword and the following whitespace from [`constructor`](index.md#removeredundantconstructorkeyword).


</div>

</div>
### removeSuperType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#removesupertype"><span class="nf">removeSuperType</span></a><span class="p">(</span>declaration<span class="o">: </span><a href="../-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">, </span>superTypeListEntry<span class="o">: </span><a href="../-kt-super-type-list-entry/index.html">KtSuperTypeListEntry</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Removes [`superTypeListEntry`](index.md#removesupertype) from [`declaration`](index.md#removesupertype).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#removesupertype"><span class="nf">removeSuperType</span></a><span class="p">(</span>superTypeList<span class="o">: </span><a href="../-kt-super-type-list/index.html">KtSuperTypeList</a><span class="p">, </span>superTypeListEntry<span class="o">: </span><a href="../-kt-super-type-list-entry/index.html">KtSuperTypeListEntry</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Removes [`superTypeListEntry`](index.md#removesupertype) from [`superTypeList`](index.md#removesupertype).


</div>

</div>
### replaceExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#replaceexpression"><span class="nf">replaceExpression</span></a><span class="p">(</span>
    expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">, </span>
    newElement<span class="o">: </span>PsiElement<span class="p">, </span>
    reformat<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    rawReplaceHandler<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span>PsiElement
<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Replaces [`expression`](index.md#replaceexpression) with [`newElement`](index.md#replaceexpression), adding parentheses or string-template braces when needed.


</div>

</div>
### replaceFileAnnotationList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#replacefileannotationlist"><span class="nf">replaceFileAnnotationList</span></a><span class="p">(</span>file<span class="o">: </span><a href="../-kt-file/index.html">KtFile</a><span class="p">, </span>annotationList<span class="o">: </span><a href="../-kt-file-annotation-list/index.html">KtFileAnnotationList</a><span class="p">)</span><span class="o">: </span><a href="../-kt-file-annotation-list/index.html">KtFileAnnotationList</a>
</span></code></pre></div>
</div>


<div markdown>

Replaces [`file`](index.md#replacefileannotationlist)'s file annotation list with [`annotationList`](index.md#replacefileannotationlist), or adds it when missing.


</div>

</div>
### replaceModifierList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#replacemodifierlist"><span class="nf">replaceModifierList</span></a><span class="p">(</span>owner<span class="o">: </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">, </span>modifierList<span class="o">: </span><a href="../-kt-modifier-list/index.html">KtModifierList</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-kt-modifier-list/index.html">KtModifierList</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces the existing modifier list on [`owner`](index.md#replacemodifierlist) with [`modifierList`](index.md#replacemodifierlist), adds it if missing, or removes it when [`modifierList`](index.md#replacemodifierlist) is `null`.


</div>

</div>
### setCallableReceiverTypeReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setcallablereceivertypereference"><span class="nf">setCallableReceiverTypeReference</span></a><span class="p">(</span>declaration<span class="o">: </span><a href="../-kt-callable-declaration/index.html">KtCallableDeclaration</a><span class="p">, </span>typeRef<span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces the receiver type on [`declaration`](index.md#setcallablereceivertypereference) with [`typeRef`](index.md#setcallablereceivertypereference), adds it if missing, or removes it when [`typeRef`](index.md#setcallablereceivertypereference) is `null`.


</div>

</div>
### setCallableTypeReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setcallabletypereference"><span class="nf">setCallableTypeReference</span></a><span class="p">(</span>
    declaration<span class="o">: </span><a href="../-kt-callable-declaration/index.html">KtCallableDeclaration</a><span class="p">, </span>
    addAfter<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">, </span>
    typeRef<span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces the explicit return type on [`declaration`](index.md#setcallabletypereference) with [`typeRef`](index.md#setcallabletypereference), adds it if missing, or removes it when [`typeRef`](index.md#setcallabletypereference) is `null`.


</div>

</div>
### setCommonFileName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setcommonfilename"><span class="nf">setCommonFileName</span></a><span class="p">(</span>file<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-common-file/index.html">KtCommonFile</a><span class="p">, </span>name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Renames [`file`](index.md#setcommonfilename), reparsing it when the rename changes whether it should be treated as a script.


</div>

</div>
### setDestructuringDeclarationEntryTypeReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setdestructuringdeclarationentrytypereference"><span class="nf">setDestructuringDeclarationEntryTypeReference</span></a><span class="p">(</span>entry<span class="o">: </span><a href="../-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">, </span>typeRef<span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces the type reference on [`entry`](index.md#setdestructuringdeclarationentrytypereference) with [`typeRef`](index.md#setdestructuringdeclarationentrytypereference), adds it if missing, or removes it when [`typeRef`](index.md#setdestructuringdeclarationentrytypereference) is `null`.


</div>

</div>
### setDoubleColonReceiverExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setdoublecolonreceiverexpression"><span class="nf">setDoubleColonReceiverExpression</span></a><span class="p">(</span>expression<span class="o">: </span><a href="../-kt-double-colon-expression/index.html">KtDoubleColonExpression</a><span class="p">, </span>newReceiverExpression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces the receiver expression on [`expression`](index.md#setdoublecolonreceiverexpression) with [`newReceiverExpression`](index.md#setdoublecolonreceiverexpression), or adds it if missing.


</div>

</div>
### setFunctionTypeReceiverTypeReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setfunctiontypereceivertypereference"><span class="nf">setFunctionTypeReceiverTypeReference</span></a><span class="p">(</span>functionType<span class="o">: </span><a href="../-kt-function-type/index.html">KtFunctionType</a><span class="p">, </span>typeRef<span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces the receiver type on [`functionType`](index.md#setfunctiontypereceivertypereference) with [`typeRef`](index.md#setfunctiontypereceivertypereference), adds it if missing, or removes it when [`typeRef`](index.md#setfunctiontypereceivertypereference) is `null`.


</div>

</div>
### setFunctionTypeReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setfunctiontypereference"><span class="nf">setFunctionTypeReference</span></a><span class="p">(</span>function<span class="o">: </span><a href="../-kt-named-function/index.html">KtNamedFunction</a><span class="p">, </span>typeRef<span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces the type reference on [`function`](index.md#setfunctiontypereference) with [`typeRef`](index.md#setfunctiontypereference), adds it if missing, or removes it when [`typeRef`](index.md#setfunctiontypereference) is `null`.


</div>

</div>
### setImportAliasName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setimportaliasname"><span class="nf">setImportAliasName</span></a><span class="p">(</span>importAlias<span class="o">: </span><a href="../-kt-import-alias/index.html">KtImportAlias</a><span class="p">, </span>name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Renames [`importAlias`](index.md#setimportaliasname).


</div>

</div>
### setLabeledExpressionName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setlabeledexpressionname"><span class="nf">setLabeledExpressionName</span></a><span class="p">(</span>expression<span class="o">: </span><a href="../-kt-labeled-expression/index.html">KtLabeledExpression</a><span class="p">, </span>name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Renames [`expression`](index.md#setlabeledexpressionname) by replacing its target label.


</div>

</div>
### setModifierList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setmodifierlist"><span class="nf">setModifierList</span></a><span class="p">(</span>owner<span class="o">: </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">, </span>newModifierList<span class="o">: </span><a href="../-kt-modifier-list/index.html">KtModifierList</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces the existing modifier list on [`owner`](index.md#setmodifierlist) with [`newModifierList`](index.md#setmodifierlist), or adds it if missing.


</div>

</div>
### setNamedDeclarationName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setnameddeclarationname"><span class="nf">setNamedDeclarationName</span></a><span class="p">(</span>declaration<span class="o">: </span><a href="../-kt-named-declaration/index.html">KtNamedDeclaration</a><span class="p">, </span>name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Renames [`declaration`](index.md#setnameddeclarationname) by replacing its name identifier directly.


</div>

</div>
### setNamedDeclarationStubName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setnameddeclarationstubname"><span class="nf">setNamedDeclarationStubName</span></a><span class="p">(</span>declaration<span class="o">: </span><a href="../-kt-named-declaration-stub/index.html">KtNamedDeclarationStub</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="p">, </span>name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Renames [`declaration`](index.md#setnameddeclarationstubname), including operator-specific modifier adjustments.


</div>

</div>
### setObjectDeclarationName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setobjectdeclarationname"><span class="nf">setObjectDeclarationName</span></a><span class="p">(</span>declaration<span class="o">: </span><a href="../-kt-object-declaration/index.html">KtObjectDeclaration</a><span class="p">, </span>name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Renames [`declaration`](index.md#setobjectdeclarationname), adding an explicit identifier when necessary.


</div>

</div>
### setPackageFqName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setpackagefqname"><span class="nf">setPackageFqName</span></a><span class="p">(</span>file<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-common-file/index.html">KtCommonFile</a><span class="p">, </span>fqName<span class="o">: </span>FqName<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces the package name of [`file`](index.md#setpackagefqname), adding a package directive when needed.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setpackagefqname"><span class="nf">setPackageFqName</span></a><span class="p">(</span>packageDirective<span class="o">: </span><a href="../-kt-package-directive/index.html">KtPackageDirective</a><span class="p">, </span>fqName<span class="o">: </span>FqName<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces the package name of [`packageDirective`](index.md#setpackagefqname) with [`fqName`](index.md#setpackagefqname).


</div>

</div>
### setParameterTypeReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setparametertypereference"><span class="nf">setParameterTypeReference</span></a><span class="p">(</span>parameter<span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a><span class="p">, </span>typeRef<span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces the type reference on [`parameter`](index.md#setparametertypereference) with [`typeRef`](index.md#setparametertypereference), adds it if missing, or removes it when [`typeRef`](index.md#setparametertypereference) is `null`.


</div>

</div>
### setPropertyInitializer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setpropertyinitializer"><span class="nf">setPropertyInitializer</span></a><span class="p">(</span>property<span class="o">: </span><a href="../-kt-property/index.html">KtProperty</a><span class="p">, </span>initializer<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces the initializer on [`property`](index.md#setpropertyinitializer) with [`initializer`](index.md#setpropertyinitializer), adds it if missing, or removes it when [`initializer`](index.md#setpropertyinitializer) is `null`.


</div>

</div>
### setPropertyTypeReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#setpropertytypereference"><span class="nf">setPropertyTypeReference</span></a><span class="p">(</span>property<span class="o">: </span><a href="../-kt-property/index.html">KtProperty</a><span class="p">, </span>typeRef<span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces the type reference on [`property`](index.md#setpropertytypereference) with [`typeRef`](index.md#setpropertytypereference), adds it if missing, or removes it when [`typeRef`](index.md#setpropertytypereference) is `null`.


</div>

</div>
### setTypeParameterExtendsBound

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#settypeparameterextendsbound"><span class="nf">setTypeParameterExtendsBound</span></a><span class="p">(</span>typeParameter<span class="o">: </span><a href="../-kt-type-parameter/index.html">KtTypeParameter</a><span class="p">, </span>typeReference<span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Replaces the extends bound on [`typeParameter`](index.md#settypeparameterextendsbound) with [`typeReference`](index.md#settypeparameterextendsbound), adds it if missing, or removes it when [`typeReference`](index.md#settypeparameterextendsbound) is `null`.


</div>

</div>
### updateKDocSectionText

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#updatekdocsectiontext"><span class="nf">updateKDocSectionText</span></a><span class="p">(</span>section<span class="o">: </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-section/index.html">KDocSection</a><span class="p">, </span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span>PsiLanguageInjectionHost
</span></code></pre></div>
</div>


<div markdown>

Updates the text of [`section`](index.md#updatekdocsectiontext) for language injection.


</div>

</div>
### updateStringTemplateText

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#updatestringtemplatetext"><span class="nf">updateStringTemplateText</span></a><span class="p">(</span>expression<span class="o">: </span><a href="../-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="p">, </span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span>PsiLanguageInjectionHost
</span></code></pre></div>
</div>


<div markdown>

Updates the text of [`expression`](index.md#updatestringtemplatetext) for language injection.


</div>

</div>
