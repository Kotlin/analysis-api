---
tags:
 - jvm
title: "copy"
---

# copy

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><span class="o"><</span><a href="copy.html">T</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.html">KaClassType</a><span class="o">> </span><a href="copy.html">T</a><span class="p">.</span><a href="copy.html"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.html">KaClassType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaClassType`](../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.md) with modifications applied via the [`init`](copy.md) block.

The builder is pre-populated with the properties of the original type. The [`init`](copy.md) block can then selectively override these properties.

#### Example:
```kotlin
val nullableListOfString = listOfStringType.copy {
    isMarkedNullable = true
}
```

#### See also


 - [`KaTypeCreator.classType`](-ka-function-type-builder/index.md#classtype)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/index.html">KaUsualClassType</a><span class="p">.</span><a href="copy.html"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/index.html">KaUsualClassType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaUsualClassType`](../org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/index.md) with modifications applied via the [`init`](copy.md) block.

The builder is pre-populated with the properties of the original type. The [`init`](copy.md) block can then selectively override these properties.

#### Example:
```kotlin
val nullableListOfString = listOfStringType.copy {
    isMarkedNullable = true
}
```

#### See also


 - [`KaTypeCreator.classType`](-ka-function-type-builder/index.md#classtype)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.html">KaFunctionType</a><span class="p">.</span><a href="copy.html"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="-ka-function-type-builder/index.html">KaFunctionTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.html">KaFunctionType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaFunctionType`](../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.md) with modifications applied via the [`init`](copy.md) block.

The builder is pre-populated with the properties of the original type. The [`init`](copy.md) block can then selectively override these properties.

#### Example:
```kotlin
val suspendVersion = functionType.copy {
    isSuspend = true
}
```

#### See also


 - [`KaTypeCreator.functionType`](-ka-function-type-builder/index.md#functiontype)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a><span class="p">.</span><a href="copy.html"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="-ka-type-parameter-type-builder/index.html">KaTypeParameterTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaTypeParameterType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.md) with modifications applied via the [`init`](copy.md) block.

The builder is pre-populated with the properties of the original type. The [`init`](copy.md) block can then selectively override these properties.

#### Example:
```kotlin
val nullableT = typeParameterType.copy {
    isMarkedNullable = true
}
```

#### See also


 - [`KaTypeCreator.typeParameterType`](-ka-function-type-builder/index.md#typeparametertype)



</div>

</div>
