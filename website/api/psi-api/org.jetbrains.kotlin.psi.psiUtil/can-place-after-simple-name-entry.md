---
tags:
 - jvm
title: "canPlaceAfterSimpleNameEntry"
---

# canPlaceAfterSimpleNameEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="can-place-after-simple-name-entry.html"><span class="nf">canPlaceAfterSimpleNameEntry</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if placing text after a `$name` simple-name template entry would not accidentally extend the name, that is, [`element`](can-place-after-simple-name-entry.md) does not begin with an identifier character.


</div>

</div>
