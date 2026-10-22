---
tags:
 - jvm
title: "KtModuleBuilder"
---

# KtModuleBuilder

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KtModuleBuilder</a>
</span></code></pre></div>#### Inheritors


 - [`KtBinaryModuleBuilder`](../-kt-binary-module-builder/index.md)
 - [`KtLibrarySourceModuleBuilder`](../-kt-library-source-module-builder/index.md)
 - [`KtScriptModuleBuilder`](../-kt-script-module-builder/index.md)
 - [`KtSourceModuleBuilder`](../-kt-source-module-builder/index.md)



</div>

## Constructors
### KtModuleBuilder

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### platform

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">lateinit </span><span class="kd">var </span><a href="../-kt-source-module-builder/index.html#platform">platform</a><span class="o">: </span>TargetPlatform
</span></code></pre></div>
</div>

</div>
## Functions
### addDependsOnDependency

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-source-module-builder/index.html#adddependsondependency"><span class="nf">addDependsOnDependency</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### addFriendDependency

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-source-module-builder/index.html#addfrienddependency"><span class="nf">addFriendDependency</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### addRegularDependency

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../-kt-source-module-builder/index.html#addregulardependency"><span class="nf">addRegularDependency</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### build

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#build"><span class="nf">build</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>

</div>
