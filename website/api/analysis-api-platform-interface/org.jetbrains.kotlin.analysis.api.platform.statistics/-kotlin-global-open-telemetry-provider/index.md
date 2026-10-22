---
tags:
 - jvm
title: "KotlinGlobalOpenTelemetryProvider"
---

# KotlinGlobalOpenTelemetryProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KotlinGlobalOpenTelemetryProvider</a> : <a href="../-kotlin-open-telemetry-provider/index.html">KotlinOpenTelemetryProvider</a>
</span></code></pre></div>Provides the global OpenTelemetry instance as the platform's instance. This approach requires the platform to initialize the OpenTelemetry SDK as a global instance.


</div>

## Constructors
### KotlinGlobalOpenTelemetryProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### openTelemetry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#opentelemetry">openTelemetry</a><span class="o">: </span>OpenTelemetry
</span></code></pre></div>
</div>

</div>
