---
tags:
 - jvm
title: "KotlinProjectMessageBusProvider"
---

# KotlinProjectMessageBusProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KotlinProjectMessageBusProvider</a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span> : <a href="../-kotlin-message-bus-provider/index.html">KotlinMessageBusProvider</a>
</span></code></pre></div>Provides the [`project`](../../../analysis-api-platform-interface/org.jetbrains.kotlin.analysis.api.platform/-kotlin-project-message-bus-provider/project.md)'s MessageBus as the Analysis API message bus. This is the default implementation for both the standalone and the IDE Analysis API.

[`KotlinMessageBusProvider`](../-kotlin-message-bus-provider/index.md) exists so that this default may change in the future without breaking the API. Hence, it should not be assumed that the message bus provided by [`KotlinMessageBusProvider`](../-kotlin-message-bus-provider/index.md) will always be equal to the project's message bus.


</div>

## Constructors
### KotlinProjectMessageBusProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Functions
### getMessageBus

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getmessagebus"><span class="nf">getMessageBus</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>MessageBus
</span></code></pre></div>
</div>

</div>
