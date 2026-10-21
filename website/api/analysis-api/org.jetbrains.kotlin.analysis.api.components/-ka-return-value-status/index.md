---
tags:
 - jvm
title: "KaReturnValueStatus"
---

# KaReturnValueStatus

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="index.html">KaReturnValueStatus</a>
</span></code></pre></div><strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.symbols.KaReturnValueStatus</strong>`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-return-value-status/index.md)<strong> instead.</strong>

The return value status of the function (should it be used, or can it be ignored).

#### See also


 - [`KaSymbolInformationProvider.returnValueStatus`](../-ka-symbol-information-provider/index.md#returnvaluestatus)


#### Inheritors


 - [`MustUse`](-must-use/index.md)
 - [`ExplicitlyIgnorable`](-explicitly-ignorable/index.md)
 - [`Unspecified`](-unspecified/index.md)



</div>

## Types
### [`ExplicitlyIgnorable`](-explicitly-ignorable/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">object </span><a href="-explicitly-ignorable/index.html">ExplicitlyIgnorable</a> : <a href="index.html">KaReturnValueStatus</a>
</span></code></pre></div>
</div>


<div markdown>

The return value of the function is declared as explicitly ignorable and should not be checked for usage.


</div>

</div>
### [`MustUse`](-must-use/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">object </span><a href="-must-use/index.html">MustUse</a> : <a href="index.html">KaReturnValueStatus</a>
</span></code></pre></div>
</div>


<div markdown>

The return value of the function must be checked for usage.


</div>

</div>
### [`Unspecified`](-unspecified/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">object </span><a href="-unspecified/index.html">Unspecified</a> : <a href="index.html">KaReturnValueStatus</a>
</span></code></pre></div>
</div>


<div markdown>

The return value status of the function is unspecified.


</div>

</div>
## Properties
### name

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="-unspecified/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
## Functions
### toString

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#tostring"><span class="nf">toString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
