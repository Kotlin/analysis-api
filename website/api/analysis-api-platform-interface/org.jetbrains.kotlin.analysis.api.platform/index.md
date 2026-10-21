---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.platform"
---

# org.jetbrains.kotlin.analysis.api.platform
## Types
### [`KaCachedService`](-ka-cached-service/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-i-e-l-d/index.html">AnnotationTarget.FIELD</a><span class="p">]</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-ka-cached-service/index.html">KaCachedService</a>
</span></code></pre></div>
</div>


<div markdown>

A property annotated with [`KaCachedService`](-ka-cached-service/index.md) stores a cached IntelliJ project or application service, or an object with a reference to such a service.


</div>

</div>
### [`KaEngineService`](-ka-engine-service/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-engine-service/index.html">KaEngineService</a>
</span></code></pre></div>
</div>


<div markdown>

An <strong>engine service</strong> as defined by the Platform Interface (see the README).


</div>

</div>
### [`KaSessionListener`](-ka-session-listener/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-session-listener/index.html">KaSessionListener</a>
</span></code></pre></div>
</div>


<div markdown>

An extension point for platforms hosting the Kotlin Analysis API to receive callbacks on analysis session creation, entry, and exit.


</div>

</div>
### [`KotlinAnalysisInWriteActionListener`](-kotlin-analysis-in-write-action-listener/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-analysis-in-write-action-listener/index.html">KotlinAnalysisInWriteActionListener</a>
</span></code></pre></div>
</div>


<div markdown>

A listener for events which happen during an [`analyze`](../../analysis-api/org.jetbrains.kotlin.analysis.api.session/index.md) call in a write action.


</div>

</div>
### [`KotlinComposableProvider`](-kotlin-composable-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-composable-provider/index.html">KotlinComposableProvider</a>
</span></code></pre></div>
</div>


<div markdown>

A marker interface for a provider that can be composed, i.e. multiple instances of the same provider can be composed into a single provider.


</div>

</div>
### [`KotlinComposableProviderMerger`](-kotlin-composable-provider-merger/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-composable-provider-merger/index.html">KotlinComposableProviderMerger</a><span class="o"><</span><a href="-kotlin-composable-provider-merger/index.html">P</a><span class="o"> : </span><a href="-kotlin-composable-provider/index.html">KotlinComposableProvider</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`KotlinCompositeProvider`](-kotlin-composite-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-composite-provider/index.html">KotlinCompositeProvider</a><span class="o"><</span><a href="-kotlin-composite-provider/index.html">P</a><span class="o"> : </span><a href="-kotlin-composable-provider/index.html">KotlinComposableProvider</a><span class="o">></span> : <a href="-kotlin-composable-provider/index.html">KotlinComposableProvider</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KotlinCompositeProvider`](-kotlin-composite-provider/index.md) is the sequential composition of a specific kind of composable provider [`P`](-kotlin-composite-provider/index.md).


</div>

</div>
### [`KotlinCompositeProviderFactory`](-kotlin-composite-provider-factory/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-composite-provider-factory/index.html">KotlinCompositeProviderFactory</a><span class="o"><</span><a href="-kotlin-composite-provider-factory/index.html">P</a><span class="o"> : </span><a href="-kotlin-composable-provider/index.html">KotlinComposableProvider</a><span class="o">></span><span class="p">(</span>emptyProvider<span class="o">: </span><a href="-kotlin-composite-provider-factory/index.html">P</a><span class="p">, </span>composeProviders<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-kotlin-composite-provider-factory/index.html">P</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span><a href="-kotlin-composite-provider-factory/index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinCompositeProviderFactory`](-kotlin-composite-provider-factory/index.md) is used by various [`KotlinCompositeProvider`](-kotlin-composite-provider/index.md)s to share code related to provider creation and flattening.


</div>

</div>
### [`KotlinDeserializedDeclarationsOrigin`](-kotlin-deserialized-declarations-origin/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-kotlin-deserialized-declarations-origin/index.html">KotlinDeserializedDeclarationsOrigin</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-kotlin-deserialized-declarations-origin/index.html">KotlinDeserializedDeclarationsOrigin</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

