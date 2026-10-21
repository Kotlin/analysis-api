---
tags:
 - jvm
title: "KDocElement"
---

# KDocElement

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KDocElement</a> : PsiElement
</span></code></pre></div>A marker interface implemented by all elements of a KDoc comment's PSI tree.

#### Inheritors


 - [`KDocElementImpl`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md)
 - [`KDoc`](../-k-doc/index.md)



</div>

## Companion properties
### [`ARRAY_FACTORY`](index.md#array_factory)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#array_factory">ARRAY_FACTORY</a><span class="o">: </span>ArrayFactory<span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`EMPTY_ARRAY`](index.md#empty_array)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#empty_array">EMPTY_ARRAY</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`ICON_FLAG_FAST_ONLY`](index.md#icon_flag_fast_only)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#icon_flag_fast_only">ICON_FLAG_FAST_ONLY</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="o"> = </span><span class="nb">-2147483648</span>
</span></code></pre></div>
</div>

</div>
### [`ICON_FLAG_READ_STATUS`](index.md#icon_flag_read_status)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#icon_flag_read_status">ICON_FLAG_READ_STATUS</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="o"> = </span><span class="nb">2</span>
</span></code></pre></div>
</div>

</div>
### [`ICON_FLAG_VISIBILITY`](index.md#icon_flag_visibility)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#icon_flag_visibility">ICON_FLAG_VISIBILITY</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="o"> = </span><span class="nb">1</span>
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
## Functions
### [`accept`](index.md#accept)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#accept"><span class="nf">accept</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElementVisitor<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`acceptChildren`](index.md#acceptchildren)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#acceptchildren"><span class="nf">acceptChildren</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElementVisitor<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`add`](index.md#add)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#add"><span class="nf">add</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`addAfter`](index.md#addafter)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#addafter"><span class="nf">addAfter</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">, </span>p1<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`addBefore`](index.md#addbefore)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#addbefore"><span class="nf">addBefore</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">, </span>p1<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`addRange`](index.md#addrange)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#addrange"><span class="nf">addRange</span></a><span class="p">(</span>p<span class="o">: </span>PsiElement<span class="p">, </span>p1<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`addRangeAfter`](index.md#addrangeafter)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#addrangeafter"><span class="nf">addRangeAfter</span></a><span class="p">(</span>
    p<span class="o">: </span>PsiElement<span class="p">, </span>
    p1<span class="o">: </span>PsiElement<span class="p">, </span>
    p2<span class="o">: </span>PsiElement
<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`addRangeBefore`](index.md#addrangebefore)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#addrangebefore"><span class="nf">addRangeBefore</span></a><span class="p">(</span>
    p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">, </span>
    p1<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">, </span>
    p2<span class="o">: </span>PsiElement
<span class="p">)</span><span class="o">: </span>PsiElement
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
### [`checkAdd`](index.md#checkadd)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#checkadd"><span class="nf">checkAdd</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">)</span>
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
### [`checkDelete`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#checkdelete)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html#checkdelete"><span class="nf">checkDelete</span></a><span class="p">(</span><span class="p">)</span>
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
### [`copy`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#copy)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html#copy"><span class="nf">copy</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`delete`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#delete)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html#delete"><span class="nf">delete</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`deleteChildRange`](index.md#deletechildrange)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#deletechildrange"><span class="nf">deleteChildRange</span></a><span class="p">(</span>p<span class="o">: </span>PsiElement<span class="p">, </span>p1<span class="o">: </span>PsiElement<span class="p">)</span>
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
### [`findElementAt`](index.md#findelementat)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#findelementat"><span class="nf">findElementAt</span></a><span class="p">(</span>p<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> PsiElement
</span></code></pre></div>
</div>

</div>
### [`findReferenceAt`](index.md#findreferenceat)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#findreferenceat"><span class="nf">findReferenceAt</span></a><span class="p">(</span>p<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> PsiReference
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
### [`getChildren`](index.md#getchildren)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getchildren"><span class="nf">getChildren</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="o">></span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getcontainingfile"><span class="nf">getContainingFile</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiFile
</span></code></pre></div>
</div>

</div>
### [`getContext`](index.md#getcontext)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getcontext"><span class="nf">getContext</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> PsiElement
</span></code></pre></div>
</div>

</div>
### [`getCopyableUserData`](index.md#getcopyableuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#getcopyableuserdata">T</a><span class="o">> </span><a href="index.html#getcopyableuserdata"><span class="nf">getCopyableUserData</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="index.html#getcopyableuserdata">T</a><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="index.html#getcopyableuserdata">T</a>
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
### [`getFirstChild`](index.md#getfirstchild)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getfirstchild"><span class="nf">getFirstChild</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`getIcon`](index.md#geticon)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#geticon"><span class="nf">getIcon</span></a><span class="p">(</span>p<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/javax/swing/Icon.html">Icon</a>
</span></code></pre></div>
</div>

</div>
### [`getLanguage`](index.md#getlanguage)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getlanguage"><span class="nf">getLanguage</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Language
</span></code></pre></div>
</div>

