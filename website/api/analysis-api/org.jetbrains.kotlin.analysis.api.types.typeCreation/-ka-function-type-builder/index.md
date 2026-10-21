---
tags:
 - jvm
title: "KaFunctionTypeBuilder"
---

# KaFunctionTypeBuilder

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaFunctionTypeBuilder</a> : <a href="../-ka-type-builder-with-annotations/index.html">KaTypeBuilderWithAnnotations</a>
</span></code></pre></div>A builder for [`KaFunctionType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.md).

#### See also


 - [`KaTypeCreator.functionType`](index.md#functiontype)



</div>

## Properties
### annotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#annotations"><span class="nf">annotations</span></a><span class="p">(</span>annotationClassIds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/index.html">Iterable</a><span class="o"><</span>ClassId<span class="o">></span><span class="p">)</span>
</span></code></pre></div><div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#annotations"><span class="nf">annotations</span></a><span class="p">(</span>annotationClassIds<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/index.html">Iterable</a><span class="o"><</span>ClassId<span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Adds [`annotationClassIds`](index.md#annotations) to [`annotations`](index.md#annotations).

Note that the builder only supports annotations that accept no value arguments. All annotation classes requiring value arguments are discarded.

**See also**



 - [`KaType.annotations`](../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.md#annotations)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#annotations">annotations</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>ClassId<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of annotation ClassIds, which are used to construct annotations of the resulting type.

**See also**



 - [`KaType.annotations`](../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.md#annotations)



</div>

</div>
### contextParameters

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#contextparameters">contextParameters</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

List of context parameters for the function type.

Note that Kotlin prohibits context parameters in reflection types. So all context parameters passed to the builder are discarded when [`isReflectType`](index.md#isreflecttype) is `true`.

**See also**



 - [`KaFunctionType.contextParameterTypes`](../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.md#contextparametertypes)



</div>

</div>
### isMarkedNullable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">var </span><a href="index.html#ismarkednullable">isMarkedNullable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the type is marked as nullable, i.e., the type is represented as `(R.(T) -> S)?`.

Default value: `false`.

**See also**



 - [`KaTypeInformationProvider.isMarkedNullable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#ismarkednullable)



</div>

</div>
### isReflectType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">var </span><a href="index.html#isreflecttype">isReflectType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the function type is a reflection type (https://kotlinlang.org/docs/reflection.html#function-references)

Default value: `false`.

Note that Kotlin prohibits context parameters in reflection types. So all context parameters passed to the builder are discarded when [`isReflectType`](index.md#isreflecttype) is `true`.

**See also**



 - [`KaFunctionType.isReflectType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.md#isreflecttype)



</div>

</div>
### isSuspend

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">var </span><a href="index.html#issuspend">isSuspend</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the function type is a suspend type (https://kotlinlang.org/spec/asynchronous-programming-with-coroutines.html#suspending-functions).

Default value: `false`.

**See also**



 - [`KaFunctionType.isSuspend`](../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.md#issuspend)



</div>

</div>
### receiverType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">var </span><a href="index.html#receivertype">receiverType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Function receiver type.

Default value: `null`.

**See also**



 - [`KaFunctionType.receiverType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.md#receivertype)



</div>

</div>
### returnType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">var </span><a href="index.html#returntype">returnType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Function return type.

Default value: [`Unit`](../../org.jetbrains.kotlin.analysis.api.components/-ka-builtin-types/index.md#unit).

**See also**



 - [`KaFunctionType.returnType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.md#returntype)



</div>

</div>
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
### valueParameters

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#valueparameters">valueParameters</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-function-value-parameter/index.html">KaFunctionValueParameter</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Function value parameters.

**See also**



 - [`KaFunctionType.parameters`](../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.md#parameters)



</div>

</div>
## Functions
### annotation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#annotation"><span class="nf">annotation</span></a><span class="p">(</span>annotationClassId<span class="o">: </span>ClassId<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Adds [`annotationClassId`](index.md#annotation) to [`annotations`](index.md#annotations).

Note that the builder only supports annotations that accept no value arguments. All annotation classes requiring value arguments are discarded.

**See also**



 - [`KaType.annotations`](../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.md#annotations)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#annotation"><span class="nf">annotation</span></a><span class="p">(</span>annotationClassId<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span>ClassId<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Adds the annotation produced by [`annotationClassId`](index.md#annotation) to [`annotations`](index.md#annotations).

Note that the builder only supports annotations that accept no value arguments. All annotation classes requiring value arguments are discarded.

**See also**



 - [`KaType.annotations`](../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.md#annotations)



</div>

</div>
### arrayType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#arraytype"><span class="nf">arrayType</span></a><span class="p">(</span>elementType<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>init<span class="o">: </span><a href="../-ka-array-type-builder/index.html">KaArrayTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds an array type from the given [`elementType`](index.md#arraytype). For primitive element types, the [`KaArrayTypeBuilder.shouldPreferPrimitiveTypes`](../-ka-array-type-builder/index.md#shouldpreferprimitivetypes) option determines whether the array type will be a [primitive array type](https://kotlinlang.org/docs/arrays.html#primitive-type-arrays).

Array types are essentially class types and could be built manually via [`classType`](index.md#classtype). This builder just provides a more convenient way to construct them.

If the type was constructed successfully, returns [`KaClassType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.md). Otherwise, returns [`KaClassErrorType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-class-error-type/index.md).


</div>

</div>
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### capturedType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#capturedtype"><span class="nf">capturedType</span></a><span class="p">(</span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-captured-type/index.html">KaCapturedType</a><span class="p">, </span>init<span class="o">: </span><a href="../-ka-captured-type-builder/index.html">KaCapturedTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-captured-type/index.html">KaCapturedType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaCapturedType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-captured-type/index.md) based on the given [`type`](index.md#capturedtype).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#capturedtype"><span class="nf">capturedType</span></a><span class="p">(</span>projection<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-projection/index.html">KaTypeProjection</a><span class="p">, </span>init<span class="o">: </span><a href="../-ka-captured-type-builder/index.html">KaCapturedTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-captured-type/index.html">KaCapturedType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaCapturedType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-captured-type/index.md) with the given [`projection`](index.md#capturedtype).

Note that if [`projection`](index.md#capturedtype) is [`KaTypeArgumentWithVariance`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type-argument-with-variance/index.md), its [`KaTypeArgumentWithVariance.variance`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type-argument-with-variance/index.md#variance) must not be Variance.INVARIANT. Captured types are only intended to capture non-invariant projections. Otherwise, an exception is thrown.


</div>

</div>
### classType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#classtype"><span class="nf">classType</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">, </span>init<span class="o">: </span><a href="../-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a class type with the given [`classId`](index.md#classtype).

If there are no classes available by [`classId`](index.md#classtype), returns [`KaClassErrorType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-class-error-type/index.md).

A generic class type can be built by providing type arguments using the [`init`](index.md#classtype) block. The caller should provide the correct number of type arguments for the class. If the number of provided type arguments is lower, missing types arguments are filled with [`star projections`](../../org.jetbrains.kotlin.analysis.api.types/-ka-star-type-projection/index.md). If there are more type arguments than required, extra arguments are ignored.

**Example**

```kotlin
classType(StandardClassIds.List) {
    invariantTypeArgument(builtinTypes.string)
}
```


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#classtype"><span class="nf">classType</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">, </span>init<span class="o">: </span><a href="../-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a class type from the given class [`symbol`](index.md#classtype).

If it's impossible to construct a type from [`symbol`](index.md#classtype), returns [`KaClassErrorType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-class-error-type/index.md).

A generic class type can be built by providing type arguments using the [`init`](index.md#classtype) block. The caller is supposed to provide the correct number of type arguments for the class.

For Kotlin built-in types, consider using the overload that accepts a ClassId instead: `classType(StandardClassIds.String)`.

**Example**

```kotlin
classType(ktClass.classSymbol as KaClassSymbol) {
    invariantTypeArgument(builtinTypes.string)
}
```


</div>

</div>
### contextParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#contextparameter"><span class="nf">contextParameter</span></a><span class="p">(</span>contextParameter<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Adds the given [`contextParameter`](index.md#contextparameter) to the [`contextParameters`](index.md#contextparameters) list.

Note that Kotlin prohibits context parameters in reflection types. So all context parameters passed to the builder are discarded when [`isReflectType`](index.md#isreflecttype) is `true`.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#contextparameter"><span class="nf">contextParameter</span></a><span class="p">(</span>contextParameter<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Adds the type produced by [`contextParameter`](index.md#contextparameter) to the [`contextParameters`](index.md#contextparameters) list.

Note that Kotlin prohibits context parameters in reflection types. So all context parameters passed to the builder are discarded when [`isReflectType`](index.md#isreflecttype) is `true`.


</div>

</div>
### definitelyNotNullType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#definitelynotnulltype"><span class="nf">definitelyNotNullType</span></a><span class="p">(</span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-captured-type/index.html">KaCapturedType</a><span class="p">, </span>init<span class="o">: </span><a href="../-ka-definitely-not-null-type-builder/index.html">KaDefinitelyNotNullTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div><div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#definitelynotnulltype"><span class="nf">definitelyNotNullType</span></a><span class="p">(</span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a><span class="p">, </span>init<span class="o">: </span><a href="../-ka-definitely-not-null-type-builder/index.html">KaDefinitelyNotNullTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaDefinitelyNotNullType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-definitely-not-null-type/index.md) wrapping the given [`type`](index.md#definitelynotnulltype).

If [`type`](index.md#definitelynotnulltype) is not nullable, the original type is returned, as wrapping it in [`KaDefinitelyNotNullType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-definitely-not-null-type/index.md) is unnecessary.


</div>

</div>
### dynamicType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#dynamictype"><span class="nf">dynamicType</span></a><span class="p">(</span>init<span class="o">: </span><a href="../-ka-dynamic-type-builder/index.html">KaDynamicTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.html">KaDynamicType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaDynamicType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.md).


</div>

</div>
### flexibleType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#flexibletype"><span class="nf">flexibleType</span></a><span class="p">(</span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.html">KaFlexibleType</a><span class="p">, </span>init<span class="o">: </span><a href="../-ka-flexible-type-builder/index.html">KaFlexibleTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md) with initial bounds taken from the given [`type`](index.md#flexibletype).

If either of the bounds is [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md) itself, then the corresponding bound of this type is considered instead. I.e., if the upper bound is a [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md), then it's upper bound is taken as the resulting upper bound.

If the lower bound is not a subtype of the upper bound, `null` is returned.

If both bounds are equal, the bound type is returned, as it's unnecessary to create a flexible type in this case.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#flexibletype"><span class="nf">flexibleType</span></a><span class="p">(</span>init<span class="o">: </span><a href="../-ka-flexible-type-builder/index.html">KaFlexibleTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md).

If either of the bounds is [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md) itself, then the corresponding bound of this type is considered instead. I.e., if the upper bound is a [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md), then it's upper bound is taken as the resulting upper bound.

If the lower bound is not a subtype of the upper bound, `null` is returned.

If both bounds are equal, the bound type is returned, as it's unnecessary to create a flexible type in this case.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#flexibletype"><span class="nf">flexibleType</span></a><span class="p">(</span>lowerBound<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>upperBound<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md) with [`lowerBound`](index.md#flexibletype) and [`upperBound`](index.md#flexibletype) as bounds.

If either of the bounds is [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md) itself, then the corresponding bound of this type is considered instead. I.e., if the upper bound is a [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md), then it's upper bound is taken as the resulting upper bound.

If the lower bound is not a subtype of the upper bound, `null` is returned.

If both bounds are equal, the bound type is returned, as it's unnecessary to create a flexible type in this case.


</div>

</div>
### functionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#functiontype"><span class="nf">functionType</span></a><span class="p">(</span>init<span class="o">: </span><a href="index.html">KaFunctionTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.html">KaFunctionType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaFunctionType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.md) based on the given [`init`](index.md#functiontype) block.


</div>

</div>
### intersectionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#intersectiontype"><span class="nf">intersectionType</span></a><span class="p">(</span>init<span class="o">: </span><a href="../-ka-intersection-type-builder/index.html">KaIntersectionTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds an [`KaIntersectionType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-intersection-type/index.md).

The builder returns a normalized version of the intersection, i.e., all duplicated types are removed, nested intersection types are unwrapped, etc.

This normalized version isn't always [`KaIntersectionType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-intersection-type/index.md). For example, if there is a [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md) among conjuncts, the intersector might return another [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md) with [`KaIntersectionType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-intersection-type/index.md)s as bounds. That's due to the distributive property of intersection as a mathematical operation: `(A..B) & C = (A & C)..(B & C)`.

If there are no conjuncts, returns [`Any?`](../../org.jetbrains.kotlin.analysis.api.components/-ka-builtin-types/index.md#nullableany) as a neutral element of intersection operation. If a single conjunct is passed, returns that conjunct.

Note that currently it's impossible to provide annotations in [`KaIntersectionTypeBuilder`](../-ka-intersection-type-builder/index.md) due to KT-80749.


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
### starTypeProjection

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#startypeprojection"><span class="nf">starTypeProjection</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-star-type-projection/index.html">KaStarTypeProjection</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaStarTypeProjection`](../../org.jetbrains.kotlin.analysis.api.types/-ka-star-type-projection/index.md) (`*`).


</div>

</div>
### typeParameterType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#typeparametertype"><span class="nf">typeParameterType</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">, </span>init<span class="o">: </span><a href="../-ka-type-parameter-type-builder/index.html">KaTypeParameterTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="o"> = </span>{}<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaTypeParameterType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.md) with the given type parameter symbol.


</div>

</div>
### typeProjection

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#typeprojection"><span class="nf">typeProjection</span></a><span class="p">(</span>variance<span class="o">: </span>Variance<span class="p">, </span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-argument-with-variance/index.html">KaTypeArgumentWithVariance</a>
</span></code></pre></div><div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#typeprojection"><span class="nf">typeProjection</span></a><span class="p">(</span>variance<span class="o">: </span>Variance<span class="p">, </span>type<span class="o">: </span><a href="../-ka-type-creator/index.html">KaTypeCreator</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-argument-with-variance/index.html">KaTypeArgumentWithVariance</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a [`KaTypeArgumentWithVariance`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type-argument-with-variance/index.md).


</div>

</div>
### valueParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#valueparameter"><span class="nf">valueParameter</span></a><span class="p">(</span>name<span class="o">: </span>Name<span class="o">?</span><span class="p">, </span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Adds a value parameter with the given [`name`](index.md#valueparameter) and [`type`](index.md#valueparameter) to the [`valueParameters`](index.md#valueparameters) list.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#valueparameter"><span class="nf">valueParameter</span></a><span class="p">(</span>name<span class="o">: </span>Name<span class="o">?</span><span class="p">, </span>type<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Adds a value parameter with the given [`name`](index.md#valueparameter) and type produced by [`type`](index.md#valueparameter) to the [`valueParameters`](index.md#valueparameters) list.


</div>

</div>
### varargArrayType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#varargarraytype"><span class="nf">varargArrayType</span></a><span class="p">(</span>elementType<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Builds the underlying array type of a [vararg](https://kotlinlang.org/docs/functions.html#variable-number-of-arguments-varargs) function parameter with the given [`elementType`](index.md#varargarraytype).

If the type was constructed successfully, returns [`KaClassType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.md). Otherwise, returns [`KaClassErrorType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-class-error-type/index.md).


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
