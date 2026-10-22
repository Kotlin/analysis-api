---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.types"
---

# org.jetbrains.kotlin.analysis.api.types
## Types
### [`KaBuiltinFunctionTypeFamilies`](-ka-builtin-function-type-families/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-builtin-function-type-families/index.html">KaBuiltinFunctionTypeFamilies</a>
</span></code></pre></div>
</div>


<div markdown>

Provides access to the four built-in [`function type families`](-ka-function-type-family/index.md).


</div>

</div>
### [`KaBuiltinTypes`](-ka-builtin-types/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-builtin-types/index.html">KaBuiltinTypes</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaType`](-ka-type/index.md) instances for built-in types.


</div>

</div>
### [`KaCapturedType`](-ka-captured-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-captured-type/index.html">KaCapturedType</a> : <a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaCapturedType`](-ka-captured-type/index.md) represents a [captured type](https://kotlinlang.org/spec/type-system.html#type-capturing).


</div>

</div>
### [`KaClassErrorType`](-ka-class-error-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-class-error-type/index.html">KaClassErrorType</a> : <a href="-ka-error-type/index.html">KaErrorType</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaClassErrorType`](-ka-class-error-type/index.md) represents a class type that failed to resolve correctly.


</div>

</div>
### [`KaClassType`](-ka-class-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-class-type/index.html">KaClassType</a> : <a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaClassType`](-ka-class-type/index.md) represents a generic class type or a function type.


</div>

</div>
### [`KaClassTypeQualifier`](-ka-class-type-qualifier/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-class-type-qualifier/index.html">KaClassTypeQualifier</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

A type qualifier is a segment in a multi-segment class type application.


</div>

</div>
### [`KaDefinitelyNotNullType`](-ka-definitely-not-null-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-definitely-not-null-type/index.html">KaDefinitelyNotNullType</a> : <a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaDefinitelyNotNullType`](-ka-definitely-not-null-type/index.md) represents a [definitely not-null type](https://kotlinlang.org/docs/generics.html#definitely-non-nullable-types), such as `T & Any` for a type parameter `T`.


</div>

</div>
### [`KaDynamicType`](-ka-dynamic-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-dynamic-type/index.html">KaDynamicType</a> : <a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaDynamicType`](-ka-dynamic-type/index.md) represents a [dynamic type](https://kotlinlang.org/docs/dynamic-type.html), which is used to support interoperability with dynamically typed libraries, platforms, or languages.


</div>

</div>
### [`KaErrorType`](-ka-error-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-error-type/index.html">KaErrorType</a> : <a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaErrorType`](-ka-error-type/index.md) represents a type that failed to resolve correctly.


</div>

</div>
### [`KaFlexibleType`](-ka-flexible-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-flexible-type/index.html">KaFlexibleType</a> : <a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaFlexibleType`](-ka-flexible-type/index.md) represents a [flexible type](https://kotlinlang.org/spec/type-system.html#flexible-types) (or a so-called [platform type](https://kotlinlang.org/docs/java-interop.html#null-safety-and-platform-types)), a range of types from the [`lowerBound`](-ka-flexible-type/index.md#lowerbound) to the [`upperBound`](-ka-flexible-type/index.md#upperbound) (both inclusive).


</div>

</div>
### [`KaFunctionType`](-ka-function-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-function-type/index.html">KaFunctionType</a> : <a href="-ka-class-type/index.html">KaClassType</a>, <a href="../org.jetbrains.kotlin.analysis.api.base/-ka-context-receivers-owner/index.html">KaContextReceiversOwner</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaFunctionType`](-ka-function-type/index.md) represents a Kotlin [function type](https://kotlinlang.org/docs/lambdas.html#function-types), such as `(String) -> Int` or `suspend () -> List<Any>`.


</div>

</div>
### [`KaFunctionTypeFamily`](-ka-function-type-family/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-function-type-family/index.html">KaFunctionTypeFamily</a>
</span></code></pre></div>
</div>


<div markdown>

Describes a family of numbered function types such as `Function0`, `Function1`, ..., `FunctionN`.


</div>

</div>
### [`KaFunctionValueParameter`](-ka-function-value-parameter/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-function-value-parameter/index.html">KaFunctionValueParameter</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a function value parameter


</div>

</div>
### [`KaIntersectionType`](-ka-intersection-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-intersection-type/index.html">KaIntersectionType</a> : <a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaIntersectionType`](-ka-intersection-type/index.md) represents an [intersection type](https://kotlinlang.org/spec/type-system.html#intersection-types), such as `A & B`. Intersection types cannot be denoted in Kotlin code, but can result from some compiler operations, such as [smart casts](https://kotlinlang.org/spec/type-inference.html#smart-casts).


