---
tags:
 - jvm
title: "importingScopeContext"
---

# importingScopeContext

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="importing-scope-context.html">importingScopeContext</a><span class="o">: </span><a href="-ka-scope-context/index.html">KaScopeContext</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScopeContext`](-ka-scope-context/index.md) formed from all imports in the [`KtFile`](../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md).

By default, the scope context also includes default importing scopes, which can be filtered by [`KaScopeKind`](-ka-scope-kind/index.md).


</div>

</div>
