---
tags:
 - jvm
title: "KaResolutionActivityTracker"
---

# KaResolutionActivityTracker

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaResolutionActivityTracker</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-ka-engine-service/index.html">KaEngineService</a>
</span></code></pre></div>This service provides a bridge between the Analysis API, Kotlin IntelliJ plugin and Java IntelliJ plugin.

In particular, this service helps to mark periods when the thread is busy with Kotlin resolution. During this time more strict rules may be applied on Java resolution, so it should take into account this to avoid Kotlin compiler contract violations.

This service should be dropped as soon as it will be possible to implement the new suppression logic for com.intellij.psi.impl.PsiFileEx.BATCH_REFERENCE_PROCESSING directly in the Kotlin repository (KT-73649 as a reference).


</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Properties
### isKotlinResolutionActive

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#iskotlinresolutionactive">isKotlinResolutionActive</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the thread is currently executing Kotlin resolution logic.


</div>

</div>
