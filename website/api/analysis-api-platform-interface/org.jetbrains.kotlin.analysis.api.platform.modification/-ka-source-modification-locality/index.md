---
tags:
 - jvm
title: "KaSourceModificationLocality"
---

# KaSourceModificationLocality

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">KaSourceModificationLocality</a>
</span></code></pre></div>[`KaSourceModificationLocality`](index.md) describes the scope of effect of a source modification detected by [`KaSourceModificationService`](../-ka-source-modification-service/index.md).

#### Inheritors


 - [`Invisible`](-invisible/index.md)
 - [`Whitespace`](-whitespace/index.md)
 - [`InBlock`](-in-block/index.md)
 - [`OutOfBlock`](-out-of-block/index.md)



</div>

## Types
### [`InBlock`](-in-block/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-in-block/index.html">InBlock</a> : <a href="index.html">KaSourceModificationLocality</a>
</span></code></pre></div>
</div>


<div markdown>

In-block modification is a source code modification that doesn't affect the state of other non-local declarations.


</div>

</div>
### [`Invisible`](-invisible/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-invisible/index.html">Invisible</a> : <a href="index.html">KaSourceModificationLocality</a>
</span></code></pre></div>
</div>


<div markdown>

A change that has no effect on cached information.


</div>

</div>
### [`OutOfBlock`](-out-of-block/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-out-of-block/index.html">OutOfBlock</a> : <a href="index.html">KaSourceModificationLocality</a>
</span></code></pre></div>
</div>


<div markdown>

Out-of-block modification is a source code modification that may affect the state of other declarations in the same module and the declarations of dependent modules.


</div>

</div>
### [`Whitespace`](-whitespace/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-whitespace/index.html">Whitespace</a> : <a href="index.html">KaSourceModificationLocality</a>
</span></code></pre></div>
</div>


<div markdown>

Whitespace modification covers changes in whitespace and comments.


</div>

</div>
