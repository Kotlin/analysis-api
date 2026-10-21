---
tags:
 - jvm
title: "KotlinOpenTelemetryProvider"
---

# KotlinOpenTelemetryProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinOpenTelemetryProvider</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>Provides an initialized OpenTelemetry instance. The Analysis API uses this instance to report statistics when statistics collection with [`KaStatisticsService`](../-ka-statistics-service/index.md) is enabled. If the platform doesn't support OpenTelemetry, this service doesn't need to be registered.

The Analysis API itself only depends on the OpenTelemetry API, which does not report any telemetry on its own. It's the responsibility of the Analysis API platform to register an OpenTelemetry SDK, which then exports the collected data. This also means that no telemetry is reported whatsoever, neither locally nor over any connection, by the Kotlin compiler and Standalone Analysis API.

#### See also


 - [`KaStatisticsService`](../-ka-statistics-service/index.md)


#### Inheritors


 - [`KotlinGlobalOpenTelemetryProvider`](../-kotlin-global-open-telemetry-provider/index.md)



</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Properties
### openTelemetry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#opentelemetry">openTelemetry</a><span class="o">: </span>OpenTelemetry
</span></code></pre></div>
</div>

</div>
