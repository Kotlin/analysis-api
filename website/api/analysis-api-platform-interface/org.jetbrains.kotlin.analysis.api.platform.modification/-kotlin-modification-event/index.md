---
tags:
 - jvm
title: "KotlinModificationEvent"
---

# KotlinModificationEvent

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">KotlinModificationEvent</a>
</span></code></pre></div>In the Analysis API, [`KotlinModificationEvent`](index.md)s signal changes in source code, module and project settings, or project structure. These events should be subscribed to and published via the [`TOPIC`](-companion/index.md#topic) on the [`Analysis API message bus`](../../org.jetbrains.kotlin.analysis.api.platform/analysis-message-bus.md). They must be published in a <strong>write action</strong>.

The specifics of the modification are determined by the type of [`KotlinModificationEvent`](index.md):

 - [`KotlinModuleStateModificationEvent`](../-kotlin-module-state-modification-event/index.md): Module settings or module structure changes for a specific module (e.g. module update/removal).


 - [`KotlinModuleOutOfBlockModificationEvent`](../-kotlin-module-out-of-block-modification-event/index.md): Out-of-block modification in the source code of a specific module.


 - [`KotlinGlobalModuleStateModificationEvent`](../-kotlin-global-module-state-modification-event/index.md): Global changes in project settings or project structure.


 - [`KotlinGlobalSourceModuleStateModificationEvent`](../-kotlin-global-source-module-state-modification-event/index.md): Global changes in source module settings or structure.


 - [`KotlinGlobalScriptModuleStateModificationEvent`](../-kotlin-global-script-module-state-modification-event/index.md): Global changes in script module settings or structure.


 - [`KotlinGlobalSourceOutOfBlockModificationEvent`](../-kotlin-global-source-out-of-block-modification-event/index.md): Global out-of-block modification potentially affecting all source modules.


 - [`KotlinCodeFragmentContextModificationEvent`](../-kotlin-code-fragment-context-modification-event/index.md): Changes to the context of code fragments depending on a specific module.


Care needs to be taken with the lack of interplay between different types of events: Publishing a global modification event, for example, does not imply the corresponding module-level event. Similarly, publishing a module state modification event does not imply out-of-block modification.

Global modification events are published when it's not feasible or desired to publish events for a single module, or a limited set of modules. For example, a change in the environment such as removing an SDK might affect all modules, so a global event is more appropriate.

### Timing Guarantees
All modification events are guaranteed to be published in the write action in which the modification happens. Beyond that, the exact timing is not strictly defined for most modification events.

Most modification events may be published before or after a modification, so subscribers should not assume that the modification has or hasn't happened yet. The reason for this design decision is that some of the underlying events (such as PSI tree changes) may be published before or after a change, or even both. Modification events published before the modification should however be published close to the modification.

Only [`KotlinModuleStateModificationEvent`](../-kotlin-module-state-modification-event/index.md) guarantees that the event is published before the module is affected. This allows subscribers to access the module's properties and dependencies to invalidate or update caches.

### Implementation Notes
Analysis API platforms need to take care of publishing modification events via the [`analysisMessageBus`](../../org.jetbrains.kotlin.analysis.api.platform/analysis-message-bus.md). In general, if a platform works with static code and static module structure, it does not need to publish any events. However, the contracts of the various modification events need to be kept in mind. For example, if a platform can guarantee a static module structure but source code can still change, module state modification events do not need to be published, but out-of-block modification events do.

Source code modification should always be handled with [`KaSourceModificationService`](../-ka-source-modification-service/index.md). It publishes out-of-block modification events if it detects an out-of-block change, which makes modification handling much easier. But it also invalidates local caches on local changes, which currently cannot be accomplished by modification events with the same level of granularity.

#### See also


 - [`KaSourceModificationLocality`](../-ka-source-modification-locality/index.md)


#### Inheritors


 - [`KotlinCodeFragmentContextModificationEvent`](../-kotlin-code-fragment-context-modification-event/index.md)
 - [`KotlinGlobalModuleStateModificationEvent`](../-kotlin-global-module-state-modification-event/index.md)
 - [`KotlinGlobalScriptModuleStateModificationEvent`](../-kotlin-global-script-module-state-modification-event/index.md)
 - [`KotlinGlobalSourceModuleStateModificationEvent`](../-kotlin-global-source-module-state-modification-event/index.md)
 - [`KotlinGlobalSourceOutOfBlockModificationEvent`](../-kotlin-global-source-out-of-block-modification-event/index.md)
 - [`KotlinModuleOutOfBlockModificationEvent`](../-kotlin-module-out-of-block-modification-event/index.md)
 - [`KotlinModuleStateModificationEvent`](../-kotlin-module-state-modification-event/index.md)



</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