</div>

</div>
### [`KaResolvedClassTypeQualifier`](-ka-resolved-class-type-qualifier/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-resolved-class-type-qualifier/index.html">KaResolvedClassTypeQualifier</a> : <a href="-ka-class-type-qualifier/index.html">KaClassTypeQualifier</a>
</span></code></pre></div>
</div>


<div markdown>

A successfully resolved [`KaClassTypeQualifier`](-ka-class-type-qualifier/index.md).


</div>

</div>
### [`KaStandardTypeClassIds`](-ka-standard-type-class-ids/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-ka-standard-type-class-ids/index.html">KaStandardTypeClassIds</a>
</span></code></pre></div>
</div>


<div markdown>

The object contains ClassIds of well known Kotlin types.


</div>

</div>
### [`KaStarTypeProjection`](-ka-star-type-projection/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-star-type-projection/index.html">KaStarTypeProjection</a> : <a href="-ka-type-projection/index.html">KaTypeProjection</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [star projection](https://kotlinlang.org/docs/generics.html#star-projections) (`*`) used in type arguments. It indicates that the specific type argument is not important or unknown.


</div>

</div>
### [`KaSubstitutor`](-ka-substitutor/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-substitutor/index.html">KaSubstitutor</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

A type substitutor which performs a substitution of type parameters inside a type to another type. The substitution can usually be represented as a map from type parameters to their corresponding substitution types.


</div>

</div>
### [`KaSubstitutorBuilder`](-ka-substitutor-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-substitutor-builder/index.html">KaSubstitutorBuilder</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

A DSL builder for [`KaSubstitutor`](-ka-substitutor/index.md).


</div>

</div>
### [`KaSubtypingErrorTypePolicy`](-ka-subtyping-error-type-policy/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

[`KaSubtypingErrorTypePolicy`](-ka-subtyping-error-type-policy/index.md) determines the treatment of error types in type equality and subtyping checks.


</div>

</div>
### [`KaType`](-ka-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type/index.html">KaType</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>, <a href="../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaType`](-ka-type/index.md) represents a concrete Kotlin type, such as `Int`, `Foo` for a class `Foo`, or `Bar<String>` for a class `Bar<T>`. It provides information about type structure, nullability, and annotations.


</div>

</div>
### [`KaTypeArgumentWithVariance`](-ka-type-argument-with-variance/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type-argument-with-variance/index.html">KaTypeArgumentWithVariance</a> : <a href="-ka-type-projection/index.html">KaTypeProjection</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a type argument with an explicit type and [variance](https://kotlinlang.org/docs/generics.html#use-site-variance-type-projections).


</div>

</div>
### [`KaTypeMappingMode`](-ka-type-mapping-mode/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-type-mapping-mode/index.html">KaTypeMappingMode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-type-mapping-mode/index.html">KaTypeMappingMode</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

