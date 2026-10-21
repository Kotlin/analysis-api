---
tags:
 - jvm
title: "KaCallableMemberCall"
---

# KaCallableMemberCall

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">KaCallableMemberCall</a><span class="o"><</span><a href="index.html">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">, </span><a href="index.html">C</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="index.html">S</a><span class="o">></span><span class="o">></span> : <a href="../-ka-call/index.html">KaCall</a>
</span></code></pre></div>A call to a function, or a simple/compound access to a property.

#### Inheritors


 - [`KaFunctionCall`](../-ka-function-call/index.md)
 - [`KaVariableAccessCall`](../-ka-variable-access-call/index.md)



</div>

## Properties
### partiallyAppliedSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#partiallyappliedsymbol">partiallyAppliedSymbol</a><span class="o">: </span><a href="../-ka-partially-applied-symbol/index.html">KaPartiallyAppliedSymbol</a><span class="o"><</span><a href="index.html">S</a><span class="p">, </span><a href="index.html">C</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A symbol wrapper for the callee, containing a substituted declaration signature (parameter types for functions, return type for functions and properties), and the actual dispatch receiver.


</div>

</div>
### symbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><span class="o"><</span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">, </span><a href="../-ka-partially-applied-symbol/index.html#symbol">C</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a><span class="o">></span><span class="o">> </span><a href="index.html">KaCallableMemberCall</a><span class="o"><</span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a><span class="p">, </span><a href="../-ka-partially-applied-symbol/index.html#symbol">C</a><span class="o">></span><span class="p">.</span><a href="../-ka-partially-applied-symbol/index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) of the [`KaCallableMemberCall`](index.md)'s callee.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><span class="o"><</span><a href="../-ka-simple-call/index.html#symbol">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">, </span><a href="../-ka-simple-call/index.html#symbol">C</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="../-ka-simple-call/index.html#symbol">S</a><span class="o">></span><span class="o">> </span><a href="../-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><a href="../-ka-simple-call/index.html#symbol">S</a><span class="p">, </span><a href="../-ka-simple-call/index.html#symbol">C</a><span class="o">></span><span class="p">.</span><a href="../-ka-simple-call/index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-simple-call/index.html#symbol">S</a>
</span></code></pre></div>
</div>


<div markdown>

The resolved [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) of the [`KaSimpleCall`](../-ka-simple-call/index.md).

This is a short-cut for [`KaCallableSignature.symbol`](../../org.jetbrains.kotlin.analysis.api.signatures/-ka-variable-signature/index.md#symbol).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><span class="o"><</span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">, </span><a href="../-ka-partially-applied-symbol/index.html#symbol">C</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a><span class="o">></span><span class="o">> </span><a href="../-ka-partially-applied-symbol/index.html">KaPartiallyAppliedSymbol</a><span class="o"><</span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a><span class="p">, </span><a href="../-ka-partially-applied-symbol/index.html#symbol">C</a><span class="o">></span><span class="p">.</span><a href="../-ka-partially-applied-symbol/index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a>
</span></code></pre></div>
</div>


<div markdown>

The [`callable symbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) which the [`KaPartiallyAppliedSymbol`](../-ka-partially-applied-symbol/index.md) represents. While the information contained in a partially applied symbol is not exhaustive (e.g. applied functions are missing value arguments), the symbol of the callable which is called is definite.


</div>

</div>
### [`token`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#token)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#token">token</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaLifetimeToken`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md) which determines the lifetime of the lifetime owner.


</div>

</div>
### typeArgumentsMapping

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#typeargumentsmapping">typeArgumentsMapping</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A map of inferred type arguments. If type placeholders were used, the actual inferred type will be used as a value. The keys for this map are from [`partiallyAppliedSymbol`](index.md#partiallyappliedsymbol)'s type parameters.

In case of a resolution or inference error, the map might be empty.


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
