---
tags:
 - jvm
title: "KtParenthesizedExpression"
---

# KtParenthesizedExpression

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="index.html">KtParenthesizedExpression</a> : <a href="../-kt-expression-impl-stub/index.html">KtExpressionImplStub</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="index.html">KtParenthesizedExpression</a><span class="o">></span><span class="o">> </span>
</span></code></pre></div>Represents an expression enclosed in parentheses. 

### Example:
```java

val x = (1 + 2) * 3
//      ^_____^

```


</div>

## Constructors
### KtParenthesizedExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> node<span class="o">: </span>ASTNode<span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> stub<span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.stubs/-kotlin-place-holder-stub/index.html">KotlinPlaceHolderStub</a><span class="o"><</span><a href="index.html">KtParenthesizedExpression</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Companion properties
### [`ARRAY_FACTORY`](../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.md#array_factory)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.html#array_factory">ARRAY_FACTORY</a><span class="o">: </span>ArrayFactory<span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-kt-throw-expression/index.html#array_factory">ARRAY_FACTORY</a><span class="o">: </span>ArrayFactory<span class="o"><</span><a href="../-kt-expression/index.html">KtExpression</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A factory for creating arrays of [`KtExpression`](../-kt-expression/index.md), used by the PSI child-access machinery.

</div>

</div>
### [`CREATION_TRACE`](../-kt-declaration-stub/index.md#creation_trace)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-kt-declaration-stub/index.html#creation_trace">CREATION_TRACE</a><span class="o">: </span>Key<span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`EMPTY_ARRAY`](../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.md#empty_array)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.html#empty_array">EMPTY_ARRAY</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-kt-throw-expression/index.html#empty_array">EMPTY_ARRAY</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="../-kt-expression/index.html">KtExpression</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A shared empty array, which can be reused to avoid unnecessary allocations.

</div>

</div>
### [`EMPTY_NAVIGATABLE_ARRAY`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#empty_navigatable_array)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#empty_navigatable_array">EMPTY_NAVIGATABLE_ARRAY</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>Navigatable<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`EMPTY_NAVIGATABLE_ELEMENT_ARRAY`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#empty_navigatable_element_array)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#empty_navigatable_element_array">EMPTY_NAVIGATABLE_ELEMENT_ARRAY</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>NavigatablePsiElement<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`EMPTY_NAVIGATION_ITEM_ARRAY`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#empty_navigation_item_array)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#empty_navigation_item_array">EMPTY_NAVIGATION_ITEM_ARRAY</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>NavigationItem<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`FLAGS_LOCKED`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#flags_locked)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#flags_locked">FLAGS_LOCKED</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="o"> = </span><span class="nb">2048</span>
</span></code></pre></div>
</div>

</div>
### [`ICON_FLAG_FAST_ONLY`](../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.md#icon_flag_fast_only)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.html#icon_flag_fast_only">ICON_FLAG_FAST_ONLY</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="o"> = </span><span class="nb">-2147483648</span>
</span></code></pre></div>
</div>

</div>
### [`ICON_FLAG_READ_STATUS`](../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.md#icon_flag_read_status)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.html#icon_flag_read_status">ICON_FLAG_READ_STATUS</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="o"> = </span><span class="nb">2</span>
</span></code></pre></div>
</div>

</div>
### [`ICON_FLAG_VISIBILITY`](../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.md#icon_flag_visibility)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.html#icon_flag_visibility">ICON_FLAG_VISIBILITY</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="o"> = </span><span class="nb">1</span>
</span></code></pre></div>
</div>

</div>
### [`ourTraceStubAstBinding`](../-kt-declaration-stub/index.md#ourtracestubastbinding)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-kt-declaration-stub/index.html#ourtracestubastbinding">ourTraceStubAstBinding</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
## Companion functions
### [`buildRowIcon`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#buildrowicon)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#buildrowicon"><span class="nf">buildRowIcon</span></a><span class="p">(</span>baseIcon<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/javax/swing/Icon.html">Icon</a><span class="p">, </span>visibilityIcon<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/javax/swing/Icon.html">Icon</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> RowIcon
</span></code></pre></div>
</div>

