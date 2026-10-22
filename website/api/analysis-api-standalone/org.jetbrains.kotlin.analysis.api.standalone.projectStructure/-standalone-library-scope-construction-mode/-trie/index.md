---
tags:
 - jvm
title: "Trie"
---

# Trie

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">object </span><a href="index.html">Trie</a> : <a href="../index.html">StandaloneLibraryScopeConstructionMode</a>
</span></code></pre></div>Determines containment by matching a file's path segments against a trie built from the library root paths.

This mode performs reasonably well, but is (likely) not as efficient as [`ParentTraversal`](../-parent-traversal/index.md), because the containment checks heavily allocate substrings. It is a workaround for rare cases when [`ParentTraversal`](../-parent-traversal/index.md) might not function correctly.

Because the trie relies on on-disk paths, this mode falls back to [`Enumeration`](../-enumeration/index.md) when a library root lacks one (for example, with an in-memory file system).


</div>

