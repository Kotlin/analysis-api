---
tags:
 - jvm
title: "contextModule"
---

# contextModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">var </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="context-module.html">contextModule</a><span class="o">: </span><a href="-ka-module/index.html">KaModule</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A context module against which analysis of this in-memory file should be performed. It can only be specified for an in-memory file.

Normally, the context module is determined automatically from a context element or an original file. This property can be used to specify the context module explicitly in certain cases.

[`contextModule`](context-module.md) cannot be specified for a code fragment. The context module of the code fragment must be determined by the context element. It is the essence of a code fragment to be analyzed in the context of another element, and this behavior should not be overridden.


</div>

</div>
