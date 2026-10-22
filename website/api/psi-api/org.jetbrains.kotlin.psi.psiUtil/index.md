---
tags:
 - jvm
title: "org.jetbrains.kotlin.psi.psiUtil"
---

# org.jetbrains.kotlin.psi.psiUtil
## Types
### [`KtStringTemplateExpressionManipulator`](-kt-string-template-expression-manipulator/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-string-template-expression-manipulator/index.html">KtStringTemplateExpressionManipulator</a> : AbstractElementManipulator<span class="o"><</span><a href="../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

The ElementManipulator of [`KtStringTemplateExpression`](../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.md), which edits the content of a string literal, e.g., when a language fragment injected into the string is edited or a reference contributed to the string is renamed.


</div>

</div>
### [`PsiChildRange`](-psi-child-range/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">class </span><a href="-psi-child-range/index.html">PsiChildRange</a><span class="p">(</span><span class="kd">val </span>first<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">, </span><span class="kd">val </span>last<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>PsiElement<span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A contiguous range of sibling PSI elements, from [`first`](-psi-child-range/index.md#first) to [`last`](-psi-child-range/index.md#last) inclusive, iterable as a [`Sequence`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html).


</div>

</div>
## Properties
### [`allChildren`](all-children.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="all-children.html">allChildren</a><span class="o">: </span><a href="-psi-child-range/index.html">PsiChildRange</a>
</span></code></pre></div>
</div>


<div markdown>

The range of all direct children of this element, or an empty range if it has none.


</div>

</div>
### [`argumentIndex`](argument-index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-value-argument/index.html">KtValueArgument</a><span class="p">.</span><a href="argument-index.html">argumentIndex</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

The index of this argument within its enclosing value argument list.


</div>

</div>
### [`containingClassId`](containing-class-id.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="containing-class-id.html">containingClassId</a><span class="o">: </span>ClassId<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The containing ClassId for this declaration. REPL [`KtScript`](../org.jetbrains.kotlin.psi/-kt-script/index.md)s are supported.


</div>

</div>
### [`containingClassOrObject`](containing-class-or-object.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-class-body/index.html">KtClassBody</a><span class="p">.</span><a href="containing-class-or-object.html">containingClassOrObject</a><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The containing class for the body.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-companion-block/index.html">KtCompanionBlock</a><span class="p">.</span><a href="containing-class-or-object.html">containingClassOrObject</a><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The containing class for the companion block.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="containing-class-or-object.html">containingClassOrObject</a><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The class or object that declares this declaration as a member (including constructors and nested classes), or `null` if it is not a class member — for example, a member function's parameter or local, or a property accessor.


</div>

</div>
### [`containingClassOrScript`](containing-class-or-script.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="containing-class-or-script.html">containingClassOrScript</a><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-named-declaration/index.html">KtNamedDeclaration</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The containing class or script for a declaration.


</div>

</div>
### [`containingScript`](containing-script.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-block-expression/index.html">KtBlockExpression</a><span class="p">.</span><a href="containing-script.html">containingScript</a><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-script/index.html">KtScript</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The containing script for the block expression.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="containing-script.html">containingScript</a><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-script/index.html">KtScript</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The containing script for top-level declarations.


</div>

</div>
### [`endOffset`](end-offset.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="end-offset.html">endOffset</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

The offset just past the end of this element's text range in the file.


</div>

</div>
### [`isCompanion`](is-companion.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration-with-return-type/index.html">KtDeclarationWithReturnType</a><span class="p">.</span><a href="is-companion.html">isCompanion</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the callable is a [companion extension](https://github.com/Kotlin/KEEP/blob/main/proposals/KEEP-0449-companions-block-extension.md#companion-extensions) or comes from a [companion block](https://github.com/Kotlin/KEEP/blob/main/proposals/KEEP-0449-companions-block-extension.md#companion-blocks).


</div>

</div>
### [`isFromCompanionBlock`](is-from-companion-block.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="is-from-companion-block.html">isFromCompanionBlock</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether this declaration is declared inside a companion object block.


</div>

</div>
### [`isPrivateNestedClassOrObject`](is-private-nested-class-or-object.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-named-declaration/index.html">KtNamedDeclaration</a><span class="p">.</span><a href="is-private-nested-class-or-object.html">isPrivateNestedClassOrObject</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

`true` if this is a private nested (non-top-level) class or object.


</div>

</div>
### [`isPublic`](is-public.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="is-public.html">isPublic</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

`true` if this declaration is effectively public (no visibility modifier or an explicit `public`), and not local.


</div>

</div>
### [`isUnderscoreInBackticks`](is-underscore-in-backticks.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.html">KtNameReferenceExpression</a><span class="p">.</span><a href="is-underscore-in-backticks.html">isUnderscoreInBackticks</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

`true` if this reference is the backtick-escaped underscore identifier `` `_` `` (distinct from the plain `_` placeholder).


</div>

</div>
### [`nextLeafs`](next-leafs.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="next-leafs.html">nextLeafs</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The following leaf elements as a lazy sequence, nearest first.


</div>

</div>
### [`parents`](parents.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="parents.html">parents</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The ancestors of this element, from its immediate parent up to and including the containing file.


</div>

</div>
### [`parentsWithSelf`](parents-with-self.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="parents-with-self.html">parentsWithSelf</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

This element and its ancestors, from the element itself up to and including the containing file.


</div>

</div>
### [`plainContent`](plain-content.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="p">.</span><a href="plain-content.html">plainContent</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

The source text between the string delimiters, including any escape or interpolation syntax.


</div>

</div>
### [`prevLeafs`](prev-leafs.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="prev-leafs.html">prevLeafs</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The preceding leaf elements as a lazy sequence, nearest first.


</div>

</div>
### [`pureEndOffset`](pure-end-offset.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-pure-element/index.html">KtPureElement</a><span class="p">.</span><a href="pure-end-offset.html">pureEndOffset</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

The end offset of this element's source.


</div>

</div>
### [`pureStartOffset`](pure-start-offset.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-pure-element/index.html">KtPureElement</a><span class="p">.</span><a href="pure-start-offset.html">pureStartOffset</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

The start offset of this element's source, excluding any leading comments.


</div>

</div>
### [`startOffset`](start-offset.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="start-offset.html">startOffset</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

The offset of the start of this element's text range in the file.


</div>

</div>
### [`startOffsetSkippingComments`](start-offset-skipping-comments.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="start-offset-skipping-comments.html">startOffsetSkippingComments</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

The start offset of this element, skipping leading comments and the whitespace that follows them.


</div>

</div>
### [`textRangeWithoutComments`](text-range-without-comments.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="text-range-without-comments.html">textRangeWithoutComments</a><span class="o">: </span>TextRange
</span></code></pre></div>
</div>


<div markdown>

The text range of this element excluding any leading comments.


</div>

</div>
### [`UNWRAPPABLE_TOKEN_TYPES`](-u-n-w-r-a-p-p-a-b-l-e_-t-o-k-e-n_-t-y-p-e-s.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="-u-n-w-r-a-p-p-a-b-l-e_-t-o-k-e-n_-t-y-p-e-s.html">UNWRAPPABLE_TOKEN_TYPES</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>IElementType<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

See org.jetbrains.kotlin.fir.builder.AbstractRawFirBuilder.unwrap


</div>

</div>
## Functions
### [`anyDescendantOfType`](any-descendant-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="any-descendant-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="any-descendant-of-type.html"><span class="nf">anyDescendantOfType</span></a><span class="p">(</span><span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="any-descendant-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element or any descendant of type [`T`](any-descendant-of-type.md) satisfies [`predicate`](any-descendant-of-type.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="any-descendant-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="any-descendant-of-type.html"><span class="nf">anyDescendantOfType</span></a><span class="p">(</span><span class="kd">crossinline </span>canGoInside<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span><span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="any-descendant-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element or any descendant of type [`T`](any-descendant-of-type.md) satisfies [`predicate`](any-descendant-of-type.md). [`canGoInside`](any-descendant-of-type.md) controls traversal into children but does not prevent the current element from being tested.


