---
tags:
 - jvm
title: "KotlinModificationTrackerByEventFactoryBase"
---

# KotlinModificationTrackerByEventFactoryBase

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KotlinModificationTrackerByEventFactoryBase</a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span> : <a href="../-kotlin-modification-tracker-factory/index.html">KotlinModificationTrackerFactory</a>, Disposable
</span></code></pre></div>A base implementation of [`KotlinModificationTrackerFactory`](../-kotlin-modification-tracker-factory/index.md) which defines basic modification trackers that are incremented after receiving [`KotlinModificationEvent`](../-kotlin-modification-event/index.md)s.


</div>

## Constructors
### KotlinModificationTrackerByEventFactoryBase

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Functions
### createProjectWideLibraryModificationTracker

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#createprojectwidelibrarymodificationtracker"><span class="nf">createProjectWideLibraryModificationTracker</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>ModificationTracker
</span></code></pre></div>
</div>


<div markdown>

Creates a ModificationTracker which is incremented every time a library in the project is changed.


</div>

</div>
### createProjectWideSourceModificationTracker

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#createprojectwidesourcemodificationtracker"><span class="nf">createProjectWideSourceModificationTracker</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>ModificationTracker
</span></code></pre></div>
</div>


<div markdown>

Creates a ModificationTracker which is incremented every time a Kotlin source file is affected by a modification, in any of the project's source modules.

Such a modification can be any out-of-block code or project structure change affecting the analyzed source code. See [`KotlinModificationEvent`](../-kotlin-modification-event/index.md) for a definition of out-of-block modification.


</div>

</div>
### dispose

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#dispose"><span class="nf">dispose</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
