---
tags:
 - jvm
title: "REMOVAL"
---

# REMOVAL

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="index.html">REMOVAL</a>

</span></code></pre></div>The [`KaModule`](../../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md) is being removed. Because this event is published before the removal, the [`KaModule`](../../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md) can still be accessed to clear caches. It should be removed from any caches managed by the subscriber to avoid stale or broken keys/values.


</div>

## Properties
### [`name`](../../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`ordinal`](../../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.md#ordinal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../../org.jetbrains.kotlin.analysis.api.platform.projectStructure/-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.html#ordinal">ordinal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
