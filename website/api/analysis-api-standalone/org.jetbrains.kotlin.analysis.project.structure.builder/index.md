---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.project.structure.builder"
---

# org.jetbrains.kotlin.analysis.project.structure.builder
## Types
### [`KaModuleContainer`](-ka-module-container/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-module-container/index.html">KaModuleContainer</a>
</span></code></pre></div>
</div>

</div>
### [`KaModuleContainerBuilder`](-ka-module-container-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-module-container-builder/index.html">KaModuleContainerBuilder</a><span class="p">(</span><span class="kd">val </span>coreApplicationEnvironment<span class="o">: </span>CoreApplicationEnvironment<span class="p">, </span><span class="kd">val </span>project<span class="o">: </span>Project<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`KtBinaryModuleBuilder`](-kt-binary-module-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-binary-module-builder/index.html">KtBinaryModuleBuilder</a> : <a href="-kt-module-builder/index.html">KtModuleBuilder</a>
</span></code></pre></div>
</div>

</div>
### [`KtLibraryModuleBuilder`](-kt-library-module-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-kt-library-module-builder/index.html">KtLibraryModuleBuilder</a><span class="p">(</span>
    coreApplicationEnvironment<span class="o">: </span>CoreApplicationEnvironment<span class="p">, </span>
    project<span class="o">: </span>Project<span class="p">, </span>
    isSdk<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
<span class="p">)</span> : <a href="-kt-binary-module-builder/index.html">KtBinaryModuleBuilder</a>
</span></code></pre></div>
</div>

</div>
### [`KtLibrarySourceModuleBuilder`](-kt-library-source-module-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-library-source-module-builder/index.html">KtLibrarySourceModuleBuilder</a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span> : <a href="-kt-module-builder/index.html">KtModuleBuilder</a>
</span></code></pre></div>
</div>

</div>
### [`KtModuleBuilder`](-kt-module-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kt-module-builder/index.html">KtModuleBuilder</a>
</span></code></pre></div>
</div>

</div>
### [`KtScriptModuleBuilder`](-kt-script-module-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-script-module-builder/index.html">KtScriptModuleBuilder</a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span> : <a href="-kt-module-builder/index.html">KtModuleBuilder</a>
</span></code></pre></div>
</div>

</div>
### [`KtSdkModuleBuilder`](-kt-sdk-module-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-sdk-module-builder/index.html">KtSdkModuleBuilder</a><span class="p">(</span>coreApplicationEnvironment<span class="o">: </span>CoreApplicationEnvironment<span class="p">, </span>project<span class="o">: </span>Project<span class="p">)</span> : <a href="-kt-library-module-builder/index.html">KtLibraryModuleBuilder</a>
</span></code></pre></div>
</div>

</div>
### [`KtSourceModuleBuilder`](-kt-source-module-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-kt-source-module-builder/index.html">KtSourceModuleBuilder</a><span class="p">(</span>coreApplicationEnvironment<span class="o">: </span>CoreApplicationEnvironment<span class="p">, </span>project<span class="o">: </span>Project<span class="p">)</span> : <a href="-kt-module-builder/index.html">KtModuleBuilder</a>
</span></code></pre></div>
</div>

</div>
## Functions