</div>

</div>
### [`asAssignment`](as-assignment.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="as-assignment.html"><span class="nf">asAssignment</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-binary-expression/index.html">KtBinaryExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns this expression as a [`KtBinaryExpression`](../org.jetbrains.kotlin.psi/-kt-binary-expression/index.md) if it is an assignment, or `null` otherwise.


</div>

</div>
### [`before`](before.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="before.html"><span class="nf">before</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element ends at or before [`element`](before.md) starts (that is, it precedes [`element`](before.md) in the file).


</div>

</div>
### [`blockExpressionsOrSingle`](block-expressions-or-single.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="block-expressions-or-single.html"><span class="nf">blockExpressionsOrSingle</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the statements of this element if it is a block, otherwise a single-element sequence of this element.


</div>

</div>
### [`canPlaceAfterSimpleNameEntry`](can-place-after-simple-name-entry.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="can-place-after-simple-name-entry.html"><span class="nf">canPlaceAfterSimpleNameEntry</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if placing text after a `$name` simple-name template entry would not accidentally extend the name, that is, [`element`](can-place-after-simple-name-entry.md) does not begin with an identifier character.


</div>

</div>
### [`checkDecompiledText`](check-decompiled-text.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="check-decompiled-text.html"><span class="nf">checkDecompiledText</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Throws if this element belongs to a compiled file that is backed by a stub. Loading decompiled text is slow and should be avoided; stubs should be used instead. Called by the descendant-traversal helpers as a guard.


</div>

</div>
### [`children`](children.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>ASTNode<span class="p">.</span><a href="children.html"><span class="nf">children</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>ASTNode<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The direct child nodes of this AST node, as a lazy sequence.


</div>

</div>
### [`closestPsiElement`](closest-psi-element.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>ASTNode<span class="p">.</span><a href="closest-psi-element.html"><span class="nf">closestPsiElement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest PSI element for this node, walking up to a parent node if this node has no PSI of its own.


</div>

</div>
### [`collectAnnotationEntriesFromStubOrPsi`](collect-annotation-entries-from-stub-or-psi.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-annotations-container/index.html">KtAnnotationsContainer</a><span class="p">.</span><a href="collect-annotation-entries-from-stub-or-psi.html"><span class="nf">collectAnnotationEntriesFromStubOrPsi</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi/-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Collects the annotation entries of this container, reading from the stub when available and falling back to the PSI.


</div>

</div>
### [`collectDescendantsOfType`](collect-descendants-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="collect-descendants-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="collect-descendants-of-type.html"><span class="nf">collectDescendantsOfType</span></a><span class="p">(</span><span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="collect-descendants-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="collect-descendants-of-type.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Collects this element and all descendants of type [`T`](collect-descendants-of-type.md) satisfying [`predicate`](collect-descendants-of-type.md) into a list in post-order.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="collect-descendants-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="collect-descendants-of-type.html"><span class="nf">collectDescendantsOfType</span></a><span class="p">(</span><span class="kd">crossinline </span>canGoInside<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span><span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="collect-descendants-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="collect-descendants-of-type.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Collects this element and all descendants of type [`T`](collect-descendants-of-type.md) satisfying [`predicate`](collect-descendants-of-type.md) into a list in post-order. [`canGoInside`](collect-descendants-of-type.md) controls traversal into children but does not prevent the current element from being collected.


</div>

</div>
### [`collectDescendantsOfTypeTo`](collect-descendants-of-type-to.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="collect-descendants-of-type-to.html">T</a><span class="o"> : </span>PsiElement<span class="p">, </span><a href="collect-descendants-of-type-to.html">C</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-collection/index.html">MutableCollection</a><span class="o"><</span><a href="collect-descendants-of-type-to.html">T</a><span class="o">></span><span class="o">> </span>PsiElement<span class="p">.</span><a href="collect-descendants-of-type-to.html"><span class="nf">collectDescendantsOfTypeTo</span></a><span class="p">(</span>
    to<span class="o">: </span><a href="collect-descendants-of-type-to.html">C</a><span class="p">, </span>
    <span class="kd">crossinline </span>canGoInside<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="collect-descendants-of-type-to.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }
<span class="p">)</span><span class="o">: </span><a href="collect-descendants-of-type-to.html">C</a>
</span></code></pre></div>
</div>


<div markdown>

Adds this element and all descendants of type [`T`](collect-descendants-of-type-to.md) satisfying [`predicate`](collect-descendants-of-type-to.md) to [`to`](collect-descendants-of-type-to.md) in post-order. [`canGoInside`](collect-descendants-of-type-to.md) controls traversal into children but does not prevent the current element from being added.


</div>

</div>
### [`containingClass`](containing-class.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="containing-class.html"><span class="nf">containingClass</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-class/index.html">KtClass</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest enclosing [`KtClass`](../org.jetbrains.kotlin.psi/-kt-class/index.md), or `null` if there is none.


</div>

</div>
### [`contains`](contains.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">operator </span><span class="kd">fun </span>SearchScope<span class="p">.</span><a href="contains.html"><span class="nf">contains</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if [`element`](contains.md) lies within this search scope.


</div>

</div>
### [`containsInside`](contains-inside.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>TextRange<span class="p">.</span><a href="contains-inside.html"><span class="nf">containsInside</span></a><span class="p">(</span>offset<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if [`offset`](contains-inside.md) lies strictly inside this range (excluding both endpoints).


</div>

</div>
### [`contentRange`](content-range.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-block-expression/index.html">KtBlockExpression</a><span class="p">.</span><a href="content-range.html"><span class="nf">contentRange</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-psi-child-range/index.html">PsiChildRange</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the range of direct PSI children between this block's braces after excluding outer whitespace. The range may contain comments and other non-statement elements. Returns an empty range if either brace is missing or no non-whitespace content remains.


</div>

</div>
### [`effectiveDeclarations`](effective-declarations.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">.</span><a href="effective-declarations.html"><span class="nf">effectiveDeclarations</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the body declarations of this class or object in source order, followed by the class's primary-constructor `val`/`var` property parameters in parameter order.


</div>

</div>
### [`elementsInRange`](elements-in-range.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiFile<span class="p">.</span><a href="elements-in-range.html"><span class="nf">elementsInRange</span></a><span class="p">(</span>range<span class="o">: </span>TextRange<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the top-level elements that together cover the given [`range`](elements-in-range.md) within this file.


</div>

</div>
### [`findAssignment`](find-assignment.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">tailrec </span><span class="kd">fun </span><a href="find-assignment.html"><span class="nf">findAssignment</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-binary-expression/index.html">KtBinaryExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Walks up from [`element`](find-assignment.md) through qualified/simple-name expressions to find a plain `=` assignment whose LHS it is.


</div>

</div>
### [`findDescendantOfType`](find-descendant-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="find-descendant-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="find-descendant-of-type.html"><span class="nf">findDescendantOfType</span></a><span class="p">(</span><span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="find-descendant-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="find-descendant-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the first element of type [`T`](find-descendant-of-type.md) in a pre-order traversal of this element and its descendants that satisfies [`predicate`](find-descendant-of-type.md), or `null` if there is none.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="find-descendant-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="find-descendant-of-type.html"><span class="nf">findDescendantOfType</span></a><span class="p">(</span><span class="kd">crossinline </span>canGoInside<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span><span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="find-descendant-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="find-descendant-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the first element of type [`T`](find-descendant-of-type.md) in a pre-order traversal of this element and its descendants that satisfies [`predicate`](find-descendant-of-type.md), or `null`. [`canGoInside`](find-descendant-of-type.md) controls traversal into children but does not prevent the current element from being tested.


</div>

