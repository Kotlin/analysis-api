---
tags:
 - jvm
title: "KaEngineService"
---

# KaEngineService

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaEngineService</a>
</span></code></pre></div>An <strong>engine service</strong> as defined by the Platform Interface (see the README).

Engine services do not need to be implemented by a platform. Quite the contrary, they are implemented by the Analysis API engine and intended to support platform implementations. They are defined in the Platform Interface, as opposed to the user-facing Analysis API, because they are intended for the consumption of platform implementations, but not Analysis API users.

As an example, a platform's lifetime token implementation (see [`KotlinLifetimeTokenFactory`](../../org.jetbrains.kotlin.analysis.api.platform.lifetime/-kotlin-lifetime-token-factory/index.md)) can make use of the [`KaLifetimeTracker`](../../org.jetbrains.kotlin.analysis.api.platform.lifetime/-ka-lifetime-tracker/index.md) engine service to retrieve the currently active lifetime token for comparison.

As a marker interface, [`KaEngineService`](index.md) clearly separates an engine service from [`KotlinPlatformComponent`](../-kotlin-platform-component/index.md)s which need to be implemented by a platform. Furthermore, engine services are always prefixed with `Ka`, in contrast to platform components which are prefixed with `Kotlin`.

#### Inheritors


 - [`KaLifetimeTracker`](../../org.jetbrains.kotlin.analysis.api.platform.lifetime/-ka-lifetime-tracker/index.md)
 - [`KaSourceModificationService`](../../org.jetbrains.kotlin.analysis.api.platform.modification/-ka-source-modification-service/index.md)
 - [`KaAnalysisPermissionChecker`](../../org.jetbrains.kotlin.analysis.api.platform.permissions/-ka-analysis-permission-checker/index.md)
 - [`KaContentScopeProvider`](../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-ka-content-scope-provider/index.md)
 - [`KaGlobalSearchScopeMerger`](../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-ka-global-search-scope-merger/index.md)
 - [`KaResolutionScopeProvider`](../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-ka-resolution-scope-provider/index.md)
 - [`KaResolutionActivityTracker`](../../org.jetbrains.kotlin.analysis.api.platform.resolution/-ka-resolution-activity-tracker/index.md)
 - [`KaStatisticsService`](../../org.jetbrains.kotlin.analysis.api.platform.statistics/-ka-statistics-service/index.md)



</div>

