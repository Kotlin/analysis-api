---
tags:
 - jvm
title: "Companion"
---

# Companion

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">Companion</a>
</span></code></pre></div>
</div>

## Properties
### TOKEN_TO_BINARY_PRECEDENCE_MAP

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#token_to_binary_precedence_map">TOKEN_TO_BINARY_PRECEDENCE_MAP</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.lexer/-kt-token/index.html">KtToken</a><span class="p">, </span><a href="../index.html">BinaryOperationPrecedence</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Maps each binary operator token to its [`BinaryOperationPrecedence`](../index.md) for O(1) lookup. Soft-keyword identifiers are not included; use [`TOKEN_TO_BINARY_PRECEDENCE_MAP_WITH_SOFT_IDENTIFIERS`](index.md#token_to_binary_precedence_map_with_soft_identifiers) when they are needed.


</div>

</div>
### TOKEN_TO_BINARY_PRECEDENCE_MAP_WITH_SOFT_IDENTIFIERS

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#token_to_binary_precedence_map_with_soft_identifiers">TOKEN_TO_BINARY_PRECEDENCE_MAP_WITH_SOFT_IDENTIFIERS</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.lexer/-kt-token/index.html">KtToken</a><span class="p">, </span><a href="../index.html">BinaryOperationPrecedence</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Defines a map, where each token is mapped on its binary precedence.<p>

It's used for fast lookup over binary precedences by a provided token. It works with O(1) complexity in a given use-site instead of O(N) where N is a number of binary precedences (currently 12).


</div>

</div>
