---
tags:
 - jvm
title: "KaCompiledFile"
---

# KaCompiledFile

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaCompiledFile</a> : <a href="../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compiled-file/index.html">KaCompiledFile</a>
</span></code></pre></div><strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.compilation.KaCompiledFile</strong>`](../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compiled-file/index.md)<strong> instead.</strong>


</div>

## Properties
### content

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#content">content</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/index.html">ByteArray</a>
</span></code></pre></div>
</div>


<div markdown>

The content of the compiled file.


</div>

</div>
### [`isClassFile`](index.md#isclassfile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compiled-file/index.html">KaCompiledFile</a><span class="p">.</span><a href="index.html#isclassfile">isClassFile</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the compiled file is a Java class file.


</div>

</div>
### path

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#path">path</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

The path of the compiled file relative to the root of the output directory.


</div>

</div>
### sourceFiles

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#sourcefiles">sourceFiles</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/io/File.html">File</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The source files that were compiled to produce this file.


</div>

</div>