</div>
### [`findFunctionByName`](find-function-by-name.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">.</span><a href="find-function-by-name.html"><span class="nf">findFunctionByName</span></a><span class="p">(</span>name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-named-declaration/index.html">KtNamedDeclaration</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the member function with the given [`name`](find-function-by-name.md), or `null` if there is none.


</div>

</div>
### [`findLabelAndCall`](find-label-and-call.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-function-literal/index.html">KtFunctionLiteral</a><span class="p">.</span><a href="find-label-and-call.html"><span class="nf">findLabelAndCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/index.html">Pair</a><span class="o"><</span>Name<span class="o">?</span><span class="p">, </span><a href="../org.jetbrains.kotlin.psi/-kt-call-expression/index.html">KtCallExpression</a><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the label (explicit or the enclosing call's name) and the call that this lambda is passed to, as a pair. Either component may be `null` if it cannot be determined.


</div>

</div>
### [`findPropertyByName`](find-property-by-name.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">.</span><a href="find-property-by-name.html"><span class="nf">findPropertyByName</span></a><span class="p">(</span>name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-named-declaration/index.html">KtNamedDeclaration</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the member property (or primary-constructor property parameter) with the given [`name`](find-property-by-name.md), or `null`.


</div>

</div>
### [`flatMapDescendantsOfTypeVisitor`](flat-map-descendants-of-type-visitor.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="flat-map-descendants-of-type-visitor.html">T</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">, </span><a href="flat-map-descendants-of-type-visitor.html">R</a><span class="o">> </span><a href="flat-map-descendants-of-type-visitor.html"><span class="nf">flatMapDescendantsOfTypeVisitor</span></a><span class="p">(</span>accumulator<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-collection/index.html">MutableCollection</a><span class="o"><</span><a href="flat-map-descendants-of-type-visitor.html">R</a><span class="o">></span><span class="p">, </span><span class="kd">noinline </span>map<span class="o">: </span><span class="p">(</span><a href="flat-map-descendants-of-type-visitor.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="flat-map-descendants-of-type-visitor.html">R</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-visitor-void/index.html">KtVisitorVoid</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a recursive visitor that maps each visited element of type [`T`](flat-map-descendants-of-type-visitor.md), including the element passed to `accept`, and adds all results to [`accumulator`](flat-map-descendants-of-type-visitor.md) in DFS-exit order.


</div>

</div>
### [`forEachDescendantOfType`](for-each-descendant-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="for-each-descendant-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="for-each-descendant-of-type.html"><span class="nf">forEachDescendantOfType</span></a><span class="p">(</span><span class="kd">noinline </span>action<span class="o">: </span><span class="p">(</span><a href="for-each-descendant-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Applies [`action`](for-each-descendant-of-type.md) to this element and every descendant of type [`T`](for-each-descendant-of-type.md), in post-order (children before parents).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="for-each-descendant-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="for-each-descendant-of-type.html"><span class="nf">forEachDescendantOfType</span></a><span class="p">(</span><span class="kd">crossinline </span>canGoInside<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span><span class="kd">noinline </span>action<span class="o">: </span><span class="p">(</span><a href="for-each-descendant-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Applies [`action`](for-each-descendant-of-type.md) to this element and every descendant of type [`T`](for-each-descendant-of-type.md), in post-order. [`canGoInside`](for-each-descendant-of-type.md) controls whether each visited element's children are traversed; the element itself is still passed to [`action`](for-each-descendant-of-type.md) when it is a [`T`](for-each-descendant-of-type.md), even if [`canGoInside`](for-each-descendant-of-type.md) returns `false` for it.


</div>

</div>
### [`forEachDescendantOfTypeInPreorder`](for-each-descendant-of-type-in-preorder.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="for-each-descendant-of-type-in-preorder.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="for-each-descendant-of-type-in-preorder.html"><span class="nf">forEachDescendantOfTypeInPreorder</span></a><span class="p">(</span><span class="kd">noinline </span>action<span class="o">: </span><span class="p">(</span><a href="for-each-descendant-of-type-in-preorder.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Applies [`action`](for-each-descendant-of-type-in-preorder.md) to this element and every descendant of type [`T`](for-each-descendant-of-type-in-preorder.md), in pre-order (parents before children).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="for-each-descendant-of-type-in-preorder.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="for-each-descendant-of-type-in-preorder.html"><span class="nf">forEachDescendantOfTypeInPreorder</span></a><span class="p">(</span><span class="kd">crossinline </span>canGoInside<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span><span class="kd">noinline </span>action<span class="o">: </span><span class="p">(</span><a href="for-each-descendant-of-type-in-preorder.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Applies [`action`](for-each-descendant-of-type-in-preorder.md) to this element and every descendant of type [`T`](for-each-descendant-of-type-in-preorder.md), in pre-order. [`canGoInside`](for-each-descendant-of-type-in-preorder.md) controls whether each visited element's children are traversed; the element itself is still passed to [`action`](for-each-descendant-of-type-in-preorder.md) when it is a [`T`](for-each-descendant-of-type-in-preorder.md), even if [`canGoInside`](for-each-descendant-of-type-in-preorder.md) returns `false` for it.


</div>

</div>
### [`forEachDescendantOfTypeVisitor`](for-each-descendant-of-type-visitor.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="for-each-descendant-of-type-visitor.html">T</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="o">> </span><a href="for-each-descendant-of-type-visitor.html"><span class="nf">forEachDescendantOfTypeVisitor</span></a><span class="p">(</span><span class="kd">noinline </span>block<span class="o">: </span><span class="p">(</span><a href="for-each-descendant-of-type-visitor.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-visitor-void/index.html">KtVisitorVoid</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a recursive visitor that calls [`block`](for-each-descendant-of-type-visitor.md) on each visited element of type [`T`](for-each-descendant-of-type-visitor.md), including the element passed to `accept`. Calls happen in DFS-exit order, so deeper nodes are visited before their ancestors.


</div>

</div>
### [`getAnnotationEntries`](get-annotation-entries.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="get-annotation-entries.html"><span class="nf">getAnnotationEntries</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi/-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the annotation entries applied to this expression through an enclosing annotated (or labeled) expression, or an empty list if there are none.


</div>

</div>
### [`getAssignmentByLHS`](get-assignment-by-l-h-s.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="get-assignment-by-l-h-s.html"><span class="nf">getAssignmentByLHS</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-binary-expression/index.html">KtBinaryExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the assignment in which this expression is the left-hand side, or `null` if it is not assigned to.


</div>

</div>
### [`getAssignmentLhsIfUnwrappable`](get-assignment-lhs-if-unwrappable.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="get-assignment-lhs-if-unwrappable.html"><span class="nf">getAssignmentLhsIfUnwrappable</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the operand this operation applies to, but only when that operand is wrapped in parentheses, a label, or annotations; returns `null` otherwise.


</div>

</div>
### [`getBinaryWithTypeParent`](get-binary-with-type-parent.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="get-binary-with-type-parent.html"><span class="nf">getBinaryWithTypeParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-binary-expression-with-type-r-h-s/index.html">KtBinaryExpressionWithTypeRHS</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the `as`/`as?` expression whose left-hand side is a call with this expression as its direct child, normally its callee. The call may be the selector of a qualified expression, and the call or qualified expression may be parenthesized. Returns `null` otherwise.


</div>

</div>
### [`getCallNameExpression`](get-call-name-expression.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-call-element/index.html">KtCallElement</a><span class="p">.</span><a href="get-call-name-expression.html"><span class="nf">getCallNameExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the simple-name reference of this call's callee (its function or constructor name), or `null`.


</div>

</div>
### [`getChildOfType`](get-child-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="get-child-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-child-of-type.html"><span class="nf">getChildOfType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="get-child-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the first direct child of type [`T`](get-child-of-type.md), or `null` if there is none.


</div>

</div>
### [`getChildrenOfType`](get-children-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="get-children-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-children-of-type.html"><span class="nf">getChildrenOfType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="get-children-of-type.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the direct children of type [`T`](get-children-of-type.md), or an empty array if there are none.


