---
tags:
 - jvm
title: "KotlinModificationTrackerFactory"
---

# KotlinModificationTrackerFactory

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinModificationTrackerFactory</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>[`KotlinModificationTrackerFactory`](index.md) creates modification trackers for sources and libraries.

In K2 mode, the modification trackers created by this factory must be incremented on specific [`KotlinModificationEvent`](../-kotlin-modification-event/index.md)s. In that sense, they can be viewed as a facade for modification events, for the use case when there are many, possibly short-lived objects that need to be notified of a change. In such cases, listener and subscriber management has too much overhead, making modification trackers the preferred solution.

### Implementation Notes
[`KotlinModificationTrackerByEventFactoryBase`](../-kotlin-modification-tracker-by-event-factory-base/index.md) can be inherited from to implement this platform component based on published modification events.

#### Inheritors


 - [`KotlinModificationTrackerByEventFactoryBase`](../-kotlin-modification-tracker-by-event-factory-base/index.md)



</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Functions
### createProjectWideLibraryModificationTracker

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createprojectwidelibrarymodificationtracker"><span class="nf">createProjectWideLibraryModificationTracker</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>ModificationTracker
</span></code></pre></div>
</div>


<div markdown>

Creates a ModificationTracker which is incremented every time a library in the project is changed.


</div>

</div>
### createProjectWideSourceModificationTracker

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createprojectwidesourcemodificationtracker"><span class="nf">createProjectWideSourceModificationTracker</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>ModificationTracker
</span></code></pre></div>
</div>


<div markdown>

Creates a ModificationTracker which is incremented every time a Kotlin source file is affected by a modification, in any of the project's source modules.

Such a modification can be any out-of-block code or project structure change affecting the analyzed source code. See [`KotlinModificationEvent`](../-kotlin-modification-event/index.md) for a definition of out-of-block modification.


</div>

</div>
