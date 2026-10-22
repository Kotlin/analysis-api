---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.signatures"
---

# org.jetbrains.kotlin.analysis.api.signatures
## Types
### [`KaCallableSignature`](-ka-callable-signature/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><span class="kd">out </span><a href="-ka-callable-signature/index.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

A use-site signature for a [`callable symbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md). Compared to the symbol, the signature carries additional use-site type information.


</div>

</div>
### [`KaFunctionSignature`](-ka-function-signature/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-function-signature/index.html">KaFunctionSignature</a><span class="o"><</span><span class="kd">out </span><a href="-ka-function-signature/index.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">></span> : <a href="-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="-ka-function-signature/index.html">S</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A [`callable signature`](-ka-callable-signature/index.md) of a [`function symbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md).


</div>

</div>
### [`KaVariableSignature`](-ka-variable-signature/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-variable-signature/index.html">KaVariableSignature</a><span class="o"><</span><span class="kd">out </span><a href="-ka-variable-signature/index.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a><span class="o">></span> : <a href="-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="-ka-variable-signature/index.html">S</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A [`callable signature`](-ka-callable-signature/index.md) of a [`variable symbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.md).


</div>

</div>
## Functions
### [`asSignature`](as-signature.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><span class="o"><</span><a href="as-signature.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">> </span><a href="as-signature.html">S</a><span class="p">.</span><a href="as-signature.html"><span class="nf">asSignature</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="as-signature.html">S</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Creates a new [`KaCallableSignature`](-ka-callable-signature/index.md) for the given symbol and leaves all types unsubstituted.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><span class="o"><</span><a href="as-signature.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">> </span><a href="as-signature.html">S</a><span class="p">.</span><a href="as-signature.html"><span class="nf">asSignature</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-function-signature/index.html">KaFunctionSignature</a><span class="o"><</span><a href="as-signature.html">S</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Creates a new [`KaFunctionSignature`](-ka-function-signature/index.md) for the given symbol and leaves all types unsubstituted.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><span class="o"><</span><a href="as-signature.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a><span class="o">> </span><a href="as-signature.html">S</a><span class="p">.</span><a href="as-signature.html"><span class="nf">asSignature</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-variable-signature/index.html">KaVariableSignature</a><span class="o"><</span><a href="as-signature.html">S</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Creates a new [`KaVariableSignature`](-ka-variable-signature/index.md) for the given symbol and leaves all types unsubstituted.


</div>

</div>
### [`substitute`](substitute.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><span class="o"><</span><a href="substitute.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">> </span><a href="substitute.html">S</a><span class="p">.</span><a href="substitute.html"><span class="nf">substitute</span></a><span class="p">(</span>substitutor<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="p">)</span><span class="o">: </span><a href="-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="substitute.html">S</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Applies a [`substitutor`](substitute.md) to the given symbol and returns a [`KaCallableSignature`](-ka-callable-signature/index.md) with substituted types.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><span class="o"><</span><a href="substitute.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">> </span><a href="substitute.html">S</a><span class="p">.</span><a href="substitute.html"><span class="nf">substitute</span></a><span class="p">(</span>substitutor<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="p">)</span><span class="o">: </span><a href="-ka-function-signature/index.html">KaFunctionSignature</a><span class="o"><</span><a href="substitute.html">S</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Applies a [`substitutor`](substitute.md) to the given symbol and returns a [`KaFunctionSignature`](-ka-function-signature/index.md) with substituted types.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><span class="o"><</span><a href="substitute.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a><span class="o">> </span><a href="substitute.html">S</a><span class="p">.</span><a href="substitute.html"><span class="nf">substitute</span></a><span class="p">(</span>substitutor<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="p">)</span><span class="o">: </span><a href="-ka-variable-signature/index.html">KaVariableSignature</a><span class="o"><</span><a href="substitute.html">S</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Applies a [`substitutor`](substitute.md) to the given symbol and returns a [`KaVariableSignature`](-ka-variable-signature/index.md) with substituted types.


</div>

</div>
