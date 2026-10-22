---
tags:
 - jvm
title: "KtNamed"
---

# KtNamed

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KtNamed</a>
</span></code></pre></div>Represents an element that carries a Kotlin Name, such as a named declaration or a label. 

Unlike getName, which returns a raw [`String`](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html), this interface exposes the name as a structured Name that already accounts for backtick-quoted identifiers.

#### Inheritors


 - [`KtNamedDeclaration`](../-kt-named-declaration/index.md)



</div>

## Functions
### getNameAsName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="../-kt-type-parameter-list-owner/index.html#getnameasname"><span class="nf">getNameAsName</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>Name
</span></code></pre></div>
</div>


<div markdown>

Returns the name of this element as a Name, or `#!java null` if the element is anonymous or its name is missing (for example, in incomplete or erroneous code).


</div>

</div>
