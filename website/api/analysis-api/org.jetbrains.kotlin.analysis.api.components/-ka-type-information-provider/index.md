---
tags:
 - jvm
title: "KaTypeInformationProvider"
---

# KaTypeInformationProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaTypeInformationProvider</a> : <a href="../-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>#### Inheritors


 - [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)



</div>

## Properties
### builtinFunctionTypeFamilies

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#builtinfunctiontypefamilies">builtinFunctionTypeFamilies</a><span class="o">: </span><a href="../-ka-builtin-function-type-families/index.html">KaBuiltinFunctionTypeFamilies</a>
</span></code></pre></div>
</div>


<div markdown>

Provides access to the built-in [`function type families`](../-ka-function-type-family/index.md).


</div>

</div>
### defaultInitializer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#defaultinitializer">defaultInitializer</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The default initializer for the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md), or `null` if the type is neither nullable, a primitive, nor a string.


</div>

</div>
### expandedSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#expandedsymbol">expandedSymbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The class symbol backing the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md), if available.


</div>

</div>
### fullyExpandedType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#fullyexpandedtype">fullyExpandedType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The type that corresponds to the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) with fully expanded type aliases.

Type aliases are usually expanded immediately by the compiler, so most [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)s should already present in their expanded forms. Nonetheless, it is possible to obtain unexpanded types from the Analysis API, and [`fullyExpandedType`](index.md#fullyexpandedtype) may be used to expand type aliases in such types.

**Example**

```kotlin
interface Base

typealias FirstAlias = @Anno1 Base
typealias SecondAlias = @Anno2 FirstAlias

fun foo(): @Anno3 SecondAlias = TODO()
```

The return type of `foo()` will be `@Anno3 @Anno2 @Anno1 Base` instead of `@Anno3 SecondAlias`

**See also**



 - [`KaType.abbreviation`](../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.md#abbreviation)



</div>

</div>
### functionTypeFamily

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#functiontypefamily">functionTypeFamily</a><span class="o">: </span><a href="../-ka-function-type-family/index.html">KaFunctionTypeFamily</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`function type family`](../-ka-function-type-family/index.md) of the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md), or `null` if the type is not a function type.

For example, `(Int) -> String` belongs to the [`Function`](../-ka-builtin-function-type-families/index.md#function) family, while `suspend () -> Unit` belongs to the [`SuspendFunction`](../-ka-builtin-function-type-families/index.md#suspendfunction) family.

**See also**



 - [`KaBuiltinFunctionTypeFamilies`](../-ka-builtin-function-type-families/index.md)



</div>

</div>
### hasFlexibleNullability

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#hasflexiblenullability">hasFlexibleNullability</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`org.jetbrains.kotlin.analysis.api.types.KaFlexibleType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.md) / [`org.jetbrains.kotlin.analysis.api.types.KaDynamicType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.md) with flexible nullability or [`org.jetbrains.kotlin.analysis.api.types.KaErrorType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-error-type/index.md) with unknown nullability. Both safe and ordinary calls are valid on such types.

Note that a flexible / dynamic type has a flexible nullability when the lower bound is non-nullable and the upper bound is nullable. E.g. `T!` has `T` as the lower bound and `T?` as the upper bound, hence it has a flexible nullability.


</div>

</div>
### isAnyType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isanytype">isAnyType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is an [`Any`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html) type.


</div>

</div>
### isArrayOrPrimitiveArray

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isarrayorprimitivearray">isArrayOrPrimitiveArray</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is an array or a primitive array type.


</div>

</div>
### isBooleanType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isbooleantype">isBooleanType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Boolean`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) type.


</div>

</div>
### isByteType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isbytetype">isByteType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Byte`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte/index.html) type.


</div>

</div>
### isCharSequenceType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#ischarsequencetype">isCharSequenceType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`CharSequence`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/index.html) type.


</div>

</div>
### isCharType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#ischartype">isCharType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Char`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char/index.html) type.


</div>

</div>
### isDenotable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isdenotable">isDenotable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is denotable. A [denotable type](https://kotlinlang.org/spec/type-system.html#type-kinds) can be expressed in Kotlin code, as opposed to being only constructible via compiler type operations (such as type inference).


</div>

</div>
### isDoubleType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isdoubletype">isDoubleType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Double`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html) type.


</div>

</div>
### isFloatType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isfloattype">isFloatType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Float`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html) type.


</div>

</div>
### isFunctionalInterface

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isfunctionalinterface">isFunctionalInterface</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [functional interface type](https://kotlinlang.org/docs/fun-interfaces.html), such as [`Runnable`](https://docs.oracle.com/javase/8/docs/api/java/lang/Runnable.html). Such types are also known as SAM types.


</div>

</div>
### isFunctionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isfunctiontype">isFunctionType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`kotlin.Function`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-function/index.html) type.


</div>

</div>
### isIntType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isinttype">isIntType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is an [`Int`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) type.


</div>

</div>
### isKFunctionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#iskfunctiontype">isKFunctionType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`kotlin.reflect.KFunction`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/-k-function/index.html) type.


</div>

</div>
### isKSuspendFunctionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isksuspendfunctiontype">isKSuspendFunctionType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a `KSuspendFunction` type.


</div>

</div>
### isLongType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#islongtype">isLongType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Long`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html) type.


</div>

</div>
### isMarkedNullable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#ismarkednullable">isMarkedNullable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is explicitly marked as nullable, i.e., is represented as `T?`.

Note that this property just reflects the presence of nullability in the type signature, and sometimes [`isMarkedNullable`](index.md#ismarkednullable) being false doesn't imply that the given type cannot hold `null` or be assigned with it.

For example, [`isMarkedNullable`](index.md#ismarkednullable) doesn't expand type aliases to check the nullability of their underlying type:

```kotlin
typealias NonMarkedNullableAlias = String?

fun main() {
    val x: NonMarkedNullableAlias = null
}
```

The type of `x` is `NonMarkedNullableAlias`, which is not marked as nullable. However, it still represents a nullable type and can hold `null` and can be assigned with that.

To explicitly check whether a type can potentially hold `null`, use [`isNullable`](index.md#isnullable).


</div>

</div>
### isNestedArray

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isnestedarray">isNestedArray</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is an array or a primitive array type, and its element is also an array type.


</div>

</div>
### isNothingType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isnothingtype">isNothingType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Nothing`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-nothing/index.html) type.


</div>

</div>
### isNullable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isnullable">isNullable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether a public value of the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) can potentially be `null`.

If a type can be `null`, it means that this type is not a subtype of [`Any`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html). However, it does not mean one can assign `null` to a variable of this type. It may be unknown whether this type can accept `null`.

**Example**

A public value of type `T : Any?` can potentially be `null`. But one cannot assign `null` to such a variable because the instantiated type may not be nullable.


</div>

</div>
### isPrimitive

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isprimitive">isPrimitive</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a primitive type.


</div>

</div>
### isShortType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isshorttype">isShortType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Short`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/index.html) type.


</div>

</div>
### isStringType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isstringtype">isStringType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`String`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) type.


</div>

</div>
### isSuspendFunctionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#issuspendfunctiontype">isSuspendFunctionType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [suspend function](https://kotlinlang.org/spec/asynchronous-programming-with-coroutines.html#suspending-functions) type.


</div>

</div>
### isUByteType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isubytetype">isUByteType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`UByte`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-byte/index.html) type.


</div>

</div>
### isUIntType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isuinttype">isUIntType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`UInt`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-int/index.html) type.


</div>

</div>
### isULongType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isulongtype">isULongType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`ULong`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-long/index.html) type.


</div>

</div>
### isUnitType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isunittype">isUnitType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`Unit`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html) type.


</div>

</div>
### isUShortType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isushorttype">isUShortType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a [`UShort`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-short/index.html) type.


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
## Functions
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
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
