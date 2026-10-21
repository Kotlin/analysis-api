---
tags:
 - jvm
title: "KaNonConstantInitializerValue"
---

# KaNonConstantInitializerValue

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KaNonConstantInitializerValue</a><span class="p">(</span><span class="kd">val </span>initializerPsi<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span><span class="p">)</span> : <a href="../-ka-initializer-value/index.html">KaInitializerValue</a>
</span></code></pre></div>An initializer value which cannot be represented as a [compile-time constant](https://kotlinlang.org/docs/properties.html#compile-time-constants).

The Analysis API is unable to evaluate the expression statically and thus cannot provide a [`KaConstantValue`](../../org.jetbrains.kotlin.analysis.api.base/-ka-constant-value/index.md) for the initializer.

#### See also


 - [`KaConstantInitializerValue`](../-ka-constant-initializer-value/index.md)



</div>

## Constructors
### KaNonConstantInitializerValue

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>initializerPsi<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### initializerPsi

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#initializerpsi">initializerPsi</a><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`KtExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md) backing the initializer. It may be `null` if the property/variable comes from a non-source file.


</div>

</div>
