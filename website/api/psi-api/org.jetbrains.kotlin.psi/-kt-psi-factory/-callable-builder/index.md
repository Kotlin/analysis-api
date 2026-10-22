---
tags:
 - jvm
title: "CallableBuilder"
---

# CallableBuilder

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">CallableBuilder</a><span class="p">(</span>target<span class="o">: </span><a href="-target/index.html">KtPsiFactory.CallableBuilder.Target</a><span class="p">)</span>
</span></code></pre></div>A fluent builder for a function, constructor, or read-only property declaration string. The available steps and their order depend on the [`Target`](-target/index.md); call [`asString`](index.md#asstring) to obtain the resulting text, then pass it to the matching `create*` method.

Calls are expected in state order. Order and target violations are checked only when JVM assertions are enabled.


</div>

## Constructors
### CallableBuilder

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>target<span class="o">: </span><a href="-target/index.html">KtPsiFactory.CallableBuilder.Target</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
### [`State`](-state/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-state/index.html">State</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-state/index.html">KtPsiFactory.CallableBuilder.State</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

The stages in the expected order for building a callable.


</div>

</div>
### [`Target`](-target/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-target/index.html">Target</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-target/index.html">KtPsiFactory.CallableBuilder.Target</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

The kind of callable being built.


</div>

</div>
## Functions
### asString

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#asstring"><span class="nf">asString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the assembled callable declaration text.


</div>

</div>
### blockBody

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#blockbody"><span class="nf">blockBody</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> body<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.CallableBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends a block body containing the given [`body`](index.md#blockbody) text (a getter block for a property).


</div>

</div>
### getterExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#getterexpression"><span class="nf">getterExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> expression<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>breakLine<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.CallableBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends an expression-body getter (`get() = expression`). Read-only properties only.


</div>

</div>
### initializer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#initializer"><span class="nf">initializer</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> body<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.CallableBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends an initializer (`= body`). Read-only properties only.


</div>

</div>
### lazyBody

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#lazybody"><span class="nf">lazyBody</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> body<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.CallableBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends a lazy delegate (`by kotlin.lazy { body }`). Read-only properties only.


</div>

</div>
### modifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#modifier"><span class="nf">modifier</span></a><span class="p">(</span>modifier<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.CallableBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends [`modifier`](index.md#modifier) verbatim. No separator is added between repeated calls, so callers must include any required whitespace. This is expected to be called before [`typeParams`](index.md#typeparams).


</div>

</div>
### name

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#name"><span class="nf">name</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o"> = </span>CONSTRUCTOR_NAME<span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.CallableBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends the callable name (defaulting to the constructor pseudo-name), opening the parameter list for functions and constructors.


</div>

</div>
### noReturnType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#noreturntype"><span class="nf">noReturnType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.CallableBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Closes the parameter list (if any) without appending a return type.


</div>

</div>
### param

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#param"><span class="nf">param</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> type<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> defaultValue<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="o"> = </span>null
<span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.CallableBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends a value parameter with the given [`name`](index.md#param), [`type`](index.md#param), and optional [`defaultValue`](index.md#param). Functions and constructors only.


</div>

</div>
### receiver

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#receiver"><span class="nf">receiver</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> receiverType<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.CallableBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends the extension receiver type.


</div>

</div>
### returnType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#returntype"><span class="nf">returnType</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> type<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.CallableBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Closes the parameter list (if any) and appends the return [`type`](index.md#returntype).


</div>

</div>
### superDelegation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#superdelegation"><span class="nf">superDelegation</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> argumentList<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.CallableBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends a `: super(...)` delegation call with the given [`argumentList`](index.md#superdelegation). Constructors only.


</div>

</div>
### transform

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#transform"><span class="nf">transform</span></a><span class="p">(</span>f<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/-string-builder/index.html">StringBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Applies an arbitrary transformation to the underlying text buffer.


</div>

</div>
### typeConstraints

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#typeconstraints"><span class="nf">typeConstraints</span></a><span class="p">(</span>values<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.CallableBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends the `where` clause type constraints, if any. Not allowed for constructors.


</div>

</div>
### typeParams

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#typeparams"><span class="nf">typeParams</span></a><span class="p">(</span>values<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">></span><span class="o"> = </span>emptyList()<span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.CallableBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends the declaration keyword (`fun`/`val`) and the type parameters, if any.


</div>

</div>
