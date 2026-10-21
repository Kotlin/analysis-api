---
tags:
 - jvm
title: "StandaloneLibraryScopeConstructionMode"
---

# StandaloneLibraryScopeConstructionMode

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="index.html">StandaloneLibraryScopeConstructionMode</a>
</span></code></pre></div>The strategy used to build a library module's content scope from its binary roots in Standalone mode.

The content scope of a library module determines the files belonging to the library. The construction mode allows picking the data structure and algorithm that implements the content scope. This has a direct impact on the memory footprint and performance profile of the scope check, and in general, Standalone's overall performance.

[`ParentTraversal`](-parent-traversal/index.md) is the default. In most cases, it should be the most performant and most memory-friendly option. In exceptional cases, particularly with non-standard virtual file system implementations, it may cause errors or performance issues. The other options are provided as workarounds, with [`Trie`](-trie/index.md) being the recommended one.

The mode can be set per module on the module builder, or as a default for all modules on the module provider builder.

#### Inheritors


 - [`ParentTraversal`](-parent-traversal/index.md)
 - [`Trie`](-trie/index.md)
 - [`Enumeration`](-enumeration/index.md)



</div>

## Types
### [`Enumeration`](-enumeration/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">object </span><a href="-enumeration/index.html">Enumeration</a> : <a href="index.html">StandaloneLibraryScopeConstructionMode</a>
</span></code></pre></div>
</div>


<div markdown>

Determines containment by checking a file against a precomputed set of all files reachable from the library roots.


</div>

</div>
### [`ParentTraversal`](-parent-traversal/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">object </span><a href="-parent-traversal/index.html">ParentTraversal</a> : <a href="index.html">StandaloneLibraryScopeConstructionMode</a>
</span></code></pre></div>
</div>


<div markdown>

Determines containment by walking a file's parents until one of them is a library root.


</div>

</div>
### [`Trie`](-trie/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">object </span><a href="-trie/index.html">Trie</a> : <a href="index.html">StandaloneLibraryScopeConstructionMode</a>
</span></code></pre></div>
</div>


<div markdown>

Determines containment by matching a file's path segments against a trie built from the library root paths.


</div>

</div>
