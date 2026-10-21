---
tags:
 - jvm
title: "resolveToSymbol"
---

# resolveToSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.html">KtReference</a><span class="p">.</span><a href="resolve-to-symbol.html"><span class="nf">resolveToSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtReference`](../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.md) to a symbol.

Returns `null` if the reference cannot be resolved, or resolves to multiple symbols due to being ambiguous.

Consider using the [new resolution API](https://kotlin.github.io/analysis-api/migrating-resolution-api.html).

#### See also


 - [`KtResolvable.tryResolveSymbols`](../org.jetbrains.kotlin.analysis.api.resolution/try-resolve-symbols.md)
 - [`KtResolvableCall.tryResolveCall`](../org.jetbrains.kotlin.analysis.api.resolution/try-resolve-call.md)



</div>

</div>
