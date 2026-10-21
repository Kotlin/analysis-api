---
tags:
 - jvm
title: "KotlinLabelProviderService"
---

# KotlinLabelProviderService

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KotlinLabelProviderService</a>
</span></code></pre></div>Supplies human-readable, localizable descriptions for the binary Kotlin file types.

The file types fall back to hard-coded English descriptions when no service is registered, so a platform only needs to implement this service if it presents the file types in a user interface.


</div>

## Constructors
### KotlinLabelProviderService

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
### getLabelForBuiltInFileType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getlabelforbuiltinfiletype"><span class="nf">getLabelForBuiltInFileType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the description of [`KotlinBuiltInFileType`](../-kotlin-built-in-file-type/index.md).


</div>

</div>
### getLabelForKlibMetaFileType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getlabelforklibmetafiletype"><span class="nf">getLabelForKlibMetaFileType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the description of [`org.jetbrains.kotlin.analysis.decompiler.konan.KlibMetaFileType`](../../org.jetbrains.kotlin.analysis.decompiler.konan/-klib-meta-file-type/index.md).


</div>

</div>