</div>
### [`getChildrenSkippingLeaves`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#getchildrenskippingleaves)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#getchildrenskippingleaves"><span class="nf">getChildrenSkippingLeaves</span></a><span class="p">(</span>element<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`iconWithVisibilityIfNeeded`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#iconwithvisibilityifneeded)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#iconwithvisibilityifneeded"><span class="nf">iconWithVisibilityIfNeeded</span></a><span class="p">(</span>
    flags<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">, </span>
    baseIcon<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/javax/swing/Icon.html">Icon</a><span class="p">, </span>
    visibility<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/javax/swing/Icon.html">Icon</a>
<span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/javax/swing/Icon.html">Icon</a>
</span></code></pre></div>
</div>

</div>
### [`isNativeFileType`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#isnativefiletype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#isnativefiletype"><span class="nf">isNativeFileType</span></a><span class="p">(</span>fileType<span class="o">: </span>FileType<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`transformFlags`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#transformflags)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#transformflags"><span class="nf">transformFlags</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">, </span>_flags<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`withForcedDeferredIcons`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#withforceddeferredicons)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#withforceddeferredicons"><span class="nf">withForcedDeferredIcons</span></a><span class="p">(</span>runnable<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Runnable.html">Runnable</a><span class="p">)</span>
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
### [`accept`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#accept)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#accept"><span class="nf">accept</span></a><span class="p">(</span>visitor<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElementVisitor<span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../-kt-throw-expression/index.html#accept">R</a><span class="p">, </span><a href="../-kt-throw-expression/index.html#accept">D</a><span class="o">> </span><a href="../-kt-throw-expression/index.html#accept"><span class="nf">accept</span></a><span class="p">(</span>visitor<span class="o">: </span><a href="../-kt-visitor/index.html">KtVisitor</a><span class="o"><</span><a href="../-kt-throw-expression/index.html#accept">R</a><span class="p">, </span><a href="../-kt-throw-expression/index.html#accept">D</a><span class="o">></span><span class="p">, </span>data<span class="o">: </span><a href="../-kt-throw-expression/index.html#accept">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-throw-expression/index.html#accept">R</a>
</span></code></pre></div>
</div>


<div markdown>

