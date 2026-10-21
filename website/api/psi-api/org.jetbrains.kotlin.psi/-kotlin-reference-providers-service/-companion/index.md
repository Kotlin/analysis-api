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
### getInstance

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="se">JvmStatic</span></a>
<span class="kd">fun </span><a href="index.html#getinstance"><span class="nf">getInstance</span></a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span><span class="o">: </span><a href="../index.html">KotlinReferenceProvidersService</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the service registered in the given [`project`](index.md#getinstance), or a no-op fallback if none is registered.


</div>

</div>
### getReferencesFromProviders

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="se">JvmStatic</span></a>
<span class="kd">fun </span><a href="index.html#getreferencesfromproviders"><span class="nf">getReferencesFromProviders</span></a><span class="p">(</span>psiElement<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>PsiReference<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A convenience shortcut that resolves the service for the element's project and returns its references.


</div>

</div>
