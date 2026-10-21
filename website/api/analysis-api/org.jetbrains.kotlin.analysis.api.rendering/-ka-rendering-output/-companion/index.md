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

## Functions
### plainString

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#plainstring"><span class="nf">plainString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../index.html">KaRenderingOutput</a>
</span></code></pre></div>
</div>


<div markdown>

A simple [`KaRenderingOutput`](../index.md) that accumulates rendered text into a plain [`String`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), ignoring all [`KaTextAttribute`](../../-ka-text-attribute/index.md)s. Uses four spaces for member indentation.

The rendered text is available via [`toString`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/to-string.html).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#plainstring"><span class="nf">plainString</span></a><span class="p">(</span>indentationUnit<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../index.html">KaRenderingOutput</a>
</span></code></pre></div>
</div>


<div markdown>

A simple [`KaRenderingOutput`](../index.md) that accumulates rendered text into a plain [`String`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), ignoring all [`KaTextAttribute`](../../-ka-text-attribute/index.md)s. Uses the [`indentationUnit`](index.md#plainstring) for member indentation.

The rendered text is available via [`toString`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/to-string.html).


</div>

</div>
