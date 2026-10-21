---
tags:
 - jvm
title: "org.jetbrains.kotlin.kdoc.psi.impl"
---

# org.jetbrains.kotlin.kdoc.psi.impl
## Types
### [`KDocElementImpl`](-k-doc-element-impl/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-k-doc-element-impl/index.html">KDocElementImpl</a> : ASTWrapperPsiElement, <a href="../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.html">KDocElement</a>
</span></code></pre></div>
</div>


<div markdown>

Base implementation of [`KDocElement`](../org.jetbrains.kotlin.kdoc.psi.api/-k-doc-element/index.md), wrapping the corresponding AST node.

</div>

</div>
### [`KDocLink`](-k-doc-link/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-k-doc-link/index.html">KDocLink</a> : <a href="../org.jetbrains.kotlin.psi/-kt-element-impl/index.html">KtElementImpl</a>
</span></code></pre></div>
</div>


<div markdown>

A Markdown link inside a KDoc comment that references a declaration by its (possibly qualified) name.


</div>

</div>
### [`KDocName`](-k-doc-name/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-k-doc-name/index.html">KDocName</a> : <a href="../org.jetbrains.kotlin.psi/-kt-element-impl/index.html">KtElementImpl</a>, <a href="../org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a>
</span></code></pre></div>
</div>


<div markdown>

A single part of a qualified name in the tag subject or link.


</div>

</div>
### [`KDocSection`](-k-doc-section/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-k-doc-section/index.html">KDocSection</a> : <a href="-k-doc-tag/index.html">KDocTag</a>, ContributedReferenceHost, PsiLanguageInjectionHost
</span></code></pre></div>
</div>


<div markdown>

The part of a doc comment which describes a single class, method or property produced by the element being documented. For example, the doc comment of a class can have sections for the class itself, its primary constructor and each of the properties defined in the primary constructor.


</div>

</div>
### [`KDocTag`](-k-doc-tag/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-k-doc-tag/index.html">KDocTag</a> : <a href="-k-doc-element-impl/index.html">KDocElementImpl</a>
</span></code></pre></div>
</div>


<div markdown>

A block tag inside a KDoc comment (such as `@param`, `@return`, or `@throws`) together with the content that follows it.


</div>

</div>
