---
tags:
 - jvm
title: "BuiltinsVirtualFileProviderBaseImpl"
---

# BuiltinsVirtualFileProviderBaseImpl

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">BuiltinsVirtualFileProviderBaseImpl</a> : <a href="../-builtins-virtual-file-provider/index.html">BuiltinsVirtualFileProvider</a>
</span></code></pre></div>A [`BuiltinsVirtualFileProvider`](../-builtins-virtual-file-provider/index.md) that discovers built-in files as resources of its own class loader.

Implementors only have to map a resource [`java.net.URL`](https://docs.oracle.com/javase/8/docs/api/java/net/URL.html) to a VirtualFile of the file system they operate on; locating the built-in resources and building the search scope are handled here.


</div>

## Constructors
### BuiltinsVirtualFileProviderBaseImpl

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Functions
### createBuiltinsScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#createbuiltinsscope"><span class="nf">createBuiltinsScope</span></a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span><span class="o">: </span>GlobalSearchScope
</span></code></pre></div>
</div>


<div markdown>

Creates a search scope covering exactly the files of [`getBuiltinVirtualFiles`](../-builtins-virtual-file-provider/index.md#getbuiltinvirtualfiles).

The scope is not a part of any module content, as built-ins do not belong to the analyzed project.


</div>

</div>
### getBuiltinVirtualFiles

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getbuiltinvirtualfiles"><span class="nf">getBuiltinVirtualFiles</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>VirtualFile<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the virtual files of all built-in declaration files.


</div>

</div>
