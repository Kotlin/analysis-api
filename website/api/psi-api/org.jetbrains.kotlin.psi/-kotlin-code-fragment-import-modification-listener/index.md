---
tags:
 - jvm
title: "KotlinCodeFragmentImportModificationListener"
---

# KotlinCodeFragmentImportModificationListener

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="kd">interface </span><a href="index.html">KotlinCodeFragmentImportModificationListener</a>
</span></code></pre></div>A listener notified when the imports of a [`KtCodeFragment`](../-kt-code-fragment/index.md) are modified.


</div>

## Functions
### onCodeFragmentImportsModification

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#oncodefragmentimportsmodification"><span class="nf">onCodeFragmentImportsModification</span></a><span class="p">(</span>codeFragment<span class="o">: </span><a href="../-kt-code-fragment/index.html">KtCodeFragment</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Called after the imports of [`codeFragment`](index.md#oncodefragmentimportsmodification) have changed.


</div>

</div>
