---
tags:
 - jvm
title: "KotlinProjectStructureProviderBase"
---

# KotlinProjectStructureProviderBase

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KotlinProjectStructureProviderBase</a> : <a href="../-kotlin-project-structure-provider/index.html">KotlinProjectStructureProvider</a>
</span></code></pre></div>
</div>

## Constructors
### KotlinProjectStructureProviderBase

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### globalLanguageVersionSettings

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="index.html#globallanguageversionsettings">globalLanguageVersionSettings</a><span class="o">: </span>LanguageVersionSettings
</span></code></pre></div>
</div>


<div markdown>

Project-global LanguageVersionSettings for source modules lacking explicit settings (such as [`KaNotUnderContentRootModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-not-under-content-root-module/index.md)).


</div>

</div>
### libraryLanguageVersionSettings

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="index.html#librarylanguageversionsettings">libraryLanguageVersionSettings</a><span class="o">: </span>LanguageVersionSettings
</span></code></pre></div>
</div>


<div markdown>

Project-global LanguageVersionSettings for [`KaLibraryModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-library-module/index.md)s and [`KaLibrarySourceModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-library-source-module/index.md)s.


</div>

</div>
## Functions
### getImplementingModules

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getimplementingmodules"><span class="nf">getImplementingModules</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### getModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getmodule"><span class="nf">getModule</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">, </span>useSiteModule<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

**See also**



 - [`KaModuleProvider.getModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module-provider/get-module.md)



</div>

</div>
