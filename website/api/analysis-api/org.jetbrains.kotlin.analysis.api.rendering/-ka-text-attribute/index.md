---
tags:
 - jvm
title: "KaTextAttribute"
---

# KaTextAttribute

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaTextAttribute</a>
</span></code></pre></div>Describes the semantic role of a fragment of rendered text, e.g. for syntax highlighting.

#### Inheritors


 - [`Keyword`](-keyword/index.md)
 - [`Punctuation`](-punctuation/index.md)
 - [`Identifier`](-identifier/index.md)
 - [`Whitespace`](-whitespace/index.md)
 - [`StringLiteral`](-string-literal/index.md)
 - [`NumberLiteral`](-number-literal/index.md)
 - [`Comment`](-comment/index.md)
 - [`Symbol`](-symbol/index.md)



</div>

## Types
### [`Comment`](-comment/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-comment/index.html">Comment</a> : <a href="index.html">KaTextAttribute</a>
</span></code></pre></div>
</div>


<div markdown>

A comment, such as `/* = kotlin.String */`.


</div>

</div>
### [`Identifier`](-identifier/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-identifier/index.html">Identifier</a> : <a href="index.html">KaTextAttribute</a>
</span></code></pre></div>
</div>


<div markdown>

An identifier, such as a declaration or type name. See [`Symbol`](-symbol/index.md) when the referenced symbol is known.


</div>

</div>
### [`Keyword`](-keyword/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-keyword/index.html">Keyword</a> : <a href="index.html">KaTextAttribute</a>
</span></code></pre></div>
</div>


<div markdown>

A hard keyword or soft/modifier keyword, such as `fun`, `val`, or `suspend`.


</div>

</div>
### [`NumberLiteral`](-number-literal/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-number-literal/index.html">NumberLiteral</a> : <a href="index.html">KaTextAttribute</a>
</span></code></pre></div>
</div>


<div markdown>

A numeric literal, such as `42`, `2f`, or `3u`.


</div>

</div>
### [`Punctuation`](-punctuation/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-punctuation/index.html">Punctuation</a> : <a href="index.html">KaTextAttribute</a>
</span></code></pre></div>
</div>


<div markdown>

Punctuation, such as `:`, `,`, or `?`.


</div>

</div>
### [`StringLiteral`](-string-literal/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-string-literal/index.html">StringLiteral</a> : <a href="index.html">KaTextAttribute</a>
</span></code></pre></div>
</div>


<div markdown>

A string or character literal, such as `"text"` or `'c'`.


</div>

</div>
### [`Symbol`](-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-symbol/index.html">Symbol</a><span class="p">(</span><span class="kd">val </span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">)</span> : <a href="index.html">KaTextAttribute</a>, <a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

An identifier that references a known [`symbol`](-symbol/index.md#symbol). Only attached when [`KaRenderingOption.LinkSymbols`](../-ka-rendering-option/-companion/index.md#linksymbols) is enabled.


</div>

</div>
### [`Whitespace`](-whitespace/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-whitespace/index.html">Whitespace</a> : <a href="index.html">KaTextAttribute</a>
</span></code></pre></div>
</div>


<div markdown>

Whitespace that is not a line break.


</div>

</div>
