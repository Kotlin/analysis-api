---
tags:
 - jvm
title: "StandaloneAnalysisAPISessionBuilder"
---

# StandaloneAnalysisAPISessionBuilder

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">StandaloneAnalysisAPISessionBuilder</a><span class="p">(</span>projectDisposable<span class="o">: </span>Disposable<span class="p">, </span>unitTestMode<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>

## Constructors
### StandaloneAnalysisAPISessionBuilder

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>projectDisposable<span class="o">: </span>Disposable<span class="p">, </span>unitTestMode<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### application

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#application">application</a><span class="o">: </span>Application
</span></code></pre></div>
</div>

</div>
### project

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#project">project</a><span class="o">: </span>Project
</span></code></pre></div>
</div>

</div>
## Functions
### build

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#build"><span class="nf">build</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-standalone-analysis-a-p-i-session/index.html">StandaloneAnalysisAPISession</a>
</span></code></pre></div>
</div>

</div>
### buildKtModuleProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#buildktmoduleprovider"><span class="nf">buildKtModuleProvider</span></a><span class="p">(</span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.project.structure.builder/-ka-module-container-builder/index.html">KaModuleContainerBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### enableCacheCleaner

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#enablecachecleaner"><span class="nf">enableCacheCleaner</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Enables a cache cleaner for the current session. It might attempt to drop internal caches to avoid memory issues.

The cleaner is mostly designed for long-running workloads where analyze affects so many modules that cache size blows out of proportion.

See [KT-70489](https://youtrack.jetbrains.com/issue/KT-70489) for more details.


</div>

</div>
### registerApplicationService

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#registerapplicationservice">T</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">> </span><a href="index.html#registerapplicationservice"><span class="nf">registerApplicationService</span></a><span class="p">(</span>serviceInterface<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="index.html#registerapplicationservice">T</a><span class="o">></span><span class="p">, </span>serviceImplementation<span class="o">: </span><a href="index.html#registerapplicationservice">T</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#registerapplicationservice">T</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">> </span><a href="index.html#registerapplicationservice"><span class="nf">registerApplicationService</span></a><span class="p">(</span>serviceImplementation<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="index.html#registerapplicationservice">T</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### registerProjectExtensionPoint

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#registerprojectextensionpoint">T</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">> </span><a href="index.html#registerprojectextensionpoint"><span class="nf">registerProjectExtensionPoint</span></a><span class="p">(</span>extensionPointName<span class="o">: </span>ExtensionPointName<span class="o"><</span><a href="index.html#registerprojectextensionpoint">T</a><span class="o">></span><span class="p">, </span>extensionClass<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="index.html#registerprojectextensionpoint">T</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### registerProjectService

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#registerprojectservice">T</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">> </span><a href="index.html#registerprojectservice"><span class="nf">registerProjectService</span></a><span class="p">(</span>serviceInterface<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="index.html#registerprojectservice">T</a><span class="o">></span><span class="p">, </span>serviceImplementation<span class="o">: </span><a href="index.html#registerprojectservice">T</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#registerprojectservice">T</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">> </span><a href="index.html#registerprojectservice"><span class="nf">registerProjectService</span></a><span class="p">(</span>serviceImplementation<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="index.html#registerprojectservice">T</a><span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
