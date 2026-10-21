---
tags:
 - jvm
title: "org.jetbrains.kotlin.kdoc.psi.api"
---

# org.jetbrains.kotlin.kdoc.psi.api
## Types
### [`KDoc`](-k-doc/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-k-doc/index.html">KDoc</a> : PsiDocCommentBase, <a href="-k-doc-element/index.html">KDocElement</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a KDoc documentation comment attached to a declaration.


</div>

</div>
### [`KDocCommentDescriptor`](-k-doc-comment-descriptor/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.psi/-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-k-doc-comment-descriptor/index.html">KDocCommentDescriptor</a>
</span></code></pre></div>
</div>


<div markdown>

A view of a KDoc comment.


</div>

</div>
### [`KDocElement`](-k-doc-element/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-k-doc-element/index.html">KDocElement</a> : PsiElement
</span></code></pre></div>
</div>


<div markdown>

A marker interface implemented by all elements of a KDoc comment's PSI tree.

</div>

</div>
