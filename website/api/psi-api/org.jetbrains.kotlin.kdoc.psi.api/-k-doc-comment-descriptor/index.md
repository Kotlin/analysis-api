---
tags:
 - jvm
title: "KDocCommentDescriptor"
---

# KDocCommentDescriptor

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.psi/-kt-implementation-detail/index.html">KtImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KDocCommentDescriptor</a>
</span></code></pre></div>A view of a KDoc comment.

This is part of a non-public API intended for use only by IDE and Dokka. Current implementation is based on the original `findKDoc` logic from Kotlin IDE Plugin.

 - If the symbol owns the KDoc, [`primaryTag`](index.md#primarytag) is the KDoc's default section and [`additionalSections`](index.md#additionalsections) contains all sections of that KDoc (including the default one).


 - For a primary constructor, if the enclosing class KDoc has an `@constructor` section, that section is used as [`primaryTag`](index.md#primarytag), and [`additionalSections`](index.md#additionalsections) contains the sections that include `@param` tags from the class's KDoc.


 - In some cases KDoc for a symbol may be extracted from the KDoc of a parent element. Examples:


 - a property-parameter of the primary constructor;


 - a type parameter;


 - a property of a class/object referenced with a @property tag in the class/object KDoc.



</div>

## Properties
### additionalSections

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#additionalsections">additionalSections</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-section/index.html">KDocSection</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Other sections from the same KDoc as [`primaryTag`](index.md#primarytag) that may provide additional context


</div>

</div>
### primaryTag

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#primarytag">primaryTag</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.kdoc.psi.impl/-k-doc-tag/index.html">KDocTag</a>
</span></code></pre></div>
</div>


<div markdown>

Primary tag/section tag/section if the KDoc that is relevant for the symbol


</div>

</div>