</div>

</div>
### [`getContainingKtFile`](get-containing-kt-file.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>LazyParseablePsiElement<span class="p">.</span><a href="get-containing-kt-file.html"><span class="nf">getContainingKtFile</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KtFile`](../org.jetbrains.kotlin.psi/-kt-file/index.md) containing this element.


</div>

</div>
### [`getContentRange`](get-content-range.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="p">.</span><a href="get-content-range.html"><span class="nf">getContentRange</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>TextRange
</span></code></pre></div>
</div>


<div markdown>

Returns the text range of the string content, excluding the interpolation prefix and the opening/closing quotes.


</div>

</div>
### [`getElementTextWithContext`](get-element-text-with-context.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="get-element-text-with-context.html"><span class="nf">getElementTextWithContext</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns this element's text with surrounding source context, for use in diagnostics and log messages.


</div>

</div>
### [`getExplicitReceiverOfDotQualified`](get-explicit-receiver-of-dot-qualified.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="get-explicit-receiver-of-dot-qualified.html"><span class="nf">getExplicitReceiverOfDotQualified</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the source of the explicit receiver if this element is a dot-qualified expression, or `null` otherwise.


</div>

</div>
### [`getFileOrScriptDeclarations`](get-file-or-script-declarations.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="get-file-or-script-declarations.html"><span class="nf">getFileOrScriptDeclarations</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the top-level declarations of this file, taking them from the script if the file is a script.


</div>

</div>
### [`getIfChildIsInBranch`](get-if-child-is-in-branch.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="get-if-child-is-in-branch.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span><a href="get-if-child-is-in-branch.html">T</a><span class="p">.</span><a href="get-if-child-is-in-branch.html"><span class="nf">getIfChildIsInBranch</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">, </span>branch<span class="o">: </span><a href="get-if-child-is-in-branch.html">T</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="get-if-child-is-in-branch.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns this element if [`element`](get-if-child-is-in-branch.md) lies within the subtree returned by [`branch`](get-if-child-is-in-branch.md), otherwise `null`.


</div>

</div>
### [`getIfChildIsInBranches`](get-if-child-is-in-branches.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="get-if-child-is-in-branches.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span><a href="get-if-child-is-in-branches.html">T</a><span class="p">.</span><a href="get-if-child-is-in-branches.html"><span class="nf">getIfChildIsInBranches</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">, </span>branches<span class="o">: </span><a href="get-if-child-is-in-branches.html">T</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/index.html">Iterable</a><span class="o"><</span>PsiElement<span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="get-if-child-is-in-branches.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns this element if [`element`](get-if-child-is-in-branches.md) lies within any of the subtrees returned by [`branches`](get-if-child-is-in-branches.md), otherwise `null`.


</div>

</div>
### [`getImportedSimpleNameByImportAlias`](get-imported-simple-name-by-import-alias.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="get-imported-simple-name-by-import-alias.html"><span class="nf">getImportedSimpleNameByImportAlias</span></a><span class="p">(</span>file<span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>aliasName<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the original short name imported under the alias [`aliasName`](get-imported-simple-name-by-import-alias.md) in [`file`](get-imported-simple-name-by-import-alias.md), or `null` if there is no such alias.


</div>

</div>
### [`getLabeledParent`](get-labeled-parent.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="get-labeled-parent.html"><span class="nf">getLabeledParent</span></a><span class="p">(</span>labelName<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-labeled-expression/index.html">KtLabeledExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest enclosing labeled expression with the given [`labelName`](get-labeled-parent.md), or `null` if there is none.


</div>

</div>
### [`getLastParentOfTypeInRow`](get-last-parent-of-type-in-row.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="get-last-parent-of-type-in-row.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-last-parent-of-type-in-row.html"><span class="nf">getLastParentOfTypeInRow</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="get-last-parent-of-type-in-row.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the outermost element in an uninterrupted chain of ancestors of type [`T`](get-last-parent-of-type-in-row.md), or `null` if the parent is not a [`T`](get-last-parent-of-type-in-row.md).


</div>

</div>
### [`getLastParentOfTypeInRowWithSelf`](get-last-parent-of-type-in-row-with-self.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="get-last-parent-of-type-in-row-with-self.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-last-parent-of-type-in-row-with-self.html"><span class="nf">getLastParentOfTypeInRowWithSelf</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="get-last-parent-of-type-in-row-with-self.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Like [`getLastParentOfTypeInRow`](get-last-parent-of-type-in-row.md), but the chain may start at this element itself.


</div>

</div>
### [`getNextSiblingIgnoringWhitespace`](get-next-sibling-ignoring-whitespace.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="get-next-sibling-ignoring-whitespace.html"><span class="nf">getNextSiblingIgnoringWhitespace</span></a><span class="p">(</span>withItself<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the next sibling that is not whitespace, or `null`. Considers this element if [`withItself`](get-next-sibling-ignoring-whitespace.md).


</div>

</div>
### [`getNextSiblingIgnoringWhitespaceAndComments`](get-next-sibling-ignoring-whitespace-and-comments.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="get-next-sibling-ignoring-whitespace-and-comments.html"><span class="nf">getNextSiblingIgnoringWhitespaceAndComments</span></a><span class="p">(</span>withItself<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the next sibling that is neither whitespace nor a comment, or `null`. Considers this element if [`withItself`](get-next-sibling-ignoring-whitespace-and-comments.md).


</div>

</div>
### [`getNonStrictParentOfType`](get-non-strict-parent-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="get-non-strict-parent-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-non-strict-parent-of-type.html"><span class="nf">getNonStrictParentOfType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="get-non-strict-parent-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest ancestor of type [`T`](get-non-strict-parent-of-type.md) including this element, or `null` if there is none.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="get-non-strict-parent-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-non-strict-parent-of-type.html"><span class="nf">getNonStrictParentOfType</span></a><span class="p">(</span>parentClass<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="get-non-strict-parent-of-type.html">T</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="get-non-strict-parent-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest ancestor of type [`T`](get-non-strict-parent-of-type.md) (including this element), or `null` if there is none.


</div>

</div>
### [`getOutermostParentContainedIn`](get-outermost-parent-contained-in.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">tailrec </span><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="get-outermost-parent-contained-in.html"><span class="nf">getOutermostParentContainedIn</span></a><span class="p">(</span>container<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the outermost element on the path from this element that is still strictly contained in [`container`](get-outermost-parent-contained-in.md), or `null`.


</div>

</div>
### [`getOutermostParenthesizerOrThis`](get-outermost-parenthesizer-or-this.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="get-outermost-parenthesizer-or-this.html"><span class="nf">getOutermostParenthesizerOrThis</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the outermost expression that wraps this one only through parentheses, labels, or annotations, or this expression itself.


</div>

</div>
### [`getParentOfType`](get-parent-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="get-parent-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-parent-of-type.html"><span class="nf">getParentOfType</span></a><span class="p">(</span>strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="get-parent-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest ancestor of type [`T`](get-parent-of-type.md), or `null`. When [`strict`](get-parent-of-type.md) is `false`, this element itself is also considered.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="get-parent-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-parent-of-type.html"><span class="nf">getParentOfType</span></a><span class="p">(</span>strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span><span class="kd">vararg </span>stopAt<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><span class="kd">out </span>PsiElement<span class="o">></span><span class="p">)</span><span class="o">: </span><a href="get-parent-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest ancestor of type [`T`](get-parent-of-type.md), stopping the search once an ancestor of any type in [`stopAt`](get-parent-of-type.md) is reached, or `null`. When [`strict`](get-parent-of-type.md) is `false`, this element itself is also considered.


</div>

