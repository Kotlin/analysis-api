---
tags:
 - jvm
title: "KtFileClassProvider"
---

# KtFileClassProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KtFileClassProvider</a>
</span></code></pre></div>A service that computes the Java light classes exposed by a [`KtFile`](../-kt-file/index.md) (its file facade class and top-level class declarations).

It backs [`KtFile.getClasses`](../-kt-type-code-fragment/index.md#getclasses); the concrete implementation is supplied by the surrounding platform, since light-class generation depends on the analysis environment.


</div>

## Functions
### getFileClasses

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getfileclasses"><span class="nf">getFileClasses</span></a><span class="p">(</span>file<span class="o">: </span><a href="../-kt-file/index.html">KtFile</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>PsiClass<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the Java light classes contributed by the given file, or an empty array if none are available.


</div>

</div>
