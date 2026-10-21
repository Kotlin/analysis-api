---
tags:
 - jvm
title: "compile"
---

# compile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="compile.html"><span class="nf">compile</span></a><span class="p">(</span>file<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>options<span class="o">: </span><a href="-ka-compilation-options/index.html">KaCompilationOptions</a><span class="p">)</span><span class="o">: </span><a href="-ka-compilation-result/index.html">KaCompilationResult</a>
</span></code></pre></div>
</div>


<div markdown>

Compiles the given [`file`](compile.md) in-memory using the specified [`options`](compile.md).

The function rethrows exceptions from the compiler, wrapped in [`KaCodeCompilationException`](-ka-code-compilation-exception/index.md). The implementation should wrap the `compile()` call into a `try`/`catch` block when necessary.

#### Parameters


 - file: A file to compile. The file must be either a source module file, or a [`KtCodeFragment`](../../psi-api/org.jetbrains.kotlin.psi/-kt-code-fragment/index.md). For a [`KtCodeFragment`](../../psi-api/org.jetbrains.kotlin.psi/-kt-code-fragment/index.md), a source module context, a compiled library source context, or an empty context (`null`) are supported.


 - options: The compilation options created via [`createCompilationOptions`](create-compilation-options.md).




#### See also


 - [`createCompilationOptions`](create-compilation-options.md)



</div>

</div>
