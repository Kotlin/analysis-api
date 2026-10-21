---
tags:
 - jvm
title: "KotlinProjectStructureProvider"
---

# KotlinProjectStructureProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinProjectStructureProvider</a>
</span></code></pre></div>[`KotlinProjectStructureProvider`](index.md) provides information about the project's structure as managed by the Analysis API platform.

The project structure provider must only provide a [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md) for files/PSI elements which are included in that module's [`content scope`](../-ka-dangling-file-module-impl/index.md#contentscope). Implementations of [`KotlinProjectStructureProvider`](index.md) are encouraged to check containing files against the content scopes of candidate [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md)s.

#### See also


 - [`KaModuleProvider`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module-provider/index.md)


#### Inheritors


 - [`KotlinProjectStructureProviderBase`](../-kotlin-project-structure-provider-base/index.md)



</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Properties
### globalLanguageVersionSettings

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../-kotlin-project-structure-provider-base/index.html#globallanguageversionsettings">globalLanguageVersionSettings</a><span class="o">: </span>LanguageVersionSettings
</span></code></pre></div>
</div>


<div markdown>

Project-global LanguageVersionSettings for source modules lacking explicit settings (such as [`KaNotUnderContentRootModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-not-under-content-root-module/index.md)).


</div>

</div>
### libraryLanguageVersionSettings

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../-kotlin-project-structure-provider-base/index.html#librarylanguageversionsettings">libraryLanguageVersionSettings</a><span class="o">: </span>LanguageVersionSettings
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-kotlin-project-structure-provider-base/index.html#getimplementingmodules"><span class="nf">getImplementingModules</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### getModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-kotlin-project-structure-provider-base/index.html#getmodule"><span class="nf">getModule</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">, </span>useSiteModule<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

**See also**



 - [`KaModuleProvider.getModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module-provider/get-module.md)



</div>

</div>
