---
tags:
 - jvm
title: "KaCallableReturnTypeFilter"
---

# KaCallableReturnTypeFilter

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaCallableReturnTypeFilter</a>
</span></code></pre></div>#### Inheritors


 - [`ALWAYS`](-a-l-w-a-y-s/index.md)
 - [`NO_UNIT_FOR_FUNCTIONS`](-n-o_-u-n-i-t_-f-o-r_-f-u-n-c-t-i-o-n-s/index.md)



</div>

## Types
### [`ALWAYS`](-a-l-w-a-y-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-a-l-w-a-y-s/index.html">ALWAYS</a> : <a href="index.html">KaCallableReturnTypeFilter</a>
</span></code></pre></div>
</div>

</div>
### [`NO_UNIT_FOR_FUNCTIONS`](-n-o_-u-n-i-t_-f-o-r_-f-u-n-c-t-i-o-n-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o_-u-n-i-t_-f-o-r_-f-u-n-c-t-i-o-n-s/index.html">NO_UNIT_FOR_FUNCTIONS</a> : <a href="index.html">KaCallableReturnTypeFilter</a>
</span></code></pre></div>
</div>

</div>
## Functions
### shouldRenderReturnType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#shouldrenderreturntype"><span class="nf">shouldRenderReturnType</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a>
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
