---
tags:
 - jvm
title: "KaSubstitutorBuilder"
---

# KaSubstitutorBuilder

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KaSubstitutorBuilder</a><span class="p">(</span><span class="kd">val </span>token<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a><span class="p">)</span> : <a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor-builder/index.html">KaSubstitutorBuilder</a>
</span></code></pre></div><strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.types.KaSubstitutorBuilder</strong>`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor-builder/index.md)<strong> instead.</strong>

A DSL builder for [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md). Instances are created internally by [`buildSubstitutor`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/index.md).

#### See also


 - [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md)



</div>

## Constructors
### KaSubstitutorBuilder

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>token<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### mappings

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#mappings">mappings</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A map of the type substitutions that have so far been accumulated by the builder.


</div>

</div>
### token

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#token">token</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaLifetimeToken`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md) which determines the lifetime of the lifetime owner.


</div>

</div>
## Functions
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`isValid`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#isvalid)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#isvalid"><span class="nf">isValid</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the lifetime owner is still valid, i.e. we are still in the scope of the lifetime owner's regular lifetime.


</div>

</div>
### substitution

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#substitution"><span class="nf">substitution</span></a><span class="p">(</span>typeParameter<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">, </span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Adds a new [`typeParameter`](index.md#substitution) ->[`type`](index.md#substitution) substitution to the substitutor.

If there already was a substitution with a [`typeParameter`](index.md#substitution), the function replaces the corresponding substitution with a new one.


</div>

</div>
### substitutions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#substitutions"><span class="nf">substitutions</span></a><span class="p">(</span>substitutions<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Adds new [`KaTypeParameterSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.md) ->[`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) substitutions to the substitutor.

If there already was a substitution with a [`KaTypeParameterSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.md), the function replaces the corresponding substitution with a new one.


</div>

</div>
### [`withValidityAssertion`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion"><span class="nf">withValidityAssertion</span></a><span class="p">(</span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a>
</span></code></pre></div>
</div>


<div markdown>

Executes [`action`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion) only if the [`KaLifetimeOwner`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.md) is still [`valid`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md#isvalid) and [`accessible`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md#isaccessible). Otherwise, throws a validity exception based on the concrete violation.


</div>

</div>
