---
tags:
 - jvm
title: "KotlinStubElement"
---

# KotlinStubElement

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinStubElement</a><span class="o"><</span><a href="index.html">T</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="o">></span> : StubElement<span class="o"><</span><a href="index.html">T</a><span class="o">> </span>
</span></code></pre></div>Base interface for all Kotlin stubs

#### Inheritors


 - [`KotlinFileStub`](../-kotlin-file-stub/index.md)
 - [`KotlinPlaceHolderStub`](../-kotlin-place-holder-stub/index.md)
 - [`KotlinStubWithFqName`](../-kotlin-stub-with-fq-name/index.md)
 - [`KotlinClassifierStub`](../-kotlin-classifier-stub/index.md)
 - [`KotlinAnnotationEntryStub`](../-kotlin-annotation-entry-stub/index.md)
 - [`KotlinAnnotationUseSiteTargetStub`](../-kotlin-annotation-use-site-target-stub/index.md)
 - [`KotlinDeclarationWithBodyStub`](../-kotlin-declaration-with-body-stub/index.md)
 - [`KotlinImportAliasStub`](../-kotlin-import-alias-stub/index.md)
 - [`KotlinImportDirectiveStub`](../-kotlin-import-directive-stub/index.md)
 - [`KotlinModifierListStub`](../-kotlin-modifier-list-stub/index.md)
 - [`KotlinNameReferenceExpressionStub`](../-kotlin-name-reference-expression-stub/index.md)
 - [`KotlinOperationReferenceExpressionStub`](../-kotlin-operation-reference-expression-stub/index.md)
 - [`KotlinEnumEntrySuperclassReferenceExpressionStub`](../-kotlin-enum-entry-superclass-reference-expression-stub/index.md)
 - [`KotlinBackingFieldStub`](../-kotlin-backing-field-stub/index.md)
 - [`KotlinDestructuringDeclarationStub`](../-kotlin-destructuring-declaration-stub/index.md)
 - [`KotlinConstantExpressionStub`](../-kotlin-constant-expression-stub/index.md)
 - [`KotlinCollectionLiteralExpressionStub`](../-kotlin-collection-literal-expression-stub/index.md)
 - [`KotlinTypeProjectionStub`](../-kotlin-type-projection-stub/index.md)
 - [`KotlinUserTypeStub`](../-kotlin-user-type-stub/index.md)
 - [`KotlinFunctionTypeStub`](../-kotlin-function-type-stub/index.md)
 - [`KotlinContextReceiverStub`](../-kotlin-context-receiver-stub/index.md)
 - [`KotlinStringInterpolationPrefixStub`](../-kotlin-string-interpolation-prefix-stub/index.md)



</div>

