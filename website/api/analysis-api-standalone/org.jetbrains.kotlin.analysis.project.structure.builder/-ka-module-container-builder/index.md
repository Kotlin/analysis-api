---
tags:
 - jvm
title: "KaModuleContainerBuilder"
---

# KaModuleContainerBuilder

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KaModuleContainerBuilder</a><span class="p">(</span><span class="kd">val </span>coreApplicationEnvironment<span class="o">: </span>CoreApplicationEnvironment<span class="p">, </span><span class="kd">val </span>project<span class="o">: </span>Project<span class="p">)</span>
</span></code></pre></div>
</div>

## Constructors
### KaModuleContainerBuilder

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>coreApplicationEnvironment<span class="o">: </span>CoreApplicationEnvironment<span class="p">, </span>project<span class="o">: </span>Project<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### coreApplicationEnvironment

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#coreapplicationenvironment">coreApplicationEnvironment</a><span class="o">: </span>CoreApplicationEnvironment
</span></code></pre></div>
</div>

</div>
### libraryScopeConstructionMode

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">var </span><a href="index.html#libraryscopeconstructionmode">libraryScopeConstructionMode</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.standalone.projectStructure/-standalone-library-scope-construction-mode/index.html">StandaloneLibraryScopeConstructionMode</a>
</span></code></pre></div>
</div>


<div markdown>

The default [`StandaloneLibraryScopeConstructionMode`](../../org.jetbrains.kotlin.analysis.api.standalone.projectStructure/-standalone-library-scope-construction-mode/index.md) for library modules created within this provider via [`buildKtLibraryModule`](index.md#buildktlibrarymodule) or [`buildKtSdkModule`](index.md#buildktsdkmodule). Individual modules may override it.

The option is a <strong>workaround</strong> for exceptional cases. See [`StandaloneLibraryScopeConstructionMode`](../../org.jetbrains.kotlin.analysis.api.standalone.projectStructure/-standalone-library-scope-construction-mode/index.md) for more information.

<strong>Caution:</strong> Because a library module's content scope is built eagerly when the module is created, this default must be set before the corresponding module-building calls.


</div>

</div>
### platform

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">lateinit </span><span class="kd">var </span><a href="index.html#platform">platform</a><span class="o">: </span>TargetPlatform
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
### addModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#addmodule">M</a><span class="o"> : </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">> </span><a href="index.html#addmodule"><span class="nf">addModule</span></a><span class="p">(</span>module<span class="o">: </span><a href="index.html#addmodule">M</a><span class="p">)</span><span class="o">: </span><a href="index.html#addmodule">M</a>
</span></code></pre></div>
</div>

</div>
### build

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#build"><span class="nf">build</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-module-container/index.html">KaModuleContainer</a>
</span></code></pre></div>
</div>

</div>
### buildKtLibraryModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="index.html">KaModuleContainerBuilder</a><span class="p">.</span><a href="index.html#buildktlibrarymodule"><span class="nf">buildKtLibraryModule</span></a><span class="p">(</span>init<span class="o">: </span><a href="../-kt-library-module-builder/index.html">KtLibraryModuleBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-library-module/index.html">KaLibraryModule</a>
</span></code></pre></div>
</div>

</div>
### buildKtLibrarySourceModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="index.html">KaModuleContainerBuilder</a><span class="p">.</span><a href="index.html#buildktlibrarysourcemodule"><span class="nf">buildKtLibrarySourceModule</span></a><span class="p">(</span>init<span class="o">: </span><a href="../-kt-library-source-module-builder/index.html">KtLibrarySourceModuleBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-library-source-module/index.html">KaLibrarySourceModule</a>
</span></code></pre></div>
</div>

</div>
### buildKtScriptModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="index.html">KaModuleContainerBuilder</a><span class="p">.</span><a href="index.html#buildktscriptmodule"><span class="nf">buildKtScriptModule</span></a><span class="p">(</span>init<span class="o">: </span><a href="../-kt-script-module-builder/index.html">KtScriptModuleBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-script-module/index.html">KaScriptModule</a>
</span></code></pre></div>
</div>

</div>
### buildKtSdkModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="index.html">KaModuleContainerBuilder</a><span class="p">.</span><a href="index.html#buildktsdkmodule"><span class="nf">buildKtSdkModule</span></a><span class="p">(</span>init<span class="o">: </span><a href="../-kt-sdk-module-builder/index.html">KtSdkModuleBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-library-module/index.html">KaLibraryModule</a>
</span></code></pre></div>
</div>

</div>
### buildKtSourceModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="index.html">KaModuleContainerBuilder</a><span class="p">.</span><a href="index.html#buildktsourcemodule"><span class="nf">buildKtSourceModule</span></a><span class="p">(</span>init<span class="o">: </span><a href="../-kt-source-module-builder/index.html">KtSourceModuleBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-source-module/index.html">KaSourceModule</a>
</span></code></pre></div>
</div>

</div>
