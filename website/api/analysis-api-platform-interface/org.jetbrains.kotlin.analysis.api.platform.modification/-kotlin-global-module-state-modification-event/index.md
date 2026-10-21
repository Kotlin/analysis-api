---
tags:
 - jvm
title: "KotlinGlobalModuleStateModificationEvent"
---

# KotlinGlobalModuleStateModificationEvent

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">KotlinGlobalModuleStateModificationEvent</a> : <a href="../-kotlin-modification-event/index.html">KotlinModificationEvent</a>
</span></code></pre></div>This event signals that project settings or project structure are changing possibly globally.

The module structure, source code, and binary content of all [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md)s in the project should be considered modified when this event is received. This includes source files being moved or removed, binary content being added, removed, or changed, and modules possibly being removed. Thus, all caches related to module structure, source code, and binaries should be invalidated.

See [`KotlinModificationEvent`](../-kotlin-modification-event/index.md) for important contracts common to all modification events.


</div>

