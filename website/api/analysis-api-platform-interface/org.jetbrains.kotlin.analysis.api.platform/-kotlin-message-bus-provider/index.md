---
tags:
 - jvm
title: "KotlinMessageBusProvider"
---

# KotlinMessageBusProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinMessageBusProvider</a> : <a href="../-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>[`KotlinMessageBusProvider`](index.md) allows Analysis API implementations to provide a custom MessageBus. When subscribing to or publishing to Analysis API topics, the message bus provided by [`getMessageBus`](index.md#getmessagebus) should be used, not the Project's message bus.

#### Inheritors


 - [`KotlinProjectMessageBusProvider`](../-kotlin-project-message-bus-provider/index.md)



</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Functions
### getMessageBus

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getmessagebus"><span class="nf">getMessageBus</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>MessageBus
</span></code></pre></div>
</div>

</div>
