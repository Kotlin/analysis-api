---
tags:
 - jvm
title: "KtLabelReferenceExpression"
---

# KtLabelReferenceExpression

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KtLabelReferenceExpression</a> : <a href="../-kt-simple-name-expression-impl/index.html">KtSimpleNameExpressionImpl</a>
</span></code></pre></div>Represents a reference to a label in a labeled expression, such as `@main` in `return@main`.

### Example:
```kotlin
fun main() {
    return@main
//        ^___^
}
```


</div>

## Constructors
### KtLabelReferenceExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>node<span class="o">: </span>ASTNode<span class="p">)</span>
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
### [`children`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#children)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#children">children</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`containingFile`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#containingfile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#containingfile">containingFile</a><span class="o">: </span>PsiFile<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`containingKtFile`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.md#containingktfile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#containingktfile">containingKtFile</a><span class="o">: </span><a href="../-kt-file/index.html">KtFile</a>
</span></code></pre></div>
</div>

</div>
### [`context`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#context)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#context">context</a><span class="o">: </span>PsiElement<span class="o">?</span>
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
### [`isPhysical`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#isphysical)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#isphysical">isPhysical</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isUserDataEmpty`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#isuserdataempty)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#isuserdataempty">isUserDataEmpty</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isValid`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#isvalid)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#isvalid">isValid</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isWritable`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#iswritable)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#iswritable">isWritable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`language`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.md#language)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#language">language</a><span class="o">: </span>Language
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
### [`manager`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#manager)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#manager">manager</a><span class="o">: </span>PsiManagerEx<span class="o">?</span>
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
### [`node`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#node)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#node">node</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ASTNode
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
### [`parent`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#parent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#parent">parent</a><span class="o">: </span>PsiElement<span class="o">?</span>
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
### [`project`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#project)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#project">project</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Project
</span></code></pre></div>
</div>

</div>
### [`psiOrParent`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.md#psiorparent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#psiorparent">psiOrParent</a><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a>
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
### [`reference`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.md#reference)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#reference">reference</a><span class="o">: </span>PsiReference<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`references`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.md#references)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#references">references</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span>PsiReference<span class="o">?</span><span class="o">></span>
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
### [`accept`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.md#accept)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#accept"><span class="nf">accept</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> visitor<span class="o">: </span>PsiElementVisitor<span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><span class="o"><</span><a href="../-kt-simple-name-expression-impl/index.html#accept">R</a><span class="p">, </span><a href="../-kt-simple-name-expression-impl/index.html#accept">D</a><span class="o">> </span><a href="../-kt-simple-name-expression-impl/index.html#accept"><span class="nf">accept</span></a><span class="p">(</span>visitor<span class="o">: </span><a href="../-kt-visitor/index.html">KtVisitor</a><span class="o"><</span><a href="../-kt-simple-name-expression-impl/index.html#accept">R</a><span class="p">, </span><a href="../-kt-simple-name-expression-impl/index.html#accept">D</a><span class="o">></span><span class="p">, </span>data<span class="o">: </span><a href="../-kt-simple-name-expression-impl/index.html#accept">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-simple-name-expression-impl/index.html#accept">R</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#acceptchildren">D</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#acceptchildren"><span class="nf">acceptChildren</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> visitor<span class="o">: </span><a href="../-kt-visitor/index.html">KtVisitor</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a><span class="p">, </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression-impl/accept-children.html">D</a><span class="o">></span><span class="p">, </span>data<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression-impl/accept-children.html">D</a><span class="p">)</span>
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
### [`asAssignment`](../../org.jetbrains.kotlin.psi.psiUtil/as-assignment.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/as-assignment.html"><span class="nf">asAssignment</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-binary-expression/index.html">KtBinaryExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns this expression as a [`KtBinaryExpression`](../-kt-binary-expression/index.md) if it is an assignment, or `null` otherwise.


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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#delete"><span class="nf">delete</span></a><span class="p">(</span><span class="p">)</span>
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
### [`getAnnotationEntries`](../../org.jetbrains.kotlin.psi.psiUtil/get-annotation-entries.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-annotation-entries.html"><span class="nf">getAnnotationEntries</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the annotation entries applied to this expression through an enclosing annotated (or labeled) expression, or an empty list if there are none.


</div>

