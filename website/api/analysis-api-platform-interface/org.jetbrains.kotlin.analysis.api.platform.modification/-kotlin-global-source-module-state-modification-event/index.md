---
tags:
 - jvm
title: "KotlinGlobalSourceModuleStateModificationEvent"
---

# KotlinGlobalSourceModuleStateModificationEvent

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">KotlinGlobalSourceModuleStateModificationEvent</a> : <a href="../-kotlin-modification-event/index.html">KotlinModificationEvent</a>
</span></code></pre></div>[`KotlinGlobalSourceModuleStateModificationEvent`](index.md) signals that source module settings or structure are changing possibly globally.

The module structure and source code of all source [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md)s in the project should be considered modified when this event is received. This includes source files being moved or removed, and source modules possibly being removed. Thus, all caches related to source module structure and source code should be invalidated.

Library modules (including library sources) do not need to be considered modified, so any caches related to library modules and their contents may be kept.

See [`KotlinModificationEvent`](../-kotlin-modification-event/index.md) for important contracts common to all modification events.


</div>

