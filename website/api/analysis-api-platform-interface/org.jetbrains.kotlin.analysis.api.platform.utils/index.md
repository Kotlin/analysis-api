---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.platform.utils"
---

# org.jetbrains.kotlin.analysis.api.platform.utils
## Types
### [`SublistMerger`](-sublist-merger/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-sublist-merger/index.html">SublistMerger</a><span class="o"><</span><a href="-sublist-merger/index.html">A</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">(</span>initialElements<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-sublist-merger/index.html">A</a><span class="o">></span><span class="p">, </span><span class="kd">val </span>destination<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-list/index.html">MutableList</a><span class="o"><</span><a href="-sublist-merger/index.html">A</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

With each call to [`merge`](-sublist-merger/index.md#merge), [`SublistMerger`](-sublist-merger/index.md) can merge all elements of a specific (reified) type into a single element using a supplied constructor and then add it to [`destination`](-sublist-merger/index.md#destination). Unmerged elements are added to [`destination`](-sublist-merger/index.md#destination) using [`finish`](-sublist-merger/index.md#finish).


</div>

</div>
## Properties
### [`KOTLIN_JAVA_ELEMENT_FINDER_CLASS_NAME`](-k-o-t-l-i-n_-j-a-v-a_-e-l-e-m-e-n-t_-f-i-n-d-e-r_-c-l-a-s-s_-n-a-m-e.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">const </span><span class="kd">val </span><a href="-k-o-t-l-i-n_-j-a-v-a_-e-l-e-m-e-n-t_-f-i-n-d-e-r_-c-l-a-s-s_-n-a-m-e.html">KOTLIN_JAVA_ELEMENT_FINDER_CLASS_NAME</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
## Functions
### [`forEachNonKotlinPsiElementFinder`](for-each-non-kotlin-psi-element-finder.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="for-each-non-kotlin-psi-element-finder.html"><span class="nf">forEachNonKotlinPsiElementFinder</span></a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">, </span>action<span class="o">: </span><span class="p">(</span>PsiElementFinder<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`mergeInto`](merge-into.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="merge-into.html">A</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="merge-into.html">A</a><span class="o">></span><span class="p">.</span><a href="merge-into.html"><span class="nf">mergeInto</span></a><span class="p">(</span>destination<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-list/index.html">MutableList</a><span class="o"><</span><a href="merge-into.html">A</a><span class="o">></span><span class="p">, </span>f<span class="o">: </span><a href="-sublist-merger/index.html">SublistMerger</a><span class="o"><</span><a href="merge-into.html">A</a><span class="o">></span><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`mergeOnly`](merge-only.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="merge-only.html">A</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span><span class="kd">reified </span><a href="merge-only.html">R</a><span class="o"> : </span><a href="merge-only.html">A</a><span class="o">> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="merge-only.html">A</a><span class="o">></span><span class="p">.</span><a href="merge-only.html"><span class="nf">mergeOnly</span></a><span class="p">(</span><span class="kd">crossinline </span>create<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="merge-only.html">R</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span><a href="merge-only.html">A</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="merge-only.html">A</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`mergeWith`](merge-with.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="merge-with.html">A</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="merge-with.html">A</a><span class="o">></span><span class="p">.</span><a href="merge-with.html"><span class="nf">mergeWith</span></a><span class="p">(</span>f<span class="o">: </span><a href="-sublist-merger/index.html">SublistMerger</a><span class="o"><</span><a href="merge-with.html">A</a><span class="o">></span><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="merge-with.html">A</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
