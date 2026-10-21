---
tags:
 - jvm
title: "KtStubbedPsiUtil"
---

# KtStubbedPsiUtil

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KtStubbedPsiUtil</a>
</span></code></pre></div>Static helpers for navigating the Kotlin PSI in a way that also works over stubs. 

The platform's PsiTreeUtil operates on the AST tree, which forces a stub-backed element to be parsed. The methods here (such as [`getContainingDeclaration`](index.md#getcontainingdeclaration) and [`getPsiOrStubParent`](index.md#getpsiorstubparent)) instead walk the stub hierarchy when one is available, avoiding unnecessary parsing.


</div>

## Companion functions
### getContainingDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getcontainingdeclaration"><span class="nf">getContainingDeclaration</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="../-kt-declaration/index.html">KtDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest enclosing [`KtDeclaration`](../-kt-declaration/index.md) of the given element (excluding the element itself), or `#!java null` if there is none.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#getcontainingdeclaration">T</a><span class="o"> : </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="o">?</span><span class="o">> </span><a href="index.html#getcontainingdeclaration"><span class="nf">getContainingDeclaration</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span>PsiElement<span class="p">, </span><span class="se">@</span><span class="se">NotNull</span> declarationClass<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="index.html#getcontainingdeclaration">T</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="index.html#getcontainingdeclaration">T</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest enclosing [`KtDeclaration`](../-kt-declaration/index.md) of the given element that is an instance of `#!java declarationClass` (excluding the element itself), or `#!java null` if there is none.


</div>

</div>
### getPsiOrStubParent

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#getpsiorstubparent">T</a><span class="o"> : </span><a href="../-kt-element/index.html">KtElement</a><span class="o">?</span><span class="o">> </span><a href="index.html#getpsiorstubparent"><span class="nf">getPsiOrStubParent</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span>PsiElement<span class="p">, </span>
    <span class="se">@</span><span class="se">NotNull</span> declarationClass<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="index.html#getpsiorstubparent">T</a><span class="o">></span><span class="p">, </span>
    strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
<span class="p">)</span><span class="o">: </span><a href="index.html#getpsiorstubparent">T</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest parent of the given element assignable to `#!java declarationClass`, or `#!java null` if there is none. When `#!java strict` is `#!java false`, the element itself is also considered a candidate. 

When the element is backed by a stub, its stub hierarchy is walked instead of the AST, avoiding parsing; otherwise this falls back to getParentOfType.


</div>

</div>
### getStubOrPsiChild

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#getstuborpsichild">T</a><span class="o"> : </span><a href="../-kt-element/index.html">KtElement</a><span class="o">?</span><span class="o">> </span><a href="index.html#getstuborpsichild"><span class="nf">getStubOrPsiChild</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span><a href="../-kt-element-impl-stub/index.html">KtElementImplStub</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="p">, </span>
    <span class="se">@</span><span class="se">NotNull</span> types<span class="o">: </span>TokenSet<span class="p">, </span>
    <span class="se">@</span><span class="se">NotNull</span> factory<span class="o">: </span>ArrayFactory<span class="o"><</span><a href="index.html#getstuborpsichild">T</a><span class="o">></span>
<span class="p">)</span><span class="o">: </span><a href="index.html#getstuborpsichild">T</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the first child of the given element whose type is in `#!java types`, or `#!java null` if there is none. Stub children are used when the element is backed by a stub, avoiding parsing; otherwise its PSI children are traversed. The `#!java factory` produces the typed array used to collect the matching children.


</div>

</div>
