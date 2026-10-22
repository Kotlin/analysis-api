---
tags:
 - jvm
title: "substitute"
---

# substitute

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><span class="o"><</span><a href="substitute.html">S</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">> </span><a href="substitute.html">S</a><span class="p">.</span><a href="substitute.html"><span class="nf">substitute</span></a><span class="p">(</span>substitutor<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="p">)</span><span class="o">: </span><a href="-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="substitute.html">S</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Applies a [`substitutor`](substitute.md) to the given symbol and returns a [`KaCallableSignature`](-ka-callable-signature/index.md) with substituted types.

#### See also


 - [`KaSubstitutor.substitute`](../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/-empty/index.md#substitute)



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

#### See also


 - [`KaSubstitutor.substitute`](../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/-empty/index.md#substitute)



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

#### See also


 - [`KaSubstitutor.substitute`](../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/-empty/index.md#substitute)



</div>

</div>