</div>
### [`getParentOfTypeAndBranch`](get-parent-of-type-and-branch.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="get-parent-of-type-and-branch.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-parent-of-type-and-branch.html"><span class="nf">getParentOfTypeAndBranch</span></a><span class="p">(</span>strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span><span class="kd">noinline </span>branch<span class="o">: </span><a href="get-parent-of-type-and-branch.html">T</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="get-parent-of-type-and-branch.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Checks the nearest element of type [`T`](get-parent-of-type-and-branch.md) and returns it if this element lies within the subtree selected by [`branch`](get-parent-of-type-and-branch.md). If that candidate's branch does not contain this element, returns `null` without checking higher ancestors. When [`strict`](get-parent-of-type-and-branch.md) is `false`, this element itself is also considered as the candidate.


</div>

</div>
### [`getParentOfTypeAndBranches`](get-parent-of-type-and-branches.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="get-parent-of-type-and-branches.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-parent-of-type-and-branches.html"><span class="nf">getParentOfTypeAndBranches</span></a><span class="p">(</span>strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span><span class="kd">noinline </span>branches<span class="o">: </span><a href="get-parent-of-type-and-branches.html">T</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/index.html">Iterable</a><span class="o"><</span>PsiElement<span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="get-parent-of-type-and-branches.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Checks the nearest element of type [`T`](get-parent-of-type-and-branches.md) and returns it if this element lies within any subtree selected by [`branches`](get-parent-of-type-and-branches.md). If none of that candidate's branches contain this element, returns `null` without checking higher ancestors. When [`strict`](get-parent-of-type-and-branches.md) is `false`, this element itself is also considered as the candidate.


</div>

</div>
### [`getParentOfTypes`](get-parent-of-types.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="get-parent-of-types.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-parent-of-types.html"><span class="nf">getParentOfTypes</span></a><span class="p">(</span>strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span><span class="kd">vararg </span>parentClasses<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><span class="kd">out </span><a href="get-parent-of-types.html">T</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="get-parent-of-types.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest ancestor that is an instance of one of [`parentClasses`](get-parent-of-types.md), or `null` if there is none. When [`strict`](get-parent-of-types.md) is `false`, this element itself is also considered.


</div>

</div>
### [`getParentOfTypes2`](get-parent-of-types2.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="get-parent-of-types2.html">T</a><span class="o"> : </span>PsiElement<span class="p">, </span><span class="kd">reified </span><a href="get-parent-of-types2.html">V</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-parent-of-types2.html"><span class="nf">getParentOfTypes2</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest strict ancestor that is a [`T`](get-parent-of-types2.md) or [`V`](get-parent-of-types2.md), or `null` if there is none.


</div>

</div>
### [`getParentOfTypes3`](get-parent-of-types3.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="get-parent-of-types3.html">T</a><span class="o"> : </span>PsiElement<span class="p">, </span><span class="kd">reified </span><a href="get-parent-of-types3.html">V</a><span class="o"> : </span>PsiElement<span class="p">, </span><span class="kd">reified </span><a href="get-parent-of-types3.html">U</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-parent-of-types3.html"><span class="nf">getParentOfTypes3</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest strict ancestor that is a [`T`](get-parent-of-types3.md), [`V`](get-parent-of-types3.md), or [`U`](get-parent-of-types3.md), or `null` if there is none.


</div>

</div>
### [`getParentOfTypesAndPredicate`](get-parent-of-types-and-predicate.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="get-parent-of-types-and-predicate.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-parent-of-types-and-predicate.html"><span class="nf">getParentOfTypesAndPredicate</span></a><span class="p">(</span>
    strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span>
    <span class="kd">vararg </span>parentClasses<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><span class="kd">out </span><a href="get-parent-of-types-and-predicate.html">T</a><span class="o">></span><span class="p">, </span>
    predicate<span class="o">: </span><span class="p">(</span><a href="get-parent-of-types-and-predicate.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
<span class="p">)</span><span class="o">: </span><a href="get-parent-of-types-and-predicate.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest ancestor that is an instance of one of [`parentClasses`](get-parent-of-types-and-predicate.md) and satisfies [`predicate`](get-parent-of-types-and-predicate.md), or `null`. When [`parentClasses`](get-parent-of-types-and-predicate.md) is empty, any type matches. When [`strict`](get-parent-of-types-and-predicate.md) is `false`, this element itself is also considered.


</div>

</div>
### [`getPossiblyQualifiedCallExpression`](get-possibly-qualified-call-expression.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="get-possibly-qualified-call-expression.html"><span class="nf">getPossiblyQualifiedCallExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-call-expression/index.html">KtCallExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the call expression this expression represents: the selector's call for a qualified expression, or this expression if it is itself a call. Returns `null` if there is no call.


</div>

</div>
### [`getPrevSiblingIgnoringWhitespace`](get-prev-sibling-ignoring-whitespace.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="get-prev-sibling-ignoring-whitespace.html"><span class="nf">getPrevSiblingIgnoringWhitespace</span></a><span class="p">(</span>withItself<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the previous sibling that is not whitespace, or `null`. Considers this element if [`withItself`](get-prev-sibling-ignoring-whitespace.md).


</div>

</div>
### [`getPrevSiblingIgnoringWhitespaceAndComments`](get-prev-sibling-ignoring-whitespace-and-comments.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="get-prev-sibling-ignoring-whitespace-and-comments.html"><span class="nf">getPrevSiblingIgnoringWhitespaceAndComments</span></a><span class="p">(</span>withItself<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the previous sibling that is neither whitespace nor a comment, or `null`. Considers this element if [`withItself`](get-prev-sibling-ignoring-whitespace-and-comments.md).


</div>

</div>
### [`getQualifiedElement`](get-qualified-element.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="get-qualified-element.html"><span class="nf">getQualifiedElement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the enclosing qualified element for this name: a [`KtQualifiedExpression`](../org.jetbrains.kotlin.psi/-kt-qualified-expression/index.md), a [`KtUserType`](../org.jetbrains.kotlin.psi/-kt-user-type/index.md), or this expression itself if there is no such qualifier.


</div>

</div>
### [`getQualifiedElementOrCallableRef`](get-qualified-element-or-callable-ref.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="get-qualified-element-or-callable-ref.html"><span class="nf">getQualifiedElementOrCallableRef</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Like [`getQualifiedElement`](get-qualified-element.md), but also returns the enclosing [`KtCallableReferenceExpression`](../org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.md) when this name is its callable reference.


</div>

</div>
### [`getQualifiedElementSelector`](get-qualified-element-selector.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="get-qualified-element-selector.html"><span class="nf">getQualifiedElementSelector</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the rightmost selector of this qualified element, or `null` if there is no such selector.


</div>

</div>
### [`getQualifiedExpressionForReceiver`](get-qualified-expression-for-receiver.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="get-qualified-expression-for-receiver.html"><span class="nf">getQualifiedExpressionForReceiver</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the qualified expression in which this expression is the receiver, or `null` if it is not a receiver.


</div>

</div>
### [`getQualifiedExpressionForReceiverOrThis`](get-qualified-expression-for-receiver-or-this.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="get-qualified-expression-for-receiver-or-this.html"><span class="nf">getQualifiedExpressionForReceiverOrThis</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the qualified expression in which this expression is the receiver, or this expression itself otherwise.


</div>

</div>
### [`getQualifiedExpressionForSelector`](get-qualified-expression-for-selector.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="get-qualified-expression-for-selector.html"><span class="nf">getQualifiedExpressionForSelector</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the qualified expression in which this element is the selector, or `null` if it is not a selector.


</div>

</div>
### [`getQualifiedExpressionForSelectorOrThis`](get-qualified-expression-for-selector-or-this.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="get-qualified-expression-for-selector-or-this.html"><span class="nf">getQualifiedExpressionForSelectorOrThis</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the qualified expression in which this expression is the selector, or this expression itself otherwise.


</div>

</div>
### [`getReceiverExpression`](get-receiver-expression.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="get-receiver-expression.html"><span class="nf">getReceiverExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the receiver this name is applied to, considering qualified expressions, binary/unary operators, and qualified user types, or `null` if this name has no receiver.