## Properties
### [`childrenStubs`](../-kotlin-block-string-template-entry-stub/index.md#childrenstubs)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">NotNull</span>
<span class="kd">abstract </span><span class="kd">override </span><span class="kd">val </span><a href="../-kotlin-block-string-template-entry-stub/index.html#childrenstubs">childrenStubs</a><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>StubElement<span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`containingFileStub`](../-kotlin-block-string-template-entry-stub/index.md#containingfilestub)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@get:</span><span class="se">Nullable</span>
<span class="kd">abstract </span><span class="kd">override </span><span class="kd">val </span><a href="../-kotlin-block-string-template-entry-stub/index.html#containingfilestub">containingFileStub</a><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> PsiFileStub<span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`elementType`](../-kotlin-block-string-template-entry-stub/index.md#elementtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">val </span><a href="../-kotlin-block-string-template-entry-stub/index.html#elementtype">elementType</a><span class="o">: </span>IElementType<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`parentStub`](../-kotlin-block-string-template-entry-stub/index.md#parentstub)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">val </span><a href="../-kotlin-block-string-template-entry-stub/index.html#parentstub">parentStub</a><span class="o">: </span>StubElement<span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`psi`](../-kotlin-block-string-template-entry-stub/index.md#psi)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">val </span><a href="../-kotlin-block-string-template-entry-stub/index.html#psi">psi</a><span class="o">: </span><a href="index.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`stubSerializer`](../-kotlin-block-string-template-entry-stub/index.md#stubserializer)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../-kotlin-block-string-template-entry-stub/index.html#stubserializer">stubSerializer</a><span class="o">: </span>ObjectStubSerializer<span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="kd">out </span>Stub<span class="o">?</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`stubType`](../-kotlin-block-string-template-entry-stub/index.md#stubtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">val </span><a href="../-kotlin-block-string-template-entry-stub/index.html#stubtype">stubType</a><span class="o">: </span>IStubElementType<span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
## Functions
### copyInto

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-kotlin-block-string-template-entry-stub/index.html#copyinto"><span class="nf">copyInto</span></a><span class="p">(</span>newParent<span class="o">: </span>StubElement<span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="index.html">KotlinStubElement</a><span class="o"><</span><a href="index.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns a copy of this stub with the parent set to [`newParent`](../-kotlin-block-string-template-entry-stub/index.md#copyinto).

<strong>Note</strong>: the implementation doesn't guarantee that com.intellij.psi.stubs.ObjectStubBase.isDangling flag is copied


</div>

</div>
### [`findChildStubByElementType`](../-kotlin-block-string-template-entry-stub/index.md#findchildstubbyelementtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kotlin-block-string-template-entry-stub/index.html#findchildstubbyelementtype"><span class="nf">findChildStubByElementType</span></a><span class="p">(</span>elementType<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> StubElement<span class="o"><</span><span class="kd">out </span>PsiElement<span class="o">?</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`findChildStubByType`](../-kotlin-block-string-template-entry-stub/index.md#findchildstubbytype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../-kotlin-block-string-template-entry-stub/index.html#findchildstubbytype">P</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="p">, </span><a href="../-kotlin-block-string-template-entry-stub/index.html#findchildstubbytype">S</a><span class="o"> : </span>StubElement<span class="o"><</span><a href="../-kotlin-block-string-template-entry-stub/index.html#findchildstubbytype">P</a><span class="o">?</span><span class="o">></span><span class="o">?</span><span class="o">> </span><a href="../-kotlin-block-string-template-entry-stub/index.html#findchildstubbytype"><span class="nf">findChildStubByType</span></a><span class="p">(</span>p0<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IStubElementType<span class="o"><</span><a href="../-kotlin-block-string-template-entry-stub/index.html#findchildstubbytype">S</a><span class="o">?</span><span class="p">, </span><a href="../-kotlin-block-string-template-entry-stub/index.html#findchildstubbytype">P</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="../-kotlin-block-string-template-entry-stub/index.html#findchildstubbytype">S</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getChildrenByType`](../-kotlin-block-string-template-entry-stub/index.md#getchildrenbytype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype">E</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype"><span class="nf">getChildrenByType</span></a><span class="p">(</span>p0<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">, </span>p1<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ArrayFactory<span class="o"><</span><span class="kd">out </span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype">E</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype">E</a><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype">E</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype"><span class="nf">getChildrenByType</span></a><span class="p">(</span>p0<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">, </span>p1<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype">E</a><span class="o">?</span><span class="o">></span><span class="o">?</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype">E</a><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype">E</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype"><span class="nf">getChildrenByType</span></a><span class="p">(</span>p0<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> TokenSet<span class="p">, </span>p1<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> ArrayFactory<span class="o"><</span><span class="kd">out </span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype">E</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype">E</a><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype">E</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype"><span class="nf">getChildrenByType</span></a><span class="p">(</span>p0<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> TokenSet<span class="p">, </span>p1<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype">E</a><span class="o">?</span><span class="o">></span><span class="o">?</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="../-kotlin-block-string-template-entry-stub/index.html#getchildrenbytype">E</a><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`getParentStubOfType`](../-kotlin-block-string-template-entry-stub/index.md#getparentstuboftype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="../-kotlin-block-string-template-entry-stub/index.html#getparentstuboftype">E</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="../-kotlin-block-string-template-entry-stub/index.html#getparentstuboftype"><span class="nf">getParentStubOfType</span></a><span class="p">(</span>p0<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="../-kotlin-block-string-template-entry-stub/index.html#getparentstuboftype">E</a><span class="o">?</span><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> <a href="../-kotlin-block-string-template-entry-stub/index.html#getparentstuboftype">E</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`getPsi`](../-kotlin-block-string-template-entry-stub/index.md#getpsi)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-kotlin-block-string-template-entry-stub/index.html#getpsi"><span class="nf">getPsi</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="index.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### isEquivalentTo

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-kotlin-block-string-template-entry-stub/index.html#isequivalentto"><span class="nf">isEquivalentTo</span></a><span class="p">(</span>other<span class="o">: </span><a href="index.html">KotlinStubElement</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether two stubs have equivalent types and properties. Doesn't compare children stubs or any other tree structure details.

<strong>Note</strong>: This method shouldn't be used outside of compiler internals. Stubs from different files aren't supposed to be comparable, that's why `equals` / `hashCode` are not implemented, as they would lead to incorrect behavior.


</div>

</div>
