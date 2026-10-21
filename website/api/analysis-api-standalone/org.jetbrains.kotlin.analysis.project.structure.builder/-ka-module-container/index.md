---
tags:
 - jvm
title: "KaModuleContainer"
---

# KaModuleContainer

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaModuleContainer</a>
</span></code></pre></div>
</div>

## Properties
### allModules

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#allmodules">allModules</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

All registered [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md)s, excluding [`KaNotUnderContentRootModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-not-under-content-root-module/index.md)s and the built-ins module.


</div>

</div>
