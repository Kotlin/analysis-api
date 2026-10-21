---
tags:
 - jvm
title: "KotlinCompilerPluginsProvider"
---

# KotlinCompilerPluginsProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinCompilerPluginsProvider</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>[`KotlinCompilerPluginsProvider`](index.md) provides information about registered compiler plugins.

The component is optional. If [`KotlinCompilerPluginsProvider`](index.md) is not implemented, the Analysis API engine will assume that no compiler plugins are registered.


</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
### [`CompilerPluginType`](-compiler-plugin-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-compiler-plugin-type/index.html">CompilerPluginType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-compiler-plugin-type/index.html">KotlinCompilerPluginsProvider.CompilerPluginType</a><span class="o">> </span>
</span></code></pre></div>
</div>

</div>
## Functions
### getRegisteredExtensions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#getregisteredextensions">T</a><span class="o"> : </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">> </span><a href="index.html#getregisteredextensions"><span class="nf">getRegisteredExtensions</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">, </span>extensionType<span class="o">: </span>ExtensionPointDescriptor<span class="o"><</span><a href="index.html#getregisteredextensions">T</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html#getregisteredextensions">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns a possibly empty list of extensions of a base [`extensionType`](index.md#getregisteredextensions) that compiler plugins have registered for [`module`](index.md#getregisteredextensions).

These extensions are used in addition to those provided by the extension descriptor's ProjectExtensionDescriptor.getInstances.


</div>

</div>
### isPluginOfTypeRegistered

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#ispluginoftyperegistered"><span class="nf">isPluginOfTypeRegistered</span></a><span class="p">(</span>module<span class="o">: </span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.html">KaModule</a><span class="p">, </span>pluginType<span class="o">: </span><a href="-compiler-plugin-type/index.html">KotlinCompilerPluginsProvider.CompilerPluginType</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if at least one plugin with the requested [`pluginType`](index.md#ispluginoftyperegistered) is registered, and `false` otherwise.


</div>

</div>
