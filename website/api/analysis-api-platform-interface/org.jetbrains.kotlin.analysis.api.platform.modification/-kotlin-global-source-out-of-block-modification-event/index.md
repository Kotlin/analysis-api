---
tags:
 - jvm
title: "KotlinGlobalSourceOutOfBlockModificationEvent"
---

# KotlinGlobalSourceOutOfBlockModificationEvent

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">KotlinGlobalSourceOutOfBlockModificationEvent</a> : <a href="../-kotlin-modification-event/index.html">KotlinModificationEvent</a>
</span></code></pre></div>[`KotlinGlobalSourceOutOfBlockModificationEvent`](index.md) signals that [`out-of-block modification`](../-ka-source-modification-locality/-out-of-block/index.md) is occurring possibly globally.

The source code of all source [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md)s in the project should be considered modified when this event is received. This includes source files being moved or removed. Thus, all caches related to source code and source files should be invalidated.

Library modules (including library sources) do not need to be considered modified, so any caches related to library modules and their contents may be kept.

See [`KotlinModificationEvent`](../-kotlin-modification-event/index.md) for important contracts common to all modification events.


</div>

