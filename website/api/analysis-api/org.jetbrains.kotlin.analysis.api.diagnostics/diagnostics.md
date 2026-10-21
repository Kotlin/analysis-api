---
tags:
 - jvm
title: "diagnostics"
---

# diagnostics

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="diagnostics.html"><span class="nf">diagnostics</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-diagnostics/index.html">KaDiagnostics</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`diagnostics`](-ka-diagnostics/index.md) reported on the given [`KtElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md).

The result is computed lazily, and only as far as it is iterated. See [`KaDiagnostics`](-ka-diagnostics/index.md) for the defaults and for the ways to adjust them.

#### Example
```kotlin
for (diagnostic in file.diagnostics()) {
    handle(diagnostic)
}
```


</div>

</div>
