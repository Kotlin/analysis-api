---
tags:
 - jvm
title: "prevLeaf"
---

# prevLeaf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="prev-leaf.html"><span class="nf">prevLeaf</span></a><span class="p">(</span>skipEmptyElements<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the previous leaf element in the tree, or `null` if there is none. Empty leaves are skipped if [`skipEmptyElements`](prev-leaf.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="prev-leaf.html"><span class="nf">prevLeaf</span></a><span class="p">(</span>filter<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest preceding leaf that satisfies [`filter`](prev-leaf.md), or `null` if there is none.


</div>

</div>
