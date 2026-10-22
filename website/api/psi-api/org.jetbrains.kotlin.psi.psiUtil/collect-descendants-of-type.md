---
tags:
 - jvm
title: "collectDescendantsOfType"
---

# collectDescendantsOfType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="collect-descendants-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="collect-descendants-of-type.html"><span class="nf">collectDescendantsOfType</span></a><span class="p">(</span><span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="collect-descendants-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="collect-descendants-of-type.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Collects this element and all descendants of type [`T`](collect-descendants-of-type.md) satisfying [`predicate`](collect-descendants-of-type.md) into a list in post-order.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="collect-descendants-of-type.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="collect-descendants-of-type.html"><span class="nf">collectDescendantsOfType</span></a><span class="p">(</span><span class="kd">crossinline </span>canGoInside<span class="o">: </span><span class="p">(</span>PsiElement<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span><span class="kd">noinline </span>predicate<span class="o">: </span><span class="p">(</span><a href="collect-descendants-of-type.html">T</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="collect-descendants-of-type.html">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Collects this element and all descendants of type [`T`](collect-descendants-of-type.md) satisfying [`predicate`](collect-descendants-of-type.md) into a list in post-order. [`canGoInside`](collect-descendants-of-type.md) controls traversal into children but does not prevent the current element from being collected.


</div>

</div>
