---
tags:
 - jvm
title: "KaTypeProvider"
---

# KaTypeProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaTypeProvider</a> : <a href="../-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>#### Inheritors


 - [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)



</div>

## Properties
### allSupertypes

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#allsupertypes"><span class="nf">allSupertypes</span></a><span class="p">(</span>shouldApproximate<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all supertypes of the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md). The resulting sequence is ordered by a breadth-first traversal of the class hierarchy, without duplicates.

**Parameters**



 - shouldApproximate: Whether to approximate [`non-denotable`](../-ka-type-information-provider/index.md#isdenotable) types. See [`directSupertypes`](index.md#directsupertypes) for more information.





</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#allsupertypes">allSupertypes</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

All supertypes of the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md). The resulting sequence is ordered by a breadth-first traversal of the class hierarchy, without duplicates.

[`Denotable`](../-ka-type-information-provider/index.md#isdenotable) types are not approximated.


</div>

</div>
### arrayElementType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#arrayelementtype">arrayElementType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The array type's element type if the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a primitive type array or [`Array`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html), and `null` otherwise.


</div>

</div>
### augmentedByWarningLevelAnnotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#augmentedbywarninglevelannotations">augmentedByWarningLevelAnnotations</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) derived from the given type by enforcing warning-level nullability annotations. If the derived type doesn't differ from the original type, the original type is used.

In general, Java type enhancement allows the Kotlin compiler to infer a more specific nullability for a Java type based on its [nullability annotations](https://kotlinlang.org/docs/java-interop.html#nullability-annotations). Normally, only strict nullability annotations have an impact on a resolved type's nullability. These annotations are already taken into account in [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).

However, there are also warning-level nullability annotations, such as Android's `RecentlyNullable` and `RecentlyNonNull`. These annotations have weaker constraints and don't affect a resolved type's nullability. [`augmentedByWarningLevelAnnotations`](index.md#augmentedbywarninglevelannotations) is a [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) with weak annotations treated as strict ones.

See the list of default report levels for different nullability annotations in NULLABILITY_ANNOTATION_SETTINGS

**Examples**

 - For `@androidx.annotation.RecentlyNullable X!` [`augmentedByWarningLevelAnnotations`](index.md#augmentedbywarninglevelannotations) is `X?`.


 - For `@androidx.annotation.RecentlyNonNull X!` [`augmentedByWarningLevelAnnotations`](index.md#augmentedbywarninglevelannotations) is `X`.



</div>

</div>
### builtinTypes

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#builtintypes">builtinTypes</a><span class="o">: </span><a href="../-ka-builtin-types/index.html">KaBuiltinTypes</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) instances for built-in types.


</div>

</div>
### commonSupertype

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/index.html">Iterable</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span><span class="p">.</span><a href="index.html#commonsupertype">commonSupertype</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The common supertype of the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)s.

**Throws**



[`IllegalArgumentException`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html)

:   If the collection of types is empty.





</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span><span class="p">.</span><a href="index.html#commonsupertype">commonSupertype</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The common supertype of the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)s.

**Throws**



[`IllegalArgumentException`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html)

:   If the array of types is empty.





</div>

</div>
### defaultType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="p">.</span><a href="index.html#defaulttype">defaultType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The representation of [`this`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) in terms of [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).

Type parameters are substituted with matching type parameter types, e.g. `List<T>` for the `List` class.

**See also**



 - [`KaTypeCreator`](../-ka-type-creator/index.md)



</div>

</div>
### defaultTypeWithStarProjections

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="p">.</span><a href="index.html#defaulttypewithstarprojections">defaultTypeWithStarProjections</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The representation of [`this`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) in terms of [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).

Type parameters are substituted with [`KaStarTypeProjection`](../../org.jetbrains.kotlin.analysis.api.types/-ka-star-type-projection/index.md), e.g. `List<*>` for the `List` class.

**See also**



 - [`KaTypeCreator`](../-ka-type-creator/index.md)



</div>

</div>
### directSupertypes

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#directsupertypes"><span class="nf">directSupertypes</span></a><span class="p">(</span>shouldApproximate<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the direct supertypes of the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).

For flexible types, direct supertypes of both the upper and lower bounds are returned. If that's not desirable, use [`directSupertypes`](index.md#directsupertypes) on [`KaFlexibleType.upperBound`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md#upperbound) or [`KaFlexibleType.lowerBound`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md#lowerbound).

**Example**

Given `MutableList<String>`, [`directSupertypes`](index.md#directsupertypes) returns `List<String>` and `MutableCollection<String>`

**Parameters**



 - shouldApproximate: Whether to approximate [`non-denotable`](../-ka-type-information-provider/index.md#isdenotable) types. For example, the supertype of `List<out String>` is `Collection<CAPTURED out String>`. With approximation set to `true`, `Collection<out String>` is returned instead.





</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#directsupertypes">directSupertypes</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The direct supertypes of the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).

For flexible types, direct supertypes of both the upper and lower bounds are included. If that's not desirable, use [`directSupertypes`](index.md#directsupertypes) on [`KaFlexibleType.upperBound`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md#upperbound) or [`KaFlexibleType.lowerBound`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md#lowerbound).

[`Denotable`](../-ka-type-information-provider/index.md#isdenotable) types are not approximated.

**Example**

Given `MutableList<String>`, [`directSupertypes`](index.md#directsupertypes) contains `List<String>` and `MutableCollection<String>`


</div>

</div>
### receiverType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-double-colon-expression/index.html">KtDoubleColonExpression</a><span class="p">.</span><a href="index.html#receivertype">receiverType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtDoubleColonExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-double-colon-expression/index.md) to the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) of its receiver.

The result may be `null` if the resolution fails or the resolved callable reference is not a reflection type.

**Example**

```kotlin
class Foo {
    fun bar() { }
}

val foo = Foo()
foo::bar
```

Here, `receiverType` for `foo::bar` is `Foo` (the type of `foo`).


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
### type

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.html">KtTypeReference</a><span class="p">.</span><a href="index.html#type">type</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtTypeReference`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.md) to its corresponding [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).

This may raise an exception if the resolution ends up with an unexpected result.


</div>

</div>
### varargArrayType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.html">KaValueParameterSymbol</a><span class="p">.</span><a href="index.html#varargarraytype">varargArrayType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The array type that represents the list of arguments passed to this parameter if [`this`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.md) is a [vararg](https://kotlinlang.org/docs/functions.html#variable-number-of-arguments-varargs) parameter.

If [`this`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.md) is not a `vararg` parameter, [`varargArrayType`](index.md#varargarraytype) is `null`. If [`this`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.md) is an invalid (e.g., in case of multiple `vararg` parameters) or useless (in anonymous functions) `vararg` parameter, [`varargArrayType`](index.md#varargarraytype) still contains a type for it.


</div>

</div>
## Functions
### approximateToDenotableSubtype

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#approximatetodenotablesubtype"><span class="nf">approximateToDenotableSubtype</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a [`denotable`](../-ka-type-information-provider/index.md#isdenotable) subtype.

The function returns `null` if the type is already denotable and does not need approximation. Otherwise, for a type `T`, returns a denotable type `S` such that `S <: T`, with all type arguments of `S` also being denotable.


</div>

</div>
### approximateToDenotableSubtypeOrSelf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#approximatetodenotablesubtypeorself"><span class="nf">approximateToDenotableSubtypeOrSelf</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a [`denotable`](../-ka-type-information-provider/index.md#isdenotable) subtype, or returns the given type itself if it is already denotable.

**See also**



 - [`approximateToDenotableSupertype`](index.md#approximatetodenotablesupertype)



</div>

</div>
### approximateToDenotableSupertype

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#approximatetodenotablesupertype"><span class="nf">approximateToDenotableSupertype</span></a><span class="p">(</span>allowLocalDenotableTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a [`denotable`](../-ka-type-information-provider/index.md#isdenotable) supertype.

The function returns `null` if the type is already denotable and does not need approximation. Otherwise, for a type `T`, returns a denotable type `S` such that `T <: S`, with all type arguments of `S` also being denotable.

**Parameters**



 - allowLocalDenotableTypes: Whether locally declared types should be approximated to local supertypes instead of non-local ones. Local type approximation is sensible when the resulting [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is analyzed in the same local context.





</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#approximatetodenotablesupertype"><span class="nf">approximateToDenotableSupertype</span></a><span class="p">(</span>position<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a [`denotable`](../-ka-type-information-provider/index.md#isdenotable) supertype based on the given [`position`](index.md#approximatetodenotablesupertype).

This [`position`](index.md#approximatetodenotablesupertype) is used when approximating local types. If the given type is local, then the function returns the first supertype, which is visible from the given [`position`](index.md#approximatetodenotablesupertype). Note that [`position`](index.md#approximatetodenotablesupertype) is required to be within [`KaAnalysisScopeProvider.analysisScope`](../-ka-analysis-scope-provider/index.md#analysisscope), otherwise, an exception is thrown.

The function returns `null` if the type is already denotable and does not need approximation. Otherwise, for a type `T`, returns a denotable type `S` such that `T <: S`, with all type arguments of `S` also being denotable.

Example:

```kotlin
<position_1>
fun foo() {
    open class <position_2> A

    fun bar() = <expr>object: A() {}</expr>
}
```

In the example above we are trying to approximate the type of `object: A() {}` expression, which is a local type `<anonymous>: A`. When this type is approximated using `<position_2>` the function returns `A`, as this type is visible from this position. However, when approximating from `<position_1>`, the function returns `Any`, as `A` is not visible from this position, so the only option left is `Any`.


</div>

</div>
### approximateToDenotableSupertypeOrSelf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#approximatetodenotablesupertypeorself"><span class="nf">approximateToDenotableSupertypeOrSelf</span></a><span class="p">(</span>allowLocalDenotableTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a [`denotable`](../-ka-type-information-provider/index.md#isdenotable) supertype, or returns the given type itself if it is already denotable.

**See also**



 - [`approximateToDenotableSupertype`](index.md#approximatetodenotablesupertype)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#approximatetodenotablesupertypeorself"><span class="nf">approximateToDenotableSupertypeOrSelf</span></a><span class="p">(</span>position<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a [`denotable`](../-ka-type-information-provider/index.md#isdenotable) subtype based on the given [`position`](index.md#approximatetodenotablesupertypeorself), or returns the given type itself if it is already denotable.

**See also**



 - [`approximateToDenotableSupertype`](index.md#approximatetodenotablesupertype)



</div>

</div>
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### hasCommonSubtypeWith

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#hascommonsubtypewith"><span class="nf">hasCommonSubtypeWith</span></a><span class="p">(</span>that<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether this [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is compatible with [`that`](index.md#hascommonsubtypewith) other type. If they are compatible, the types can have a common subtype.


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
### lowerBoundIfFlexible

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#lowerboundifflexible"><span class="nf">lowerBoundIfFlexible</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md)'s lower bound, or the type itself if it is not flexible.


</div>

</div>
### upperBoundIfFlexible

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#upperboundifflexible"><span class="nf">upperBoundIfFlexible</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md)'s upper bound, or the type itself if it is not flexible.


</div>

</div>
### withNullability

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#withnullability"><span class="nf">withNullability</span></a><span class="p">(</span>isMarkedNullable<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a new [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) based on the given type with the updated nullability specified by [`isMarkedNullable`](index.md#withnullability).


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