</div>

</div>
### [`getStartOffsetIn`](get-start-offset-in.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="get-start-offset-in.html"><span class="nf">getStartOffsetIn</span></a><span class="p">(</span>ancestor<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the offset of this element relative to the start of [`ancestor`](get-start-offset-in.md) (which must be an ancestor of this element).


</div>

</div>
### [`getStrictParentOfType`](get-strict-parent-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="get-strict-parent-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-strict-parent-of-type.html"><span class="nf">getStrictParentOfType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="get-strict-parent-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest strict ancestor of type [`T`](get-strict-parent-of-type.md), or `null` if there is none.


</div>

</div>
### [`getSuperNames`](get-super-names.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>StubBasedPsiElementBase<span class="o"><</span><span class="kd">out </span><a href="../org.jetbrains.kotlin.psi.stubs/-kotlin-class-or-object-stub/index.html">KotlinClassOrObjectStub</a><span class="o"><</span><span class="kd">out </span><a href="../org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="o">></span><span class="o">></span><span class="p">.</span><a href="get-super-names.html"><span class="nf">getSuperNames</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the unqualified names indexed as this class's superclass names. For names that might be imported through an alias, this includes both the original and aliased names; reference resolution during inheritor search disambiguates them.


</div>

</div>
### [`getTextWithLocation`](get-text-with-location.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="get-text-with-location.html"><span class="nf">getTextWithLocation</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns this element's text together with its source location, for use in diagnostics and log messages.


</div>

</div>
### [`getTopmostParentOfType`](get-topmost-parent-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="get-topmost-parent-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-topmost-parent-of-type.html"><span class="nf">getTopmostParentOfType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="get-topmost-parent-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the outermost ancestor of type [`T`](get-topmost-parent-of-type.md) including this element, or `null` if there is none.


</div>

</div>
### [`getTopmostParentQualifiedExpressionForSelector`](get-topmost-parent-qualified-expression-for-selector.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="get-topmost-parent-qualified-expression-for-selector.html"><span class="nf">getTopmostParentQualifiedExpressionForSelector</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the outermost qualified expression in which this name is (transitively) the selector, or `null`.


</div>

</div>
### [`getTrailingCommaByClosingElement`](get-trailing-comma-by-closing-element.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="get-trailing-comma-by-closing-element.html"><span class="nf">getTrailingCommaByClosingElement</span></a><span class="p">(</span>closingElement<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the trailing comma immediately before [`closingElement`](get-trailing-comma-by-closing-element.md) (a closing bracket/parenthesis), or `null`.


</div>

</div>
### [`getTrailingCommaByElementsList`](get-trailing-comma-by-elements-list.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="get-trailing-comma-by-elements-list.html"><span class="nf">getTrailingCommaByElementsList</span></a><span class="p">(</span>elementList<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the trailing comma at the end of [`elementList`](get-trailing-comma-by-elements-list.md) (skipping a trailing comment), or `null` if there is none.


</div>

</div>
### [`getValueParameterList`](get-value-parameter-list.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-named-declaration/index.html">KtNamedDeclaration</a><span class="p">.</span><a href="get-value-parameter-list.html"><span class="nf">getValueParameterList</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-parameter-list/index.html">KtParameterList</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the value parameter list of this declaration (the primary constructor's for a class), or `null`.


</div>

</div>
### [`getValueParameters`](get-value-parameters.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-named-declaration/index.html">KtNamedDeclaration</a><span class="p">.</span><a href="get-value-parameters.html"><span class="nf">getValueParameters</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi/-kt-parameter/index.html">KtParameter</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the value parameters of this declaration (constructor value parameters for a class), or an empty list.


</div>

</div>
### [`hasActualModifier`](has-actual-modifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list/index.html">KtModifierList</a><span class="p">.</span><a href="has-actual-modifier.html"><span class="nf">hasActualModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this modifier list contains the `actual` modifier.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="has-actual-modifier.html"><span class="nf">hasActualModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration has the `actual` modifier.


</div>

</div>
### [`hasBody`](has-body.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="has-body.html"><span class="nf">hasBody</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration is a function or property that defines a body.


</div>

</div>
### [`hasExpectModifier`](has-expect-modifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list/index.html">KtModifierList</a><span class="p">.</span><a href="has-expect-modifier.html"><span class="nf">hasExpectModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this modifier list contains the `expect` modifier.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="has-expect-modifier.html"><span class="nf">hasExpectModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration has the `expect` modifier.


</div>

</div>
### [`hasExternalModifier`](has-external-modifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="has-external-modifier.html"><span class="nf">hasExternalModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration has the `external` modifier.


</div>

</div>
### [`hasFunModifier`](has-fun-modifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list/index.html">KtModifierList</a><span class="p">.</span><a href="has-fun-modifier.html"><span class="nf">hasFunModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this modifier list contains the `fun` modifier (a functional interface).


</div>

</div>
### [`hasInnerModifier`](has-inner-modifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="has-inner-modifier.html"><span class="nf">hasInnerModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration has the `inner` modifier.


</div>

</div>
### [`hasSuspendModifier`](has-suspend-modifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list/index.html">KtModifierList</a><span class="p">.</span><a href="has-suspend-modifier.html"><span class="nf">hasSuspendModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this modifier list contains the `suspend` modifier.


</div>

</div>
### [`hasValueModifier`](has-value-modifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list/index.html">KtModifierList</a><span class="p">.</span><a href="has-value-modifier.html"><span class="nf">hasValueModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this modifier list contains the `value` modifier (a value class).


</div>

</div>
### [`inferClassIdByPsi`](infer-class-id-by-psi.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-constant-expression/index.html">KtConstantExpression</a><span class="p">.</span><a href="infer-class-id-by-psi.html"><span class="nf">inferClassIdByPsi</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>ClassId<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A best-effort way to get the ClassId of this expression's type without semantic resolution.


</div>

</div>
### [`isAbstract`](is-abstract.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-class/index.html">KtClass</a><span class="p">.</span><a href="is-abstract.html"><span class="nf">isAbstract</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this class is abstract, that is, it is an interface or has the `abstract` modifier.


</div>

</div>
### [`isActualDeclaration`](is-actual-declaration.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="is-actual-declaration.html"><span class="nf">isActualDeclaration</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration is `actual`: either it has an explicit `actual` modifier, or it is a constructor of an `actual` annotation, value, or inline class.


</div>

</div>
### [`isAncestor`](is-ancestor.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="o">?</span><span class="p">.</span><a href="is-ancestor.html"><span class="nf">isAncestor</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">, </span>strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element is an ancestor of [`element`](is-ancestor.md). When [`strict`](is-ancestor.md) is `false`, an element is its own ancestor.


</div>

</div>
### [`isCallee`](is-callee.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="is-callee.html"><span class="nf">isCallee</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this expression can be the callee of a call with the same name.


</div>

</div>
### [`isContextualDeclaration`](is-contextual-declaration.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="is-contextual-declaration.html"><span class="nf">isContextualDeclaration</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this callable, class, or object declares at least one legacy context receiver. Named context parameters are ignored.


</div>

</div>
### [`isContractDescriptionCallPsiCheck`](is-contract-description-call-psi-check.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="is-contract-description-call-psi-check.html"><span class="nf">isContractDescriptionCallPsiCheck</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Best-effort PSI check for whether this expression is a `contract { ... }` (or `kotlin.contracts.contract { ... }`) call.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="p">.</span><a href="is-contract-description-call-psi-check.html"><span class="nf">isContractDescriptionCallPsiCheck</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Best-effort PSI check for whether this qualified expression is a `kotlin.contracts.contract { ... }` call.


</div>

