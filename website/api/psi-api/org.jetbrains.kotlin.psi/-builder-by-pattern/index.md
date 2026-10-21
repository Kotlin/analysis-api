---
tags:
 - jvm
title: "BuilderByPattern"
---

# BuilderByPattern

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">BuilderByPattern</a><span class="o"><</span><a href="index.html">TElement</a><span class="o">></span>
</span></code></pre></div>A builder that assembles a [`createByPattern`](../create-by-pattern.md) pattern step by step, appending fixed text, expressions, type references, names, and child ranges in order and tracking their placeholders automatically.

Use it through the `KtPsiFactory.build*` entry points (such as [`KtPsiFactory.buildExpression`](../-kt-psi-factory/index.md#buildexpression)), which create a builder, run the configuration block on it, and parse the result into an element.

#### Type Parameters


 - TElement: the kind of element the assembled pattern produces





</div>

## Constructors
### BuilderByPattern

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

**Type Parameters**



 - TElement: the kind of element the assembled pattern produces





</div>

</div>
## Functions
### appendChildRange

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#appendchildrange"><span class="nf">appendChildRange</span></a><span class="p">(</span>range<span class="o">: </span><a href="../../org.jetbrains.kotlin.psi.psiUtil/-psi-child-range/index.html">PsiChildRange</a><span class="p">)</span><span class="o">: </span><a href="index.html">BuilderByPattern</a><span class="o"><</span><a href="index.html">TElement</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Appends the given child [`range`](index.md#appendchildrange) as an argument.


</div>

</div>
### appendExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#appendexpression"><span class="nf">appendExpression</span></a><span class="p">(</span>expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="index.html">BuilderByPattern</a><span class="o"><</span><a href="index.html">TElement</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Appends [`expression`](index.md#appendexpression) as an argument, or nothing if it is `null`.


</div>

</div>
### appendExpressions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#appendexpressions"><span class="nf">appendExpressions</span></a><span class="p">(</span>expressions<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/index.html">Iterable</a><span class="o"><</span><a href="../-kt-expression/index.html">KtExpression</a><span class="o">?</span><span class="o">></span><span class="p">, </span>separator<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o"> = </span><span class="s">","</span><span class="p">)</span><span class="o">: </span><a href="index.html">BuilderByPattern</a><span class="o"><</span><a href="index.html">TElement</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Appends the given [`expressions`](index.md#appendexpressions), placing [`separator`](index.md#appendexpressions) between each pair of iterable positions. A `null` position emits no expression but still participates in separator placement, so `null` entries can produce leading, trailing, or repeated separators.


</div>

</div>
### appendFixedText

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#appendfixedtext"><span class="nf">appendFixedText</span></a><span class="p">(</span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">BuilderByPattern</a><span class="o"><</span><a href="index.html">TElement</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Appends literal text to the pattern verbatim (no placeholder).


</div>

</div>
### appendName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#appendname"><span class="nf">appendName</span></a><span class="p">(</span>name<span class="o">: </span>Name<span class="p">)</span><span class="o">: </span><a href="index.html">BuilderByPattern</a><span class="o"><</span><a href="index.html">TElement</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Appends [`name`](index.md#appendname) as an argument, rendered as text.


</div>

</div>
### appendNonFormattedText

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#appendnonformattedtext"><span class="nf">appendNonFormattedText</span></a><span class="p">(</span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">BuilderByPattern</a><span class="o"><</span><a href="index.html">TElement</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Appends [`text`](index.md#appendnonformattedtext) as an argument spliced in as-is, without reformatting.


</div>

</div>
### appendTypeReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#appendtypereference"><span class="nf">appendTypeReference</span></a><span class="p">(</span>typeRef<span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="index.html">BuilderByPattern</a><span class="o"><</span><a href="index.html">TElement</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Appends [`typeRef`](index.md#appendtypereference) as an argument, or nothing if it is `null`.


</div>

</div>
### create

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#create"><span class="nf">create</span></a><span class="p">(</span>factory<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><span class="kd">out </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span><a href="index.html">TElement</a><span class="p">)</span><span class="o">: </span><a href="index.html">TElement</a>
</span></code></pre></div>
</div>


<div markdown>

Builds the element by passing the assembled pattern and arguments to [`factory`](index.md#create).


</div>

</div>
