---
tags:
 - jvm
title: "KaInternalsTypeCreatorProvider"
---

# KaInternalsTypeCreatorProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaInternalsTypeCreatorProvider</a>
</span></code></pre></div>
</div>

## Properties
### typeCreator

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#typecreator">typeCreator</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-type-creator/index.html">KaTypeCreator</a>
</span></code></pre></div>
</div>

</div>
## Functions
### copy

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#copy">T</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.html">KaClassType</a><span class="o">> </span><a href="index.html#copy"><span class="nf">copy</span></a><span class="p">(</span>type<span class="o">: </span><a href="index.html#copy">T</a><span class="p">, </span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.html">KaClassType</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#copy"><span class="nf">copy</span></a><span class="p">(</span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/index.html">KaUsualClassType</a><span class="p">, </span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/index.html">KaUsualClassType</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#copy"><span class="nf">copy</span></a><span class="p">(</span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.html">KaFunctionType</a><span class="p">, </span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-function-type-builder/index.html">KaFunctionTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.html">KaFunctionType</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#copy"><span class="nf">copy</span></a><span class="p">(</span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a><span class="p">, </span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-type-parameter-type-builder/index.html">KaTypeParameterTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a>
</span></code></pre></div>
</div>

</div>
