---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.platform.statistics"
---

# org.jetbrains.kotlin.analysis.api.platform.statistics
## Types
### [`KaStatisticsService`](-ka-statistics-service/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-statistics-service/index.html">KaStatisticsService</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-ka-engine-service/index.html">KaEngineService</a>
</span></code></pre></div>
</div>


<div markdown>

Collects and reports statistics about the Analysis API's internal components.


</div>

</div>
### [`KotlinGlobalOpenTelemetryProvider`](-kotlin-global-open-telemetry-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-global-open-telemetry-provider/index.html">KotlinGlobalOpenTelemetryProvider</a> : <a href="-kotlin-open-telemetry-provider/index.html">KotlinOpenTelemetryProvider</a>
</span></code></pre></div>
</div>


<div markdown>

Provides the global OpenTelemetry instance as the platform's instance. This approach requires the platform to initialize the OpenTelemetry SDK as a global instance.


</div>

</div>
### [`KotlinObjectSizeCalculator`](-kotlin-object-size-calculator/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-object-size-calculator/index.html">KotlinObjectSizeCalculator</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

Provides endpoints for calculating the runtime size of objects.


</div>

</div>
### [`KotlinOpenTelemetryProvider`](-kotlin-open-telemetry-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-open-telemetry-provider/index.html">KotlinOpenTelemetryProvider</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

Provides an initialized OpenTelemetry instance. The Analysis API uses this instance to report statistics when statistics collection with [`KaStatisticsService`](-ka-statistics-service/index.md) is enabled. If the platform doesn't support OpenTelemetry, this service doesn't need to be registered.


</div>

</div>
