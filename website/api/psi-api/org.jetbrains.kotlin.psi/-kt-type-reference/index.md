---
tags:
 - jvm
title: "KtTypeReference"
---

# KtTypeReference

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KtTypeReference</a> : <a href="../-kt-modifier-list-owner-stub/index.html">KtModifierListOwnerStub</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="index.html">KtTypeReference</a><span class="o">></span><span class="o">> </span>, <a href="../-kt-annotated/index.html">KtAnnotated</a>, <a href="../-kt-annotations-container/index.html">KtAnnotationsContainer</a>, <a href="../../org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a>
</span></code></pre></div>Represents a type reference.

### Example:
```kotlin
val x: String = ""
//     ^____^
```


</div>

## Constructors
### KtTypeReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>node<span class="o">: </span>ASTNode<span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>stub<span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="index.html">KtTypeReference</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Properties
### [`allChildren`](../../org.jetbrains.kotlin.psi.psiUtil/all-children.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/all-children.html">allChildren</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/-psi-child-range/index.html">PsiChildRange</a>
</span></code></pre></div>
</div>


<div markdown>

The range of all direct children of this element, or an empty range if it has none.


</div>

</div>
### [`allModifierLists`](index.md#allmodifierlists)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#allmodifierlists">allModifierLists</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-kt-declaration-modifier-list/index.html">KtDeclarationModifierList</a><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### annotationEntries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#annotationentries">annotationEntries</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### annotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#annotations">annotations</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-kt-annotation/index.html">KtAnnotation</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`children`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#children)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#children">children</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`containingFile`](index.md#containingfile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#containingfile">containingFile</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiFile
</span></code></pre></div>
</div>

</div>
### [`containingKtFile`](index.md#containingktfile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#containingktfile">containingKtFile</a><span class="o">: </span><a href="../-kt-file/index.html">KtFile</a>
</span></code></pre></div>
</div>

</div>
### [`context`](index.md#context)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#context">context</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`elementType`](index.md#elementtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#elementtype">elementType</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IStubElementType<span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`endOffset`](../../org.jetbrains.kotlin.psi.psiUtil/end-offset.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/end-offset.html">endOffset</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

The offset just past the end of this element's text range in the file.


</div>

