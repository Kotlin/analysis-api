---
tags:
 - jvm
title: "Kind"
---

# Kind

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">Kind</a>
</span></code></pre></div>Determines the kind of access to the [`variable`](../index.md) (read or write), alongside additional information

#### See also


 - [`KaVariableAccessCall`](../index.md)


#### Inheritors


 - [`Read`](-read/index.md)
 - [`Write`](-write/index.md)



</div>

## Types
### [`Read`](-read/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-read/index.html">Read</a> : <a href="index.html">KaVariableAccessCall.Kind</a>
</span></code></pre></div>
</div>


<div markdown>

The [`variable access`](../index.md) reads the variable.


</div>

</div>
### [`Write`](-write/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-write/index.html">Write</a> : <a href="index.html">KaVariableAccessCall.Kind</a>
</span></code></pre></div>
</div>


<div markdown>

The [`variable access`](../index.md) writes to the variable.


</div>

</div>
