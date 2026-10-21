---
tags:
 - jvm
title: "BuiltinsVirtualFileProvider"
---

# BuiltinsVirtualFileProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">BuiltinsVirtualFileProvider</a>
</span></code></pre></div>Provides the `.kotlin_builtins` files that back the fallback built-ins of the analysis.

Built-ins normally resolve from the Kotlin stdlib among the analyzed module's dependencies, which ships `.kotlin_builtins` files of its own. The fallback built-ins are a second source, ordered behind every real dependency, so they answer only what the stdlib did not: a module with no stdlib on its dependency path, or a declaration its stdlib variant does not publish — `kotlin-stdlib-common`, for one, leaves built-in declarations out of its `.kotlin_metadata` files.

They therefore have to be there even when the analyzed project has no stdlib at all, which is why they are read from the classpath of the analysis implementation rather than from the project: resources of the Kotlin plugin in the IDE, entries of a JAR on the classpath in Standalone mode. Turning such a resource into a VirtualFile is what a platform supplies here.

A platform is expected to implement [`BuiltinsVirtualFileProviderBaseImpl`](../-builtins-virtual-file-provider-base-impl/index.md) instead of this class directly and register the result as an application service.

#### Inheritors


 - [`BuiltinsVirtualFileProviderBaseImpl`](../-builtins-virtual-file-provider-base-impl/index.md)



</div>

## Constructors
### BuiltinsVirtualFileProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Functions
### createBuiltinsScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createbuiltinsscope"><span class="nf">createBuiltinsScope</span></a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span><span class="o">: </span>GlobalSearchScope
</span></code></pre></div>
</div>


<div markdown>

Creates a search scope covering exactly the files of [`getBuiltinVirtualFiles`](index.md#getbuiltinvirtualfiles).

The scope is not a part of any module content, as built-ins do not belong to the analyzed project.


</div>

</div>
### getBuiltinVirtualFiles

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getbuiltinvirtualfiles"><span class="nf">getBuiltinVirtualFiles</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>VirtualFile<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the virtual files of all built-in declaration files.


</div>

</div>