</div>
### [`isContractPresentPsiCheck`](is-contract-present-psi-check.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-named-function/index.html">KtNamedFunction</a><span class="p">.</span><a href="is-contract-present-psi-check.html"><span class="nf">isContractPresentPsiCheck</span></a><span class="p">(</span>isAllowedOnMembers<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Best-effort PSI check for whether this function's body begins with a `contract { ... }` call, taking into account whether contracts are allowed on member functions via [`isAllowedOnMembers`](is-contract-present-psi-check.md). `false` is definitive; `true` is not a guarantee.


</div>

</div>
### [`isDotReceiver`](is-dot-receiver.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="is-dot-receiver.html"><span class="nf">isDotReceiver</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this expression is the receiver of an enclosing dot-qualified expression.


</div>

</div>
### [`isDotSelector`](is-dot-selector.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="is-dot-selector.html"><span class="nf">isDotSelector</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this expression is the selector of an enclosing dot-qualified expression.


</div>

</div>
### [`isDoubleColonReceiver`](is-double-colon-receiver.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="is-double-colon-receiver.html"><span class="nf">isDoubleColonReceiver</span></a><span class="p">(</span>expression<span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if [`expression`](is-double-colon-receiver.md) is the receiver of an enclosing `::` (callable reference or class literal) expression.


</div>

</div>
### [`isExpectDeclaration`](is-expect-declaration.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="is-expect-declaration.html"><span class="nf">isExpectDeclaration</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration is `expect`, either directly (via the modifier) or by being contained in an `expect` declaration.


</div>

</div>
### [`isExtensionDeclaration`](is-extension-declaration.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="is-extension-declaration.html"><span class="nf">isExtensionDeclaration</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element is an extension function or property (that is, it declares a receiver).


</div>

</div>
### [`isFirstStatement`](is-first-statement.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="is-first-statement.html"><span class="nf">isFirstStatement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element is the first statement of its enclosing block.


</div>

</div>
### [`isFunctionalExpression`](is-functional-expression.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="is-functional-expression.html"><span class="nf">isFunctionalExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element is an anonymous function, such as the `fun` expression in `val predicate = fun(x: Int): Boolean = x > 0`.


</div>

</div>
### [`isIdentifier`](is-identifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">.</span><a href="is-identifier.html"><span class="nf">isIdentifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks if this string is a valid Kotlin identifier.


</div>

</div>
### [`isImportDirectiveExpression`](is-import-directive-expression.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="is-import-directive-expression.html"><span class="nf">isImportDirectiveExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this name is part of an `import` directive.


</div>

</div>
### [`isInImportDirective`](is-in-import-directive.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="is-in-import-directive.html"><span class="nf">isInImportDirective</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this expression appears inside an `import` directive.


</div>

</div>
### [`isInsideOf`](is-inside-of.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="is-inside-of.html"><span class="nf">isInsideOf</span></a><span class="p">(</span>elements<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/index.html">Iterable</a><span class="o"><</span>PsiElement<span class="o">></span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element lies within, or is equal to, any of the given [`elements`](is-inside-of.md).


</div>

</div>
### [`isLambdaOutsideParentheses`](is-lambda-outside-parentheses.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="is-lambda-outside-parentheses.html"><span class="nf">isLambdaOutsideParentheses</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this expression is a trailing lambda argument written outside the call parentheses.


</div>

</div>
### [`isLegacyContractPresentPsiCheck`](is-legacy-contract-present-psi-check.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration-with-body/index.html">KtDeclarationWithBody</a><span class="p">.</span><a href="is-legacy-contract-present-psi-check.html"><span class="nf">isLegacyContractPresentPsiCheck</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the declaration may have a legacy contract (a contract defined inside the body).


</div>

</div>
### [`isNull`](is-null.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="is-null.html"><span class="nf">isNull</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this expression is the `null` literal. Smart-casts the receiver to [`KtConstantExpression`](../org.jetbrains.kotlin.psi/-kt-constant-expression/index.md) on `true`.


</div>

</div>
### [`isObjectLiteral`](is-object-literal.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">.</span><a href="is-object-literal.html"><span class="nf">isObjectLiteral</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this is the body of an object literal (`object : Foo { ... }`).


</div>

</div>
### [`isPackageDirectiveExpression`](is-package-directive-expression.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="is-package-directive-expression.html"><span class="nf">isPackageDirectiveExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this name is part of a `package` directive.


</div>

</div>
### [`isPlain`](is-plain.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="p">.</span><a href="is-plain.html"><span class="nf">isPlain</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this string consists only of literal text, with no interpolation or escape sequences.


</div>

</div>
### [`isPlainWithEscapes`](is-plain-with-escapes.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="p">.</span><a href="is-plain-with-escapes.html"><span class="nf">isPlainWithEscapes</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this string consists only of literal text and escape sequences, with no interpolation.


</div>

</div>
### [`isPrivate`](is-private.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="is-private.html"><span class="nf">isPrivate</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration has the `private` modifier.


</div>

</div>
### [`isPropertyParameter`](is-property-parameter.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-parameter/index.html">KtParameter</a><span class="p">.</span><a href="is-property-parameter.html"><span class="nf">isPropertyParameter</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this parameter is a primary-constructor `val`/`var` property parameter.


</div>

</div>
### [`isProtected`](is-protected.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="is-protected.html"><span class="nf">isProtected</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration has the `protected` modifier.


</div>

</div>
### [`isSingleQuoted`](is-single-quoted.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="p">.</span><a href="is-single-quoted.html"><span class="nf">isSingleQuoted</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this uses the regular one-character quote delimiter (`"`) rather than a triple-quote delimiter (`"""`).


</div>

</div>
### [`isTopLevelInFileOrScript`](is-top-level-in-file-or-script.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="is-top-level-in-file-or-script.html"><span class="nf">isTopLevelInFileOrScript</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if [`element`](is-top-level-in-file-or-script.md) is a top-level element of a file or a top-level statement of a script.


</div>

</div>
### [`isTopLevelKtOrJavaMember`](is-top-level-kt-or-java-member.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="is-top-level-kt-or-java-member.html"><span class="nf">isTopLevelKtOrJavaMember</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element is a top-level member of a Kotlin file or a top-level Java class.


</div>

</div>
### [`isTypeConstructorReference`](is-type-constructor-reference.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="is-type-constructor-reference.html"><span class="nf">isTypeConstructorReference</span></a><span class="p">(</span>e<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if [`e`](is-type-constructor-reference.md) is the reference expression naming the classifier in a user type.


</div>

</div>
### [`lastBlockStatementOrThis`](last-block-statement-or-this.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="last-block-statement-or-this.html"><span class="nf">lastBlockStatementOrThis</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the last statement if this expression is a block, otherwise this expression itself.


</div>

</div>
### [`leaves`](leaves.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>ASTNode<span class="p">.</span><a href="leaves.html"><span class="nf">leaves</span></a><span class="p">(</span>forward<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>ASTNode<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The leaf nodes following (or preceding, if not [`forward`](leaves.md)) this AST node, as a lazy sequence.


</div>

</div>
### [`modalityModifier`](modality-modifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="modality-modifier.html"><span class="nf">modalityModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the modality modifier token (`abstract`/`open`/`final`/`sealed`), or `null` if none is present.


</div>

</div>
### [`modalityModifierType`](modality-modifier-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="modality-modifier-type.html"><span class="nf">modalityModifierType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the type of this declaration's modality modifier, or `null` if none is present.


</div>

</div>
### [`nextLeaf`](next-leaf.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="next-leaf.html"><span class="nf">nextLeaf</span></a><span class="p">(</span>skipEmptyElements<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the next leaf element in the tree, or `null` if there is none. Empty leaves are skipped if [`skipEmptyElements`](next-leaf.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="next-leaf.html"><span class="nf">nextLeaf</span></a><span class="p">(</span>filter<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest following leaf that satisfies [`filter`](next-leaf.md), or `null` if there is none.


</div>

