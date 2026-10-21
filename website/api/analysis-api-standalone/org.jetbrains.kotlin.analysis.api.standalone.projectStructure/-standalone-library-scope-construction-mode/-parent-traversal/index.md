---
tags:
 - jvm
title: "ParentTraversal"
---

# ParentTraversal

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">object </span><a href="index.html">ParentTraversal</a> : <a href="../index.html">StandaloneLibraryScopeConstructionMode</a>
</span></code></pre></div>Determines containment by walking a file's parents until one of them is a library root.

In most cases, this mode should perform the best. It should also work with in-memory file systems. If the mode causes problems with a particular file system, it is recommended to switch to [`Trie`](../-trie/index.md).

This is the default mode.


</div>

