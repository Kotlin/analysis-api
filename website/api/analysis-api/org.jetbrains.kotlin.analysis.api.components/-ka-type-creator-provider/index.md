---
tags:
 - jvm
title: "KaTypeCreatorProvider"
---

# KaTypeCreatorProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaTypeCreatorProvider</a> : <a href="../-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>Provides an instance of [`KaTypeCreator`](../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-type-creator/index.md) to create various [`types`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).

#### Inheritors


 - [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)



</div>

## Properties
### [`token`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#token)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#token">token</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaLifetimeToken`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md) which determines the lifetime of the lifetime owner.


</div>

</div>
### typeCreator

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#typecreator">typeCreator</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-type-creator/index.html">KaTypeCreator</a>
</span></code></pre></div>
</div>


<div markdown>

A single entry point for the type building infrastructure.


</div>

</div>
## Functions
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### copy

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#copy">T</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.html">KaClassType</a><span class="o">> </span><a href="index.html#copy">T</a><span class="p">.</span><a href="index.html#copy"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.html">KaClassType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaClassType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.md) with modifications applied via the [`init`](index.md#copy) block.

The builder is pre-populated with the properties of the original type. The [`init`](index.md#copy) block can then selectively override these properties.

**Example:**

```kotlin
val nullableListOfString = listOfStringType.copy {
    isMarkedNullable = true
}
```

**See also**



 - [`KaTypeCreator.classType`](../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-function-type-builder/index.md#classtype)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/index.html">KaUsualClassType</a><span class="p">.</span><a href="index.html#copy"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/index.html">KaUsualClassType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaUsualClassType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/index.md) with modifications applied via the [`init`](index.md#copy) block.

The builder is pre-populated with the properties of the original type. The [`init`](index.md#copy) block can then selectively override these properties.

**Example:**

```kotlin
val nullableListOfString = listOfStringType.copy {
    isMarkedNullable = true
}
```

**See also**



 - [`KaTypeCreator.classType`](../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-function-type-builder/index.md#classtype)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.html">KaFunctionType</a><span class="p">.</span><a href="index.html#copy"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-function-type-builder/index.html">KaFunctionTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.html">KaFunctionType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaFunctionType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.md) with modifications applied via the [`init`](index.md#copy) block.

The builder is pre-populated with the properties of the original type. The [`init`](index.md#copy) block can then selectively override these properties.

**Example:**

```kotlin
val suspendVersion = functionType.copy {
    isSuspend = true
}
```

**See also**



 - [`KaTypeCreator.functionType`](../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-function-type-builder/index.md#functiontype)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a><span class="p">.</span><a href="index.html#copy"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-type-parameter-type-builder/index.html">KaTypeParameterTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaTypeParameterType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.md) with modifications applied via the [`init`](index.md#copy) block.

The builder is pre-populated with the properties of the original type. The [`init`](index.md#copy) block can then selectively override these properties.

**Example:**

```kotlin
val nullableT = typeParameterType.copy {
    isMarkedNullable = true
}
```

**See also**



 - [`KaTypeCreator.typeParameterType`](../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-function-type-builder/index.md#typeparametertype)



</div>

</div>
### [`isValid`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#isvalid)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#isvalid"><span class="nf">isValid</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the lifetime owner is still valid, i.e. we are still in the scope of the lifetime owner's regular lifetime.


</div>

</div>
### [`withValidityAssertion`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion"><span class="nf">withValidityAssertion</span></a><span class="p">(</span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a>
</span></code></pre></div>
</div>


<div markdown>

Executes [`action`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion) only if the [`KaLifetimeOwner`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.md) is still [`valid`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md#isvalid) and [`accessible`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md#isaccessible). Otherwise, throws a validity exception based on the concrete violation.


</div>

</div>
