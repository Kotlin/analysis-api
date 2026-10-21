---
tags:
 - jvm
title: "computeTransitiveDependsOnDependencies"
---

# computeTransitiveDependsOnDependencies

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="compute-transitive-depends-on-dependencies.html"><span class="nf">computeTransitiveDependsOnDependencies</span></a><span class="p">(</span>directDependsOnDependencies<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Computes the transitive `dependsOn` dependencies of [`directDependsOnDependencies`](compute-transitive-depends-on-dependencies.md). [`computeTransitiveDependsOnDependencies`](compute-transitive-depends-on-dependencies.md) is the default computation strategy to provide [`KaModule.transitiveDependsOnDependencies`](../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/transitive-depends-on-dependencies.md).

The algorithm is a depth-first search-based topological sort. `dependsOn` dependencies cannot be cyclical and thus form a DAG, which allows the application of a topological sort.


</div>

</div>