</div>
### [`firstChild`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#firstchild)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#firstchild">firstChild</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`greenStub`](index.md#greenstub)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">Nullable</span>
<span class="kd">override </span><span class="kd">val </span><a href="index.html#greenstub">greenStub</a><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="../../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="index.html">KtTypeReference</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`iElementType`](index.md#ielementtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#ielementtype">iElementType</a><span class="o">: </span>IElementType<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`isPhysical`](index.md#isphysical)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#isphysical">isPhysical</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### isPlaceholder

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#isplaceholder">isPlaceholder</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

`true` if this reference is the underscore placeholder type `_` (used, for example, in partially specified generic type arguments where the rest is inferred).


</div>

</div>
### [`isPublic`](../../org.jetbrains.kotlin.psi.psiUtil/is-public.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-public.html">isPublic</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

`true` if this declaration is effectively public (no visibility modifier or an explicit `public`), and not local.


</div>

</div>
### [`isUserDataEmpty`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#isuserdataempty)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#isuserdataempty">isUserDataEmpty</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isValid`](index.md#isvalid)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#isvalid">isValid</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isWritable`](index.md#iswritable)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#iswritable">isWritable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`language`](index.md#language)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#language">language</a><span class="o">: </span>Language
</span></code></pre></div>
</div>

</div>
### [`lastChild`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#lastchild)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#lastchild">lastChild</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`manager`](index.md#manager)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#manager">manager</a><span class="o">: </span>PsiManagerEx<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`modifierList`](index.md#modifierlist)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#modifierlist">modifierList</a><span class="o">: </span><a href="../-kt-modifier-list/index.html">KtModifierList</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`name`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`navigationElement`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#navigationelement)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#navigationelement">navigationElement</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement
</span></code></pre></div>
</div>

</div>
### [`nextLeafs`](../../org.jetbrains.kotlin.psi.psiUtil/next-leafs.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/next-leafs.html">nextLeafs</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The following leaf elements as a lazy sequence, nearest first.


</div>

</div>
### [`nextSibling`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#nextsibling)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#nextsibling">nextSibling</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`node`](index.md#node)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">var </span><a href="index.html#node">node</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ASTNode
</span></code></pre></div>
</div>

</div>
### [`originalElement`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#originalelement)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#originalelement">originalElement</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`ownDeclarations`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#owndeclarations)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html#owndeclarations">ownDeclarations</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><span class="kd">out </span><span class="se">@</span><span class="se">NotNull</span> PsiSymbolDeclaration<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`ownReferences`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#ownreferences)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html#ownreferences">ownReferences</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><span class="kd">out </span><span class="se">@</span><span class="se">NotNull</span> PsiSymbolReference<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`parent`](index.md#parent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#parent">parent</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`parents`](../../org.jetbrains.kotlin.psi.psiUtil/parents.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/parents.html">parents</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The ancestors of this element, from its immediate parent up to and including the containing file.


</div>

</div>
### [`parentsWithSelf`](../../org.jetbrains.kotlin.psi.psiUtil/parents-with-self.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/parents-with-self.html">parentsWithSelf</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

This element and its ancestors, from the element itself up to and including the containing file.


</div>

</div>
### [`presentation`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#presentation)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#presentation">presentation</a><span class="o">: </span>ItemPresentation<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`prevLeafs`](../../org.jetbrains.kotlin.psi.psiUtil/prev-leafs.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/prev-leafs.html">prevLeafs</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The preceding leaf elements as a lazy sequence, nearest first.


</div>

</div>
### [`prevSibling`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#prevsibling)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#prevsibling">prevSibling</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`project`](index.md#project)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#project">project</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Project
</span></code></pre></div>
</div>

</div>
### [`psiOrParent`](index.md#psiorparent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#psiorparent">psiOrParent</a><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>

</div>
### [`pureEndOffset`](../../org.jetbrains.kotlin.psi.psiUtil/pure-end-offset.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-kt-pure-element/index.html">KtPureElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/pure-end-offset.html">pureEndOffset</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

The end offset of this element's source.


</div>

</div>
### [`pureStartOffset`](../../org.jetbrains.kotlin.psi.psiUtil/pure-start-offset.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-kt-pure-element/index.html">KtPureElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/pure-start-offset.html">pureStartOffset</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

The start offset of this element's source, excluding any leading comments.


</div>

</div>
### [`reference`](index.md#reference)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#reference">reference</a><span class="o">: </span>PsiReference<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`references`](index.md#references)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#references">references</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span>PsiReference<span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`resolveScope`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#resolvescope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#resolvescope">resolveScope</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> GlobalSearchScope
</span></code></pre></div>
</div>

</div>
### [`startOffset`](../../org.jetbrains.kotlin.psi.psiUtil/start-offset.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/start-offset.html">startOffset</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

The offset of the start of this element's text range in the file.


</div>

</div>
### [`startOffsetInParent`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#startoffsetinparent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#startoffsetinparent">startOffsetInParent</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`startOffsetSkippingComments`](../../org.jetbrains.kotlin.psi.psiUtil/start-offset-skipping-comments.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/start-offset-skipping-comments.html">startOffsetSkippingComments</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

The start offset of this element, skipping leading comments and the whitespace that follows them.


</div>

</div>
### [`stub`](index.md#stub)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#stub">stub</a><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="../../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="index.html">KtTypeReference</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`text`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#text)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#text">text</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`textLength`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#textlength)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#textlength">textLength</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`textOffset`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#textoffset)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#textoffset">textOffset</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`textRange`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#textrange)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#textrange">textRange</a><span class="o">: </span>TextRange<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`textRangeInParent`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#textrangeinparent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">Contract</span><span class="p">(</span>pure<span class="o"> = </span><span class="kc">true</span><span class="p">)</span>
<span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html#textrangeinparent">textRangeInParent</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> TextRange
</span></code></pre></div>
</div>

</div>
### [`textRangeWithoutComments`](../../org.jetbrains.kotlin.psi.psiUtil/text-range-without-comments.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/text-range-without-comments.html">textRangeWithoutComments</a><span class="o">: </span>TextRange
</span></code></pre></div>
</div>


<div markdown>

The text range of this element excluding any leading comments.


</div>

</div>
### typeElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#typeelement">typeElement</a><span class="o">: </span><a href="../-kt-type-element/index.html">KtTypeElement</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The actual type syntax this reference wraps (for example, a [`KtUserType`](../-kt-user-type/index.md) or a [`KtFunctionType`](../-kt-function-type/index.md)), stripped of leading annotations and modifiers, or `null` if it is absent in incomplete code.


</div>

</div>
### [`userDataString`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#userdatastring)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">TestOnly</span>
<span class="kd">open </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#userdatastring">userDataString</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`userMap`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#usermap)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">var </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#usermap">userMap</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> KeyFMap
</span></code></pre></div>
</div>

</div>
### [`useScope`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#usescope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#usescope">useScope</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> SearchScope
</span></code></pre></div>
</div>

</div>
## Functions
### [`accept`](index.md#accept)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#accept"><span class="nf">accept</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> visitor<span class="o">: </span>PsiElementVisitor<span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#accept">R</a><span class="p">, </span><a href="index.html#accept">D</a><span class="o">> </span><a href="index.html#accept"><span class="nf">accept</span></a><span class="p">(</span>visitor<span class="o">: </span><a href="../-kt-visitor/index.html">KtVisitor</a><span class="o"><</span><a href="index.html#accept">R</a><span class="p">, </span><a href="index.html#accept">D</a><span class="o">></span><span class="p">, </span>data<span class="o">: </span><a href="index.html#accept">D</a><span class="p">)</span><span class="o">: </span><a href="index.html#accept">R</a>
</span></code></pre></div>
</div>


<div markdown>

Dispatches this element to the corresponding `visit*` method of the given [`visitor`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#accept) and returns its result.


</div>

</div>
### [`acceptChildren`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#acceptchildren)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#acceptchildren"><span class="nf">acceptChildren</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> visitor<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElementVisitor<span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#acceptchildren">D</a><span class="o">> </span><a href="index.html#acceptchildren"><span class="nf">acceptChildren</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> visitor<span class="o">: </span><a href="../-kt-visitor/index.html">KtVisitor</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a><span class="p">, </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/accept-children.html">D</a><span class="o">></span><span class="p">, </span>data<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/accept-children.html">D</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Passes each direct child of this element to the given [`visitor`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#acceptchildren).


</div>

</div>
### [`add`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#add)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#add"><span class="nf">add</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`addAfter`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#addafter)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#addafter"><span class="nf">addAfter</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">, </span>anchor<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`addBefore`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#addbefore)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#addbefore"><span class="nf">addBefore</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">, </span>anchor<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`addInternal`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#addinternal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#addinternal"><span class="nf">addInternal</span></a><span class="p">(</span>
    first<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ASTNode<span class="p">, </span>
    last<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ASTNode<span class="p">, </span>
    anchor<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> ASTNode<span class="o">?</span><span class="p">, </span>
    before<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">?</span>
<span class="p">)</span><span class="o">: </span>ASTNode<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`addRange`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#addrange)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#addrange"><span class="nf">addRange</span></a><span class="p">(</span>first<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">, </span>last<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`addRangeAfter`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#addrangeafter)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#addrangeafter"><span class="nf">addRangeAfter</span></a><span class="p">(</span>
    first<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">, </span>
    last<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">, </span>
    anchor<span class="o">: </span>PsiElement<span class="o">?</span>
<span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`addRangeBefore`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#addrangebefore)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#addrangebefore"><span class="nf">addRangeBefore</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NotNull</span> first<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">, </span>
    <span class="se">@</span><span class="se">NotNull</span> last<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">, </span>
    anchor<span class="o">: </span>PsiElement<span class="o">?</span>
<span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`anyDescendantOfType`](../../org.jetbrains.kotlin.psi.psiUtil/any-descendant-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/any-descendant-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/any-descendant-of-type.html"><span class="nf">anyDescendantOfType</span></a><span class="p">(</span><span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/any-descendant-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element or any descendant of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/any-descendant-of-type.md) satisfies [`predicate`](../../org.jetbrains.kotlin.psi.psiUtil/any-descendant-of-type.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/any-descendant-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/any-descendant-of-type.html"><span class="nf">anyDescendantOfType</span></a><span class="p">(</span><span class="kd">crossinline </span>canGoInside<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span><span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/any-descendant-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element or any descendant of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/any-descendant-of-type.md) satisfies [`predicate`](../../org.jetbrains.kotlin.psi.psiUtil/any-descendant-of-type.md). [`canGoInside`](../../org.jetbrains.kotlin.psi.psiUtil/any-descendant-of-type.md) controls traversal into children but does not prevent the current element from being tested.


</div>

</div>
### [`before`](../../org.jetbrains.kotlin.psi.psiUtil/before.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/before.html"><span class="nf">before</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element ends at or before [`element`](../../org.jetbrains.kotlin.psi.psiUtil/before.md) starts (that is, it precedes [`element`](../../org.jetbrains.kotlin.psi.psiUtil/before.md) in the file).


</div>

</div>
### [`blockExpressionsOrSingle`](../../org.jetbrains.kotlin.psi.psiUtil/block-expressions-or-single.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-element/index.html">KtElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/block-expressions-or-single.html"><span class="nf">blockExpressionsOrSingle</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-kt-element/index.html">KtElement</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the statements of this element if it is a block, otherwise a single-element sequence of this element.


</div>

</div>
### [`canNavigate`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#cannavigate)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#cannavigate"><span class="nf">canNavigate</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`canNavigateToSource`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#cannavigatetosource)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#cannavigatetosource"><span class="nf">canNavigateToSource</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`checkAdd`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#checkadd)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#checkadd"><span class="nf">checkAdd</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`checkDecompiledText`](../../org.jetbrains.kotlin.psi.psiUtil/check-decompiled-text.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/check-decompiled-text.html"><span class="nf">checkDecompiledText</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Throws if this element belongs to a compiled file that is backed by a stub. Loading decompiled text is slow and should be avoided; stubs should be used instead. Called by the descendant-traversal helpers as a guard.


</div>

</div>
### [`checkDelete`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#checkdelete)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#checkdelete"><span class="nf">checkDelete</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`collectAnnotationEntriesFromStubOrPsi`](../../org.jetbrains.kotlin.psi.psiUtil/collect-annotation-entries-from-stub-or-psi.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-annotations-container/index.html">KtAnnotationsContainer</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-annotation-entries-from-stub-or-psi.html"><span class="nf">collectAnnotationEntriesFromStubOrPsi</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Collects the annotation entries of this container, reading from the stub when available and falling back to the PSI.


</div>

</div>
### [`collectDescendantsOfType`](../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type.html"><span class="nf">collectDescendantsOfType</span></a><span class="p">(</span><span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Collects this element and all descendants of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type.md) satisfying [`predicate`](../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type.md) into a list in post-order.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type.html"><span class="nf">collectDescendantsOfType</span></a><span class="p">(</span><span class="kd">crossinline </span>canGoInside<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span><span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Collects this element and all descendants of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type.md) satisfying [`predicate`](../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type.md) into a list in post-order. [`canGoInside`](../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type.md) controls traversal into children but does not prevent the current element from being collected.


</div>

</div>
### [`collectDescendantsOfTypeTo`](../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type-to.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type-to.html">T</a><span class="o"> : </span>PsiElement<span class="p">, </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type-to.html">C</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-collection/index.html">MutableCollection</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type-to.html">T</a><span class="o">></span><span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type-to.html"><span class="nf">collectDescendantsOfTypeTo</span></a><span class="p">(</span>
    to<span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type-to.html">C</a><span class="p">, </span>
    <span class="kd">crossinline </span>canGoInside<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type-to.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }
