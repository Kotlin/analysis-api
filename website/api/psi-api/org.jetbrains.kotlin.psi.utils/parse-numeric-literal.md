---
tags:
 - jvm
title: "parseNumericLiteral"
---

# parseNumericLiteral

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="parse-numeric-literal.html"><span class="nf">parseNumericLiteral</span></a><span class="p">(</span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>isFloatingPointLiteral<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-number/index.html">Number</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Parses the [`text`](parse-numeric-literal.md) representation of a number literal into a [`Number`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-number/index.html) instance.

For integer literals, always returns a [`Long`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html) instance. For floating-point literals, returns either a [`Float`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html) or a [`Double`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html), depending on the literal precision. Returns `null` if the text is not a valid representation of a number literal.

#### Parameters


 - isFloatingPointLiteral: Specifies whether the number is floating-point (`Float` or `Double`) or integer (`Byte`, `Short`, `Int` or `Long`).





</div>

</div>
