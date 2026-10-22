---
tags:
 - jvm
title: "findTypeAlias"
---

# findTypeAlias

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="find-type-alias.html"><span class="nf">findTypeAlias</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="-ka-type-alias-symbol/index.html">KaTypeAliasSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaTypeAliasSymbol`](-ka-type-alias-symbol/index.md) for the specified ClassId, or `null` if such a symbol cannot be found.


</div>

</div>
