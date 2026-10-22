---
tags:
 - jvm
title: "ValueArgument"
---

# ValueArgument

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">ValueArgument</a>
</span></code></pre></div>Represents a single argument passed in a call, such as `foo(1, message = "hi", *array)`.

A value argument carries the argument expression, an optional argument name (for named arguments), and an optional spread element (for `*`-spread arguments). It is not itself a [`KtElement`](../-kt-element/index.md); use [`asElement`](../-lambda-argument/index.md#aselement) to obtain the underlying PSI element. Besides the regular PSI-backed [`KtValueArgument`](../-kt-value-argument/index.md), synthetic implementations exist for modeling arguments of callable references.

#### Inheritors


 - [`KtValueArgument`](../-kt-value-argument/index.md)
 - [`FakePositionalValueArgumentForCallableReference`](../-fake-positional-value-argument-for-callable-reference/index.md)
 - [`FakeImplicitSpreadValueArgumentForCallableReference`](../-fake-implicit-spread-value-argument-for-callable-reference/index.md)
 - [`LambdaArgument`](../-lambda-argument/index.md)



</div>

## Properties
### isSpread

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../-lambda-argument/index.html#isspread">isSpread</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

`true` if this is a spread argument (`*array`).

**See also**



 - [`getSpreadElement`](../-lambda-argument/index.md#getspreadelement)



</div>

</div>
## Functions
### asElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-lambda-argument/index.html#aselement"><span class="nf">asElement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the underlying PSI element that this argument corresponds to.


</div>

</div>
### getArgumentExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-lambda-argument/index.html#getargumentexpression"><span class="nf">getArgumentExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the argument expression, or `null` if it is missing in incomplete code.


</div>

</div>
### getArgumentName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-lambda-argument/index.html#getargumentname"><span class="nf">getArgumentName</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-value-argument-name/index.html">ValueArgumentName</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the argument name for a named argument (`name = value`), or `null` if this argument is positional.


</div>

</div>
### getSpreadElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-lambda-argument/index.html#getspreadelement"><span class="nf">getSpreadElement</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>LeafPsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the `*` spread token for a spread argument (`foo(*array)`, which passes an array as a series of vararg arguments), or `null` if this argument is not spread.


</div>

</div>
### isExternal

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-lambda-argument/index.html#isexternal"><span class="nf">isExternal</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if the argument is located outside of the call element, as with the range in a `when` condition with a subject: `when (a) { in c -> }`.


</div>

</div>
### isNamed

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-lambda-argument/index.html#isnamed"><span class="nf">isNamed</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if this is a named argument (`name = value`).


</div>

</div>
