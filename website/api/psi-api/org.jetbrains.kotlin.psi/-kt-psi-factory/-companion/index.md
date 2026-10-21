---
tags:
 - jvm
title: "Companion"
---

# Companion

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">Companion</a>
</span></code></pre></div>
</div>

## Functions
### contextual

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="se">JvmStatic</span></a>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html"><span class="se">JvmOverloads</span></a>
<span class="kd">fun </span><a href="index.html#contextual"><span class="nf">contextual</span></a><span class="p">(</span>
    context<span class="o">: </span>PsiElement<span class="p">, </span>
    markGenerated<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">, </span>
    eventSystemEnabled<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span>
<span class="p">)</span><span class="o">: </span><a href="../index.html">KtPsiFactory</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a factory bound to the given [`context`](index.md#contextual) element. Files created by such a factory carry [`context`](index.md#contextual) as their analysis context, so the elements produced can be resolved as if they appeared at that location.


</div>

</div>
