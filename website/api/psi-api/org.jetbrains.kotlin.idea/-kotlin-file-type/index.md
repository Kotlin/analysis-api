---
tags:
 - jvm
title: "KotlinFileType"
---

# KotlinFileType

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="index.html">KotlinFileType</a> : LanguageFileType
</span></code></pre></div>
</div>

## Companion properties
### DOT_DEFAULT_EXTENSION

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#dot_default_extension">DOT_DEFAULT_EXTENSION</a><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="o"> = </span><span class="s">".kt"</span>
</span></code></pre></div>
</div>

</div>
### DOT_SCRIPT_EXTENSION

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#dot_script_extension">DOT_SCRIPT_EXTENSION</a><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="o"> = </span><span class="s">".kts"</span>
</span></code></pre></div>
</div>

</div>
### [`EMPTY_ARRAY`](../-kotlin-module-file-type/index.md#empty_array)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-kotlin-module-file-type/index.html#empty_array">EMPTY_ARRAY</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>FileType<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### EXTENSION

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#extension">EXTENSION</a><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="o"> = </span><span class="s">"kt"</span>
</span></code></pre></div>
</div>

</div>
### INSTANCE

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#instance">INSTANCE</a><span class="o">: </span><a href="index.html">KotlinFileType</a>
</span></code></pre></div>
</div>

</div>
### SCRIPT_EXTENSION

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#script_extension">SCRIPT_EXTENSION</a><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="o"> = </span><span class="s">"kts"</span>
</span></code></pre></div>
</div>

</div>
## Functions
### [`extractCharsetFromFileContent`](index.md#extractcharsetfromfilecontent)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#extractcharsetfromfilecontent"><span class="nf">extractCharsetFromFileContent</span></a><span class="p">(</span>
    project<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> Project<span class="p">, </span>
    file<span class="o">: </span><span class="se">@</span><span class="se">Nullable</span> VirtualFile<span class="p">, </span>
    content<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
<span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/nio/charset/Charset.html">Charset</a>
</span></code></pre></div>
</div>

</div>
### [`getCharset`](index.md#getcharset)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getcharset"><span class="nf">getCharset</span></a><span class="p">(</span>file<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> VirtualFile<span class="p">, </span>content<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte/index.html">Byte</a><span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NonNls</span> <span class="se">@</span><span class="se">Nullable</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getdisplayname"><span class="nf">getDisplayName</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">Nls</span> <span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
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
### [`getLanguage`](index.md#getlanguage)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#getlanguage"><span class="nf">getLanguage</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Language
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
### [`isBinary`](index.md#isbinary)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#isbinary"><span class="nf">isBinary</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isCharsetHardcoded`](../-kotlin-module-file-type/index.md#ischarsethardcoded)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kotlin-module-file-type/index.html#ischarsethardcoded"><span class="nf">isCharsetHardcoded</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isJVMDebuggingSupported`](index.md#isjvmdebuggingsupported)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isjvmdebuggingsupported"><span class="nf">isJVMDebuggingSupported</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isReadOnly`](index.md#isreadonly)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isreadonly"><span class="nf">isReadOnly</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`isSecondary`](index.md#issecondary)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#issecondary"><span class="nf">isSecondary</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
