---
tags:
 - jvm
title: "KotlinStubVersions"
---

# KotlinStubVersions

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">KotlinStubVersions</a>
</span></code></pre></div>
</div>

## Properties
### BUILTIN_STUB_VERSION

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">const </span><span class="kd">val </span><a href="index.html#builtin_stub_version">BUILTIN_STUB_VERSION</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

BuiltIn stub version should be increased if changes are made to builtIn stub building subsystem (org.jetbrains.kotlin.idea.decompiler.builtIns) Increasing this version will lead to reindexing of all builtIn files (see KotlinBuiltInFileType).


</div>

</div>
### CLASSFILE_STUB_VERSION

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">const </span><span class="kd">val </span><a href="index.html#classfile_stub_version">CLASSFILE_STUB_VERSION</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

Classfile stub version should be increased if changes are made to classfile stub building subsystem (org.jetbrains.kotlin.idea.decompiler.classFile) Increasing this version will lead to reindexing of all classfiles.


</div>

</div>
### KLIB_STUB_VERSION

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">const </span><span class="kd">val </span><a href="index.html#klib_stub_version">KLIB_STUB_VERSION</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

Klib stub version should be increased if changes are made to the Klib stub building subsystem (org.jetbrains.kotlin.analysis.decompiler.konan). Increasing this version will lead to reindexing of .knm binary files (see KlibMetaFileType).


</div>

</div>
### SOURCE_STUB_VERSION

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">const </span><span class="kd">val </span><a href="index.html#source_stub_version">SOURCE_STUB_VERSION</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="o"> = </span><span class="nb">312</span>
</span></code></pre></div>
</div>


<div markdown>

Source stub version should be increased if stub format (org.jetbrains.kotlin.psi.stubs.impl) is changed or changes are made to the parser that can potentially modify the psi structure of kotlin source code. Though only kotlin declarations (no code in the bodies) are stubbed, please do increase this version if you are not 100% sure it can be avoided. Increasing this version will lead to reindexing of all kotlin source files on the first IDE startup with the new version.


</div>

</div>
