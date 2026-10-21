---
tags:
 - jvm
title: "PsiChildRange"
---

# PsiChildRange

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">class </span><a href="index.html">PsiChildRange</a><span class="p">(</span><span class="kd">val </span>first<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">, </span><span class="kd">val </span>last<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span>PsiElement<span class="o">> </span>
</span></code></pre></div>A contiguous range of sibling PSI elements, from [`first`](index.md#first) to [`last`](index.md#last) inclusive, iterable as a [`Sequence`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html).

Both endpoints must share the same parent. A range is empty when [`first`](index.md#first) is `null` (in which case [`last`](index.md#last) is `null` too); otherwise it always contains at least [`first`](index.md#first).


</div>

## Constructors
### PsiChildRange

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>first<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">, </span>last<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Properties
### first

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#first">first</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### isEmpty

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#isempty">isEmpty</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

`true` if this range contains no elements.


</div>

</div>
### last

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#last">last</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### textRange

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html">PsiChildRange</a><span class="p">.</span><a href="index.html#textrange">textRange</a><span class="o">: </span>TextRange<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The text range spanning this child range, or `null` if the range is empty.


</div>

</div>
## Functions
### getText

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">PsiChildRange</a><span class="p">.</span><a href="index.html#gettext"><span class="nf">getText</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the concatenated text of all elements in this range, or an empty string if the range is empty.


</div>

</div>
### iterator

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">operator override </span><span class="kd">fun </span><a href="index.html#iterator"><span class="nf">iterator</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/index.html">Iterator</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### trimWhiteSpaces

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">PsiChildRange</a><span class="p">.</span><a href="index.html#trimwhitespaces"><span class="nf">trimWhiteSpaces</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="index.html">PsiChildRange</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a copy of this range with leading and trailing whitespace elements removed.


</div>

</div>
