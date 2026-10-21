---
tags:
 - jvm
title: "KaSuperTypesFilter"
---

# KaSuperTypesFilter

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="kd">interface </span><a href="index.html">KaSuperTypesFilter</a>
</span></code></pre></div>#### Inheritors


 - [`NO_DEFAULT_TYPES`](-n-o_-d-e-f-a-u-l-t_-t-y-p-e-s/index.md)
 - [`NO_ANY_FOR_INTERFACES`](-n-o_-a-n-y_-f-o-r_-i-n-t-e-r-f-a-c-e-s/index.md)
 - [`ALL`](-a-l-l/index.md)
 - [`NONE`](-n-o-n-e/index.md)



</div>

## Types
### [`ALL`](-a-l-l/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-a-l-l/index.html">ALL</a> : <a href="index.html">KaSuperTypesFilter</a>
</span></code></pre></div>
</div>

</div>
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
### [`NO_ANY_FOR_INTERFACES`](-n-o_-a-n-y_-f-o-r_-i-n-t-e-r-f-a-c-e-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o_-a-n-y_-f-o-r_-i-n-t-e-r-f-a-c-e-s/index.html">NO_ANY_FOR_INTERFACES</a> : <a href="index.html">KaSuperTypesFilter</a>
</span></code></pre></div>
</div>

</div>
### [`NO_DEFAULT_TYPES`](-n-o_-d-e-f-a-u-l-t_-t-y-p-e-s/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o_-d-e-f-a-u-l-t_-t-y-p-e-s/index.html">NO_DEFAULT_TYPES</a> : <a href="index.html">KaSuperTypesFilter</a>
</span></code></pre></div>
</div>

</div>
### [`NONE`](-n-o-n-e/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-n-o-n-e/index.html">NONE</a> : <a href="index.html">KaSuperTypesFilter</a>
</span></code></pre></div>
</div>

</div>
## Functions
### filter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#filter"><span class="nf">filter</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    superType<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a>
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
