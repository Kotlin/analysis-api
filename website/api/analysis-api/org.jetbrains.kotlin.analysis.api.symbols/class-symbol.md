---
tags:
 - jvm
title: "classSymbol"
---

# classSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">.</span><a href="class-symbol.html">classSymbol</a><span class="o">: </span><a href="-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaClassSymbol`](-ka-class-symbol/index.md) for the given [`KtClassOrObject`](../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.md), or `null` for [`KtEnumEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry/index.md) declarations.

To retrieve a [`KaEnumEntrySymbol`](-ka-enum-entry-symbol/index.md), please refer to [`KtEnumEntry.symbol`](symbol.md).


</div>

</div>
