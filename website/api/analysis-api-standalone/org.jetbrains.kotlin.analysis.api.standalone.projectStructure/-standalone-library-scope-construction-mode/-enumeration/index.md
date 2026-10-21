---
tags:
 - jvm
title: "Enumeration"
---

# Enumeration

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">object </span><a href="index.html">Enumeration</a> : <a href="../index.html">StandaloneLibraryScopeConstructionMode</a>
</span></code></pre></div>Determines containment by checking a file against a precomputed set of all files reachable from the library roots.

This mode is inefficient, as it eagerly enumerates and retains every file under each library root. It should only be used as a last resort.


</div>

