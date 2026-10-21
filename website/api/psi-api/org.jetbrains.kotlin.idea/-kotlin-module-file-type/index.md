---
tags:
 - jvm
title: "KotlinModuleFileType"
---

# KotlinModuleFileType

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="index.html">KotlinModuleFileType</a> : FileType
</span></code></pre></div>
</div>

## Companion properties
### [`EMPTY_ARRAY`](index.md#empty_array)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#empty_array">EMPTY_ARRAY</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>FileType<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### EXTENSION

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#extension">EXTENSION</a><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="o"> = </span><span class="s">"kotlin_module"</span>
</span></code></pre></div>
</div>

</div>
### INSTANCE

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#instance">INSTANCE</a><span class="o">: </span><a href="index.html">KotlinModuleFileType</a>
</span></code></pre></div>
</div>

</div>
## Functions
### getCharset

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getcharset"><span class="nf">getCharset</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> file<span class="o">: </span>VirtualFile<span class="p">, </span><span class="se">@</span><span class="se">NotNull</span> content<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte/index.html">Byte</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
### getDefaultExtension

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getdefaultextension"><span class="nf">getDefaultExtension</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
### getDescription

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getdescription"><span class="nf">getDescription</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`getDisplayName`](index.md#getdisplayname)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getdisplayname"><span class="nf">getDisplayName</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <span class="se">@</span><span class="se">Nls</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
### getIcon

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#geticon"><span class="nf">getIcon</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/javax/swing/Icon.html">Icon</a>
</span></code></pre></div>
</div>

</div>
### getName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getname"><span class="nf">getName</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
### isBinary

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isbinary"><span class="nf">isBinary</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isCharsetHardcoded`](index.md#ischarsethardcoded)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#ischarsethardcoded"><span class="nf">isCharsetHardcoded</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### isReadOnly

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isreadonly"><span class="nf">isReadOnly</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
