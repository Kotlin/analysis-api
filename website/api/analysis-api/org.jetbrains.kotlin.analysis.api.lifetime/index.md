---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.lifetime"
---

# org.jetbrains.kotlin.analysis.api.lifetime
## Types
### [`KaIllegalLifetimeOwnerAccessException`](-ka-illegal-lifetime-owner-access-exception/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-illegal-lifetime-owner-access-exception/index.html">KaIllegalLifetimeOwnerAccessException</a> : <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/IllegalStateException.html">IllegalStateException</a>
</span></code></pre></div>
</div>

</div>
### [`KaInaccessibleLifetimeOwnerAccessException`](-ka-inaccessible-lifetime-owner-access-exception/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-inaccessible-lifetime-owner-access-exception/index.html">KaInaccessibleLifetimeOwnerAccessException</a><span class="p">(</span><span class="kd">val </span>message<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span> : <a href="-ka-illegal-lifetime-owner-access-exception/index.html">KaIllegalLifetimeOwnerAccessException</a>
</span></code></pre></div>
</div>

</div>
### [`KaInvalidLifetimeOwnerAccessException`](-ka-invalid-lifetime-owner-access-exception/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-invalid-lifetime-owner-access-exception/index.html">KaInvalidLifetimeOwnerAccessException</a><span class="p">(</span><span class="kd">val </span>message<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span> : <a href="-ka-illegal-lifetime-owner-access-exception/index.html">KaIllegalLifetimeOwnerAccessException</a>
</span></code></pre></div>
</div>

</div>
### [`KaLifetimeOwner`](-ka-lifetime-owner/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

An Analysis API entity with a lifetime bound to the [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) where the entity was created.


</div>

</div>
### [`KaLifetimeToken`](-ka-lifetime-token/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-platform-interface/index.html">KaPlatformInterface::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-lifetime-token/index.html">KaLifetimeToken</a>
</span></code></pre></div>
</div>


<div markdown>

A token which is used as an anchor for determining the lifetime of a [`session`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)'s [`lifetime owner`](-ka-lifetime-owner/index.md).


</div>

</div>
## Functions
