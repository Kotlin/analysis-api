---
tags:
 - jvm
title: "org.jetbrains.kotlin.psi.utils"
---

# org.jetbrains.kotlin.psi.utils
## Types
### [`OperatorTokens`](-operator-tokens/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-operator-tokens/index.html">OperatorTokens</a>
</span></code></pre></div>
</div>


<div markdown>

Maps between Kotlin operator tokens and the operator-convention function names they desugar to (for example, `+` maps to `plus`), and groups the operator tokens by category (unary, binary, assignment, comparison, and so on).


</div>

</div>
## Functions
### [`hasFloatNumericLiteralSuffix`](has-float-numeric-literal-suffix.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="has-float-numeric-literal-suffix.html"><span class="nf">hasFloatNumericLiteralSuffix</span></a><span class="p">(</span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether the [`text`](has-float-numeric-literal-suffix.md) representation of a number literal has a float number suffix.


</div>

</div>
### [`hasIllegallyPositionedUnderscore`](has-illegally-positioned-underscore.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="has-illegally-positioned-underscore.html"><span class="nf">hasIllegallyPositionedUnderscore</span></a><span class="p">(</span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>isFloatingPoint<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether the given [`text`](has-illegally-positioned-underscore.md) contains an underscore in an illegal position. Underscores are allowed only between digits, not at the beginning or end of the number or one of its parts.


</div>

</div>
### [`hasLongNumericLiteralSuffix`](has-long-numeric-literal-suffix.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="has-long-numeric-literal-suffix.html"><span class="nf">hasLongNumericLiteralSuffix</span></a><span class="p">(</span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether the [`text`](has-long-numeric-literal-suffix.md) representation of a number literal has a long number suffix.


</div>

</div>
### [`hasUnsignedLongNumericLiteralSuffix`](has-unsigned-long-numeric-literal-suffix.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="has-unsigned-long-numeric-literal-suffix.html"><span class="nf">hasUnsignedLongNumericLiteralSuffix</span></a><span class="p">(</span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether the [`text`](has-unsigned-long-numeric-literal-suffix.md) representation of a number literal has both a long and an unsigned number suffix.


</div>

</div>
### [`hasUnsignedNumericLiteralSuffix`](has-unsigned-numeric-literal-suffix.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="has-unsigned-numeric-literal-suffix.html"><span class="nf">hasUnsignedNumericLiteralSuffix</span></a><span class="p">(</span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether the [`text`](has-unsigned-numeric-literal-suffix.md) representation of a number literal has an unsigned number suffix.


</div>

</div>
### [`parseBooleanLiteral`](parse-boolean-literal.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="parse-boolean-literal.html"><span class="nf">parseBooleanLiteral</span></a><span class="p">(</span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`text`](parse-boolean-literal.md), either `true` or `false`, to a boolean value.


</div>

</div>
### [`parseNumericLiteral`](parse-numeric-literal.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="parse-numeric-literal.html"><span class="nf">parseNumericLiteral</span></a><span class="p">(</span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>isFloatingPointLiteral<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-number/index.html">Number</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Parses the [`text`](parse-numeric-literal.md) representation of a number literal into a [`Number`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-number/index.html) instance.


</div>

</div>
### [`toConstantExpressionElementType`](to-constant-expression-element-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi.stubs/-constant-value-kind/index.html">ConstantValueKind</a><span class="p">.</span><a href="to-constant-expression-element-type.html"><span class="nf">toConstantExpressionElementType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin/-kt-node-type/index.html">KtNodeType</a>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`ConstantValueKind`](../org.jetbrains.kotlin.psi.stubs/-constant-value-kind/index.md) to the corresponding com.intellij.psi.tree.IElementType.


</div>

</div>
