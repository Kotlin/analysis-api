---
tags:
 - jvm
title: "PsiDiagnosticUtils"
---

# PsiDiagnosticUtils

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="index.html">PsiDiagnosticUtils</a>
</span></code></pre></div>Utilities for rendering the source location of PSI elements as human-readable strings for use in diagnostic and log messages.


</div>

## Constructors
### PsiDiagnosticUtils

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Types
### [`LineAndColumn`](-line-and-column/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-line-and-column/index.html">LineAndColumn</a>
</span></code></pre></div>
</div>


<div markdown>

A line and column position in a file, optionally carrying the text of the line.

</div>

</div>
### [`LineAndColumnRange`](-line-and-column-range/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-line-and-column-range/index.html">LineAndColumnRange</a>
</span></code></pre></div>
</div>


<div markdown>

A range spanning from a start to an end [`LineAndColumn`](-line-and-column/index.md) position.

</div>

</div>
## Companion functions
### atLocation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#atlocation"><span class="nf">atLocation</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a human-readable description of the source location of the given `#!java element` (its file plus line and column), falling back to an offset-based description if the element is invalid.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#atlocation"><span class="nf">atLocation</span></a><span class="p">(</span>expression<span class="o">: </span><a href="../../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a human-readable description of the source location of the given `#!java expression`.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#atlocation"><span class="nf">atLocation</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> node<span class="o">: </span>ASTNode<span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a human-readable description of the source location of the given AST `#!java node`.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#atlocation"><span class="nf">atLocation</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> file<span class="o">: </span>PsiFile<span class="p">, </span><span class="se">@</span><span class="se">NotNull</span> textRange<span class="o">: </span>TextRange<span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a human-readable description of the location of `#!java textRange` within `#!java file`.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#atlocation"><span class="nf">atLocation</span></a><span class="p">(</span>
    file<span class="o">: </span>PsiFile<span class="p">, </span>
    textRange<span class="o">: </span>TextRange<span class="p">, </span>
    document<span class="o">: </span>Document
<span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a human-readable description of the location of `#!java textRange` within `#!java file`, using the given `#!java document` to compute the line and column.


</div>

</div>
### offsetToLineAndColumn

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#offsettolineandcolumn"><span class="nf">offsetToLineAndColumn</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> document<span class="o">: </span>Document<span class="p">, </span>offset<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span><a href="-line-and-column/index.html">PsiDiagnosticUtils.LineAndColumn</a>
</span></code></pre></div>
</div>


<div markdown>

Converts a character `#!java offset` within `#!java document` to a [`LineAndColumn`](-line-and-column/index.md). If `#!java document` is `#!java null` or empty, the line is `#!java -1` and the column field contains the original `#!java offset`. For a nonempty document, `#!java offset` is expected to be within its text.


</div>

</div>