[`KaTypeMappingMode`](-ka-type-mapping-mode/index.md) determines how a Kotlin type is mapped to a Java type when calling [`KaType.asPsiType`](../org.jetbrains.kotlin.analysis.api.components/-ka-java-interoperability-component/index.md#aspsitype).


</div>

</div>
### [`KaTypeParameterType`](-ka-type-parameter-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-type-parameter-type/index.html">KaTypeParameterType</a> : <a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaTypeParameterType`](-ka-type-parameter-type/index.md) represents a type parameter type, such as `T` in the declaration `class Box<T>(val element: T)`.


</div>

</div>
### [`KaTypePointer`](-ka-type-pointer/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type-pointer/index.html">KaTypePointer</a><span class="o"><</span><span class="kd">out </span><a href="-ka-type-pointer/index.html">T</a><span class="o"> : </span><a href="-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

[`KaTypePointer`](-ka-type-pointer/index.md) allows to point to a [`KaType`](-ka-type/index.md) and later retrieve it in another [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md). A pointer is necessary because [`KaType`](-ka-type/index.md)s cannot be shared past the boundaries of the [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) they were created in, as they are valid only there.


</div>

</div>
### [`KaTypeProjection`](-ka-type-projection/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-type-projection/index.html">KaTypeProjection</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaTypeProjection`](-ka-type-projection/index.md) represents a type argument used in the context of a class or function type. It provides information about the type and its variance.


</div>

</div>
### [`KaUnificationSubstitutorPolicy`](-ka-unification-substitutor-policy/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-unification-substitutor-policy/index.html">KaUnificationSubstitutorPolicy</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-unification-substitutor-policy/index.html">KaUnificationSubstitutorPolicy</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

[`KaUnificationSubstitutorPolicy`](-ka-unification-substitutor-policy/index.md) determines the way unification [`KaSubstitutor`](-ka-substitutor/index.md)s are created in [`createSubtypingUnificationSubstitutor`](create-subtyping-unification-substitutor.md). Note that the policy only affects the construction when at least one of the involved types is generic, i.e., depends on a type parameter.


</div>

</div>
### [`KaUnresolvedClassTypeQualifier`](-ka-unresolved-class-type-qualifier/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-unresolved-class-type-qualifier/index.html">KaUnresolvedClassTypeQualifier</a> : <a href="-ka-class-type-qualifier/index.html">KaClassTypeQualifier</a>
</span></code></pre></div>
</div>


<div markdown>

An unresolved [`KaClassTypeQualifier`](-ka-class-type-qualifier/index.md) due to a type error.


</div>

</div>
### [`KaUsualClassType`](-ka-usual-class-type/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-usual-class-type/index.html">KaUsualClassType</a> : <a href="-ka-class-type/index.html">KaClassType</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaUsualClassType`](-ka-usual-class-type/index.md) represents a generic class type, such as `String` or `List<Int>`.


</div>

</div>
## Properties
### [`builtinFunctionTypeFamilies`](builtin-function-type-families.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="builtin-function-type-families.html">builtinFunctionTypeFamilies</a><span class="o">: </span><a href="-ka-builtin-function-type-families/index.html">KaBuiltinFunctionTypeFamilies</a>
</span></code></pre></div>
</div>


<div markdown>

Provides access to the built-in [`function type families`](-ka-function-type-family/index.md).


</div>

</div>
### [`builtinTypes`](builtin-types.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="builtin-types.html">builtinTypes</a><span class="o">: </span><a href="-ka-builtin-types/index.html">KaBuiltinTypes</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaType`](-ka-type/index.md) instances for built-in types.


</div>

</div>
### [`commonSupertype`](common-supertype.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="-ka-type/index.html">KaType</a><span class="o">></span><span class="p">.</span><a href="common-supertype.html">commonSupertype</a><span class="o">: </span><a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The common supertype of the given [`KaType`](-ka-type/index.md)s.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterable/index.html">Iterable</a><span class="o"><</span><a href="-ka-type/index.html">KaType</a><span class="o">></span><span class="p">.</span><a href="common-supertype.html">commonSupertype</a><span class="o">: </span><a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The common supertype of the given [`KaType`](-ka-type/index.md)s.


</div>

</div>
### [`defaultType`](default-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="p">.</span><a href="default-type.html">defaultType</a><span class="o">: </span><a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The representation of [`this`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) in terms of [`KaType`](-ka-type/index.md).


</div>

</div>
### [`defaultTypeWithStarProjections`](default-type-with-star-projections.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="p">.</span><a href="default-type-with-star-projections.html">defaultTypeWithStarProjections</a><span class="o">: </span><a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The representation of [`this`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) in terms of [`KaType`](-ka-type/index.md).


</div>

</div>
### [`emptySubstitutor`](empty-substitutor.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="empty-substitutor.html">emptySubstitutor</a><span class="o">: </span><a href="-ka-substitutor/-empty/index.html">KaSubstitutor.Empty</a>
</span></code></pre></div>
</div>


<div markdown>

Creates [`KaSubstitutor.Empty`](-ka-substitutor/-empty/index.md), i.e., a substitutor without any mappings.


</div>

</div>
### [`receiverType`](receiver-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-double-colon-expression/index.html">KtDoubleColonExpression</a><span class="p">.</span><a href="receiver-type.html">receiverType</a><span class="o">: </span><a href="-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtDoubleColonExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-double-colon-expression/index.md) to the [`KaType`](-ka-type/index.md) of its receiver.


</div>

</div>
### [`type`](type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.html">KtTypeReference</a><span class="p">.</span><a href="type.html">type</a><span class="o">: </span><a href="-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtTypeReference`](../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.md) to its corresponding [`KaType`](-ka-type/index.md).


</div>

</div>
### [`varargArrayType`](vararg-array-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.html">KaValueParameterSymbol</a><span class="p">.</span><a href="vararg-array-type.html">varargArrayType</a><span class="o">: </span><a href="-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The array type that represents the list of arguments passed to this parameter if [`this`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.md) is a [vararg](https://kotlinlang.org/docs/functions.html#variable-number-of-arguments-varargs) parameter.


</div>

</div>
## Functions
### [`buildSubstitutor`](build-substitutor.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="build-substitutor.html"><span class="nf">buildSubstitutor</span></a><span class="p">(</span>build<span class="o">: </span><a href="-ka-substitutor-builder/index.html">KaSubstitutorBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="-ka-substitutor/index.html">KaSubstitutor</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a new [`KaSubstitutor`](-ka-substitutor/index.md) from substitutions specified inside [`build`](build-substitutor.md).


</div>

</div>
### [`createInheritanceTypeSubstitutor`](create-inheritance-type-substitutor.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="create-inheritance-type-substitutor.html"><span class="nf">createInheritanceTypeSubstitutor</span></a><span class="p">(</span>subClass<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">, </span>superClass<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="-ka-substitutor/index.html">KaSubstitutor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](-ka-substitutor/index.md) based on the inheritance relationship between [`subClass`](create-inheritance-type-substitutor.md) and [`superClass`](create-inheritance-type-substitutor.md). [`subClass`](create-inheritance-type-substitutor.md) must inherit from [`superClass`](create-inheritance-type-substitutor.md) and there may not be any error types in the inheritance path. Otherwise, `null` is returned.


</div>

</div>
### [`createSubstitutor`](create-substitutor.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="create-substitutor.html"><span class="nf">createSubstitutor</span></a><span class="p">(</span>mappings<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">, </span><a href="-ka-type/index.html">KaType</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="-ka-substitutor/index.html">KaSubstitutor</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](-ka-substitutor/index.md) based on the given [`mappings`](create-substitutor.md).


</div>

</div>
### [`createSubtypingUnificationSubstitutor`](create-subtyping-unification-substitutor.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="create-subtyping-unification-substitutor.html"><span class="nf">createSubtypingUnificationSubstitutor</span></a><span class="p">(</span>leftTypesToRightTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/index.html">Pair</a><span class="o"><</span><a href="-ka-type/index.html">KaType</a><span class="p">, </span><a href="-ka-type/index.html">KaType</a><span class="o">></span><span class="o">></span><span class="p">, </span>isFreeTypeParameter<span class="o">: </span><span class="p">(</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="-ka-substitutor/index.html">KaSubstitutor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](-ka-substitutor/index.md) which assigns type arguments such that, for each pair in [`leftTypesToRightTypes`](create-subtyping-unification-substitutor.md), the substituted left type is a subtype of the substituted right type. Returns `null` if such an assignment is not possible.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="create-subtyping-unification-substitutor.html"><span class="nf">createSubtypingUnificationSubstitutor</span></a><span class="p">(</span>leftTypesToRightTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/index.html">Pair</a><span class="o"><</span><a href="-ka-type/index.html">KaType</a><span class="p">, </span><a href="-ka-type/index.html">KaType</a><span class="o">></span><span class="o">></span><span class="p">, </span>constructionPolicy<span class="o">: </span><a href="-ka-unification-substitutor-policy/index.html">KaUnificationSubstitutorPolicy</a><span class="p">)</span><span class="o">: </span><a href="-ka-substitutor/index.html">KaSubstitutor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](-ka-substitutor/index.md) which assigns type arguments such that, for each pair in [`leftTypesToRightTypes`](create-subtyping-unification-substitutor.md), the substituted left type is a subtype of the substituted right type. Returns `null` if such an assignment is not possible.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="create-subtyping-unification-substitutor.html"><span class="nf">createSubtypingUnificationSubstitutor</span></a><span class="p">(</span>
    leftType<span class="o">: </span><a href="-ka-type/index.html">KaType</a><span class="p">, </span>
    rightType<span class="o">: </span><a href="-ka-type/index.html">KaType</a><span class="p">, </span>
    constructionPolicy<span class="o">: </span><a href="-ka-unification-substitutor-policy/index.html">KaUnificationSubstitutorPolicy</a>
<span class="p">)</span><span class="o">: </span><a href="-ka-substitutor/index.html">KaSubstitutor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](-ka-substitutor/index.md) which assigns type arguments such that the substituted [`leftType`](create-subtyping-unification-substitutor.md) is a subtype of the substituted [`rightType`](create-subtyping-unification-substitutor.md). Returns `null` if such an assignment is not possible.


</div>

</div>
