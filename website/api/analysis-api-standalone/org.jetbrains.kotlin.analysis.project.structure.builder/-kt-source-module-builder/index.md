---
tags:
 - jvm
title: "KtSourceModuleBuilder"
---

# KtSourceModuleBuilder

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KtSourceModuleBuilder</a><span class="p">(</span>coreApplicationEnvironment<span class="o">: </span>CoreApplicationEnvironment<span class="p">, </span>project<span class="o">: </span>Project<span class="p">)</span> : <a href="../-kt-module-builder/index.html">KtModuleBuilder</a>
</span></code></pre></div>
</div>

## Constructors
### KtSourceModuleBuilder

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>coreApplicationEnvironment<span class="o">: </span>CoreApplicationEnvironment<span class="p">, </span>project<span class="o">: </span>Project<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### contentScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">var </span><a href="index.html#contentscope">contentScope</a><span class="o">: </span>GlobalSearchScope<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### languageVersionSettings

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">var </span><a href="index.html#languageversionsettings">languageVersionSettings</a><span class="o">: </span>LanguageVersionSettings
</span></code></pre></div>
</div>

</div>
### moduleName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">lateinit </span><span class="kd">var </span><a href="index.html#modulename">moduleName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### platform

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">lateinit </span><span class="kd">var </span><a href="index.html#platform">platform</a><span class="o">: </span>TargetPlatform
</span></code></pre></div>
</div>

</div>
## Functions
### addDependsOnDependency

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#adddependsondependency"><span class="nf">addDependsOnDependency</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### addFriendDependency

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#addfrienddependency"><span class="nf">addFriendDependency</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### addRegularDependency

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#addregulardependency"><span class="nf">addRegularDependency</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### addSourceRoot

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#addsourceroot"><span class="nf">addSourceRoot</span></a><span class="p">(</span>path<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/nio/file/Path.html">Path</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### addSourceRoots

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#addsourceroots"><span class="nf">addSourceRoots</span></a><span class="p">(</span>paths<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/nio/file/Path.html">Path</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### addSourceVirtualFile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#addsourcevirtualfile"><span class="nf">addSourceVirtualFile</span></a><span class="p">(</span>virtualFile<span class="o">: </span>VirtualFile<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### addSourceVirtualFiles

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#addsourcevirtualfiles"><span class="nf">addSourceVirtualFiles</span></a><span class="p">(</span>virtualFiles<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span>VirtualFile<span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### build

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#build"><span class="nf">build</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-source-module/index.html">KaSourceModule</a>
</span></code></pre></div>
</div>

</div>
