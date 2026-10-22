---
tags:
 - jvm
title: "hasBody"
---

# hasBody

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="has-body.html"><span class="nf">hasBody</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this declaration is a function or property that defines a body.

Only [`KtFunction`](../org.jetbrains.kotlin.psi/-kt-function/index.md) and [`KtProperty`](../org.jetbrains.kotlin.psi/-kt-property/index.md) are considered; every other declaration, including a [`KtPropertyAccessor`](../org.jetbrains.kotlin.psi/-kt-property-accessor/index.md), returns `false`.


</div>

</div>
