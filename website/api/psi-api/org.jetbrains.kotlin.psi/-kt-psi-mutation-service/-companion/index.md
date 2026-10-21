---
tags:
 - jvm
title: "Companion"
---

# Companion

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">Companion</a>
</span></code></pre></div>
</div>

## Functions
### getInstance

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="se">JvmStatic</span></a>
<span class="kd">fun </span><a href="index.html#getinstance"><span class="nf">getInstance</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../index.html">KtPsiMutationService</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the registered Kotlin PSI mutation service.

**Throws**



[`IllegalStateException`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-state-exception/index.html)

:   if the service is not registered.





</div>

</div>
### getInstanceOrNull

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="se">JvmStatic</span></a>
<span class="kd">fun </span><a href="index.html#getinstanceornull"><span class="nf">getInstanceOrNull</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../index.html">KtPsiMutationService</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the registered Kotlin PSI mutation service, or `null` if the environment does not provide one.


</div>

</div>
