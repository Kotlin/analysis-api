---
tags:
 - jvm
title: "findPackage"
---

# findPackage

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="find-package.html"><span class="nf">findPackage</span></a><span class="p">(</span>fqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="-ka-package-symbol/index.html">KaPackageSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaPackageSymbol`](-ka-package-symbol/index.md) corresponding to the given [`fqName`](find-package.md) if that package exists and is visible from the current use site, or `null` otherwise.


</div>

</div>
