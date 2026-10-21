---
tags:
 - jvm
title: "KotlinPlatformSettings"
---

# KotlinPlatformSettings

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinPlatformSettings</a> : <a href="../-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>[`KotlinPlatformSettings`](index.md) allow the Analysis API platform to control the behavior of the Analysis API engine.


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
### allowUseSiteLibraryModuleAnalysis

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="index.html#allowusesitelibrarymoduleanalysis">allowUseSiteLibraryModuleAnalysis</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether analysis of use-site [`KaLibraryModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-library-module/index.md)s is allowed by the platform. When this is `false`, attempts to analyze a [`KaLibraryModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-library-module/index.md) will result in an exception.

See KT-76042 for more information.


</div>

</div>
### deserializedDeclarationsOrigin

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#deserializeddeclarationsorigin">deserializedDeclarationsOrigin</a><span class="o">: </span><a href="../-kotlin-deserialized-declarations-origin/index.html">KotlinDeserializedDeclarationsOrigin</a>
</span></code></pre></div>
</div>


<div markdown>

**See also**



 - [`KotlinDeserializedDeclarationsOrigin`](../-kotlin-deserialized-declarations-origin/index.md)



</div>

</div>
