---
tags:
 - jvm
title: "KotlinStringLiteralTextEscaper"
---

# KotlinStringLiteralTextEscaper

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KotlinStringLiteralTextEscaper</a><span class="p">(</span>host<span class="o">: </span><a href="../-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="p">)</span> : LiteralTextEscaper<span class="o"><</span><a href="../-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="o">> </span>
</span></code></pre></div>A LiteralTextEscaper for Kotlin string literals, enabling language injection into them.

It decodes the raw literal text of a [`KtStringTemplateExpression`](../-kt-string-template-expression/index.md) into the string value it denotes (resolving escape sequences) and maintains a mapping between offsets in the decoded value and offsets in the host PSI, so that an injected language can be edited and its ranges translated back to the original source.


</div>

## Constructors
### KotlinStringLiteralTextEscaper

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>host<span class="o">: </span><a href="../-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### isOneLine

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#isoneline"><span class="nf">isOneLine</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#isoneline">isOneLine</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### relevantTextRange

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#relevanttextrange">relevantTextRange</a><span class="o">: </span>TextRange
</span></code></pre></div>
</div>

</div>
## Functions
### decode

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#decode"><span class="nf">decode</span></a><span class="p">(</span>rangeInsideHost<span class="o">: </span>TextRange<span class="p">, </span>outChars<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/-string-builder/index.html">StringBuilder</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### getOffsetInHost

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getoffsetinhost"><span class="nf">getOffsetInHost</span></a><span class="p">(</span>offsetInDecoded<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">, </span>rangeInsideHost<span class="o">: </span>TextRange<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### getRelevantTextRange

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getrelevanttextrange"><span class="nf">getRelevantTextRange</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>TextRange
</span></code></pre></div>
</div>

</div>
