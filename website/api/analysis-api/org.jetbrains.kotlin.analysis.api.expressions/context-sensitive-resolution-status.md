---
tags:
 - jvm
title: "contextSensitiveResolutionStatus"
---

# contextSensitiveResolutionStatus

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="context-sensitive-resolution-status.html">contextSensitiveResolutionStatus</a><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.resolution/-ka-context-sensitive-resolution-status/index.html">KaContextSensitiveResolutionStatus</a>
</span></code></pre></div>
</div>


<div markdown>

The [context-sensitive resolution](https://github.com/Kotlin/KEEP/issues/379) status of the [`KtSimpleNameExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.md): whether the name is already resolved through context-sensitive resolution, and whether a redundant explicit qualifier or import could be removed in favor of it.

The information is available even when the `-Xcontext-sensitive-resolution` feature is not enabled.

#### Example
```
enum class Foo { BAR }

fun usage(): Foo {
    return Foo.BAR // the 'Foo.' qualifier can be removed -> KaContextSensitiveResolutionStatus.QualifierCanBeRemoved
}
```

#### See also


 - [`KaContextSensitiveResolutionStatus`](../org.jetbrains.kotlin.analysis.api.resolution/-ka-context-sensitive-resolution-status/index.md)



</div>

</div>
