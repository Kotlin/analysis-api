---
tags:
 - jvm
title: "createByPattern"
---

# createByPattern

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="create-by-pattern.html">TElement</a><span class="o"> : </span><a href="-kt-element/index.html">KtElement</a><span class="o">> </span><a href="create-by-pattern.html"><span class="nf">createByPattern</span></a><span class="p">(</span>
    pattern<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    <span class="kd">vararg </span>args<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span>
    reformat<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">, </span>
    factory<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o"> -> </span><a href="create-by-pattern.html">TElement</a>
<span class="p">)</span><span class="o">: </span><a href="create-by-pattern.html">TElement</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a PSI element from a textual [`pattern`](create-by-pattern.md) with `$0`, `$1`, … placeholders replaced by the corresponding [`args`](create-by-pattern.md).

The pattern is a piece of Kotlin source with numbered placeholders. [`String`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) and Name arguments are inserted as text before [`factory`](create-by-pattern.md) parses the pattern. PSI arguments are represented by parseable placeholder text and then structurally replace the corresponding nodes in the parsed result instead of being rendered as text.

Supported argument types are [`KtExpression`](-kt-expression/index.md), [`KtTypeReference`](-kt-type-reference/index.md), [`String`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), Name, and [`PsiChildRange`](../org.jetbrains.kotlin.psi.psiUtil/-psi-child-range/index.md).

For example, `psiFactory.createExpressionByPattern("$0 + $1", left, right)` creates an addition expression whose operands have the PSI structure of `left` and `right`.

Prefer the specialized entry points ([`KtPsiFactory.createExpressionByPattern`](-kt-psi-factory/index.md#createexpressionbypattern) and friends) when creating a known kind of element.

#### Parameters


 - reformat: whether to reformat the created element according to the code style


 - factory: parses the pattern with textual arguments and PSI placeholder text inserted




#### Throws


[`IllegalArgumentException`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html)

:   if the pattern is malformed, an argument is unsupported, the argument and placeholder counts differ, or a parsed placeholder cannot be matched to the expected PSI element type





</div>

</div>