<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type-to.html">C</a>
</span></code></pre></div>
</div>


<div markdown>

Adds this element and all descendants of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type-to.md) satisfying [`predicate`](../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type-to.md) to [`to`](../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type-to.md) in post-order. [`canGoInside`](../../org.jetbrains.kotlin.psi.psiUtil/collect-descendants-of-type-to.md) controls traversal into children but does not prevent the current element from being added.


</div>

</div>
### [`containingClass`](../../org.jetbrains.kotlin.psi.psiUtil/containing-class.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-element/index.html">KtElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/containing-class.html"><span class="nf">containingClass</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-class/index.html">KtClass</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest enclosing [`KtClass`](../-kt-class/index.md), or `null` if there is none.


</div>

</div>
### [`copy`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#copy)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#copy"><span class="nf">copy</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`copyCopyableDataTo`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#copycopyabledatato)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#copycopyabledatato"><span class="nf">copyCopyableDataTo</span></a><span class="p">(</span>clone<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> UserDataHolderBase<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`copyUserDataTo`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#copyuserdatato)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#copyuserdatato"><span class="nf">copyUserDataTo</span></a><span class="p">(</span>other<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> UserDataHolderBase<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### delete

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#delete"><span class="nf">delete</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Deletes this element. 

 When [`KtPsiMutationService`](../-kt-psi-mutation-service/index.md) is registered, as in the IntelliJ Kotlin plugin, the deletion may also adjust the surrounding code, e.g., delete a semicolon that follows the element. Without the service, it performs only the plain platform deletion.


</div>

</div>
### [`deleteChildInternal`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#deletechildinternal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#deletechildinternal"><span class="nf">deleteChildInternal</span></a><span class="p">(</span>child<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ASTNode<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`deleteChildRange`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#deletechildrange)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#deletechildrange"><span class="nf">deleteChildRange</span></a><span class="p">(</span>first<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">, </span>last<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`findDescendantOfType`](../../org.jetbrains.kotlin.psi.psiUtil/find-descendant-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/find-descendant-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/find-descendant-of-type.html"><span class="nf">findDescendantOfType</span></a><span class="p">(</span><span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/find-descendant-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/find-descendant-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the first element of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/find-descendant-of-type.md) in a pre-order traversal of this element and its descendants that satisfies [`predicate`](../../org.jetbrains.kotlin.psi.psiUtil/find-descendant-of-type.md), or `null` if there is none.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/find-descendant-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/find-descendant-of-type.html"><span class="nf">findDescendantOfType</span></a><span class="p">(</span><span class="kd">crossinline </span>canGoInside<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span><span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/find-descendant-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/find-descendant-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the first element of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/find-descendant-of-type.md) in a pre-order traversal of this element and its descendants that satisfies [`predicate`](../../org.jetbrains.kotlin.psi.psiUtil/find-descendant-of-type.md), or `null`. [`canGoInside`](../../org.jetbrains.kotlin.psi.psiUtil/find-descendant-of-type.md) controls traversal into children but does not prevent the current element from being tested.


</div>

</div>
### [`findElementAt`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#findelementat)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#findelementat"><span class="nf">findElementAt</span></a><span class="p">(</span>offset<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`findReferenceAt`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#findreferenceat)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#findreferenceat"><span class="nf">findReferenceAt</span></a><span class="p">(</span>offset<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span>PsiReference<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`forEachDescendantOfType`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.html"><span class="nf">forEachDescendantOfType</span></a><span class="p">(</span><span class="kd">noinline </span>action<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Applies [`action`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.md) to this element and every descendant of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.md), in post-order (children before parents).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.html"><span class="nf">forEachDescendantOfType</span></a><span class="p">(</span><span class="kd">crossinline </span>canGoInside<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span><span class="kd">noinline </span>action<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Applies [`action`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.md) to this element and every descendant of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.md), in post-order. [`canGoInside`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.md) controls whether each visited element's children are traversed; the element itself is still passed to [`action`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.md) when it is a [`T`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.md), even if [`canGoInside`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type.md) returns `false` for it.


</div>

</div>
### [`forEachDescendantOfTypeInPreorder`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.html"><span class="nf">forEachDescendantOfTypeInPreorder</span></a><span class="p">(</span><span class="kd">noinline </span>action<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Applies [`action`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.md) to this element and every descendant of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.md), in pre-order (parents before children).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.html"><span class="nf">forEachDescendantOfTypeInPreorder</span></a><span class="p">(</span><span class="kd">crossinline </span>canGoInside<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span><span class="kd">noinline </span>action<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Applies [`action`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.md) to this element and every descendant of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.md), in pre-order. [`canGoInside`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.md) controls whether each visited element's children are traversed; the element itself is still passed to [`action`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.md) when it is a [`T`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.md), even if [`canGoInside`](../../org.jetbrains.kotlin.psi.psiUtil/for-each-descendant-of-type-in-preorder.md) returns `false` for it.


</div>

</div>
### getAnnotationEntries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getannotationentries"><span class="nf">getAnnotationEntries</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Retrieves the list of [`KtAnnotationEntry`](../-kt-annotation-entry/index.md) associated with this element. 

 The list may contain directly declared [`KtAnnotationEntry`](../-kt-annotation-entry/index.md) or unwrapped entries from [`KtAnnotation`](../-kt-annotation/index.md). 

