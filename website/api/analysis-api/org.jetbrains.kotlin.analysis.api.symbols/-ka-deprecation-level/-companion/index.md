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

## Properties
### ERROR

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#error">ERROR</a><span class="o">: </span><a href="../index.html">KaDeprecationLevel</a>
</span></code></pre></div>
</div>


<div markdown>

The deprecated symbol can still be referenced, but a compilation error is reported at the call site.

Corresponds to [`DeprecationLevel.ERROR`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-deprecation-level/-e-r-r-o-r/index.html).


</div>

</div>
### HIDDEN

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#hidden">HIDDEN</a><span class="o">: </span><a href="../index.html">KaDeprecationLevel</a>
</span></code></pre></div>
</div>


<div markdown>

The deprecated symbol is no longer visible to new code. Existing compiled code that references it will still work, but new source code cannot reference it.

Corresponds to [`DeprecationLevel.HIDDEN`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-deprecation-level/-h-i-d-d-e-n/index.html).


</div>

</div>
### WARNING

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#warning">WARNING</a><span class="o">: </span><a href="../index.html">KaDeprecationLevel</a>
</span></code></pre></div>
</div>


<div markdown>

The deprecated symbol can still be used, but a warning is reported at the call site.

Corresponds to [`DeprecationLevel.WARNING`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-deprecation-level/-w-a-r-n-i-n-g/index.html).


</div>

</div>
