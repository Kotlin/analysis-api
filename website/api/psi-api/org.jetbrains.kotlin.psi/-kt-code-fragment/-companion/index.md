---
tags:
 - jvm
title: "Companion"
---

# Companion

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">Companion</a>
</span></code></pre></div>
</div>

## Properties
### FAKE_CONTEXT_FOR_JAVA_FILE

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#fake_context_for_java_file">FAKE_CONTEXT_FOR_JAVA_FILE</a><span class="o">: </span>Key<span class="o"><</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="../../-kt-element/index.html">KtElement</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A copyable user-data key holding a provider of a fake Kotlin context element. It is used when a fragment's real context is a non-Kotlin (for example, Java) file, so that references can still be resolved as Kotlin.


</div>

</div>
### IMPORT_MODIFICATION

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#import_modification">IMPORT_MODIFICATION</a><span class="o">: </span>Topic<span class="o"><</span><a href="../../-kotlin-code-fragment-import-modification-listener/index.html">KotlinCodeFragmentImportModificationListener</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### IMPORT_SEPARATOR

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">const </span><span class="kd">val </span><a href="index.html#import_separator">IMPORT_SEPARATOR</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

The separator between individual imports in the raw import string accepted by a code fragment.


</div>

</div>
