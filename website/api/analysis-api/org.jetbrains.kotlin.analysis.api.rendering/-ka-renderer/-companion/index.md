---
tags:
 - jvm
title: "Companion"
---

# Companion

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">Companion</a>
</span></code></pre></div>
</div>

## Properties
### default

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#default">default</a><span class="o">: </span><a href="../index.html">KaRenderer</a>
</span></code></pre></div>
</div>


<div markdown>

The standard [`KaRenderer`](../index.md), which renders declarations and types close to their Kotlin source form.

Neither accessing this property nor deriving a renderer from it with [`copy`](../index.md#copy) requires an initialized application: the engine-provided renderer is resolved on the first rendering call. Both are therefore safe to use from a class initializer, such as when caching a customized renderer in a companion object property.


</div>

</div>
