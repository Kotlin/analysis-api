---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.platform.modification"
---

# org.jetbrains.kotlin.analysis.api.platform.modification
## Types
### [`KaElementModificationType`](-ka-element-modification-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-element-modification-type/index.html">KaElementModificationType</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaElementModificationType`](-ka-element-modification-type/index.md) describes which kind of modification was applied to a changed PsiElement. [`KaSourceModificationService`](-ka-source-modification-service/index.md) uses this information to perform change locality detection.


</div>

</div>
### [`KaSourceModificationLocality`](-ka-source-modification-locality/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-source-modification-locality/index.html">KaSourceModificationLocality</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaSourceModificationLocality`](-ka-source-modification-locality/index.md) describes the scope of effect of a source modification detected by [`KaSourceModificationService`](-ka-source-modification-service/index.md).


</div>

</div>
### [`KaSourceModificationService`](-ka-source-modification-service/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-source-modification-service/index.html">KaSourceModificationService</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-ka-engine-service/index.html">KaEngineService</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaSourceModificationService`](-ka-source-modification-service/index.md) is an <strong>engine service</strong> which handles cache invalidation after source code changes:


</div>

</div>
### [`KotlinCodeFragmentContextModificationEvent`](-kotlin-code-fragment-context-modification-event/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-code-fragment-context-modification-event/index.html">KotlinCodeFragmentContextModificationEvent</a><span class="p">(</span><span class="kd">val </span>module<span class="o">: </span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span> : <a href="-kotlin-modification-event/index.html">KotlinModificationEvent</a>
</span></code></pre></div>
</div>


<div markdown>