** Example: **

```java

    Anno2] @Anno3
    fun foo() {

    }

```

 The list will contain `#!java Anno1`, `#!java Anno2`, and `#!java Anno3`.
</div>

</div>
### getAnnotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getannotations"><span class="nf">getAnnotations</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-kt-annotation/index.html">KtAnnotation</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Retrieves the list of [`KtAnnotation`](../-kt-annotation/index.md) associated with this element. 

Important: this list contains only [`KtAnnotation`](../-kt-annotation/index.md) and not [`KtAnnotationEntry`](../-kt-annotation-entry/index.md).

**See also**



 - [`getAnnotationEntries`](../-kt-type-parameter-list-owner/index.md#getannotationentries)



</div>

</div>
### [`getAssignmentLhsIfUnwrappable`](../../org.jetbrains.kotlin.psi.psiUtil/get-assignment-lhs-if-unwrappable.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-assignment-lhs-if-unwrappable.html"><span class="nf">getAssignmentLhsIfUnwrappable</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the operand this operation applies to, but only when that operand is wrapped in parentheses, a label, or annotations; returns `null` otherwise.


</div>

</div>
### [`getChildOfType`](../../org.jetbrains.kotlin.psi.psiUtil/get-child-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-child-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-child-of-type.html"><span class="nf">getChildOfType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-child-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the first direct child of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/get-child-of-type.md), or `null` if there is none.


</div>

</div>
### [`getChildren`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getchildren)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getchildren"><span class="nf">getChildren</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`getChildrenOfType`](../../org.jetbrains.kotlin.psi.psiUtil/get-children-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-children-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-children-of-type.html"><span class="nf">getChildrenOfType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-children-of-type.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the direct children of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/get-children-of-type.md), or an empty array if there are none.


</div>

</div>
### [`getContainingFile`](index.md#getcontainingfile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getcontainingfile"><span class="nf">getContainingFile</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiFile
</span></code></pre></div>
</div>

</div>
### getContainingKtFile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getcontainingktfile"><span class="nf">getContainingKtFile</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-file/index.html">KtFile</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KtFile`](../-kt-file/index.md) this element belongs to.


</div>

</div>
### [`getContext`](index.md#getcontext)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getcontext"><span class="nf">getContext</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getCopyableUserData`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getcopyableuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getcopyableuserdata">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getcopyableuserdata"><span class="nf">getCopyableUserData</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/get-copyable-user-data.html">T</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/get-copyable-user-data.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getElementTextWithContext`](../../org.jetbrains.kotlin.psi.psiUtil/get-element-text-with-context.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-element-text-with-context.html"><span class="nf">getElementTextWithContext</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns this element's text with surrounding source context, for use in diagnostics and log messages.


</div>

</div>
### [`getExplicitReceiverOfDotQualified`](../../org.jetbrains.kotlin.psi.psiUtil/get-explicit-receiver-of-dot-qualified.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-explicit-receiver-of-dot-qualified.html"><span class="nf">getExplicitReceiverOfDotQualified</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the source of the explicit receiver if this element is a dot-qualified expression, or `null` otherwise.


</div>

</div>
### [`getFirstChild`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getfirstchild)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getfirstchild"><span class="nf">getFirstChild</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getGreenStub`](index.md#getgreenstub)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">fun </span><a href="index.html#getgreenstub"><span class="nf">getGreenStub</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="../../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="index.html">KtTypeReference</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getIcon`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#geticon)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#geticon"><span class="nf">getIcon</span></a><span class="p">(</span>flags<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="https://docs.oracle.com/javase/8/docs/api/javax/swing/Icon.html">Icon</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### getLanguage

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getlanguage"><span class="nf">getLanguage</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>Language
</span></code></pre></div>
</div>

</div>
### [`getLastChild`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getlastchild)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getlastchild"><span class="nf">getLastChild</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getLastParentOfTypeInRow`](../../org.jetbrains.kotlin.psi.psiUtil/get-last-parent-of-type-in-row.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-last-parent-of-type-in-row.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-last-parent-of-type-in-row.html"><span class="nf">getLastParentOfTypeInRow</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-last-parent-of-type-in-row.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the outermost element in an uninterrupted chain of ancestors of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/get-last-parent-of-type-in-row.md), or `null` if the parent is not a [`T`](../../org.jetbrains.kotlin.psi.psiUtil/get-last-parent-of-type-in-row.md).


</div>

</div>
### [`getLastParentOfTypeInRowWithSelf`](../../org.jetbrains.kotlin.psi.psiUtil/get-last-parent-of-type-in-row-with-self.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-last-parent-of-type-in-row-with-self.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-last-parent-of-type-in-row-with-self.html"><span class="nf">getLastParentOfTypeInRowWithSelf</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-last-parent-of-type-in-row-with-self.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Like [`getLastParentOfTypeInRow`](../../org.jetbrains.kotlin.psi.psiUtil/get-last-parent-of-type-in-row.md), but the chain may start at this element itself.


</div>

</div>
### [`getManager`](index.md#getmanager)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getmanager"><span class="nf">getManager</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiManagerEx<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### getModificationStamp

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-element/index.html">KtElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html#getmodificationstamp"><span class="nf">getModificationStamp</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the modification stamp of the nearest enclosing element that tracks one (a file, a stub-based declaration, or a supertype list). The stamp changes whenever that element's subtree is modified, so it can be used to invalidate caches keyed on this element.


</div>

</div>
### [`getName`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.md#getname)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#getname"><span class="nf">getName</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getNavigationElement`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getnavigationelement)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getnavigationelement"><span class="nf">getNavigationElement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement
</span></code></pre></div>
</div>

</div>
### [`getNextSibling`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getnextsibling)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getnextsibling"><span class="nf">getNextSibling</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getNextSiblingIgnoringWhitespace`](../../org.jetbrains.kotlin.psi.psiUtil/get-next-sibling-ignoring-whitespace.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-next-sibling-ignoring-whitespace.html"><span class="nf">getNextSiblingIgnoringWhitespace</span></a><span class="p">(</span>withItself<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the next sibling that is not whitespace, or `null`. Considers this element if [`withItself`](../../org.jetbrains.kotlin.psi.psiUtil/get-next-sibling-ignoring-whitespace.md).


</div>

</div>
### [`getNextSiblingIgnoringWhitespaceAndComments`](../../org.jetbrains.kotlin.psi.psiUtil/get-next-sibling-ignoring-whitespace-and-comments.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-next-sibling-ignoring-whitespace-and-comments.html"><span class="nf">getNextSiblingIgnoringWhitespaceAndComments</span></a><span class="p">(</span>withItself<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the next sibling that is neither whitespace nor a comment, or `null`. Considers this element if [`withItself`](../../org.jetbrains.kotlin.psi.psiUtil/get-next-sibling-ignoring-whitespace-and-comments.md).


</div>

</div>
### [`getNode`](index.md#getnode)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getnode"><span class="nf">getNode</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ASTNode
</span></code></pre></div>
</div>

</div>
### [`getNonStrictParentOfType`](../../org.jetbrains.kotlin.psi.psiUtil/get-non-strict-parent-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-non-strict-parent-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-non-strict-parent-of-type.html"><span class="nf">getNonStrictParentOfType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-non-strict-parent-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest ancestor of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/get-non-strict-parent-of-type.md) including this element, or `null` if there is none.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-non-strict-parent-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-non-strict-parent-of-type.html"><span class="nf">getNonStrictParentOfType</span></a><span class="p">(</span>parentClass<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-non-strict-parent-of-type.html">T</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-non-strict-parent-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest ancestor of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/get-non-strict-parent-of-type.md) (including this element), or `null` if there is none.


</div>

</div>
### [`getOriginalElement`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getoriginalelement)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getoriginalelement"><span class="nf">getOriginalElement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getOutermostParentContainedIn`](../../org.jetbrains.kotlin.psi.psiUtil/get-outermost-parent-contained-in.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">tailrec </span><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-outermost-parent-contained-in.html"><span class="nf">getOutermostParentContainedIn</span></a><span class="p">(</span>container<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the outermost element on the path from this element that is still strictly contained in [`container`](../../org.jetbrains.kotlin.psi.psiUtil/get-outermost-parent-contained-in.md), or `null`.


</div>

</div>
### [`getParent`](index.md#getparent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getparent"><span class="nf">getParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getParentOfType`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type.html"><span class="nf">getParentOfType</span></a><span class="p">(</span>strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest ancestor of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type.md), or `null`. When [`strict`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type.md) is `false`, this element itself is also considered.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type.html"><span class="nf">getParentOfType</span></a><span class="p">(</span>strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span><span class="kd">vararg </span>stopAt<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><span class="kd">out </span>PsiElement<span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest ancestor of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type.md), stopping the search once an ancestor of any type in [`stopAt`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type.md) is reached, or `null`. When [`strict`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type.md) is `false`, this element itself is also considered.


</div>

</div>
### [`getParentOfTypeAndBranch`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branch.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branch.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branch.html"><span class="nf">getParentOfTypeAndBranch</span></a><span class="p">(</span>strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span><span class="kd">noinline </span>branch<span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branch.html">T</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branch.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Checks the nearest element of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branch.md) and returns it if this element lies within the subtree selected by [`branch`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branch.md). If that candidate's branch does not contain this element, returns `null` without checking higher ancestors. When [`strict`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branch.md) is `false`, this element itself is also considered as the candidate.


</div>

</div>
### [`getParentOfTypeAndBranches`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branches.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branches.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branches.html"><span class="nf">getParentOfTypeAndBranches</span></a><span class="p">(</span>strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span><span class="kd">noinline </span>branches<span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branches.html">T</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/index.html">Iterable</a><span class="o"><</span>PsiElement<span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branches.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Checks the nearest element of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branches.md) and returns it if this element lies within any subtree selected by [`branches`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branches.md). If none of that candidate's branches contain this element, returns `null` without checking higher ancestors. When [`strict`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-type-and-branches.md) is `false`, this element itself is also considered as the candidate.


</div>

</div>
### [`getParentOfTypes`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types.html"><span class="nf">getParentOfTypes</span></a><span class="p">(</span>strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span><span class="kd">vararg </span>parentClasses<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><span class="kd">out </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types.html">T</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest ancestor that is an instance of one of [`parentClasses`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types.md), or `null` if there is none. When [`strict`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types.md) is `false`, this element itself is also considered.


</div>

</div>
### [`getParentOfTypes2`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types2.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types2.html">T</a><span class="o"> : </span>PsiElement<span class="p">, </span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types2.html">V</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types2.html"><span class="nf">getParentOfTypes2</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest strict ancestor that is a [`T`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types2.md) or [`V`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types2.md), or `null` if there is none.


</div>

</div>
### [`getParentOfTypes3`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types3.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types3.html">T</a><span class="o"> : </span>PsiElement<span class="p">, </span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types3.html">V</a><span class="o"> : </span>PsiElement<span class="p">, </span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types3.html">U</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types3.html"><span class="nf">getParentOfTypes3</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest strict ancestor that is a [`T`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types3.md), [`V`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types3.md), or [`U`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types3.md), or `null` if there is none.


</div>

</div>
### [`getParentOfTypesAndPredicate`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types-and-predicate.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types-and-predicate.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types-and-predicate.html"><span class="nf">getParentOfTypesAndPredicate</span></a><span class="p">(</span>
    strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span>
    <span class="kd">vararg </span>parentClasses<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><span class="kd">out </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types-and-predicate.html">T</a><span class="o">></span><span class="p">, </span>
    predicate<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types-and-predicate.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types-and-predicate.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest ancestor that is an instance of one of [`parentClasses`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types-and-predicate.md) and satisfies [`predicate`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types-and-predicate.md), or `null`. When [`parentClasses`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types-and-predicate.md) is empty, any type matches. When [`strict`](../../org.jetbrains.kotlin.psi.psiUtil/get-parent-of-types-and-predicate.md) is `false`, this element itself is also considered.


</div>

</div>
### [`getPresentation`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.md#getpresentation)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#getpresentation"><span class="nf">getPresentation</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>ItemPresentation<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getPrevSibling`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getprevsibling)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getprevsibling"><span class="nf">getPrevSibling</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getPrevSiblingIgnoringWhitespace`](../../org.jetbrains.kotlin.psi.psiUtil/get-prev-sibling-ignoring-whitespace.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-prev-sibling-ignoring-whitespace.html"><span class="nf">getPrevSiblingIgnoringWhitespace</span></a><span class="p">(</span>withItself<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the previous sibling that is not whitespace, or `null`. Considers this element if [`withItself`](../../org.jetbrains.kotlin.psi.psiUtil/get-prev-sibling-ignoring-whitespace.md).


</div>

</div>
### [`getPrevSiblingIgnoringWhitespaceAndComments`](../../org.jetbrains.kotlin.psi.psiUtil/get-prev-sibling-ignoring-whitespace-and-comments.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-prev-sibling-ignoring-whitespace-and-comments.html"><span class="nf">getPrevSiblingIgnoringWhitespaceAndComments</span></a><span class="p">(</span>withItself<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the previous sibling that is neither whitespace nor a comment, or `null`. Considers this element if [`withItself`](../../org.jetbrains.kotlin.psi.psiUtil/get-prev-sibling-ignoring-whitespace-and-comments.md).


</div>

</div>
### [`getProject`](index.md#getproject)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getproject"><span class="nf">getProject</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Project
</span></code></pre></div>
</div>

</div>
### getPsiOrParent

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getpsiorparent"><span class="nf">getPsiOrParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Returns this or parent source element (for synthetic element declarations). Use it only for the purposes of source attribution.


</div>

</div>
### [`getQualifiedElementSelector`](../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-element-selector.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-element/index.html">KtElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-element-selector.html"><span class="nf">getQualifiedElementSelector</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the rightmost selector of this qualified element, or `null` if there is no such selector.


</div>

</div>
### [`getQualifiedExpressionForSelector`](../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-expression-for-selector.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-element/index.html">KtElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-expression-for-selector.html"><span class="nf">getQualifiedExpressionForSelector</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the qualified expression in which this element is the selector, or `null` if it is not a selector.


</div>

</div>
### getReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getreference"><span class="nf">getReference</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiReference
</span></code></pre></div>
</div>

</div>
### getReferences

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getreferences"><span class="nf">getReferences</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>PsiReference<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`getRequiredStubOrPsiChild`](index.md#getrequiredstuborpsichild)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#getrequiredstuborpsichild">S</a><span class="o"> : </span>StubElement<span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span><span class="p">, </span><a href="index.html#getrequiredstuborpsichild">Psi</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="index.html#getrequiredstuborpsichild"><span class="nf">getRequiredStubOrPsiChild</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IStubElementType<span class="o"><</span><a href="index.html#getrequiredstuborpsichild">S</a><span class="o">?</span><span class="p">, </span><a href="index.html#getrequiredstuborpsichild">Psi</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="index.html#getrequiredstuborpsichild">Psi</a><span class="o"> & </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#getrequiredstuborpsichild"><span class="nf">getRequiredStubOrPsiChild</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#getrequiredstuborpsichild">Psi</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="index.html#getrequiredstuborpsichild"><span class="nf">getRequiredStubOrPsiChild</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">, </span>psiClass<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="index.html#getrequiredstuborpsichild">Psi</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="index.html#getrequiredstuborpsichild">Psi</a><span class="o"> & </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>
</span></code></pre></div>
</div>

</div>
### [`getResolveScope`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getresolvescope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getresolvescope"><span class="nf">getResolveScope</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> GlobalSearchScope
</span></code></pre></div>
</div>

</div>
### getShortTypeText

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#getshorttypetext"><span class="nf">getShortTypeText</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns short names presentable text, for `() -> kotlin.Boolean` result would be `() -> Boolean` No decompilation happens if [`KtTypeReference`](index.md) represents compiled code.


</div>

</div>
### [`getStartOffsetIn`](../../org.jetbrains.kotlin.psi.psiUtil/get-start-offset-in.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-start-offset-in.html"><span class="nf">getStartOffsetIn</span></a><span class="p">(</span>ancestor<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the offset of this element relative to the start of [`ancestor`](../../org.jetbrains.kotlin.psi.psiUtil/get-start-offset-in.md) (which must be an ancestor of this element).


</div>

</div>
### [`getStartOffsetInParent`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getstartoffsetinparent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getstartoffsetinparent"><span class="nf">getStartOffsetInParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`getStrictParentOfType`](../../org.jetbrains.kotlin.psi.psiUtil/get-strict-parent-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-strict-parent-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-strict-parent-of-type.html"><span class="nf">getStrictParentOfType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-strict-parent-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest strict ancestor of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/get-strict-parent-of-type.md), or `null` if there is none.


</div>

</div>
### [`getStub`](index.md#getstub)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getstub"><span class="nf">getStub</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="../../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="index.html">KtTypeReference</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getStubOrPsiChild`](index.md#getstuborpsichild)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#getstuborpsichild">Psi</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="index.html#getstuborpsichild"><span class="nf">getStubOrPsiChild</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IStubElementType<span class="o"><</span><span class="kd">out </span>StubElement<span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span><span class="p">, </span><a href="index.html#getstuborpsichild">Psi</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="index.html#getstuborpsichild">Psi</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#getstuborpsichild"><span class="nf">getStubOrPsiChild</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#getstuborpsichild">Psi</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="index.html#getstuborpsichild"><span class="nf">getStubOrPsiChild</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">, </span>psiClass<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="index.html#getstuborpsichild">Psi</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="index.html#getstuborpsichild">Psi</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getStubOrPsiChildren`](index.md#getstuborpsichildren)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#getstuborpsichildren">S</a><span class="o"> : </span>StubElement<span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span><span class="p">, </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="index.html#getstuborpsichildren"><span class="nf">getStubOrPsiChildren</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IStubElementType<span class="o"><</span><a href="index.html#getstuborpsichildren">S</a><span class="o">?</span><span class="p">, </span><span class="kd">out </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o">?</span><span class="o">></span><span class="p">, </span>f<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ArrayFactory<span class="o"><</span><span class="kd">out </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#getstuborpsichildren">S</a><span class="o"> : </span>StubElement<span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span><span class="p">, </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="index.html#getstuborpsichildren"><span class="nf">getStubOrPsiChildren</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IStubElementType<span class="o"><</span><a href="index.html#getstuborpsichildren">S</a><span class="o">?</span><span class="p">, </span><span class="kd">out </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o">?</span><span class="o">></span><span class="p">, </span>array<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#getstuborpsichildren">Psi</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="index.html#getstuborpsichildren"><span class="nf">getStubOrPsiChildren</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">, </span>f<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ArrayFactory<span class="o"><</span><span class="kd">out </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#getstuborpsichildren">Psi</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="index.html#getstuborpsichildren"><span class="nf">getStubOrPsiChildren</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">, </span>array<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#getstuborpsichildren">Psi</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="index.html#getstuborpsichildren"><span class="nf">getStubOrPsiChildren</span></a><span class="p">(</span>filter<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> TokenSet<span class="p">, </span>f<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ArrayFactory<span class="o"><</span><span class="kd">out </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#getstuborpsichildren">Psi</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="index.html#getstuborpsichildren"><span class="nf">getStubOrPsiChildren</span></a><span class="p">(</span>filter<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> TokenSet<span class="p">, </span>array<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="index.html#getstuborpsichildren">Psi</a><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`getSuperNames`](../../org.jetbrains.kotlin.psi.psiUtil/get-super-names.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>StubBasedPsiElementBase<span class="o"><</span><span class="kd">out </span><a href="../../org.jetbrains.kotlin.psi.stubs/-kotlin-class-or-object-stub/index.html">KotlinClassOrObjectStub</a><span class="o"><</span><span class="kd">out </span><a href="../-kt-class-or-object/index.html">KtClassOrObject</a><span class="o">></span><span class="o">></span><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-super-names.html"><span class="nf">getSuperNames</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the unqualified names indexed as this class's superclass names. For names that might be imported through an alias, this includes both the original and aliased names; reference resolution during inheritor search disambiguates them.


</div>

</div>
### [`getText`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#gettext)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#gettext"><span class="nf">getText</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getTextLength`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#gettextlength)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#gettextlength"><span class="nf">getTextLength</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`getTextOffset`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#gettextoffset)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#gettextoffset"><span class="nf">getTextOffset</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`getTextRange`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#gettextrange)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#gettextrange"><span class="nf">getTextRange</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>TextRange<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getTextWithLocation`](../../org.jetbrains.kotlin.psi.psiUtil/get-text-with-location.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-text-with-location.html"><span class="nf">getTextWithLocation</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns this element's text together with its source location, for use in diagnostics and log messages.


</div>

</div>
### [`getTopmostParentOfType`](../../org.jetbrains.kotlin.psi.psiUtil/get-topmost-parent-of-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-topmost-parent-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-topmost-parent-of-type.html"><span class="nf">getTopmostParentOfType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-topmost-parent-of-type.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the outermost ancestor of type [`T`](../../org.jetbrains.kotlin.psi.psiUtil/get-topmost-parent-of-type.md) including this element, or `null` if there is none.


</div>

</div>
### getTypeText

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#gettypetext"><span class="nf">getTypeText</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns fully qualified presentable text for the underlying type based on stubs when provided. No decompilation happens if [`KtTypeReference`](index.md) represents compiled code.


</div>

</div>
### [`getUserData`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getuserdata">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getuserdata"><span class="nf">getUserData</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/get-user-data.html">T</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/get-user-data.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getUseScope`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getusescope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getusescope"><span class="nf">getUseScope</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> SearchScope
</span></code></pre></div>
</div>

</div>
### [`hasActualModifier`](../../org.jetbrains.kotlin.psi.psiUtil/has-actual-modifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/has-actual-modifier.html"><span class="nf">hasActualModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration has the `actual` modifier.


</div>

</div>
### [`hasExpectModifier`](../../org.jetbrains.kotlin.psi.psiUtil/has-expect-modifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/has-expect-modifier.html"><span class="nf">hasExpectModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration has the `expect` modifier.


</div>

</div>
### [`hasExternalModifier`](../../org.jetbrains.kotlin.psi.psiUtil/has-external-modifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/has-external-modifier.html"><span class="nf">hasExternalModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration has the `external` modifier.


</div>

</div>
### [`hasInnerModifier`](../../org.jetbrains.kotlin.psi.psiUtil/has-inner-modifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/has-inner-modifier.html"><span class="nf">hasInnerModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration has the `inner` modifier.


</div>

</div>
### [`hasModifier`](index.md#hasmodifier)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#hasmodifier"><span class="nf">hasModifier</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> modifier<span class="o">: </span><a href="../../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if this element declares the given modifier keyword (for example, [`PRIVATE_KEYWORD`](../../org.jetbrains.kotlin.lexer/-kt-tokens/index.md#private_keyword)).

</div>

</div>
### hasParentheses

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#hasparentheses"><span class="nf">hasParentheses</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this type reference is wrapped in parentheses (as in `(Int) -> String` written as `((Int)) -> String`, or a parenthesized nullable function type).


</div>

</div>
### [`isAncestor`](../../org.jetbrains.kotlin.psi.psiUtil/is-ancestor.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="o">?</span><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-ancestor.html"><span class="nf">isAncestor</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">, </span>strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element is an ancestor of [`element`](../../org.jetbrains.kotlin.psi.psiUtil/is-ancestor.md). When [`strict`](../../org.jetbrains.kotlin.psi.psiUtil/is-ancestor.md) is `false`, an element is its own ancestor.


</div>

</div>
### [`isContextualDeclaration`](../../org.jetbrains.kotlin.psi.psiUtil/is-contextual-declaration.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-element/index.html">KtElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-contextual-declaration.html"><span class="nf">isContextualDeclaration</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this callable, class, or object declares at least one legacy context receiver. Named context parameters are ignored.


</div>

</div>
### [`isCopyableDataEqual`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#iscopyabledataequal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#iscopyabledataequal"><span class="nf">isCopyableDataEqual</span></a><span class="p">(</span>other<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> UserDataHolderBase<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isEquivalentTo`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#isequivalentto)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#isequivalentto"><span class="nf">isEquivalentTo</span></a><span class="p">(</span>another<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isExtensionDeclaration`](../../org.jetbrains.kotlin.psi.psiUtil/is-extension-declaration.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-extension-declaration.html"><span class="nf">isExtensionDeclaration</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element is an extension function or property (that is, it declares a receiver).


</div>

</div>
### [`isFirstStatement`](../../org.jetbrains.kotlin.psi.psiUtil/is-first-statement.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-element/index.html">KtElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-first-statement.html"><span class="nf">isFirstStatement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element is the first statement of its enclosing block.


</div>

</div>
### [`isFunctionalExpression`](../../org.jetbrains.kotlin.psi.psiUtil/is-functional-expression.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-functional-expression.html"><span class="nf">isFunctionalExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element is an anonymous function, such as the `fun` expression in `val predicate = fun(x: Int): Boolean = x > 0`.


</div>

</div>
### [`isInsideOf`](../../org.jetbrains.kotlin.psi.psiUtil/is-inside-of.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-inside-of.html"><span class="nf">isInsideOf</span></a><span class="p">(</span>elements<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/index.html">Iterable</a><span class="o"><</span>PsiElement<span class="o">></span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element lies within, or is equal to, any of the given [`elements`](../../org.jetbrains.kotlin.psi.psiUtil/is-inside-of.md).


</div>

</div>
### [`isPhysical`](index.md#isphysical)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isphysical"><span class="nf">isPhysical</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isPrivate`](../../org.jetbrains.kotlin.psi.psiUtil/is-private.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-private.html"><span class="nf">isPrivate</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration has the `private` modifier.


</div>

</div>
### [`isProtected`](../../org.jetbrains.kotlin.psi.psiUtil/is-protected.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-protected.html"><span class="nf">isProtected</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration has the `protected` modifier.


</div>

</div>
### [`isTopLevelKtOrJavaMember`](../../org.jetbrains.kotlin.psi.psiUtil/is-top-level-kt-or-java-member.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-top-level-kt-or-java-member.html"><span class="nf">isTopLevelKtOrJavaMember</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element is a top-level member of a Kotlin file or a top-level Java class.


</div>

</div>
### [`isValid`](index.md#isvalid)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isvalid"><span class="nf">isValid</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isWritable`](index.md#iswritable)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#iswritable"><span class="nf">isWritable</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### nameForReceiverLabel

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#nameforreceiverlabel"><span class="nf">nameForReceiverLabel</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the short name to use as an implicit label for a receiver of this type (the simple name of the user type), or `null` if the type is not a user type.


</div>

</div>
### [`navigate`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#navigate)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#navigate"><span class="nf">navigate</span></a><span class="p">(</span>requestFocus<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`navigationRequest`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#navigationrequest)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">RequiresReadLock</span>
<span class="se">@</span><span class="se">RequiresBackgroundThread</span>
<span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#navigationrequest"><span class="nf">navigationRequest</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> NavigationRequest<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`nextLeaf`](../../org.jetbrains.kotlin.psi.psiUtil/next-leaf.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/next-leaf.html"><span class="nf">nextLeaf</span></a><span class="p">(</span>skipEmptyElements<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the next leaf element in the tree, or `null` if there is none. Empty leaves are skipped if [`skipEmptyElements`](../../org.jetbrains.kotlin.psi.psiUtil/next-leaf.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/next-leaf.html"><span class="nf">nextLeaf</span></a><span class="p">(</span>filter<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest following leaf that satisfies [`filter`](../../org.jetbrains.kotlin.psi.psiUtil/next-leaf.md), or `null` if there is none.


</div>

</div>
### [`nonStaticOuterClasses`](../../org.jetbrains.kotlin.psi.psiUtil/non-static-outer-classes.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-element/index.html">KtElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/non-static-outer-classes.html"><span class="nf">nonStaticOuterClasses</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-kt-class/index.html">KtClass</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the enclosing classes that this element can access an outer instance of, from innermost to outermost.


</div>

</div>
### [`parameterIndex`](../../org.jetbrains.kotlin.psi.psiUtil/parameter-index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/parameter-index.html"><span class="nf">parameterIndex</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the index of this parameter within its own parameter list (Kotlin or Java), or `-1` if it is not a parameter.


</div>

</div>
### [`prevLeaf`](../../org.jetbrains.kotlin.psi.psiUtil/prev-leaf.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/prev-leaf.html"><span class="nf">prevLeaf</span></a><span class="p">(</span>skipEmptyElements<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the previous leaf element in the tree, or `null` if there is none. Empty leaves are skipped if [`skipEmptyElements`](../../org.jetbrains.kotlin.psi.psiUtil/prev-leaf.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/prev-leaf.html"><span class="nf">prevLeaf</span></a><span class="p">(</span>filter<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest preceding leaf that satisfies [`filter`](../../org.jetbrains.kotlin.psi.psiUtil/prev-leaf.md), or `null` if there is none.


</div>

</div>
### [`processDeclarations`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#processdeclarations)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#processdeclarations"><span class="nf">processDeclarations</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NotNull</span> processor<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiScopeProcessor<span class="p">, </span>
    <span class="se">@</span><span class="se">NotNull</span> state<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ResolveState<span class="p">, </span>
    lastParent<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">, </span>
    <span class="se">@</span><span class="se">NotNull</span> place<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`putCopyableUserData`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#putcopyableuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#putcopyableuserdata">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#putcopyableuserdata"><span class="nf">putCopyableUserData</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/put-copyable-user-data.html">T</a><span class="o">?</span><span class="o">></span><span class="p">, </span>value<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/put-copyable-user-data.html">T</a><span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`putUserData`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#putuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#putuserdata">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#putuserdata"><span class="nf">putUserData</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/put-user-data.html">T</a><span class="o">?</span><span class="o">></span><span class="p">, </span><span class="se">@</span><span class="se">Nullable</span> value<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/put-user-data.html">T</a><span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`putUserDataIfAbsent`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#putuserdataifabsent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#putuserdataifabsent">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#putuserdataifabsent"><span class="nf">putUserDataIfAbsent</span></a><span class="p">(</span>key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#putuserdataifabsent">T</a><span class="o">?</span><span class="o">></span><span class="p">, </span>value<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#putuserdataifabsent">T</a><span class="o"> & </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#putuserdataifabsent">T</a><span class="o"> & </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>
</span></code></pre></div>
</div>

</div>
### rawDelete

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#rawdelete"><span class="nf">rawDelete</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Deletes this PSI element using the raw platform implementation, bypassing Kotlin PSI-specific [`delete`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#delete) overrides.

Regular clients should use [`delete`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#delete) instead. When [`KtPsiMutationService`](../-kt-psi-mutation-service/index.md) is not registered, it performs the same plain deletion, and when the service is registered, as in the IntelliJ Kotlin plugin, it may also adjust the surrounding code, e.g., delete a semicolon that follows the element.


</div>

</div>
### [`replace`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#replace)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#replace"><span class="nf">replace</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> newElement<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#replace">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#replace"><span class="nf">replace</span></a><span class="p">(</span>
    key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#replace">T</a><span class="o">?</span><span class="o">></span><span class="p">, </span>
    oldValue<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#replace">T</a><span class="o">?</span><span class="p">, </span>
    newValue<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#replace">T</a><span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`replaceChildInternal`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#replacechildinternal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#replacechildinternal"><span class="nf">replaceChildInternal</span></a><span class="p">(</span>child<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">, </span>newElement<span class="o">: </span>TreeElement<span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`setSubstrateRef`](index.md#setsubstrateref)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#setsubstrateref"><span class="nf">setSubstrateRef</span></a><span class="p">(</span>substrateRef<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> SubstrateRef<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`siblings`](../../org.jetbrains.kotlin.psi.psiUtil/siblings.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/siblings.html"><span class="nf">siblings</span></a><span class="p">(</span>forward<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">, </span>withItself<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the siblings of this element as a lazy sequence, going [`forward`](../../org.jetbrains.kotlin.psi.psiUtil/siblings.md) (or backward) and optionally including the element itself ([`withItself`](../../org.jetbrains.kotlin.psi.psiUtil/siblings.md)).


</div>

</div>
### [`startsWithComment`](../../org.jetbrains.kotlin.psi.psiUtil/starts-with-comment.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/starts-with-comment.html"><span class="nf">startsWithComment</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this element's first child is a comment.


</div>

</div>
### [`subtreeChanged`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#subtreechanged)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#subtreechanged"><span class="nf">subtreeChanged</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`textContains`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#textcontains)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#textcontains"><span class="nf">textContains</span></a><span class="p">(</span>c<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char/index.html">Char</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`textMatches`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#textmatches)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#textmatches"><span class="nf">textMatches</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> text<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/index.html">CharSequence</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#textmatches"><span class="nf">textMatches</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`textToCharArray`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#texttochararray)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#texttochararray"><span class="nf">textToCharArray</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-array/index.html">CharArray</a>
</span></code></pre></div>
</div>

</div>
### toString

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#tostring"><span class="nf">toString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`unwrapParenthesesLabelsAndAnnotations`](../../org.jetbrains.kotlin.psi.psiUtil/unwrap-parentheses-labels-and-annotations.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="o">?</span><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/unwrap-parentheses-labels-and-annotations.html"><span class="nf">unwrapParenthesesLabelsAndAnnotations</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Recursively unwraps this element while it is a parenthesized, labeled, or annotated expression, returning the innermost base element. A non-wrapper element is returned unchanged.


</div>

</div>
### [`unwrapParenthesesLabelsAndAnnotationsDeeply`](../../org.jetbrains.kotlin.psi.psiUtil/unwrap-parentheses-labels-and-annotations-deeply.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/unwrap-parentheses-labels-and-annotations-deeply.html"><span class="nf">unwrapParenthesesLabelsAndAnnotationsDeeply</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Walks up through immediately enclosing parentheses, labels, and annotations, returning the first parent outside that wrapper chain.


</div>

</div>
### [`visibilityModifier`](../../org.jetbrains.kotlin.psi.psiUtil/visibility-modifier.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/visibility-modifier.html"><span class="nf">visibilityModifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the visibility modifier token of this declaration, or `null` if none is present.


</div>

</div>
### [`visibilityModifierType`](../../org.jetbrains.kotlin.psi.psiUtil/visibility-modifier-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/visibility-modifier-type.html"><span class="nf">visibilityModifierType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the type of this declaration's visibility modifier, or `null` if none is present.


</div>

</div>
### [`visibilityModifierTypeOrDefault`](../../org.jetbrains.kotlin.psi.psiUtil/visibility-modifier-type-or-default.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/visibility-modifier-type-or-default.html"><span class="nf">visibilityModifierTypeOrDefault</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the type of this declaration's visibility modifier, or the default visibility (`public`) if none is present.


</div>

</div>
