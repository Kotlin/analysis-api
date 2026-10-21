---
tags:
 - jvm
title: "scopeContext"
---

# scopeContext

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="scope-context.html"><span class="nf">scopeContext</span></a><span class="p">(</span>position<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="-ka-scope-context/index.html">KaScopeContext</a>
</span></code></pre></div>
</div>


<div markdown>

Computes the lexical scope context for a given [`position`](scope-context.md) in the [`KtFile`](../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md). The scope context includes all scopes that are relevant for the given position, together with all available implicit receivers.


</div>

</div>
