---
tags:
 - jvm
title: "explicitModule"
---

# explicitModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">var </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="explicit-module.html">explicitModule</a><span class="o">: </span><a href="-ka-module/index.html">KaModule</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A module to be used for analyzing the given file. Currently, only [`KaDanglingFileModule`](-ka-dangling-file-module/index.md)s can be set as explicit modules.

[`explicitModule`](explicit-module.md) can be useful for constructing dangling file modules consisting of more than one file:

1. Create all in-memory files;


1. Manually initiate a [`KaDanglingFileModule`](-ka-dangling-file-module/index.md), passing all created files.


1. Set the newly created module as an [`explicitModule`](explicit-module.md) to all of the created files.


Use with extreme care – [`explicitModule`](explicit-module.md) overrides all other configuration. If you only need to provide the context module for an in-memory file, use [`contextModule`](context-module.md) instead.

An explicit module can only be specified for an in-memory file.


</div>

</div>