</div>
### [`getAssignmentByLHS`](../../org.jetbrains.kotlin.psi.psiUtil/get-assignment-by-l-h-s.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-assignment-by-l-h-s.html"><span class="nf">getAssignmentByLHS</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-binary-expression/index.html">KtBinaryExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the assignment in which this expression is the left-hand side, or `null` if it is not assigned to.


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
### [`getBinaryWithTypeParent`](../../org.jetbrains.kotlin.psi.psiUtil/get-binary-with-type-parent.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-binary-with-type-parent.html"><span class="nf">getBinaryWithTypeParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-binary-expression-with-type-r-h-s/index.html">KtBinaryExpressionWithTypeRHS</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the `as`/`as?` expression whose left-hand side is a call with this expression as its direct child, normally its callee. The call may be the selector of a qualified expression, and the call or qualified expression may be parenthesized. Returns `null` otherwise.


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
### [`getContainingFile`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getcontainingfile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getcontainingfile"><span class="nf">getContainingFile</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiFile<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### getContainingKtFile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#getcontainingktfile"><span class="nf">getContainingKtFile</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-file/index.html">KtFile</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KtFile`](../-kt-file/index.md) this element belongs to.


</div>

</div>
### [`getContext`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getcontext)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getcontext"><span class="nf">getContext</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getCopyableUserData`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getcopyableuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getcopyableuserdata">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getcopyableuserdata"><span class="nf">getCopyableUserData</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression-impl/get-copyable-user-data.html">T</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression-impl/get-copyable-user-data.html">T</a><span class="o">?</span>
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
### [`getIcon`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#geticon)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#geticon"><span class="nf">getIcon</span></a><span class="p">(</span>flags<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="https://docs.oracle.com/javase/8/docs/api/javax/swing/Icon.html">Icon</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### getIdentifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="../-kt-simple-name-expression-impl/index.html#getidentifier"><span class="nf">getIdentifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the identifier token of this reference, or `null` if the name is not a plain identifier (for example, an operation sign).


</div>

</div>
### [`getLabeledParent`](../../org.jetbrains.kotlin.psi.psiUtil/get-labeled-parent.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-labeled-parent.html"><span class="nf">getLabeledParent</span></a><span class="p">(</span>labelName<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-labeled-expression/index.html">KtLabeledExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest enclosing labeled expression with the given [`labelName`](../../org.jetbrains.kotlin.psi.psiUtil/get-labeled-parent.md), or `null` if there is none.


</div>

</div>
### getLanguage

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#getlanguage"><span class="nf">getLanguage</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>Language
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
### [`getManager`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getmanager)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getmanager"><span class="nf">getManager</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiManagerEx<span class="o">?</span>
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
### [`getNode`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getnode)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getnode"><span class="nf">getNode</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ASTNode
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
### [`getOutermostParenthesizerOrThis`](../../org.jetbrains.kotlin.psi.psiUtil/get-outermost-parenthesizer-or-this.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-outermost-parenthesizer-or-this.html"><span class="nf">getOutermostParenthesizerOrThis</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the outermost expression that wraps this one only through parentheses, labels, or annotations, or this expression itself.


</div>

</div>
### [`getParent`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getparent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getparent"><span class="nf">getParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
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
### [`getPossiblyQualifiedCallExpression`](../../org.jetbrains.kotlin.psi.psiUtil/get-possibly-qualified-call-expression.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-possibly-qualified-call-expression.html"><span class="nf">getPossiblyQualifiedCallExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-call-expression/index.html">KtCallExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the call expression this expression represents: the selector's call for a qualified expression, or this expression if it is itself a call. Returns `null` if there is no call.


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
### [`getProject`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getproject)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getproject"><span class="nf">getProject</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Project
</span></code></pre></div>
</div>

</div>
### getPsiOrParent

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#getpsiorparent"><span class="nf">getPsiOrParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Returns this or parent source element (for synthetic element declarations). Use it only for the purposes of source attribution.


</div>

</div>
### [`getQualifiedElement`](../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-element.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-element.html"><span class="nf">getQualifiedElement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the enclosing qualified element for this name: a [`KtQualifiedExpression`](../-kt-qualified-expression/index.md), a [`KtUserType`](../-kt-user-type/index.md), or this expression itself if there is no such qualifier.


</div>

</div>
### [`getQualifiedElementOrCallableRef`](../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-element-or-callable-ref.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-element-or-callable-ref.html"><span class="nf">getQualifiedElementOrCallableRef</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Like [`getQualifiedElement`](../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-element.md), but also returns the enclosing [`KtCallableReferenceExpression`](../-kt-callable-reference-expression/index.md) when this name is its callable reference.


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
### [`getQualifiedExpressionForReceiver`](../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-expression-for-receiver.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-expression-for-receiver.html"><span class="nf">getQualifiedExpressionForReceiver</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the qualified expression in which this expression is the receiver, or `null` if it is not a receiver.


