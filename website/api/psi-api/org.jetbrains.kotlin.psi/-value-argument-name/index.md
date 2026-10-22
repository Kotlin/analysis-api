---
tags:
 - jvm
title: "ValueArgumentName"
---

# ValueArgumentName

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">ValueArgumentName</a>
</span></code></pre></div>The name of a named [`ValueArgument`](../-value-argument/index.md) (the `name` in `name = value`).

#### Inheritors


 - [`KtValueArgumentName`](../-kt-value-argument-name/index.md)



</div>

## Properties
### asName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#asname">asName</a><span class="o">: </span>Name
</span></code></pre></div>
</div>


<div markdown>

The argument name as a Name.


</div>

</div>
### referenceExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#referenceexpression">referenceExpression</a><span class="o">: </span><a href="../-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The reference expression that carries the name, or `null` if it is absent.


</div>

</div>
