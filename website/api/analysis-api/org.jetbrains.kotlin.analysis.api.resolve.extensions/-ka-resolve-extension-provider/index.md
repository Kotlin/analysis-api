---
tags:
 - jvm
title: "KaResolveExtensionProvider"
---

# KaResolveExtensionProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KaResolveExtensionProvider</a>
</span></code></pre></div>Provides [`resolve extensions`](../-ka-resolve-extension/index.md) for [`KaModule`](../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md)s. Resolve extensions provide additional Kotlin files containing generated declarations, which will be included in the resolution as if they were regular source files in the module.


</div>

## Constructors
### KaResolveExtensionProvider

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
### provideExtensionsFor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#provideextensionsfor"><span class="nf">provideExtensionsFor</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-resolve-extension/index.html">KaResolveExtension</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Provides a list of [`resolve extensions`](../-ka-resolve-extension/index.md) for the given [`module`](index.md#provideextensionsfor).

The function should not generate the actual file text or perform any heavy analysis. Any file text should only be generated lazily in [`KaResolveExtensionFile.buildFileText`](../-ka-resolve-extension-file/index.md#buildfiletext).

Additionally, all implementations should:

 - Consider caching the results for subsequent invocations.


 - Avoid using Kotlin resolution, as this function is called during session initialization, so Analysis API access is forbidden.


 - Avoid using [`KaModule.contentScope`](../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-not-under-content-root-module/index.md#contentscope) of [`module`](index.md#provideextensionsfor), as [`KaResolveExtensionProvider.provideExtensionsFor`](index.md#provideextensionsfor) is used to lazily calculate content scopes.


 - Also avoid using [`KaModuleProvider`](../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module-provider/index.md) or the project structure      provider, as content scope calculation may be triggered during `getModule`.



</div>

</div>
