---
tags:
 - jvm
title: "KotlinPlatformComponent"
---

# KotlinPlatformComponent

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinPlatformComponent</a>
</span></code></pre></div>A <strong>platform component</strong> as defined by the Platform Interface (see the README).

Mandatory platform components must be implemented by a platform to fully support the Analysis API in the desired environment. A few platform components are optional, signified by [`KotlinOptionalPlatformComponent`](../-kotlin-optional-platform-component/index.md). As a marker interface, [`KotlinPlatformComponent`](index.md) makes it easy to find all platform components to implement.

The Platform Interface provides a number of default and base implementations which may be specified or extended by a platform implementation, such as [`KotlinProjectMessageBusProvider`](../-kotlin-project-message-bus-provider/index.md) for [`KotlinMessageBusProvider`](../-kotlin-message-bus-provider/index.md).

Platform component interfaces and their default implementations are always prefixed with the word `Kotlin`, in contrast to [`KaEngineService`](../-ka-engine-service/index.md)s which are prefixed with `Ka`. It is recommended to keep this naming convention in platform implementations. For example, the Standalone API uses a `KotlinStandalone` prefix for its own platform component implementations.

#### Inheritors


 - [`KotlinMessageBusProvider`](../-kotlin-message-bus-provider/index.md)
 - [`KotlinOptionalPlatformComponent`](../-kotlin-optional-platform-component/index.md)
 - [`KotlinPlatformSettings`](../-kotlin-platform-settings/index.md)
 - [`KotlinAnnotationsResolverFactory`](../../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-annotations-resolver-factory/index.md)
 - [`KotlinDeclarationProviderFactory`](../../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-declaration-provider-factory/index.md)
 - [`KotlinDeclarationProviderMerger`](../../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-declaration-provider-merger/index.md)
 - [`KotlinDirectInheritorsProvider`](../../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-direct-inheritors-provider/index.md)
 - [`KotlinJavaModuleAnnotationsProvider`](../../org.jetbrains.kotlin.analysis.api.platform.java/-kotlin-java-module-annotations-provider/index.md)
 - [`KotlinLifetimeTokenFactory`](../../org.jetbrains.kotlin.analysis.api.platform.lifetime/-kotlin-lifetime-token-factory/index.md)
 - [`KotlinModificationTrackerFactory`](../../org.jetbrains.kotlin.analysis.api.platform.modification/-kotlin-modification-tracker-factory/index.md)
 - [`KotlinPackagePartProviderFactory`](../../org.jetbrains.kotlin.analysis.api.platform.packages/-kotlin-package-part-provider-factory/index.md)
 - [`KotlinPackageProviderFactory`](../../org.jetbrains.kotlin.analysis.api.platform.packages/-kotlin-package-provider-factory/index.md)
 - [`KotlinPackageProviderMerger`](../../org.jetbrains.kotlin.analysis.api.platform.packages/-kotlin-package-provider-merger/index.md)
 - [`KotlinContentScopeRefiner`](../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-kotlin-content-scope-refiner/index.md)
 - [`KotlinGlobalSearchScopeMergeStrategy`](../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-kotlin-global-search-scope-merge-strategy/index.md)
 - [`KotlinModuleDependentsProvider`](../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-kotlin-module-dependents-provider/index.md)



</div>

