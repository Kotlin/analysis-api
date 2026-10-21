---
tags:
 - jvm
title: "KaStatisticsService"
---

# KaStatisticsService

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaStatisticsService</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-ka-engine-service/index.html">KaEngineService</a>
</span></code></pre></div>Collects and reports statistics about the Analysis API's internal components.

Statistics collection needs to be enabled with the registry key `kotlin.analysis.statistics` ([`areStatisticsEnabled`](-companion/index.md#arestatisticsenabled)). This is needed because statistics incur an overhead. If [`areStatisticsEnabled`](-companion/index.md#arestatisticsenabled) is `false`, [`getInstance`](-companion/index.md#getinstance) will return `null`.

When statistics collection is enabled, the [`start`](index.md#start) function should be called soon after the project has been opened. While most metrics will be collected independently of whether [`start`](index.md#start) is called, the statistics service may need to schedule periodic updates and information gathering. These scheduled tasks contribute to the reported statistics.

[`KaStatisticsService`](index.md) uses the platform's OpenTelemetry instance (provided by [`KotlinOpenTelemetryProvider`](../-kotlin-open-telemetry-provider/index.md)) to report metrics. If no OpenTelemetry provider is available, statistics will not be collected and reported.

The reporting of Analysis API statistics is entirely dependent on the OpenTelemetry configuration. The Analysis API itself does not publish any data itself, neither locally nor over any network connection. The Analysis API platform has full control over this part of the process. For example, IntelliJ gathers and exports metrics data locally to a file, while Standalone does not set up any publishing whatsoever.

### Usage
When the Analysis API is used on top of IntelliJ and statistics collection is enabled, the `logs` folder will contain CSV and JSON files called `open-telemetry-metrics.*` (one file per IntelliJ run). In the same logs folder, there is a file called `open-telemetry-metrics-plotter.html`, which can be opened locally. This HTML file allows plotting the metrics gathered during a run of IntelliJ simply by opening the relevant CSV in the metrics plotter interface.

The metrics plotter won't immediately plot Analysis API metrics. Instead, the "plot other" section can be used to search for and plot such metrics. All Analysis API metrics have the prefix `kotlin.analysis`.

While local logging of statistics comes out of the box in IntelliJ, other Analysis API platforms need to set up statistics collection on their own. Notably, Standalone does not collect any statistics at all.


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
### start

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#start"><span class="nf">start</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Schedules periodic updates and information gathering if statistics collection is [`enabled`](-companion/index.md#arestatisticsenabled). These tasks contribute to the collected statistics.

[`start`](index.md#start) should be called soon after the project has been opened. The function implementation is thread-safe and may be called from any thread.


</div>

</div>
