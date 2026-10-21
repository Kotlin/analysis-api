---
tags:
 - jvm
title: "KtDeclarationContainer"
---

# KtDeclarationContainer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KtDeclarationContainer</a>
</span></code></pre></div>Represents an element that contains a list of declarations, such as a file, a class or object body, or a script. 

This interface groups only the directly nested declarations; it does not recurse into them, and it does not include declarations synthesized by the compiler.

#### Inheritors


 - [`KtPureClassOrObject`](../-kt-pure-class-or-object/index.md)
 - [`KtClassBody`](../-kt-class-body/index.md)
 - [`KtClassOrObject`](../-kt-class-or-object/index.md)
 - [`KtCompanionBlock`](../-kt-companion-block/index.md)
 - [`KtScript`](../-kt-script/index.md)



</div>

## Functions
### getDeclarations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="se">@</span><span class="se">ReadOnly</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="../-kt-pure-class-or-object/index.html#getdeclarations"><span class="nf">getDeclarations</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/List.html">List</a><span class="o"><</span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the declarations directly contained in this element, in their source order. Returns an empty list if there are none.


</div>

</div>
