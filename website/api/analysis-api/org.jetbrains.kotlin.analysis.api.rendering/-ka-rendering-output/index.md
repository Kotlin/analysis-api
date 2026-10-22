---
tags:
 - jvm
title: "KaRenderingOutput"
---

# KaRenderingOutput

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaRenderingOutput</a>
</span></code></pre></div>A destination for rendered output. A [`KaRenderer`](../-ka-renderer/index.md) writes text fragments, each tagged with [`KaTextAttribute`](../-ka-text-attribute/index.md)s that describe its semantic role, so an output may add syntax highlighting, produce plain text, or ignore the attributes entirely.

All methods return `this` to allow chaining.


</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Functions
### append

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#append"><span class="nf">append</span></a><span class="p">(</span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>attributes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../-ka-text-attribute/index.html">KaTextAttribute</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="index.html">KaRenderingOutput</a>
</span></code></pre></div>
</div>


<div markdown>

Appends [`text`](index.md#append) tagged with the given [`attributes`](index.md#append).


</div>

</div>
### append

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">KaRenderingOutput</a><span class="p">.</span><a href="index.html#append"><span class="nf">append</span></a><span class="p">(</span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span><span class="kd">vararg </span>attributes<span class="o">: </span><a href="../-ka-text-attribute/index.html">KaTextAttribute</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaRenderingOutput</a>
</span></code></pre></div>
</div>


<div markdown>

Appends [`text`](index.md#append) tagged with the given [`attributes`](index.md#append).


</div>

</div>
### enter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#enter"><span class="nf">enter</span></a><span class="p">(</span>piece<span class="o">: </span><a href="../-ka-piece/index.html">KaPiece</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Called when rendering of [`piece`](index.md#enter) begins. Everything appended until the balancing [`leave`](index.md#leave) call is the output of that piece; the calls nest when a piece renders other pieces.


</div>

</div>
### group

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#group"><span class="nf">group</span></a><span class="p">(</span>children<span class="o">: </span><a href="../-ka-piece/index.html">KaPiece</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="p">, </span>block<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Renders a region which groups a sequence of child pieces of the [`children`](index.md#group) kind, such as a value parameter list grouping its [`KaPiece.ValueParameter`](../-ka-piece/-companion/index.md#valueparameter)s.

[`block`](index.md#group) renders the entire content of the group, including the enclosing brackets and the separators between the children. The hook lets an output lay the group out as a whole, e.g. to fold it.

An output which needs no special treatment of groups invokes [`block`](index.md#group) as it is.


</div>

</div>
### identifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>context<span class="o">: </span><a href="../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">)</span>
<span class="kd">fun </span><a href="index.html">KaRenderingOutput</a><span class="p">.</span><a href="index.html#identifier"><span class="nf">identifier</span></a><span class="p">(</span>name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaRenderingOutput</a>
</span></code></pre></div><div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>context<span class="o">: </span><a href="../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">)</span>
<span class="kd">fun </span><a href="index.html">KaRenderingOutput</a><span class="p">.</span><a href="index.html#identifier"><span class="nf">identifier</span></a><span class="p">(</span>name<span class="o">: </span>Name<span class="p">, </span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaRenderingOutput</a>
</span></code></pre></div>
</div>


<div markdown>

Renders [`name`](index.md#identifier) as an identifier, linked to [`symbol`](index.md#identifier) when [`KaRenderingOption.LinkSymbols`](../-ka-rendering-option/-companion/index.md#linksymbols) is enabled.


</div>

</div>
### keyword

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>context<span class="o">: </span><a href="../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">)</span>
<span class="kd">fun </span><a href="index.html">KaRenderingOutput</a><span class="p">.</span><a href="index.html#keyword"><span class="nf">keyword</span></a><span class="p">(</span>token<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.lexer/-kt-keyword-token/index.html">KtKeywordToken</a><span class="p">, </span>trailingSpace<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">)</span><span class="o">: </span><a href="index.html">KaRenderingOutput</a>
</span></code></pre></div>
</div>


<div markdown>

Renders [`token`](index.md#keyword) unless it is filtered out by [`KaRenderingOption.AllowedKeywords`](../-ka-rendering-option/-companion/index.md#allowedkeywords).

**Parameters**



 - trailingSpace: whether a space is appended after the keyword. Pass `false` when the keyword is directly followed by punctuation, as in `constructor(`.





</div>

</div>
### leave

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#leave"><span class="nf">leave</span></a><span class="p">(</span>piece<span class="o">: </span><a href="../-ka-piece/index.html">KaPiece</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Called when rendering of [`piece`](index.md#leave) ends. Balances the corresponding [`enter`](index.md#enter) call, also when rendering fails with an exception.


</div>

</div>
### newLine

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#newline"><span class="nf">newLine</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="index.html">KaRenderingOutput</a>
</span></code></pre></div>
</div>


<div markdown>

Starts a new line at the current indentation level.


</div>

</div>
### popIndent

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#popindent"><span class="nf">popIndent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="index.html">KaRenderingOutput</a>
</span></code></pre></div>
</div>


<div markdown>

Decreases the indentation level. Must be balanced with a preceding [`pushIndent`](index.md#pushindent).


</div>

</div>
### punctuation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>context<span class="o">: </span><a href="../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">)</span>
<span class="kd">fun </span><a href="index.html">KaRenderingOutput</a><span class="p">.</span><a href="index.html#punctuation"><span class="nf">punctuation</span></a><span class="p">(</span>text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaRenderingOutput</a>
</span></code></pre></div>
</div>


<div markdown>

Appends [`text`](index.md#punctuation) as a [`KaTextAttribute.Punctuation`](../-ka-text-attribute/-punctuation/index.md) fragment, such as `(` or `.`.


</div>

</div>
### pushIndent

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#pushindent"><span class="nf">pushIndent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="index.html">KaRenderingOutput</a>
</span></code></pre></div>
</div>


<div markdown>

Increases the indentation level applied at the start of subsequent lines.


</div>

</div>
### space

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#space"><span class="nf">space</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="index.html">KaRenderingOutput</a>
</span></code></pre></div>
</div>


<div markdown>

Append a single space unless the last rendered character was a whitespace.


</div>

</div>
### withIndent

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="index.html">KaRenderingOutput</a><span class="p">.</span><a href="index.html#withindent"><span class="nf">withIndent</span></a><span class="p">(</span>block<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Runs [`block`](index.md#withindent) with the indentation level increased, balancing [`pushIndent`](index.md#pushindent) with [`popIndent`](index.md#popindent).


</div>

</div>
