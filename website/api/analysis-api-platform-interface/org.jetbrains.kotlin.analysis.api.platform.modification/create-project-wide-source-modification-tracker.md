---
tags:
 - jvm
title: "createProjectWideSourceModificationTracker"
---

# createProjectWideSourceModificationTracker

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Project<span class="p">.</span><a href="create-project-wide-source-modification-tracker.html"><span class="nf">createProjectWideSourceModificationTracker</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>ModificationTracker
</span></code></pre></div>
</div>


<div markdown>

Creates a ModificationTracker which is incremented every time a Kotlin source file is affected by a modification, in any of the project's source modules.

Such a modification can be any [`out-of-block`](-ka-source-modification-locality/-out-of-block/index.md) code or project structure change affecting the analyzed source code.


</div>

</div>