</div>

</div>
### [`getQualifiedExpressionForReceiverOrThis`](../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-expression-for-receiver-or-this.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-expression-for-receiver-or-this.html"><span class="nf">getQualifiedExpressionForReceiverOrThis</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the qualified expression in which this expression is the receiver, or this expression itself otherwise.


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
### [`getQualifiedExpressionForSelectorOrThis`](../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-expression-for-selector-or-this.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-qualified-expression-for-selector-or-this.html"><span class="nf">getQualifiedExpressionForSelectorOrThis</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the qualified expression in which this expression is the selector, or this expression itself otherwise.


</div>

</div>
### [`getReceiverExpression`](../../org.jetbrains.kotlin.psi.psiUtil/get-receiver-expression.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-receiver-expression.html"><span class="nf">getReceiverExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the receiver this name is applied to, considering qualified expressions, binary/unary operators, and qualified user types, or `null` if this name has no receiver.


</div>

</div>
### getReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#getreference"><span class="nf">getReference</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiReference
</span></code></pre></div>
</div>

</div>
### getReferencedName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="../-kt-simple-name-expression-impl/index.html#getreferencedname"><span class="nf">getReferencedName</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the referenced name as it appears in the source, with any surrounding backticks removed.


</div>

</div>
### getReferencedNameAsName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="../-kt-simple-name-expression-impl/index.html#getreferencednameasname"><span class="nf">getReferencedNameAsName</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>Name
</span></code></pre></div>
</div>


<div markdown>

Returns the referenced name as a Name.


</div>

</div>
### getReferencedNameElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getreferencednameelement"><span class="nf">getReferencedNameElement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Returns the token or element that carries the referenced name (for example, the identifier or the operation sign). Never `null`, even for operation references.


</div>

</div>
### getReferencedNameElementType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="../-kt-simple-name-expression-impl/index.html#getreferencednameelementtype"><span class="nf">getReferencedNameElementType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>IElementType
</span></code></pre></div>
</div>


<div markdown>

