---
tags:
 - jvm
title: "KaCompiledClassHandler"
---

# KaCompiledClassHandler

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="kd">interface </span><a href="index.html">KaCompiledClassHandler</a> : <a href="../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compiled-class-handler/index.html">KaCompiledClassHandler</a>
</span></code></pre></div><strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.compilation.KaCompiledClassHandler</strong>`](../../org.jetbrains.kotlin.analysis.api.compilation/-ka-compiled-class-handler/index.md)<strong> instead.</strong>

A handler which is called whenever a new class file is produced, when compiling sources to the JVM target.

#### See also


 - [`KaCompilationTarget.JVM`](../-ka-compilation-target/-j-v-m/index.md)



</div>

## Functions
### handleClassDefinition

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#handleclassdefinition"><span class="nf">handleClassDefinition</span></a><span class="p">(</span>file<span class="o">: </span>PsiFile<span class="o">?</span><span class="p">, </span>className<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

[`handleClassDefinition`](index.md#handleclassdefinition) is called whenever a new class file is produced.

**Parameters**



 - file: The PsiFile containing the class definition. It can be `null` when the generated class file has no PSI file in sources, for example if it's an anonymous object from another module, regenerated during inlining.


 - className: The name of the class in the JVM's internal name format, for example `"java/lang/Object"`.





</div>

</div>
