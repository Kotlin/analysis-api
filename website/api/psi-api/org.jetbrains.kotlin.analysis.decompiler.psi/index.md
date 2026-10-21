---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.decompiler.psi"
---

# org.jetbrains.kotlin.analysis.decompiler.psi
## Types
### [`BuiltinsVirtualFileProvider`](-builtins-virtual-file-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-builtins-virtual-file-provider/index.html">BuiltinsVirtualFileProvider</a>
</span></code></pre></div>
</div>


<div markdown>

Provides the `.kotlin_builtins` files that back the fallback built-ins of the analysis.


</div>

</div>
### [`BuiltinsVirtualFileProviderBaseImpl`](-builtins-virtual-file-provider-base-impl/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-builtins-virtual-file-provider-base-impl/index.html">BuiltinsVirtualFileProviderBaseImpl</a> : <a href="-builtins-virtual-file-provider/index.html">BuiltinsVirtualFileProvider</a>
</span></code></pre></div>
</div>


<div markdown>

A [`BuiltinsVirtualFileProvider`](-builtins-virtual-file-provider/index.md) that discovers built-in files as resources of its own class loader.


</div>

</div>
### [`KotlinBuiltInFileType`](-kotlin-built-in-file-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-kotlin-built-in-file-type/index.html">KotlinBuiltInFileType</a> : FileType
</span></code></pre></div>
</div>


<div markdown>

The file type of Kotlin built-in declaration files: `.kotlin_builtins` and `.kotlin_metadata`.


</div>

</div>
### [`KotlinLabelProviderService`](-kotlin-label-provider-service/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-kotlin-label-provider-service/index.html">KotlinLabelProviderService</a>
</span></code></pre></div>
</div>


<div markdown>

Supplies human-readable, localizable descriptions for the binary Kotlin file types.


</div>

</div>
