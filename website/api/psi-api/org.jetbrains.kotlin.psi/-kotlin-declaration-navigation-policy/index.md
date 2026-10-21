---
tags:
 - jvm
title: "KotlinDeclarationNavigationPolicy"
---

# KotlinDeclarationNavigationPolicy

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinDeclarationNavigationPolicy</a>
</span></code></pre></div>A service that maps a [`KtDeclaration`](../-kt-declaration/index.md) between its "original" and its "navigation" element.

These may differ when a declaration is viewed through more than one PSI representation — for example, a declaration decompiled from a library exposes a synthetic element for display while the source (or another canonical element) is the target of navigation. Implementations back [`com.intellij.psi.PsiElement.getNavigationElement`](../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.md#getnavigationelement) and [`com.intellij.psi.PsiElement.getOriginalElement`](../../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.md#getoriginalelement) for Kotlin declarations.


</div>

## Functions
### getNavigationElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getnavigationelement"><span class="nf">getNavigationElement</span></a><span class="p">(</span>declaration<span class="o">: </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="p">)</span><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the element that navigation (Go to Declaration and similar) should land on for the given declaration.


</div>

</div>
### getOriginalElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getoriginalelement"><span class="nf">getOriginalElement</span></a><span class="p">(</span>declaration<span class="o">: </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="p">)</span><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the canonical/original element for the given declaration, or the declaration itself if there is no distinct original.


</div>

</div>
