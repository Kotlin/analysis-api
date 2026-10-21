---
tags:
 - jvm
title: "StatementFilter"
---

# StatementFilter

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="index.html">StatementFilter</a>
</span></code></pre></div>Selects which statements of a block should be taken into account (for example, during analysis). The base implementation applies no filtering; subclasses may restrict the considered statements by overriding [`filter`](index.md#filter).


</div>

## Constructors
### StatementFilter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
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
## Properties
### filter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="index.html#filter">filter</a><span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A predicate that returns `true` for the statements to keep, or `null` to keep all statements.


</div>

</div>
## Functions
### filterStatements

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">StatementFilter</a><span class="p">.</span><a href="index.html#filterstatements"><span class="nf">filterStatements</span></a><span class="p">(</span>block<span class="o">: </span><a href="../../org.jetbrains.kotlin.psi/-kt-block-expression/index.html">KtBlockExpression</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the statements of [`block`](index.md#filterstatements) that pass this filter, or all of them if this filter keeps everything.


</div>

</div>
### getLastStatementInABlock

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">StatementFilter</a><span class="p">.</span><a href="index.html#getlaststatementinablock"><span class="nf">getLastStatementInABlock</span></a><span class="p">(</span>block<span class="o">: </span><a href="../../org.jetbrains.kotlin.psi/-kt-block-expression/index.html">KtBlockExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the last statement of [`block`](index.md#getlaststatementinablock) that passes this filter, or `null` if none do.


</div>

</div>