This event signals that the context of any code fragment depending on [`module`](-kotlin-code-fragment-context-modification-event/index.md#module) is changing. All code fragments depending on [`module`](-kotlin-code-fragment-context-modification-event/index.md#module), both directly or transitively, should be considered modified when this event is received.


</div>

</div>
### [`KotlinGlobalModuleStateModificationEvent`](-kotlin-global-module-state-modification-event/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-kotlin-global-module-state-modification-event/index.html">KotlinGlobalModuleStateModificationEvent</a> : <a href="-kotlin-modification-event/index.html">KotlinModificationEvent</a>
</span></code></pre></div>
</div>


<div markdown>

This event signals that project settings or project structure are changing possibly globally.


</div>

</div>
### [`KotlinGlobalScriptModuleStateModificationEvent`](-kotlin-global-script-module-state-modification-event/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-kotlin-global-script-module-state-modification-event/index.html">KotlinGlobalScriptModuleStateModificationEvent</a> : <a href="-kotlin-modification-event/index.html">KotlinModificationEvent</a>
</span></code></pre></div>
</div>


<div markdown>

This event signals that Kotlin script module settings or structure are changing possibly globally.


</div>

</div>
### [`KotlinGlobalSourceModuleStateModificationEvent`](-kotlin-global-source-module-state-modification-event/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-kotlin-global-source-module-state-modification-event/index.html">KotlinGlobalSourceModuleStateModificationEvent</a> : <a href="-kotlin-modification-event/index.html">KotlinModificationEvent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinGlobalSourceModuleStateModificationEvent`](-kotlin-global-source-module-state-modification-event/index.md) signals that source module settings or structure are changing possibly globally.


</div>

</div>
### [`KotlinGlobalSourceOutOfBlockModificationEvent`](-kotlin-global-source-out-of-block-modification-event/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-kotlin-global-source-out-of-block-modification-event/index.html">KotlinGlobalSourceOutOfBlockModificationEvent</a> : <a href="-kotlin-modification-event/index.html">KotlinModificationEvent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinGlobalSourceOutOfBlockModificationEvent`](-kotlin-global-source-out-of-block-modification-event/index.md) signals that [`out-of-block modification`](-ka-source-modification-locality/-out-of-block/index.md) is occurring possibly globally.


</div>

</div>
### [`KotlinModificationEvent`](-kotlin-modification-event/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-kotlin-modification-event/index.html">KotlinModificationEvent</a>
</span></code></pre></div>
</div>


<div markdown>

In the Analysis API, [`KotlinModificationEvent`](-kotlin-modification-event/index.md)s signal changes in source code, module and project settings, or project structure. These events should be subscribed to and published via the [`TOPIC`](-kotlin-modification-event/-companion/index.md#topic) on the [`Analysis API message bus`](../org.jetbrains.kotlin.analysis.api.platform/analysis-message-bus.md). They must be published in a <strong>write action</strong>.


</div>

</div>
### [`KotlinModificationEventKind`](-kotlin-modification-event-kind/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-kotlin-modification-event-kind/index.html">KotlinModificationEventKind</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-kotlin-modification-event-kind/index.html">KotlinModificationEventKind</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinModificationEventKind`](-kotlin-modification-event-kind/index.md) represents the kinds of [`KotlinModificationEvent`](-kotlin-modification-event/index.md)s. While it is not required to publish or subscribe to modification events, it can be useful when abstracting over modification events in general, for example in tests.


</div>

</div>
### [`KotlinModificationEventListener`](-kotlin-modification-event-listener/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="kd">interface </span><a href="-kotlin-modification-event-listener/index.html">KotlinModificationEventListener</a>
</span></code></pre></div>
</div>


<div markdown>

A listener for [`KotlinModificationEvent`](-kotlin-modification-event/index.md)s. It should be registered on the [`analysisMessageBus`](../org.jetbrains.kotlin.analysis.api.platform/analysis-message-bus.md) with [`KotlinModificationEvent.TOPIC`](-kotlin-modification-event/-companion/index.md#topic).


</div>

</div>
### [`KotlinModificationTrackerByEventFactoryBase`](-kotlin-modification-tracker-by-event-factory-base/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kotlin-modification-tracker-by-event-factory-base/index.html">KotlinModificationTrackerByEventFactoryBase</a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span> : <a href="-kotlin-modification-tracker-factory/index.html">KotlinModificationTrackerFactory</a>, Disposable
</span></code></pre></div>
</div>


<div markdown>

A base implementation of [`KotlinModificationTrackerFactory`](-kotlin-modification-tracker-factory/index.md) which defines basic modification trackers that are incremented after receiving [`KotlinModificationEvent`](-kotlin-modification-event/index.md)s.


</div>

</div>
### [`KotlinModificationTrackerFactory`](-kotlin-modification-tracker-factory/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-modification-tracker-factory/index.html">KotlinModificationTrackerFactory</a> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KotlinModificationTrackerFactory`](-kotlin-modification-tracker-factory/index.md) creates modification trackers for sources and libraries.


</div>

</div>
### [`KotlinModuleOutOfBlockModificationEvent`](-kotlin-module-out-of-block-modification-event/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-module-out-of-block-modification-event/index.html">KotlinModuleOutOfBlockModificationEvent</a><span class="p">(</span><span class="kd">val </span>module<span class="o">: </span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span> : <a href="-kotlin-modification-event/index.html">KotlinModificationEvent</a>
</span></code></pre></div>
</div>


<div markdown>

This event signals that an [`out-of-block modification`](-ka-source-modification-locality/-out-of-block/index.md) is occurring in the sources of [`module`](-kotlin-module-out-of-block-modification-event/index.md#module).


</div>

</div>
### [`KotlinModuleStateModificationEvent`](-kotlin-module-state-modification-event/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kotlin-module-state-modification-event/index.html">KotlinModuleStateModificationEvent</a><span class="p">(</span><span class="kd">val </span>module<span class="o">: </span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">, </span><span class="kd">val </span>modificationKind<span class="o">: </span><a href="-kotlin-module-state-modification-kind/index.html">KotlinModuleStateModificationKind</a><span class="p">)</span> : <a href="-kotlin-modification-event/index.html">KotlinModificationEvent</a>
</span></code></pre></div>
</div>


<div markdown>

This event signals that [`module`](-kotlin-module-state-modification-event/index.md#module)'s settings or structure are changing. The event is published in a write action before the [`module`](-kotlin-module-state-modification-event/index.md#module) is updated or removed (see [`KotlinModuleStateModificationKind`](-kotlin-module-state-modification-kind/index.md) for specifics). This allows subscribers to access the module's properties and dependencies to invalidate or update caches.


</div>

</div>
### [`KotlinModuleStateModificationKind`](-kotlin-module-state-modification-kind/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-kotlin-module-state-modification-kind/index.html">KotlinModuleStateModificationKind</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-kotlin-module-state-modification-kind/index.html">KotlinModuleStateModificationKind</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Describes the kind of module state modification affecting a [`KaModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md) in more detail.


</div>

</div>
## Properties
## Functions
### [`createProjectWideLibraryModificationTracker`](create-project-wide-library-modification-tracker.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="create-project-wide-library-modification-tracker.html"><span class="nf">createProjectWideLibraryModificationTracker</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>ModificationTracker
</span></code></pre></div>
</div>


<div markdown>

Creates a ModificationTracker which is incremented every time a library in the project is changed.


</div>

</div>
### [`createProjectWideSourceModificationTracker`](create-project-wide-source-modification-tracker.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="create-project-wide-source-modification-tracker.html"><span class="nf">createProjectWideSourceModificationTracker</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>ModificationTracker
</span></code></pre></div>
</div>


<div markdown>

Creates a ModificationTracker which is incremented every time a Kotlin source file is affected by a modification, in any of the project's source modules.


</div>

</div>
### [`publishCodeFragmentContextModificationEvent`](publish-code-fragment-context-modification-event.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">.</span><a href="publish-code-fragment-context-modification-event.html"><span class="nf">publishCodeFragmentContextModificationEvent</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Publishes a [`KotlinCodeFragmentContextModificationEvent`](-kotlin-code-fragment-context-modification-event/index.md) for this [`KaModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md). Must be called in a write action.


</div>

</div>
### [`publishGlobalModuleStateModificationEvent`](publish-global-module-state-modification-event.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="publish-global-module-state-modification-event.html"><span class="nf">publishGlobalModuleStateModificationEvent</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Publishes a [`KotlinGlobalModuleStateModificationEvent`](-kotlin-global-module-state-modification-event/index.md). Must be called in a write action.


</div>

</div>
### [`publishGlobalScriptModuleStateModificationEvent`](publish-global-script-module-state-modification-event.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="publish-global-script-module-state-modification-event.html"><span class="nf">publishGlobalScriptModuleStateModificationEvent</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Publishes a [`KotlinGlobalScriptModuleStateModificationEvent`](-kotlin-global-script-module-state-modification-event/index.md). Must be called in a write action.


</div>

</div>
### [`publishGlobalSourceModuleStateModificationEvent`](publish-global-source-module-state-modification-event.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="publish-global-source-module-state-modification-event.html"><span class="nf">publishGlobalSourceModuleStateModificationEvent</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Publishes a [`KotlinGlobalSourceModuleStateModificationEvent`](-kotlin-global-source-module-state-modification-event/index.md). Must be called in a write action.


</div>

</div>
### [`publishGlobalSourceOutOfBlockModificationEvent`](publish-global-source-out-of-block-modification-event.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="publish-global-source-out-of-block-modification-event.html"><span class="nf">publishGlobalSourceOutOfBlockModificationEvent</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Publishes a [`KotlinGlobalSourceOutOfBlockModificationEvent`](-kotlin-global-source-out-of-block-modification-event/index.md). Must be called in a write action.


</div>

</div>
### [`publishModificationEvent`](publish-modification-event.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="publish-modification-event.html"><span class="nf">publishModificationEvent</span></a><span class="p">(</span>event<span class="o">: </span><a href="-kotlin-modification-event/index.html">KotlinModificationEvent</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Publishes a [`KotlinModificationEvent`](-kotlin-modification-event/index.md) to the project's [`analysisMessageBus`](../org.jetbrains.kotlin.analysis.api.platform/analysis-message-bus.md). Must be called in a write action.


</div>

</div>
### [`publishModuleOutOfBlockModificationEvent`](publish-module-out-of-block-modification-event.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">.</span><a href="publish-module-out-of-block-modification-event.html"><span class="nf">publishModuleOutOfBlockModificationEvent</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Publishes a [`KotlinModuleOutOfBlockModificationEvent`](-kotlin-module-out-of-block-modification-event/index.md) for this [`KaModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md). Must be called in a write action.


</div>

</div>
### [`publishModuleStateModificationEvent`](publish-module-state-modification-event.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">.</span><a href="publish-module-state-modification-event.html"><span class="nf">publishModuleStateModificationEvent</span></a><span class="p">(</span>modificationKind<span class="o">: </span><a href="-kotlin-module-state-modification-kind/index.html">KotlinModuleStateModificationKind</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Publishes a [`KotlinModuleStateModificationEvent`](-kotlin-module-state-modification-event/index.md) for this [`KaModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md). Must be called in a write action.


</div>

</div>