</div>
### [`nextSiblingOfSameType`](next-sibling-of-same-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="next-sibling-of-same-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span><a href="next-sibling-of-same-type.html">T</a><span class="p">.</span><a href="next-sibling-of-same-type.html"><span class="nf">nextSiblingOfSameType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="next-sibling-of-same-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the next sibling of the same type [`T`](next-sibling-of-same-type.md), or `null` if there is none.


</div>

</div>
### [`nonStaticOuterClasses`](non-static-outer-classes.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="non-static-outer-classes.html"><span class="nf">nonStaticOuterClasses</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi/-kt-class/index.html">KtClass</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the enclosing classes that this element can access an outer instance of, from innermost to outermost.


</div>

</div>
### [`parameterIndex`](parameter-index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="parameter-index.html"><span class="nf">parameterIndex</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the index of this parameter within its own parameter list (Kotlin or Java), or `-1` if it is not a parameter.


</div>

</div>
### [`parents`](parents.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>ASTNode<span class="p">.</span><a href="parents.html"><span class="nf">parents</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>ASTNode<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The ancestor nodes of this AST node, from its parent upward, as a lazy sequence.


</div>

</div>
### [`prevLeaf`](prev-leaf.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="prev-leaf.html"><span class="nf">prevLeaf</span></a><span class="p">(</span>skipEmptyElements<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the previous leaf element in the tree, or `null` if there is none. Empty leaves are skipped if [`skipEmptyElements`](prev-leaf.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="prev-leaf.html"><span class="nf">prevLeaf</span></a><span class="p">(</span>filter<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest preceding leaf that satisfies [`filter`](prev-leaf.md), or `null` if there is none.


</div>

</div>
### [`prevSiblingOfSameType`](prev-sibling-of-same-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="prev-sibling-of-same-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span><a href="prev-sibling-of-same-type.html">T</a><span class="p">.</span><a href="prev-sibling-of-same-type.html"><span class="nf">prevSiblingOfSameType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="prev-sibling-of-same-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the previous sibling of the same type [`T`](prev-sibling-of-same-type.md), or `null` if there is none.


</div>

</div>
### [`quoteIfNeeded`](quote-if-needed.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">.</span><a href="quote-if-needed.html"><span class="nf">quoteIfNeeded</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns this string as-is if it is a valid identifier, otherwise wrapped in backticks.


</div>

</div>
### [`referenceExpression`](reference-expression.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="reference-expression.html"><span class="nf">referenceExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-reference-expression/index.html">KtReferenceExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the reference expression of this expression (the callee for a call), or `null` if it is not a reference.


</div>

</div>
### [`safeFqNameForLazyResolve`](safe-fq-name-for-lazy-resolve.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-named-declaration/index.html">KtNamedDeclaration</a><span class="p">.</span><a href="safe-fq-name-for-lazy-resolve.html"><span class="nf">safeFqNameForLazyResolve</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>FqName<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns this declaration's fully qualified name using the safe name for lazy resolution, or `null` if unavailable.


</div>

</div>
### [`safeNameForLazyResolve`](safe-name-for-lazy-resolve.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Name<span class="o">?</span><span class="p">.</span><a href="safe-name-for-lazy-resolve.html"><span class="nf">safeNameForLazyResolve</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>Name
</span></code></pre></div>
</div>


<div markdown>

Returns this name, or the "no name provided" special name if it is `null` or special.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-named-declaration/index.html">KtNamedDeclaration</a><span class="p">.</span><a href="safe-name-for-lazy-resolve.html"><span class="nf">safeNameForLazyResolve</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>Name
</span></code></pre></div>
</div>


<div markdown>

Returns this declaration's name, substituting the "no name provided" special name for a missing or special name.


</div>

</div>
### [`siblings`](siblings.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>ASTNode<span class="p">.</span><a href="siblings.html"><span class="nf">siblings</span></a><span class="p">(</span>forward<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>ASTNode<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The sibling nodes of this AST node, going [`forward`](siblings.md) (or backward), as a lazy sequence.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="siblings.html"><span class="nf">siblings</span></a><span class="p">(</span>forward<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">, </span>withItself<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the siblings of this element as a lazy sequence, going [`forward`](siblings.md) (or backward) and optionally including the element itself ([`withItself`](siblings.md)).


</div>

</div>
### [`startsWithComment`](starts-with-comment.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="starts-with-comment.html"><span class="nf">startsWithComment</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element's first child is a comment.


</div>

</div>
### [`topParenthesizedParentOrMe`](top-parenthesized-parent-or-me.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="top-parenthesized-parent-or-me.html"><span class="nf">topParenthesizedParentOrMe</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the outermost enclosing expression that this expression is wrapped in only through parentheses, or this expression itself.


</div>

</div>
### [`tryFlattenStringConcatenationArguments`](try-flatten-string-concatenation-arguments.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-binary-expression/index.html">KtBinaryExpression</a><span class="p">.</span><a href="try-flatten-string-concatenation-arguments.html"><span class="nf">tryFlattenStringConcatenationArguments</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the string-template arguments of this expression if it is a string-literal concatenation; otherwise, returns `null`.


</div>

</div>
### [`tryFlattenStringConcatenationDescendants`](try-flatten-string-concatenation-descendants.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-binary-expression/index.html">KtBinaryExpression</a><span class="p">.</span><a href="try-flatten-string-concatenation-descendants.html"><span class="nf">tryFlattenStringConcatenationDescendants</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>PsiElement<span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns all descendants of this expression in flattened form if it is a string-literal concatenation; otherwise, returns `null`.


</div>

</div>
### [`unwrapNullability`](unwrap-nullability.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">tailrec </span><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-type-element/index.html">KtTypeElement</a><span class="p">.</span><a href="unwrap-nullability.html"><span class="nf">unwrapNullability</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-type-element/index.html">KtTypeElement</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns this type after stripping all outer [`KtNullableType`](../org.jetbrains.kotlin.psi/-kt-nullable-type/index.md) layers. Returns `null` only if a nullable-type node is malformed and has no inner type.


</div>

</div>
### [`unwrapParenthesesLabelsAndAnnotations`](unwrap-parentheses-labels-and-annotations.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="o">?</span><span class="p">.</span><a href="unwrap-parentheses-labels-and-annotations.html"><span class="nf">unwrapParenthesesLabelsAndAnnotations</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Recursively unwraps this element while it is a parenthesized, labeled, or annotated expression, returning the innermost base element. A non-wrapper element is returned unchanged.


</div>

</div>
### [`unwrapParenthesesLabelsAndAnnotationsDeeply`](unwrap-parentheses-labels-and-annotations-deeply.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="unwrap-parentheses-labels-and-annotations-deeply.html"><span class="nf">unwrapParenthesesLabelsAndAnnotationsDeeply</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Walks up through immediately enclosing parentheses, labels, and annotations, returning the first parent outside that wrapper chain.


</div>

</div>
### [`visibilityModifier`](visibility-modifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list/index.html">KtModifierList</a><span class="p">.</span><a href="visibility-modifier.html"><span class="nf">visibilityModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the visibility modifier token (`public`/`private`/`protected`/`internal`), or `null` if none is present.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="visibility-modifier.html"><span class="nf">visibilityModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the visibility modifier token of this declaration, or `null` if none is present.


</div>

</div>
### [`visibilityModifierType`](visibility-modifier-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list/index.html">KtModifierList</a><span class="p">.</span><a href="visibility-modifier-type.html"><span class="nf">visibilityModifierType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the type of the visibility modifier, or `null` if none is present.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="visibility-modifier-type.html"><span class="nf">visibilityModifierType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the type of this declaration's visibility modifier, or `null` if none is present.


</div>

</div>
### [`visibilityModifierTypeOrDefault`](visibility-modifier-type-or-default.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="visibility-modifier-type-or-default.html"><span class="nf">visibilityModifierTypeOrDefault</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the type of this declaration's visibility modifier, or the default visibility (`public`) if none is present.


</div>

</div>
