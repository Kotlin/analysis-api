---
tags:
 - jvm
title: "org.jetbrains.kotlin.psi.typeRefHelpers"
---

# org.jetbrains.kotlin.psi.typeRefHelpers
## Functions
### [`getTypeReference`](get-type-reference.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="get-type-reference.html"><span class="nf">getTypeReference</span></a><span class="p">(</span>declaration<span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-callable-declaration/index.html">KtCallableDeclaration</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the type reference written after the `:` of the given callable [`declaration`](get-type-reference.md) (its explicit return type or property type), or `null` if the type is not written explicitly.


</div>

</div>
