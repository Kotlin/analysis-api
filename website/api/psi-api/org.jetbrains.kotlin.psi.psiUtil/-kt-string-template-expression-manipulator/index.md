---
tags:
 - jvm
title: "KtStringTemplateExpressionManipulator"
---

# KtStringTemplateExpressionManipulator

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KtStringTemplateExpressionManipulator</a> : AbstractElementManipulator<span class="o"><</span><a href="../../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="o">> </span>
</span></code></pre></div>The ElementManipulator of [`KtStringTemplateExpression`](../../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.md), which edits the content of a string literal, e.g., when a language fragment injected into the string is edited or a reference contributed to the string is renamed.

The IntelliJ Kotlin plugin registers it as the element manipulator of [`KtStringTemplateExpression`](../../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.md). By default, it edits the [`content`](../get-content-range.md) between the quotes. In a single-quoted string, it escapes quotes, backslashes, and control characters in the new content, but keeps interpolated expressions (`$name` and `${...}`) as is. In a raw string, it inserts the new content as is.


</div>

## Constructors
### KtStringTemplateExpressionManipulator

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Functions
### getRangeInElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getrangeinelement"><span class="nf">getRangeInElement</span></a><span class="p">(</span>element<span class="o">: </span><a href="../../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="p">)</span><span class="o">: </span>TextRange
</span></code></pre></div>
</div>

</div>
### [`handleContentChange`](index.md#handlecontentchange)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#handlecontentchange"><span class="nf">handleContentChange</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="../../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="p">, </span>newContent<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#handlecontentchange"><span class="nf">handleContentChange</span></a><span class="p">(</span>
    element<span class="o">: </span><a href="../../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="p">, </span>
    range<span class="o">: </span>TextRange<span class="p">, </span>
    newContent<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