Returns the element type of the [`referenced name element`](../-kt-simple-name-expression-impl/index.md#getreferencednameelement).


</div>

</div>
### getReferences

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#getreferences"><span class="nf">getReferences</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>PsiReference<span class="o">></span>
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
### [`getTopmostParentQualifiedExpressionForSelector`](../../org.jetbrains.kotlin.psi.psiUtil/get-topmost-parent-qualified-expression-for-selector.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/get-topmost-parent-qualified-expression-for-selector.html"><span class="nf">getTopmostParentQualifiedExpressionForSelector</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the outermost qualified expression in which this name is (transitively) the selector, or `null`.


</div>

</div>
### [`getUserData`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getuserdata">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getuserdata"><span class="nf">getUserData</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression-impl/get-user-data.html">T</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression-impl/get-user-data.html">T</a><span class="o">?</span>
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
### [`isCallee`](../../org.jetbrains.kotlin.psi.psiUtil/is-callee.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-callee.html"><span class="nf">isCallee</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this expression can be the callee of a call with the same name.


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
### [`isContractDescriptionCallPsiCheck`](../../org.jetbrains.kotlin.psi.psiUtil/is-contract-description-call-psi-check.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-contract-description-call-psi-check.html"><span class="nf">isContractDescriptionCallPsiCheck</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Best-effort PSI check for whether this expression is a `contract { ... }` (or `kotlin.contracts.contract { ... }`) call.


</div>

</div>
### [`isCopyableDataEqual`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#iscopyabledataequal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#iscopyabledataequal"><span class="nf">isCopyableDataEqual</span></a><span class="p">(</span>other<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> UserDataHolderBase<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isDotReceiver`](../../org.jetbrains.kotlin.psi.psiUtil/is-dot-receiver.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-dot-receiver.html"><span class="nf">isDotReceiver</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this expression is the receiver of an enclosing dot-qualified expression.


</div>

</div>
### [`isDotSelector`](../../org.jetbrains.kotlin.psi.psiUtil/is-dot-selector.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-dot-selector.html"><span class="nf">isDotSelector</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this expression is the selector of an enclosing dot-qualified expression.


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
### [`isImportDirectiveExpression`](../../org.jetbrains.kotlin.psi.psiUtil/is-import-directive-expression.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-import-directive-expression.html"><span class="nf">isImportDirectiveExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this name is part of an `import` directive.


</div>

</div>
### [`isInImportDirective`](../../org.jetbrains.kotlin.psi.psiUtil/is-in-import-directive.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-in-import-directive.html"><span class="nf">isInImportDirective</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this expression appears inside an `import` directive.


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
### [`isLambdaOutsideParentheses`](../../org.jetbrains.kotlin.psi.psiUtil/is-lambda-outside-parentheses.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-lambda-outside-parentheses.html"><span class="nf">isLambdaOutsideParentheses</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this expression is a trailing lambda argument written outside the call parentheses.


</div>

</div>
### [`isNull`](../../org.jetbrains.kotlin.psi.psiUtil/is-null.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-null.html"><span class="nf">isNull</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this expression is the `null` literal. Smart-casts the receiver to [`KtConstantExpression`](../-kt-constant-expression/index.md) on `true`.


</div>

</div>
### [`isPackageDirectiveExpression`](../../org.jetbrains.kotlin.psi.psiUtil/is-package-directive-expression.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/is-package-directive-expression.html"><span class="nf">isPackageDirectiveExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this name is part of a `package` directive.


</div>

</div>
### [`isPhysical`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#isphysical)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#isphysical"><span class="nf">isPhysical</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
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
### [`isValid`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#isvalid)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#isvalid"><span class="nf">isValid</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isWritable`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#iswritable)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#iswritable"><span class="nf">isWritable</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`lastBlockStatementOrThis`](../../org.jetbrains.kotlin.psi.psiUtil/last-block-statement-or-this.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/last-block-statement-or-this.html"><span class="nf">lastBlockStatementOrThis</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the last statement if this expression is a block, otherwise this expression itself.


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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#putcopyableuserdata">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#putcopyableuserdata"><span class="nf">putCopyableUserData</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression-impl/put-copyable-user-data.html">T</a><span class="o">?</span><span class="o">></span><span class="p">, </span>value<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression-impl/put-copyable-user-data.html">T</a><span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`putUserData`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#putuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#putuserdata">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#putuserdata"><span class="nf">putUserData</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression-impl/put-user-data.html">T</a><span class="o">?</span><span class="o">></span><span class="p">, </span><span class="se">@</span><span class="se">Nullable</span> value<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression-impl/put-user-data.html">T</a><span class="o">?</span><span class="p">)</span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#rawdelete"><span class="nf">rawDelete</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Deletes this PSI element using the raw platform implementation, bypassing Kotlin PSI-specific [`delete`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#delete) overrides.

Regular clients should use [`delete`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#delete) instead. When [`KtPsiMutationService`](../-kt-psi-mutation-service/index.md) is not registered, it performs the same plain deletion, and when the service is registered, as in the IntelliJ Kotlin plugin, it may also adjust the surrounding code, e.g., delete a semicolon that follows the element.


</div>

</div>
### [`referenceExpression`](../../org.jetbrains.kotlin.psi.psiUtil/reference-expression.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/reference-expression.html"><span class="nf">referenceExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-reference-expression/index.html">KtReferenceExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the reference expression of this expression (the callee for a call), or `null` if it is not a reference.


</div>

</div>
### [`replace`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#replace)

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

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="../-kt-simple-name-expression-impl/index.html#replace"><span class="nf">replace</span></a><span class="p">(</span>newElement<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Replaces this expression with [`newElement`](../-kt-simple-name-expression-impl/index.md#replace).


</div>

</div>
### [`replaceChildInternal`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#replacechildinternal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#replacechildinternal"><span class="nf">replaceChildInternal</span></a><span class="p">(</span>child<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">, </span>newElement<span class="o">: </span>TreeElement<span class="o">?</span><span class="p">)</span>
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
### [`topParenthesizedParentOrMe`](../../org.jetbrains.kotlin.psi.psiUtil/top-parenthesized-parent-or-me.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/top-parenthesized-parent-or-me.html"><span class="nf">topParenthesizedParentOrMe</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the outermost enclosing expression that this expression is wrapped in only through parentheses, or this expression itself.


</div>

</div>
### toString

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#tostring"><span class="nf">toString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
### unpackFunctionLiteral

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="../-kt-type-alias/index.html#unpackfunctionliteral"><span class="nf">unpackFunctionLiteral</span></a><span class="p">(</span>allowParentheses<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span><a href="../-kt-lambda-expression/index.html">KtLambdaExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

If this expression is a lambda expression, or wraps one in a label or an annotation, returns that [`KtLambdaExpression`](../-kt-lambda-expression/index.md); otherwise returns `null`. Parentheses are unwrapped only when [`allowParentheses`](../-kt-type-alias/index.md#unpackfunctionliteral) is `true`.


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
