---
tags:
 - jvm
title: "sortModifiers"
---

# sortModifiers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="sort-modifiers.html"><span class="nf">sortModifiers</span></a><span class="p">(</span>modifiers<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the given [`modifiers`](sort-modifiers.md) reordered into the canonical order used by the Kotlin code style. Tokens that are not recognized as modifier keywords are placed at the end.


</div>

</div>
