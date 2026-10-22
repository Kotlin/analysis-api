---
tags:
 - jvm
title: "isPublicApi"
---

# isPublicApi

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="is-public-api.html">isPublicApi</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the symbol is effectively public, including internal declarations with the [`PublishedApi`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-published-api/index.html) annotation.

In ['Explicit API' mode](https://github.com/Kotlin/KEEP/blob/master/proposals/explicit-api-mode.md), explicit visibility modifiers and explicit return types are required for such symbols.


</div>

</div>
