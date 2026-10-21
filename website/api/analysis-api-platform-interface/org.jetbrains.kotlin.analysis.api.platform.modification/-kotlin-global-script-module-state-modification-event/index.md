---
tags:
 - jvm
title: "KotlinGlobalScriptModuleStateModificationEvent"
---

# KotlinGlobalScriptModuleStateModificationEvent

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">KotlinGlobalScriptModuleStateModificationEvent</a> : <a href="../-kotlin-modification-event/index.html">KotlinModificationEvent</a>
</span></code></pre></div>This event signals that Kotlin script module settings or structure are changing possibly globally.

When this event is received, the module structure, source code, and binary content of all [`KaScriptModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-script-module/index.md)s and [`KaScriptDependencyModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-script-dependency-module/index.md)s in the project should be considered modified. Therefore, all caches related to Kotlin script module structure, source code, and binaries must be invalidated.

See [`KotlinModificationEvent`](../-kotlin-modification-event/index.md) for important contracts common to all modification events.


</div>

