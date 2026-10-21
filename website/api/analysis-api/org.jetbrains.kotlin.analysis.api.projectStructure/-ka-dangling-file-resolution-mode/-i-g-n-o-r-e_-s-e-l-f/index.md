---
tags:
 - jvm
title: "IGNORE_SELF"
---

# IGNORE_SELF

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="index.html">IGNORE_SELF</a>

</span></code></pre></div>Resolve only to declarations in the original file or module by default. Ignore all non-local declarations in the dangling file during resolution. The mode is only supported for single-file dangling file modules.

If a declaration from the dangling file is explicitly requested through the Analysis API, it will be resolved from the dangling file. [`IGNORE_SELF`](index.md) only affects declarations which are internally resolved in the course of an analysis request, for example when getting the type of an expression or resolving a call.

The mode is offered for optimization purposes, as it removes the need to re-analyze the declarations in the dangling file and instead reuses the (possibly) resolved declarations from the original file.


</div>

## Properties
### [`name`](../../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`ordinal`](../../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md#ordinal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.html#ordinal">ordinal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