Dispatches this element to the corresponding `visit*` method of the given [`visitor`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#accept) and returns its result.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-declaration-stub/index.html#accept"><span class="nf">accept</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> visitor<span class="o">: </span>PsiElementVisitor<span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#accept">R</a><span class="p">, </span><a href="index.html#accept">D</a><span class="o">> </span><a href="index.html#accept"><span class="nf">accept</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> visitor<span class="o">: </span><a href="../-kt-visitor/index.html">KtVisitor</a><span class="o"><</span><a href="index.html#accept">R</a><span class="p">, </span><a href="index.html#accept">D</a><span class="o">></span><span class="p">, </span>data<span class="o">: </span><a href="index.html#accept">D</a><span class="p">)</span><span class="o">: </span><a href="index.html#accept">R</a>
</span></code></pre></div>
</div>


<div markdown>

Dispatches this element to the corresponding `visit*` method of the given [`visitor`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#accept) and returns its result.

</div>

</div>
### [`acceptChildren`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#acceptchildren)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#acceptchildren"><span class="nf">acceptChildren</span></a><span class="p">(</span>visitor<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElementVisitor<span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../-kt-throw-expression/index.html#acceptchildren">D</a><span class="o">> </span><a href="../-kt-throw-expression/index.html#acceptchildren"><span class="nf">acceptChildren</span></a><span class="p">(</span>visitor<span class="o">: </span><a href="../-kt-visitor/index.html">KtVisitor</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a><span class="p">, </span><a href="../-kt-throw-expression/index.html#acceptchildren">D</a><span class="o">></span><span class="p">, </span>data<span class="o">: </span><a href="../-kt-throw-expression/index.html#acceptchildren">D</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Passes each direct child of this element to the given [`visitor`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#acceptchildren).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../-kt-declaration-stub/index.html#acceptchildren">D</a><span class="o">> </span><a href="../-kt-declaration-stub/index.html#acceptchildren"><span class="nf">acceptChildren</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> visitor<span class="o">: </span><a href="../-kt-visitor/index.html">KtVisitor</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a><span class="p">, </span><a href="../-kt-declaration-stub/index.html#acceptchildren">D</a><span class="o">></span><span class="p">, </span>data<span class="o">: </span><a href="../-kt-declaration-stub/index.html#acceptchildren">D</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Passes each direct child of this element to the given [`visitor`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#acceptchildren).

</div>

</div>
### [`add`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#add)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#add"><span class="nf">add</span></a><span class="p">(</span>element<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`addAfter`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#addafter)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#addafter"><span class="nf">addAfter</span></a><span class="p">(</span>element<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">, </span>anchor<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`addBefore`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#addbefore)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#addbefore"><span class="nf">addBefore</span></a><span class="p">(</span>element<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">, </span>anchor<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`addInternal`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#addinternal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#addinternal"><span class="nf">addInternal</span></a><span class="p">(</span>
    first<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ASTNode<span class="p">, </span>
    last<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ASTNode<span class="p">, </span>
    anchor<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> ASTNode<span class="p">, </span>
    before<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html">Boolean</a>
<span class="p">)</span><span class="o">: </span>ASTNode
</span></code></pre></div>
</div>

</div>
### [`addRange`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#addrange)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#addrange"><span class="nf">addRange</span></a><span class="p">(</span>first<span class="o">: </span>PsiElement<span class="p">, </span>last<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`addRangeAfter`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#addrangeafter)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#addrangeafter"><span class="nf">addRangeAfter</span></a><span class="p">(</span>
    first<span class="o">: </span>PsiElement<span class="p">, </span>
    last<span class="o">: </span>PsiElement<span class="p">, </span>
    anchor<span class="o">: </span>PsiElement
<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`addRangeBefore`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#addrangebefore)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#addrangebefore"><span class="nf">addRangeBefore</span></a><span class="p">(</span>
    first<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">, </span>
    last<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">, </span>
    anchor<span class="o">: </span>PsiElement
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
### [`checkAdd`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#checkadd)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#checkadd"><span class="nf">checkAdd</span></a><span class="p">(</span>element<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">)</span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#copy"><span class="nf">copy</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`copyCopyableDataTo`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#copycopyabledatato)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#copycopyabledatato"><span class="nf">copyCopyableDataTo</span></a><span class="p">(</span>clone<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> UserDataHolderBase<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`copyUserDataTo`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#copyuserdatato)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#copyuserdatato"><span class="nf">copyUserDataTo</span></a><span class="p">(</span>other<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> UserDataHolderBase<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`delete`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#delete)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#delete"><span class="nf">delete</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#delete"><span class="nf">delete</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Deletes this element.

</div>

</div>
### [`deleteChildInternal`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#deletechildinternal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#deletechildinternal"><span class="nf">deleteChildInternal</span></a><span class="p">(</span>child<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ASTNode<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`deleteChildRange`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#deletechildrange)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#deletechildrange"><span class="nf">deleteChildRange</span></a><span class="p">(</span>first<span class="o">: </span>PsiElement<span class="p">, </span>last<span class="o">: </span>PsiElement<span class="p">)</span>
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
### [`findElementAt`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#findelementat)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#findelementat"><span class="nf">findElementAt</span></a><span class="p">(</span>offset<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`findReferenceAt`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#findreferenceat)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#findreferenceat"><span class="nf">findReferenceAt</span></a><span class="p">(</span>offset<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span>PsiReference
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getchildren"><span class="nf">getChildren</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>PsiElement<span class="o">></span>
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
### [`getContainingFile`](../-kt-type-reference/index.md#getcontainingfile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#getcontainingfile"><span class="nf">getContainingFile</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiFile
</span></code></pre></div>
</div>

</div>
### getContainingKtFile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#getcontainingktfile"><span class="nf">getContainingKtFile</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-file/index.html">KtFile</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KtFile`](../-kt-file/index.md) this element belongs to.


</div>

</div>
### [`getContext`](../-kt-type-reference/index.md#getcontext)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#getcontext"><span class="nf">getContext</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`getCopyableUserData`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#getcopyableuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#getcopyableuserdata">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#getcopyableuserdata"><span class="nf">getCopyableUserData</span></a><span class="p">(</span>key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#getcopyableuserdata">T</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#getcopyableuserdata">T</a>
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
### [`getElementType`](../-kt-declaration-stub/index.md#getelementtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-declaration-stub/index.html#getelementtype"><span class="nf">getElementType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IStubElementType
</span></code></pre></div>
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
### getExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getexpression"><span class="nf">getExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the expression inside the parentheses, or `#!java null` if it is absent in incomplete code.


</div>

</div>
### [`getFirstChild`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getfirstchild)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getfirstchild"><span class="nf">getFirstChild</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`getGreenStub`](../-kt-type-reference/index.md#getgreenstub)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-type-reference/index.html#getgreenstub"><span class="nf">getGreenStub</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> T
</span></code></pre></div>
</div>

</div>
### [`getIcon`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#geticon)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#geticon"><span class="nf">getIcon</span></a><span class="p">(</span>flags<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="https://docs.oracle.com/javase/8/docs/api/javax/swing/Icon.html">Icon</a>
</span></code></pre></div>
</div>

</div>
### [`getIElementType`](../-kt-declaration-stub/index.md#getielementtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-declaration-stub/index.html#getielementtype"><span class="nf">getIElementType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>IElementType
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-declaration-stub/index.html#getielementtype"><span class="nf">getIElementType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>IElementType
</span></code></pre></div>
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
### [`getLanguage`](../-kt-declaration-stub/index.md#getlanguage)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-declaration-stub/index.html#getlanguage"><span class="nf">getLanguage</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Language
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#getlanguage"><span class="nf">getLanguage</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>Language
</span></code></pre></div>
</div>

</div>
### [`getLastChild`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getlastchild)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getlastchild"><span class="nf">getLastChild</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
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
### [`getManager`](../-kt-type-reference/index.md#getmanager)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#getmanager"><span class="nf">getManager</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiManagerEx
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#getmanager"><span class="nf">getManager</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiManager
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#getname"><span class="nf">getName</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`getNavigationElement`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getnavigationelement)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getnavigationelement"><span class="nf">getNavigationElement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement
</span></code></pre></div>
</div>

</div>
### [`getNextSibling`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getnextsibling)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getnextsibling"><span class="nf">getNextSibling</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
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
### [`getNode`](../-kt-type-reference/index.md#getnode)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#getnode"><span class="nf">getNode</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ASTNode
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getoriginalelement"><span class="nf">getOriginalElement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
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
### [`getOwnDeclarations`](../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.md#getowndeclarations)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.html#getowndeclarations"><span class="nf">getOwnDeclarations</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html">Collection</a><span class="o"><</span><span class="kd">out </span><span class="se">@</span><span class="se">NotNull</span> PsiSymbolDeclaration<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`getOwnReferences`](../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.md#getownreferences)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.html#getownreferences"><span class="nf">getOwnReferences</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html">Collection</a><span class="o"><</span><span class="kd">out </span><span class="se">@</span><span class="se">NotNull</span> PsiSymbolReference<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`getParent`](../-kt-type-reference/index.md#getparent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#getparent"><span class="nf">getParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-kt-throw-expression/index.html#getparent"><span class="nf">getParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Returns parent source element.

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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-name/index.html#getpresentation"><span class="nf">getPresentation</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>ItemPresentation
</span></code></pre></div>
</div>

</div>
### [`getPrevSibling`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getprevsibling)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getprevsibling"><span class="nf">getPrevSibling</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
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
### [`getProject`](../-kt-type-reference/index.md#getproject)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#getproject"><span class="nf">getProject</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Project
</span></code></pre></div>
</div>

</div>
### getPsiOrParent

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#getpsiorparent"><span class="nf">getPsiOrParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a>
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
### [`getReference`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getreference)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getreference"><span class="nf">getReference</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiReference
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-kt-throw-expression/index.html#getreference"><span class="nf">getReference</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiReference
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#getreference"><span class="nf">getReference</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiReference
</span></code></pre></div>
</div>

</div>
### [`getReferences`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getreferences)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getreferences"><span class="nf">getReferences</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>PsiReference<span class="o">></span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#getreferences"><span class="nf">getReferences</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>PsiReference<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`getRequiredStubOrPsiChild`](../-kt-declaration-stub/index.md#getrequiredstuborpsichild)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-declaration-stub/index.html#getrequiredstuborpsichild"><span class="nf">getRequiredStubOrPsiChild</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="../-kt-declaration-stub/index.html#getrequiredstuborpsichild">Psi</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="../-kt-declaration-stub/index.html#getrequiredstuborpsichild"><span class="nf">getRequiredStubOrPsiChild</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">, </span>psiClass<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="../-kt-declaration-stub/index.html#getrequiredstuborpsichild">Psi</a><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="../-kt-declaration-stub/index.html#getrequiredstuborpsichild">Psi</a>
</span></code></pre></div>
</div>

</div>
### [`getResolveScope`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getresolvescope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getresolvescope"><span class="nf">getResolveScope</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> GlobalSearchScope
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
### [`getStub`](../-kt-type-reference/index.md#getstub)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#getstub"><span class="nf">getStub</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> T
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-kt-declaration-stub/index.html#getstub"><span class="nf">getStub</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>Stub
</span></code></pre></div>
</div>

</div>
### [`getStubOrPsiChild`](../-kt-declaration-stub/index.md#getstuborpsichild)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-declaration-stub/index.html#getstuborpsichild"><span class="nf">getStubOrPsiChild</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> PsiElement
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="../-kt-declaration-stub/index.html#getstuborpsichild">Psi</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="../-kt-declaration-stub/index.html#getstuborpsichild"><span class="nf">getStubOrPsiChild</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">, </span>psiClass<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="../-kt-declaration-stub/index.html#getstuborpsichild">Psi</a><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="../-kt-declaration-stub/index.html#getstuborpsichild">Psi</a>
</span></code></pre></div>
</div>

</div>
### [`getStubOrPsiChildren`](../-kt-declaration-stub/index.md#getstuborpsichildren)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="../-kt-declaration-stub/index.html#getstuborpsichildren">Psi</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="../-kt-declaration-stub/index.html#getstuborpsichildren"><span class="nf">getStubOrPsiChildren</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">, </span>f<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ArrayFactory<span class="o"><</span><span class="kd">out </span><a href="../-kt-declaration-stub/index.html#getstuborpsichildren">Psi</a><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="../-kt-declaration-stub/index.html#getstuborpsichildren">Psi</a><span class="o">></span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#gettext"><span class="nf">getText</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#gettextrange"><span class="nf">getTextRange</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>TextRange
</span></code></pre></div>
</div>

</div>
### [`getTextRangeInParent`](../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.md#gettextrangeinparent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.html#gettextrangeinparent"><span class="nf">getTextRangeInParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> TextRange
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
### [`getUserData`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#getuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#getuserdata">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#getuserdata"><span class="nf">getUserData</span></a><span class="p">(</span>key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#getuserdata">T</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#getuserdata">T</a>
</span></code></pre></div>
</div>

</div>
### [`getUserDataString`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#getuserdatastring)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#getuserdatastring"><span class="nf">getUserDataString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`getUserMap`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#getusermap)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#getusermap"><span class="nf">getUserMap</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> KeyFMap
</span></code></pre></div>
</div>

</div>
### [`getUseScope`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#getusescope)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#getusescope"><span class="nf">getUseScope</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> SearchScope
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
### [`isCopyableDataEqual`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#iscopyabledataequal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#iscopyabledataequal"><span class="nf">isCopyableDataEqual</span></a><span class="p">(</span>other<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> UserDataHolderBase<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
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
### [`isEquivalentTo`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#isequivalentto)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#isequivalentto"><span class="nf">isEquivalentTo</span></a><span class="p">(</span>another<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
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
### [`isPhysical`](../-kt-type-reference/index.md#isphysical)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#isphysical"><span class="nf">isPhysical</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
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
### [`isUserDataEmpty`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#isuserdataempty)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#isuserdataempty"><span class="nf">isUserDataEmpty</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isValid`](../-kt-type-reference/index.md#isvalid)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#isvalid"><span class="nf">isValid</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isWritable`](../-kt-type-reference/index.md#iswritable)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#iswritable"><span class="nf">isWritable</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
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
### [`navigate`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#navigate)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#navigate"><span class="nf">navigate</span></a><span class="p">(</span>requestFocus<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`navigationRequest`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#navigationrequest)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#navigationrequest"><span class="nf">navigationRequest</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>NavigationRequest
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
### [`processDeclarations`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#processdeclarations)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#processdeclarations"><span class="nf">processDeclarations</span></a><span class="p">(</span>
    processor<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiScopeProcessor<span class="p">, </span>
    state<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ResolveState<span class="p">, </span>
    lastParent<span class="o">: </span>PsiElement<span class="p">, </span>
    place<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`putCopyableUserData`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#putcopyableuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#putcopyableuserdata">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#putcopyableuserdata"><span class="nf">putCopyableUserData</span></a><span class="p">(</span>key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#putcopyableuserdata">T</a><span class="o">></span><span class="p">, </span>value<span class="o">: </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#putcopyableuserdata">T</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`putUserData`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#putuserdata)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#putuserdata">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#putuserdata"><span class="nf">putUserData</span></a><span class="p">(</span>key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#putuserdata">T</a><span class="o">></span><span class="p">, </span>value<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#putuserdata">T</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`putUserDataIfAbsent`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#putuserdataifabsent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#putuserdataifabsent">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#putuserdataifabsent"><span class="nf">putUserDataIfAbsent</span></a><span class="p">(</span>key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#putuserdataifabsent">T</a><span class="o">></span><span class="p">, </span>value<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#putuserdataifabsent">T</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#putuserdataifabsent">T</a>
</span></code></pre></div>
</div>

</div>
### rawDelete

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html#rawdelete"><span class="nf">rawDelete</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Deletes this PSI element using the raw platform implementation, bypassing Kotlin PSI-specific [`delete`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#delete) overrides.

Regular clients should use [`delete`](../../org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md#delete) instead. When [`KtPsiMutationService`](../-kt-psi-mutation-service/index.md) is not registered, it performs the same plain deletion, and when the service is registered, as in the IntelliJ Kotlin plugin, it may also adjust the surrounding code, e.g., delete a semicolon that follows the element.


</div>

</div>
### rawReplace

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../-kt-constant-expression/index.html#rawreplace"><span class="nf">rawReplace</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> newElement<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Replaces this element using the raw platform implementation, bypassing the Kotlin-specific [`replace`](../-kt-constant-expression/index.md#replace) handling. Intended for use by the PSI mutation machinery.


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
### [`replace`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#replace)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#replace"><span class="nf">replace</span></a><span class="p">(</span>newElement<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#replace">T</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#replace"><span class="nf">replace</span></a><span class="p">(</span>
    key<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Key<span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#replace">T</a><span class="o">></span><span class="p">, </span>
    oldValue<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#replace">T</a><span class="p">, </span>
    newValue<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#replace">T</a>
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="../-kt-constant-expression/index.html#replace"><span class="nf">replace</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> newElement<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Replaces this expression with `#!java newElement`.

</div>

</div>
### [`replaceChildInternal`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#replacechildinternal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#replacechildinternal"><span class="nf">replaceChildInternal</span></a><span class="p">(</span>child<span class="o">: </span>PsiElement<span class="p">, </span>newElement<span class="o">: </span>TreeElement<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`setNode`](../-kt-declaration-stub/index.md#setnode)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-declaration-stub/index.html#setnode"><span class="nf">setNode</span></a><span class="p">(</span>node<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ASTNode<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`setSubstrateRef`](../-kt-declaration-stub/index.md#setsubstrateref)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-declaration-stub/index.html#setsubstrateref"><span class="nf">setSubstrateRef</span></a><span class="p">(</span>substrateRef<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> SubstrateRef<span class="p">)</span>
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
### [`textContains`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#textcontains)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#textcontains"><span class="nf">textContains</span></a><span class="p">(</span>c<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char/index.html">Char</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`textMatches`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.md#textmatches)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-element-impl/index.html#textmatches"><span class="nf">textMatches</span></a><span class="p">(</span>text<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/CharSequence.html">CharSequence</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`textToCharArray`](../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.md#texttochararray)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html#texttochararray"><span class="nf">textToCharArray</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char/index.html">Char</a><span class="o">></span>
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
### [`toString`](../-kt-declaration-stub/index.md#tostring)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-declaration-stub/index.html#tostring"><span class="nf">toString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kt-type-reference/index.html#tostring"><span class="nf">toString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
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