</div>
### [`getLastChild`](index.md#getlastchild)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getlastchild"><span class="nf">getLastChild</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getmanager"><span class="nf">getManager</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiManager
</span></code></pre></div>
</div>

</div>
### [`getNavigationElement`](index.md#getnavigationelement)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getnavigationelement"><span class="nf">getNavigationElement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`getNextSibling`](index.md#getnextsibling)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getnextsibling"><span class="nf">getNextSibling</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getnode"><span class="nf">getNode</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>ASTNode
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
### [`getOriginalElement`](index.md#getoriginalelement)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getoriginalelement"><span class="nf">getOriginalElement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
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
### [`getOwnDeclarations`](index.md#getowndeclarations)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getowndeclarations"><span class="nf">getOwnDeclarations</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html">Collection</a><span class="o"><</span><span class="kd">out </span><span class="se">@</span><span class="se">NotNull</span> PsiSymbolDeclaration<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`getOwnReferences`](index.md#getownreferences)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getownreferences"><span class="nf">getOwnReferences</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html">Collection</a><span class="o"><</span><span class="kd">out </span><span class="se">@</span><span class="se">NotNull</span> PsiSymbolReference<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`getParent`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#getparent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html#getparent"><span class="nf">getParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
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
### [`getPrevSibling`](index.md#getprevsibling)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getprevsibling"><span class="nf">getPrevSibling</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getproject"><span class="nf">getProject</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Project
</span></code></pre></div>
</div>

</div>
### [`getReference`](index.md#getreference)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getreference"><span class="nf">getReference</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> PsiReference
</span></code></pre></div>
</div>

</div>
### [`getReferences`](index.md#getreferences)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getreferences"><span class="nf">getReferences</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>PsiReference<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`getResolveScope`](index.md#getresolvescope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getresolvescope"><span class="nf">getResolveScope</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> GlobalSearchScope
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
### [`getStartOffsetInParent`](index.md#getstartoffsetinparent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getstartoffsetinparent"><span class="nf">getStartOffsetInParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
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
### [`getText`](index.md#gettext)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#gettext"><span class="nf">getText</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`getTextLength`](index.md#gettextlength)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#gettextlength"><span class="nf">getTextLength</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`getTextOffset`](index.md#gettextoffset)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#gettextoffset"><span class="nf">getTextOffset</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`getTextRange`](index.md#gettextrange)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#gettextrange"><span class="nf">getTextRange</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>TextRange
</span></code></pre></div>
</div>

</div>
### [`getTextRangeInParent`](index.md#gettextrangeinparent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#gettextrangeinparent"><span class="nf">getTextRangeInParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> TextRange
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
### [`getUserData`](index.md#getuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#getuserdata">T</a><span class="o">> </span><a href="index.html#getuserdata"><span class="nf">getUserData</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="index.html#getuserdata">T</a><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="index.html#getuserdata">T</a>
</span></code></pre></div>
</div>

</div>
### [`getUseScope`](index.md#getusescope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getusescope"><span class="nf">getUseScope</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> SearchScope
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
### [`isEquivalentTo`](index.md#isequivalentto)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#isequivalentto"><span class="nf">isEquivalentTo</span></a><span class="p">(</span>p<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#isphysical"><span class="nf">isPhysical</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
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
### [`isValid`](index.md#isvalid)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#isvalid"><span class="nf">isValid</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isWritable`](index.md#iswritable)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#iswritable"><span class="nf">isWritable</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
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
### [`processDeclarations`](index.md#processdeclarations)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#processdeclarations"><span class="nf">processDeclarations</span></a><span class="p">(</span>
    p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiScopeProcessor<span class="p">, </span>
    p1<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ResolveState<span class="p">, </span>
    p2<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> PsiElement<span class="p">, </span>
    p3<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`putCopyableUserData`](index.md#putcopyableuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#putcopyableuserdata">T</a><span class="o">> </span><a href="index.html#putcopyableuserdata"><span class="nf">putCopyableUserData</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="index.html#putcopyableuserdata">T</a><span class="o">></span><span class="p">, </span>p1<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="index.html#putcopyableuserdata">T</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`putUserData`](index.md#putuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#putuserdata">T</a><span class="o">> </span><a href="index.html#putuserdata"><span class="nf">putUserData</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="index.html#putuserdata">T</a><span class="o">></span><span class="p">, </span>p1<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="index.html#putuserdata">T</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`replace`](index.md#replace)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#replace"><span class="nf">replace</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
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
### [`textContains`](index.md#textcontains)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#textcontains"><span class="nf">textContains</span></a><span class="p">(</span>p<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char/index.html">Char</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`textMatches`](index.md#textmatches)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#textmatches"><span class="nf">textMatches</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <span class="se">@</span><span class="se">NonNls</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/CharSequence.html">CharSequence</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`textToCharArray`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#texttochararray)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html#texttochararray"><span class="nf">textToCharArray</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char/index.html">Char</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`toString`](index.md#tostring)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#tostring"><span class="nf">toString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NonNls</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
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
