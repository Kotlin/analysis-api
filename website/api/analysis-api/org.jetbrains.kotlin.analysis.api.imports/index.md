---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.imports"
---

# org.jetbrains.kotlin.analysis.api.imports
## Types
### [`KaDefaultImport`](-ka-default-import/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-default-import/index.html">KaDefaultImport</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a default import that the Kotlin compiler adds to each file during resolution.


</div>

</div>
### [`KaDefaultImportPriority`](-ka-default-import-priority/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-default-import-priority/index.html">KaDefaultImportPriority</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-default-import-priority/index.html">KaDefaultImportPriority</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Represents the priority of a default import.


</div>

</div>
### [`KaDefaultImports`](-ka-default-imports/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-default-imports/index.html">KaDefaultImports</a>
</span></code></pre></div>
</div>


<div markdown>

Represents information for [default imports](https://kotlinlang.org/docs/packages.html#default-imports) for a specific platform.


</div>

</div>
### [`KaDefaultImportsProvider`](-ka-default-imports-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-default-imports-provider/index.html">KaDefaultImportsProvider</a>
</span></code></pre></div>
</div>


<div markdown>

Provides a list of default imports for a specific TargetPlatform.


</div>

</div>
## Functions
### [`getDefaultImports`](get-default-imports.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>TargetPlatform<span class="p">.</span><a href="get-default-imports.html"><span class="nf">getDefaultImports</span></a><span class="p">(</span>project<span class="o">: </span>Project<span class="p">)</span><span class="o">: </span><a href="-ka-default-imports/index.html">KaDefaultImports</a>
</span></code></pre></div>
</div>


<div markdown>

Provides a list of default imports for a specific TargetPlatform.


</div>

</div>