This [`setting`](-kotlin-platform-settings/index.md) controls where [`declarations`](../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-declaration-provider/index.md) provided by the platform come from.


</div>

</div>
### [`KotlinMessageBusProvider`](-kotlin-message-bus-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-message-bus-provider/index.html">KotlinMessageBusProvider</a> : <a href="-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinMessageBusProvider`](-kotlin-message-bus-provider/index.md) allows Analysis API implementations to provide a custom MessageBus. When subscribing to or publishing to Analysis API topics, the message bus provided by [`getMessageBus`](-kotlin-message-bus-provider/index.md#getmessagebus) should be used, not the Project's message bus.


</div>

</div>
### [`KotlinOptionalPlatformComponent`](-kotlin-optional-platform-component/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a> : <a href="-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

An optional [`KotlinPlatformComponent`](-kotlin-platform-component/index.md). The Analysis API engine does not require an optional platform component to be implemented and will use sensible fallbacks or disable/avoid certain behaviors instead.


</div>

</div>
### [`KotlinPlatformComponent`](-kotlin-platform-component/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

A <strong>platform component</strong> as defined by the Platform Interface (see the README).


</div>

</div>
### [`KotlinPlatformSettings`](-kotlin-platform-settings/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-platform-settings/index.html">KotlinPlatformSettings</a> : <a href="-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinPlatformSettings`](-kotlin-platform-settings/index.md) allow the Analysis API platform to control the behavior of the Analysis API engine.


</div>

</div>
### [`KotlinProjectMessageBusProvider`](-kotlin-project-message-bus-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-project-message-bus-provider/index.html">KotlinProjectMessageBusProvider</a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span> : <a href="-kotlin-message-bus-provider/index.html">KotlinMessageBusProvider</a>
</span></code></pre></div>
</div>


<div markdown>

Provides the [`project`](../../analysis-api-platform-interface/org.jetbrains.kotlin.analysis.api.platform/-kotlin-project-message-bus-provider/project.md)'s MessageBus as the Analysis API message bus. This is the default implementation for both the standalone and the IDE Analysis API.


</div>

</div>
## Properties
### [`analysisMessageBus`](analysis-message-bus.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span>Project<span class="p">.</span><a href="analysis-message-bus.html">analysisMessageBus</a><span class="o">: </span>MessageBus
</span></code></pre></div>
</div>


<div markdown>

The MessageBus used to subscribe to and publish to Analysis API topics.


</div>

</div>
## Functions
### [`mergeSpecificProviders`](merge-specific-providers.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="merge-specific-providers.html">P</a><span class="o"> : </span><a href="-kotlin-composable-provider/index.html">KotlinComposableProvider</a><span class="p">, </span><span class="kd">reified </span><a href="merge-specific-providers.html">T</a><span class="o"> : </span><a href="merge-specific-providers.html">P</a><span class="o">> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="merge-specific-providers.html">P</a><span class="o">></span><span class="p">.</span><a href="merge-specific-providers.html"><span class="nf">mergeSpecificProviders</span></a><span class="p">(</span>factory<span class="o">: </span><a href="-kotlin-composite-provider-factory/index.html">KotlinCompositeProviderFactory</a><span class="o"><</span><a href="merge-specific-providers.html">P</a><span class="o">></span><span class="p">, </span><span class="kd">crossinline </span>mergeTargets<span class="o">: </span><span class="p">(</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="merge-specific-providers.html">T</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span><a href="merge-specific-providers.html">P</a><span class="p">)</span><span class="o">: </span><a href="merge-specific-providers.html">P</a>
</span></code></pre></div>
</div>


<div markdown>

Uses the given [`factory`](merge-specific-providers.md) to merge all providers of type [`T`](merge-specific-providers.md) with the given [`mergeTargets`](merge-specific-providers.md) strategy. Other providers (not of type [`T`](merge-specific-providers.md)) are added to the resulting composite provider unmerged.


</div>

</div>
