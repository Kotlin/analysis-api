---
tags:
 - jvm
title: "refinedContextModule"
---

# refinedContextModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">var </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-code-fragment/index.html">KtCodeFragment</a><span class="p">.</span><a href="refined-context-module.html">refinedContextModule</a><span class="o">: </span><a href="-ka-module/index.html">KaModule</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A context module against which analysis of this code fragment should be performed.

[`refinedContextModule`](refined-context-module.md) is a [`KtCodeFragment`](../../psi-api/org.jetbrains.kotlin.psi/-kt-code-fragment/index.md)-tailored version of [`KtFile.contextModule`](context-module.md).

Normally, the context module is taken from the context element. However, in some cases the code fragment needs to be analyzed in a refined environment. Such as, the context element may be in the common module, while the code fragment is analyzed in its JVM counterpart.

This is an advanced and rarely needed feature. Use it with caution.


</div>

</div>
