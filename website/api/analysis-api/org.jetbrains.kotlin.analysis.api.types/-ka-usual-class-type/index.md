---
tags:
 - jvm
title: "KaUsualClassType"
---

# KaUsualClassType

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KaUsualClassType</a> : <a href="../-ka-class-type/index.html">KaClassType</a>
</span></code></pre></div>[`KaUsualClassType`](index.md) represents a generic class type, such as `String` or `List<Int>`.


</div>

## Constructors
### KaUsualClassType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### abbreviation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-dynamic-type/index.html#abbreviation">abbreviation</a><span class="o">: </span><a href="index.html">KaUsualClassType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The abbreviated type for this expanded [`KaType`](../-ka-type/index.md), or `null` if this type has not been expanded from an abbreviated type or the abbreviated type cannot be resolved.

An abbreviated type is a type alias application that has been expanded to some other Kotlin type. For example, if we have a type alias `typealias MyString = String` and its application `MyString`, `String` would be the type alias expansion and `MyString` its abbreviated type.

The abbreviated type contains the type arguments of a specific type alias application. For example, if we have a `typealias MyList<A> = List<A>`, for an application `MyList<String>`, `MyList<String>` would be the abbreviated type for such a type alias application, not simply `MyList`.

If this [`KaType`](../-ka-type/index.md) is an unexpanded type alias application, [`abbreviation`](../-ka-dynamic-type/index.md#abbreviation) is `null`. Not all type alias applications are currently expanded right away and the Analysis API makes no guarantees about the specific circumstances.

While [`abbreviation`](../-ka-dynamic-type/index.md#abbreviation) is available for all [`KaType`](../-ka-type/index.md)s, it can currently only be present in [`KaClassType`](../-ka-class-type/index.md)s. However, abbreviated types are a general concept and if the type system changes (e.g. with denotable union/intersection types), other kinds of types may also be expanded from a type alias. This would allow more kinds of types to carry an abbreviated type.

The [`abbreviation`](../-ka-dynamic-type/index.md#abbreviation) itself is always a [`KaUsualClassType`](index.md), as the application of a type alias is always a class type. It cannot be a [`KaClassErrorType`](../-ka-class-error-type/index.md) because [`abbreviation`](../-ka-dynamic-type/index.md#abbreviation) would then be `null`.

**Resolvability**

Even when this [`KaType`](../-ka-type/index.md) is an expansion, the abbreviated type may be `null` if it is not resolvable from this type's use-site module. This can occur when the abbreviated type from a module `M1` was expanded at some declaration `D` in module `M2`, and the use-site module uses `D`, but only has a dependency on `M2`. Then the type alias of `M1` remains unresolved and [`abbreviation`](../-ka-dynamic-type/index.md#abbreviation) is `null`.

**Type arguments and nested abbreviated types**

The type arguments of an abbreviated type are not converted to abbreviated types automatically. That is, if a type argument is a type expansion, its [`abbreviation`](../-ka-dynamic-type/index.md#abbreviation) doesn't automatically replace the expanded type. For example:

```
typealias MyString = String
typealias MyList<A> = List<A>

val list: MyList<MyString> = listOf()
```

`MyList<MyString>` may be expanded to a type `List<String>` with an abbreviated type `MyList<String>`, where `String` also has the abbreviated type `MyString`. The abbreviated type is not `MyList<MyString>`, although it might be rendered as such.

**Transitive expansion**

Types are always expanded to their final form. That is, if we have a chain of type alias expansions, the [`KaType`](../-ka-type/index.md) only represents the final expanded type, and its [`abbreviation`](../-ka-dynamic-type/index.md#abbreviation) the initial type alias application. For example:

```
typealias Inner = String
typealias Outer = Inner

val outer: Outer = ""
```

Here, `outer`'s type would be expanded to `String`, but its abbreviated type would be `Outer`. `Inner` would be lost.


</div>

</div>
### abbreviationOrSelf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#abbreviationorself">abbreviationOrSelf</a><span class="o">: </span><a href="../-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaType`](../-ka-type/index.md)'s [`abbreviated type`](../-ka-dynamic-type/index.md#abbreviation), or the type itself if it doesn't have an abbreviated type.

A common pattern is to prefer the abbreviated type if it exists, and otherwise take the original type, for example to find the best target for navigation.


</div>

</div>
### allSupertypes

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#allsupertypes"><span class="nf">allSupertypes</span></a><span class="p">(</span>shouldApproximate<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all supertypes of the given [`KaType`](../-ka-type/index.md). The resulting sequence is ordered by a breadth-first traversal of the class hierarchy, without duplicates.

**Parameters**



 - shouldApproximate: Whether to approximate [`non-denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) types. See [`directSupertypes`](../-ka-dynamic-type/index.md#directsupertypes) for more information.





</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#allsupertypes">allSupertypes</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

All supertypes of the given [`KaType`](../-ka-type/index.md). The resulting sequence is ordered by a breadth-first traversal of the class hierarchy, without duplicates.

[`Denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) types are not approximated.


</div>

</div>
### [`annotations`](../-ka-dynamic-type/index.md#annotations)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-dynamic-type/index.html#annotations">annotations</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-list/index.html">KaAnnotationList</a>
</span></code></pre></div>
</div>


<div markdown>

A list of annotations applied to the annotated entity.


</div>

</div>
### arrayElementType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#arrayelementtype">arrayElementType</a><span class="o">: </span><a href="../-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The array type's element type if the given [`KaType`](../-ka-type/index.md) is a primitive type array or [`Array`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html), and `null` otherwise.


</div>

</div>
### augmentedByWarningLevelAnnotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#augmentedbywarninglevelannotations">augmentedByWarningLevelAnnotations</a><span class="o">: </span><a href="../-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaType`](../-ka-type/index.md) derived from the given type by enforcing warning-level nullability annotations. If the derived type doesn't differ from the original type, the original type is used.

In general, Java type enhancement allows the Kotlin compiler to infer a more specific nullability for a Java type based on its [nullability annotations](https://kotlinlang.org/docs/java-interop.html#nullability-annotations). Normally, only strict nullability annotations have an impact on a resolved type's nullability. These annotations are already taken into account in [`KaType`](../-ka-type/index.md).

However, there are also warning-level nullability annotations, such as Android's `RecentlyNullable` and `RecentlyNonNull`. These annotations have weaker constraints and don't affect a resolved type's nullability. [`augmentedByWarningLevelAnnotations`](../-ka-dynamic-type/index.md#augmentedbywarninglevelannotations) is a [`KaType`](../-ka-type/index.md) with weak annotations treated as strict ones.

See the list of default report levels for different nullability annotations in NULLABILITY_ANNOTATION_SETTINGS

**Examples**

 - For `@androidx.annotation.RecentlyNullable X!` [`augmentedByWarningLevelAnnotations`](../-ka-dynamic-type/index.md#augmentedbywarninglevelannotations) is `X?`.


 - For `@androidx.annotation.RecentlyNonNull X!` [`augmentedByWarningLevelAnnotations`](../-ka-dynamic-type/index.md#augmentedbywarninglevelannotations) is `X`.



</div>

</div>
### classId

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#classid">classId</a><span class="o">: </span>ClassId
</span></code></pre></div>
</div>


<div markdown>

The ClassId of the class.


</div>

</div>
### classId

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#classid">classId</a><span class="o">: </span>ClassId<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The ClassId provided the type exposes any (it is the case for [`KaClassType`](../-ka-class-type/index.md)).


</div>

</div>
### defaultInitializer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#defaultinitializer">defaultInitializer</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The default initializer for the given [`KaType`](../-ka-type/index.md), or `null` if the type is neither nullable, a primitive, nor a string.


</div>

</div>
### directSupertypes

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#directsupertypes"><span class="nf">directSupertypes</span></a><span class="p">(</span>shouldApproximate<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the direct supertypes of the given [`KaType`](../-ka-type/index.md).

For flexible types, direct supertypes of both the upper and lower bounds are returned. If that's not desirable, use [`directSupertypes`](../-ka-dynamic-type/index.md#directsupertypes) on [`KaFlexibleType.upperBound`](../-ka-flexible-type/index.md#upperbound) or [`KaFlexibleType.lowerBound`](../-ka-flexible-type/index.md#lowerbound).

**Example**

Given `MutableList<String>`, [`directSupertypes`](../-ka-dynamic-type/index.md#directsupertypes) returns `List<String>` and `MutableCollection<String>`

**Parameters**



 - shouldApproximate: Whether to approximate [`non-denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) types. For example, the supertype of `List<out String>` is `Collection<CAPTURED out String>`. With approximation set to `true`, `Collection<out String>` is returned instead.





</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#directsupertypes">directSupertypes</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The direct supertypes of the given [`KaType`](../-ka-type/index.md).

For flexible types, direct supertypes of both the upper and lower bounds are included. If that's not desirable, use [`directSupertypes`](../-ka-dynamic-type/index.md#directsupertypes) on [`KaFlexibleType.upperBound`](../-ka-flexible-type/index.md#upperbound) or [`KaFlexibleType.lowerBound`](../-ka-flexible-type/index.md#lowerbound).

[`Denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) types are not approximated.

**Example**

Given `MutableList<String>`, [`directSupertypes`](../-ka-dynamic-type/index.md#directsupertypes) contains `List<String>` and `MutableCollection<String>`


</div>

</div>
### expandedSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#expandedsymbol">expandedSymbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The class symbol backing the given [`KaType`](../-ka-type/index.md), if available.


</div>

</div>
### fullyExpandedType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#fullyexpandedtype">fullyExpandedType</a><span class="o">: </span><a href="../-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The type that corresponds to the given [`KaType`](../-ka-type/index.md) with fully expanded type aliases.

Type aliases are usually expanded immediately by the compiler, so most [`KaType`](../-ka-type/index.md)s should already present in their expanded forms. Nonetheless, it is possible to obtain unexpanded types from the Analysis API, and [`fullyExpandedType`](../-ka-dynamic-type/index.md#fullyexpandedtype) may be used to expand type aliases in such types.

**Example**

```kotlin
interface Base

typealias FirstAlias = @Anno1 Base
typealias SecondAlias = @Anno2 FirstAlias

fun foo(): @Anno3 SecondAlias = TODO()
```

The return type of `foo()` will be `@Anno3 @Anno2 @Anno1 Base` instead of `@Anno3 SecondAlias`

**See also**



 - [`KaType.abbreviation`](../-ka-dynamic-type/index.md#abbreviation)



</div>

</div>
### functionTypeFamily

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#functiontypefamily">functionTypeFamily</a><span class="o">: </span><a href="../-ka-function-type-family/index.html">KaFunctionTypeFamily</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`function type family`](../-ka-function-type-family/index.md) of the given [`KaType`](../-ka-type/index.md), or `null` if the type is not a function type.

For example, `(Int) -> String` belongs to the [`Function`](../-ka-builtin-function-type-families/index.md#function) family, while `suspend () -> Unit` belongs to the [`SuspendFunction`](../-ka-builtin-function-type-families/index.md#suspendfunction) family.

**See also**



 - [`KaBuiltinFunctionTypeFamilies`](../-ka-builtin-function-type-families/index.md)



</div>

</div>
### hasFlexibleNullability

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#hasflexiblenullability">hasFlexibleNullability</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../-ka-type/index.md) is a [`org.jetbrains.kotlin.analysis.api.types.KaFlexibleType`](../-ka-flexible-type/index.md) / [`org.jetbrains.kotlin.analysis.api.types.KaDynamicType`](../-ka-dynamic-type/index.md) with flexible nullability or [`org.jetbrains.kotlin.analysis.api.types.KaErrorType`](../-ka-error-type/index.md) with unknown nullability. Both safe and ordinary calls are valid on such types.

Note that a flexible / dynamic type has a flexible nullability when the lower bound is non-nullable and the upper bound is nullable. E.g. `T!` has `T` as the lower bound and `T?` as the upper bound, hence it has a flexible nullability.


</div>

</div>
### isArrayOrPrimitiveArray

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#isarrayorprimitivearray">isArrayOrPrimitiveArray</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../-ka-type/index.md) is an array or a primitive array type.


</div>

</div>
### isDenotable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#isdenotable">isDenotable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../-ka-type/index.md) is denotable. A [denotable type](https://kotlinlang.org/spec/type-system.html#type-kinds) can be expressed in Kotlin code, as opposed to being only constructible via compiler type operations (such as type inference).


</div>

</div>
### isFunctionalInterface

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#isfunctionalinterface">isFunctionalInterface</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../-ka-type/index.md) is a [functional interface type](https://kotlinlang.org/docs/fun-interfaces.html), such as [`Runnable`](https://docs.oracle.com/javase/8/docs/api/java/lang/Runnable.html). Such types are also known as SAM types.


</div>

</div>
### isFunctionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#isfunctiontype">isFunctionType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../-ka-type/index.md) is a [`kotlin.Function`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-function/index.html) type.


</div>

</div>
### isKFunctionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#iskfunctiontype">isKFunctionType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../-ka-type/index.md) is a [`kotlin.reflect.KFunction`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/-k-function/index.html) type.


</div>

</div>
### isKSuspendFunctionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#isksuspendfunctiontype">isKSuspendFunctionType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../-ka-type/index.md) is a `KSuspendFunction` type.


</div>

</div>
### isMarkedNullable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#ismarkednullable">isMarkedNullable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../-ka-type/index.md) is explicitly marked as nullable, i.e., is represented as `T?`.

Note that this property just reflects the presence of nullability in the type signature, and sometimes [`isMarkedNullable`](../-ka-dynamic-type/index.md#ismarkednullable) being false doesn't imply that the given type cannot hold `null` or be assigned with it.

For example, [`isMarkedNullable`](../-ka-dynamic-type/index.md#ismarkednullable) doesn't expand type aliases to check the nullability of their underlying type:

```kotlin
typealias NonMarkedNullableAlias = String?

fun main() {
    val x: NonMarkedNullableAlias = null
}
```

The type of `x` is `NonMarkedNullableAlias`, which is not marked as nullable. However, it still represents a nullable type and can hold `null` and can be assigned with that.

To explicitly check whether a type can potentially hold `null`, use [`isNullable`](../-ka-dynamic-type/index.md#isnullable).


</div>

</div>
### isNestedArray

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#isnestedarray">isNestedArray</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../-ka-type/index.md) is an array or a primitive array type, and its element is also an array type.


</div>

</div>
### isNullable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#isnullable">isNullable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether a public value of the [`KaType`](../-ka-type/index.md) can potentially be `null`.

If a type can be `null`, it means that this type is not a subtype of [`Any`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html). However, it does not mean one can assign `null` to a variable of this type. It may be unknown whether this type can accept `null`.

**Example**

A public value of type `T : Any?` can potentially be `null`. But one cannot assign `null` to such a variable because the instantiated type may not be nullable.


</div>

</div>
### [`isPrimitiveBacked`](../../org.jetbrains.kotlin.analysis.api.javaInterop/is-primitive-backed.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.javaInterop/is-primitive-backed.html">isPrimitiveBacked</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the given [`KaType`](../-ka-type/index.md) is backed by a single JVM primitive type.


</div>

</div>
### isSuspendFunctionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#issuspendfunctiontype">isSuspendFunctionType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../-ka-type/index.md) is a [suspend function](https://kotlinlang.org/spec/asynchronous-programming-with-coroutines.html#suspending-functions) type.


</div>

</div>
### qualifiers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#qualifiers">qualifiers</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-resolved-class-type-qualifier/index.html">KaResolvedClassTypeQualifier</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The list of [`KaResolvedClassTypeQualifier`](../-ka-resolved-class-type-qualifier/index.md)s describing the segments of the class type.

**See also**



 - [`KaClassTypeQualifier`](../-ka-class-type-qualifier/index.md)



</div>

</div>
### [`scope`](../../org.jetbrains.kotlin.analysis.api.scopes/scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/scope.html">scope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.html">KaTypeScope</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.md) for the given [`KaType`](../-ka-type/index.md), or `null` if the type is [`erroneous`](../-ka-error-type/index.md). The scope includes all members which are callable on a given type. It also includes [synthetic Java properties](https://kotlinlang.org/docs/java-interop.html#getters-and-setters).


</div>

</div>
### symbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

The class symbol which this class type is an instance of.


</div>

</div>
### symbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#symbol">symbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaClassLikeSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.md) for this [`KaType`](../-ka-type/index.md) if the type represents a uniquely resolvable class/object/type alias.


</div>

</div>
### [`syntheticJavaPropertiesScope`](../../org.jetbrains.kotlin.analysis.api.scopes/synthetic-java-properties-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/synthetic-java-properties-scope.html">syntheticJavaPropertiesScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.html">KaTypeScope</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.md) containing the [synthetic Java properties](https://kotlinlang.org/docs/java-interop.html#getters-and-setters) created for a given [`KaType`](../-ka-type/index.md).


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
### typeArguments

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#typearguments">typeArguments</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-type-projection/index.html">KaTypeProjection</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The type arguments of the class type.

Type arguments should not be confused with the [`symbol`](index.md#symbol)'s type parameters (for some subtypes of [`KaClassLikeSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.md)).


</div>

</div>
## Functions
### approximateToDenotableSubtype

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#approximatetodenotablesubtype"><span class="nf">approximateToDenotableSubtype</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../-ka-type/index.md) to a [`denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) subtype.

The function returns `null` if the type is already denotable and does not need approximation. Otherwise, for a type `T`, returns a denotable type `S` such that `S <: T`, with all type arguments of `S` also being denotable.


</div>

</div>
### approximateToDenotableSubtypeOrSelf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#approximatetodenotablesubtypeorself"><span class="nf">approximateToDenotableSubtypeOrSelf</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../-ka-type/index.md) to a [`denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) subtype, or returns the given type itself if it is already denotable.

**See also**



 - [`approximateToDenotableSupertype`](../-ka-dynamic-type/index.md#approximatetodenotablesupertype)



</div>

</div>
### approximateToDenotableSupertype

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#approximatetodenotablesupertype"><span class="nf">approximateToDenotableSupertype</span></a><span class="p">(</span>allowLocalDenotableTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../-ka-type/index.md) to a [`denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) supertype.

The function returns `null` if the type is already denotable and does not need approximation. Otherwise, for a type `T`, returns a denotable type `S` such that `T <: S`, with all type arguments of `S` also being denotable.

**Parameters**



 - allowLocalDenotableTypes: Whether locally declared types should be approximated to local supertypes instead of non-local ones. Local type approximation is sensible when the resulting [`KaType`](../-ka-type/index.md) is analyzed in the same local context.





</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#approximatetodenotablesupertype"><span class="nf">approximateToDenotableSupertype</span></a><span class="p">(</span>position<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="../-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../-ka-type/index.md) to a [`denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) supertype based on the given [`position`](../-ka-dynamic-type/index.md#approximatetodenotablesupertype).

This [`position`](../-ka-dynamic-type/index.md#approximatetodenotablesupertype) is used when approximating local types. If the given type is local, then the function returns the first supertype, which is visible from the given [`position`](../-ka-dynamic-type/index.md#approximatetodenotablesupertype). Note that [`position`](../-ka-dynamic-type/index.md#approximatetodenotablesupertype) is required to be within [`KaAnalysisScopeProvider.analysisScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-analysis-scope-provider/index.md#analysisscope), otherwise, an exception is thrown.

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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#approximatetodenotablesupertypeorself"><span class="nf">approximateToDenotableSupertypeOrSelf</span></a><span class="p">(</span>allowLocalDenotableTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../-ka-type/index.md) to a [`denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) supertype, or returns the given type itself if it is already denotable.

**See also**



 - [`approximateToDenotableSupertype`](../-ka-dynamic-type/index.md#approximatetodenotablesupertype)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#approximatetodenotablesupertypeorself"><span class="nf">approximateToDenotableSupertypeOrSelf</span></a><span class="p">(</span>position<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="../-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Approximates [`KaType`](../-ka-type/index.md) to a [`denotable`](../../org.jetbrains.kotlin.analysis.api.components/-ka-type-information-provider/index.md#isdenotable) subtype based on the given [`position`](../-ka-dynamic-type/index.md#approximatetodenotablesupertypeorself), or returns the given type itself if it is already denotable.

**See also**



 - [`approximateToDenotableSupertype`](../-ka-dynamic-type/index.md#approximatetodenotablesupertype)



</div>

</div>
### [`asPsiType`](../../org.jetbrains.kotlin.analysis.api.components/as-psi-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.components/as-psi-type.html"><span class="nf">asPsiType</span></a><span class="p">(</span>
    useSitePosition<span class="o">: </span>PsiElement<span class="p">, </span>
    allowErrorTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    mode<span class="o">: </span><a href="../-ka-type-mapping-mode/index.html">KaTypeMappingMode</a><span class="o"> = </span>KaTypeMappingMode.DEFAULT<span class="p">, </span>
    isAnnotationMethod<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span>
    suppressWildcards<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">?</span><span class="o"> = </span>null<span class="p">, </span>
    preserveAnnotations<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">, </span>
    allowNonJvmPlatforms<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span>
<span class="p">)</span><span class="o">: </span>PsiType<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaType`](../-ka-type/index.md) to a PsiType in the context of the [`useSitePosition`](../../org.jetbrains.kotlin.analysis.api.components/as-psi-type.md).


</div>

</div>
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`copy`](../../org.jetbrains.kotlin.analysis.api.types.typeCreation/copy.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="index.html">KaUsualClassType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/copy.html"><span class="nf">copy</span></a><span class="p">(</span>init<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types.typeCreation/-ka-class-type-builder/index.html">KaClassTypeBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaUsualClassType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a copy of this [`KaUsualClassType`](index.md) with modifications applied via the [`init`](../../org.jetbrains.kotlin.analysis.api.types.typeCreation/copy.md) block.


</div>

</div>
### createPointer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#createpointer"><span class="nf">createPointer</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-type-pointer/index.html">KaTypePointer</a><span class="o"><</span><a href="index.html">KaUsualClassType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Creates a type pointer.

Unlike [`KaType`](../-ka-type/index.md), a [`KaTypePointer`](../-ka-type-pointer/index.md) may be safely stored and passed around outside the (analyze)[`org.jetbrains.kotlin.analysis.api.session.analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) block. Use the [`KaSession.restore`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md#restore) function to get the type instance back. Note that depending on the use-site session (analysisScope)[`KaSession.analysisScope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-analysis-scope-provider/index.md#analysisscope), a type might not be restored.


</div>

</div>
### hasCommonSubtypeWith

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#hascommonsubtypewith"><span class="nf">hasCommonSubtypeWith</span></a><span class="p">(</span>that<span class="o">: </span><a href="../-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether this [`KaType`](../-ka-type/index.md) is compatible with [`that`](../-ka-dynamic-type/index.md#hascommonsubtypewith) other type. If they are compatible, the types can have a common subtype.


</div>

</div>
### isSubtypeOf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>supertype<span class="o">: </span><a href="../-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../-ka-type/index.md) is a subtype of [`supertype`](../-ka-dynamic-type/index.md#issubtypeof). The relation is non-strict, i.e. any type `t` is a subtype of itself.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>supertype<span class="o">: </span><a href="../-ka-type/index.html">KaType</a><span class="p">, </span>errorTypePolicy<span class="o">: </span><a href="../-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../-ka-type/index.md) is a subtype of [`supertype`](../-ka-dynamic-type/index.md#issubtypeof). The relation is non-strict, i.e. any type `t` is a subtype of itself.

The [`errorTypePolicy`](../-ka-dynamic-type/index.md#issubtypeof) determines the treatment of error types in the subtyping check.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../-ka-type/index.md) is a subtype of a class called [`classId`](../-ka-dynamic-type/index.md#issubtypeof).

This function provides a convenient way to check if a class extends a certain base class or interface while disregarding type arguments. For example, one may check if this [`KaType`](../-ka-type/index.md) is a subtype of StandardClassIds.Iterable.

See the overload taking a [`KaSubtypingErrorTypePolicy`](../-ka-subtyping-error-type-policy/index.md) for the treatment of error types.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">, </span>errorTypePolicy<span class="o">: </span><a href="../-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../-ka-type/index.md) is a subtype of a class called [`classId`](../-ka-dynamic-type/index.md#issubtypeof).

This function provides a convenient way to check if a class extends a certain base class or interface while disregarding type arguments. For example, one may check if this [`KaType`](../-ka-type/index.md) is a subtype of StandardClassIds.Iterable.

The [`errorTypePolicy`](../-ka-dynamic-type/index.md#issubtypeof) is applied as such: If this [`KaType`](../-ka-type/index.md) is an error type, the [`LENIENT`](../-ka-subtyping-error-type-policy/-l-e-n-i-e-n-t/index.md) policy leads to a trivially `true` result. Errors in type arguments are not considered, as the subclass check is concerned with the applied class type and not its type arguments.

This function for ClassIds is a convenient dual to other [`isSubtypeOf`](../-ka-dynamic-type/index.md#issubtypeof) functions. As such, its result is the same as a call to [`isSubtypeOf`](../-ka-dynamic-type/index.md#issubtypeof) with the following right-hand [`KaType`](../-ka-type/index.md): `a.b.Class<*, *, ...>?` given a class ID `a.b.Class` with all type arguments instantiated to a star projection.

This has the following interesting implications:

 - If the [`classId`](../-ka-dynamic-type/index.md#issubtypeof) points to or actualizes to a type alias, subclassing is checked for the expanded type, as other [`isSubtypeOf`](../-ka-dynamic-type/index.md#issubtypeof) implementations also take expansion into account. If the type alias doesn't expand to a [`KaClassType`](../-ka-class-type/index.md), [`isSubtypeOf`](../-ka-dynamic-type/index.md#issubtypeof) is trivially `false`.


 - If the [`classId`](../-ka-dynamic-type/index.md#issubtypeof) cannot be resolved, it effectively means that we would have an "unresolved symbol" error [`KaType`](../-ka-type/index.md) on the right-hand side of [`isSubtypeOf`](../-ka-dynamic-type/index.md#issubtypeof). Hence, with a [`LENIENT`](../-ka-subtyping-error-type-policy/-l-e-n-i-e-n-t/index.md) error type policy, [`isSubtypeOf`](../-ka-dynamic-type/index.md#issubtypeof) is `true` for all unresolved class IDs.



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../-ka-type/index.md) is a subtype of a class represented by [`symbol`](../-ka-dynamic-type/index.md#issubtypeof).

This function provides a convenient way to check if a class extends a certain base class or interface while disregarding type arguments.

See the overload taking a [`KaSubtypingErrorTypePolicy`](../-ka-subtyping-error-type-policy/index.md) for the treatment of error types.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">, </span>errorTypePolicy<span class="o">: </span><a href="../-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../-ka-type/index.md) is a subtype of a class represented by [`symbol`](../-ka-dynamic-type/index.md#issubtypeof).

This function provides a convenient way to check if a class extends a certain base class or interface while disregarding type arguments.

The [`errorTypePolicy`](../-ka-dynamic-type/index.md#issubtypeof) is applied as such: If this [`KaType`](../-ka-type/index.md) is an error type, the [`LENIENT`](../-ka-subtyping-error-type-policy/-l-e-n-i-e-n-t/index.md) policy leads to a trivially `true` result. Errors in type arguments are not considered, as the subclass check is concerned with the applied class type and not its type arguments.

This function for [`KaClassLikeSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.md)s is a convenient dual to other [`isSubtypeOf`](../-ka-dynamic-type/index.md#issubtypeof) functions. As such, its result is the same as a call to [`isSubtypeOf`](../-ka-dynamic-type/index.md#issubtypeof) with the following right-hand [`KaType`](../-ka-type/index.md): `a.b.Class<*, *, ...>?` given a class called `a.b.Class` with all type arguments instantiated to a star projection.

This has the following interesting implication: If the [`symbol`](../-ka-dynamic-type/index.md#issubtypeof) points to or actualizes to a type alias, subclassing is checked for the expanded type, as other [`isSubtypeOf`](../-ka-dynamic-type/index.md#issubtypeof) implementations also take expansion into account. If the type alias doesn't expand to a [`KaClassType`](../-ka-class-type/index.md), [`isSubtypeOf`](../-ka-dynamic-type/index.md#issubtypeof) is trivially `false`.


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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#lowerboundifflexible"><span class="nf">lowerBoundIfFlexible</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KaFlexibleType`](../-ka-flexible-type/index.md)'s lower bound, or the type itself if it is not flexible.


</div>

</div>
### [`mapToJvmTypeDescriptor`](../../org.jetbrains.kotlin.analysis.api.javaInterop/map-to-jvm-type-descriptor.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.javaInterop/map-to-jvm-type-descriptor.html"><span class="nf">mapToJvmTypeDescriptor</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Convert the given [`KaType`](../-ka-type/index.md) to a JVM type descriptor with the [`KaTypeMappingMode.DEFAULT`](../-ka-type-mapping-mode/-d-e-f-a-u-l-t/index.md). To learn more about JVM descriptors, check out the [JVM specification](https://docs.oracle.com/javase/specs/jvms/se24/html/jvms-4.html#jvms-4.3).


</div>

</div>
### [`render`](../../org.jetbrains.kotlin.analysis.api.renderer/render.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.renderer/render.html"><span class="nf">render</span></a><span class="p">(</span>position<span class="o">: </span>Variance<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Renders the given [`KaType`](../-ka-type/index.md) into a string using the default rendering strategy ([`KaTypeRendererForSource.WITH_QUALIFIED_NAMES`](../../org.jetbrains.kotlin.analysis.api.renderer.types.impl/-ka-type-renderer-for-source/index.md#with_qualified_names)).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.renderer/render.html"><span class="nf">render</span></a><span class="p">(</span>renderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.types/-ka-type-renderer/index.html">KaTypeRenderer</a><span class="p">, </span>position<span class="o">: </span>Variance<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Renders the given [`KaType`](../-ka-type/index.md) into a string. The particular rendering strategy is defined by the [`renderer`](../../org.jetbrains.kotlin.analysis.api.renderer/render.md).


</div>

</div>
### semanticallyEquals

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#semanticallyequals"><span class="nf">semanticallyEquals</span></a><span class="p">(</span>other<span class="o">: </span><a href="../-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../-ka-type/index.md) is semantically equal to [`other`](../-ka-dynamic-type/index.md#semanticallyequals).

Semantic equality stands in contrast to the structural equality implemented by [`KaType.equals`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/equals.html). See [`KaType`](../-ka-type/index.md) for a detailed discussion about structural vs. semantic type equality.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#semanticallyequals"><span class="nf">semanticallyEquals</span></a><span class="p">(</span>other<span class="o">: </span><a href="../-ka-type/index.html">KaType</a><span class="p">, </span>errorTypePolicy<span class="o">: </span><a href="../-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../-ka-type/index.md) is semantically equal to [`other`](../-ka-dynamic-type/index.md#semanticallyequals).

Semantic equality stands in contrast to the structural equality implemented by [`KaType.equals`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/equals.html). See [`KaType`](../-ka-type/index.md) for a detailed discussion about structural vs. semantic type equality.

The [`errorTypePolicy`](../-ka-dynamic-type/index.md#semanticallyequals) determines the treatment of error types in the equality check.


</div>

</div>
### upperBoundIfFlexible

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#upperboundifflexible"><span class="nf">upperBoundIfFlexible</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KaFlexibleType`](../-ka-flexible-type/index.md)'s upper bound, or the type itself if it is not flexible.


</div>

</div>
### withNullability

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-type/index.html">KaType</a><span class="p">.</span><a href="../-ka-dynamic-type/index.html#withnullability"><span class="nf">withNullability</span></a><span class="p">(</span>isMarkedNullable<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a new [`KaType`](../-ka-type/index.md) based on the given type with the updated nullability specified by [`isMarkedNullable`](../-ka-dynamic-type/index.md#withnullability).


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
