---
tags:
 - jvm
title: "createDeclarationProvider"
---

# createDeclarationProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="create-declaration-provider.html"><span class="nf">createDeclarationProvider</span></a><span class="p">(</span>scope<span class="o">: </span>GlobalSearchScope<span class="p">, </span>contextualModule<span class="o">: </span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KotlinDeclarationProvider`](-kotlin-declaration-provider/index.md) providing symbols within the given [`scope`](create-declaration-provider.md).

The [`contextualModule`](create-declaration-provider.md) is the module which contains the symbols to be provided, if applicable. The declaration provider may use the contextual module to provide declarations differently, such as providing alternative declarations for an outsider module. Some functionality such as package set computation may also depend on the contextual module, as the declaration provider may require additional information not available in the [`scope`](create-declaration-provider.md).


</div>

</div>
