---
tags:
 - jvm
title: "KotlinModificationEventListener"
---

# KotlinModificationEventListener

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="kd">interface </span><a href="index.html">KotlinModificationEventListener</a>
</span></code></pre></div>A listener for [`KotlinModificationEvent`](../-kotlin-modification-event/index.md)s. It should be registered on the [`analysisMessageBus`](../../org.jetbrains.kotlin.analysis.api.platform/analysis-message-bus.md) with [`KotlinModificationEvent.TOPIC`](../-kotlin-modification-event/-companion/index.md#topic).


</div>

## Functions
### onModification

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#onmodification"><span class="nf">onModification</span></a><span class="p">(</span>event<span class="o">: </span><a href="../-kotlin-modification-event/index.html">KotlinModificationEvent</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

[`onModification`](index.md#onmodification) is invoked before or after the modification and usually in a write action. However, the specific timing depends on the type of [`event`](index.md#onmodification).

See also the KDoc of [`KotlinModificationEvent`](../-kotlin-modification-event/index.md) for an in-depth explanation of timing guarantees.


</div>

</div>
