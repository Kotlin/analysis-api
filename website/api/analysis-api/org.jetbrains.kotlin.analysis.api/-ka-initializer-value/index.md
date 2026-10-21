---
tags:
 - jvm
title: "KaInitializerValue"
---

# KaInitializerValue

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="index.html">KaInitializerValue</a>
</span></code></pre></div>A value of a property or variable initializer.

#### See also


 - [`KaPropertySymbol.initializer`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-synthetic-java-property-symbol/index.md#initializer)


#### Inheritors


 - [`KaConstantInitializerValue`](../-ka-constant-initializer-value/index.md)
 - [`KaNonConstantInitializerValue`](../-ka-non-constant-initializer-value/index.md)
 - [`KaConstantValueForAnnotation`](../-ka-constant-value-for-annotation/index.md)



</div>

## Properties
### initializerPsi

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#initializerpsi">initializerPsi</a><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`KtExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md) backing the initializer. It may be `null` if the property/variable comes from a non-source file.


</div>

</div>
