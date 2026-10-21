---
tags:
 - jvm
title: "kaModule"
---

# kaModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="ka-module.html"><span class="nf">kaModule</span></a><span class="p">(</span>useSiteModule<span class="o">: </span><a href="-ka-module/index.html">KaModule</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaModule`](-ka-module/index.md) for a given this in the context of the [`useSiteModule`](ka-module.md).

#### See also


 - [`KaModuleProvider.module`](-ka-module-provider/index.md#module)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span>PsiElement<span class="p">.</span><a href="ka-module.html">kaModule</a><span class="o">: </span><a href="-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaModule`](-ka-module/index.md) for a given this in the context of the session's [`useSiteModule`](../org.jetbrains.kotlin.analysis.api.session/use-site-module.md).

#### See also


 - [`KaModuleProvider.module`](-ka-module-provider/index.md#module)



</div>

</div>
