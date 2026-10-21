---
tags:
 - jvm
title: "KaFunctionTypeFamily"
---

# KaFunctionTypeFamily

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaFunctionTypeFamily</a>
</span></code></pre></div>Describes a family of numbered function types such as `Function0`, `Function1`, ..., `FunctionN`.

Kotlin has the following built-in function type families:

 - `Function` — regular function types, e.g., `(Int) -> String`


 - `SuspendFunction` — suspend function types, e.g., `suspend () -> Unit`


 - `KFunction` — reflection types for regular functions


 - `KSuspendFunction` — reflection types for suspend functions


Compiler plugins may introduce additional custom function type families.

#### See also


 - [`functionTypeFamily`](../-ka-dynamic-type/index.md#functiontypefamily)
 - [`KaBuiltinFunctionTypeFamilies`](../-ka-builtin-function-type-families/index.md)


#### Inheritors


 - [`KaFunctionTypeFamily`](../../org.jetbrains.kotlin.analysis.api.components/-ka-function-type-family/index.md)



</div>

## Properties
### isInlinable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#isinlinable">isInlinable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether function types in this family can be inlined by the compiler.

For built-in families, `Function` and `SuspendFunction` are inlinable, while `KFunction` and `KSuspendFunction` are not.


</div>

</div>
### isReflect

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#isreflect">isReflect</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether this family represents reflection function types (`KFunction`, `KSuspendFunction`).


</div>

</div>
### isSuspend

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#issuspend">isSuspend</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether this family represents suspend function types (`SuspendFunction`, `KSuspendFunction`).


</div>

</div>
### markerAnnotationClassId

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#markerannotationclassid">markerAnnotationClassId</a><span class="o">: </span>ClassId<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The ClassId of the annotation which marks a function type as belonging to this family, such as `androidx.compose.runtime.Composable`.

Families provided by a compiler plugin always have such an annotation, while built-in families have none.


</div>

</div>
### maxArity

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#maxarity">maxArity</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

The maximum number of parameters supported by function types in this family.


</div>

</div>
### nameBase

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#namebase">nameBase</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

The class name prefix shared by all types in this family.

For example, `"Function"` for the `Function` family, `"SuspendFunction"` for the `SuspendFunction` family.


</div>

</div>
### supportsConversionFromSimpleFunctionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#supportsconversionfromsimplefunctiontype">supportsConversionFromSimpleFunctionType</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether function references with a simple function type (e.g., `Function0`, `KFunction0`) can be converted to this family.


</div>

</div>
### typeRenderingPrefix

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#typerenderingprefix">typeRenderingPrefix</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The prefix which precedes a function type of this family when the type is rendered, such as `"suspend"` for the `SuspendFunction` family, or `"@Composable"` for the `ComposableFunction` family provided by the Compose compiler plugin.

`null` if types of this family are rendered without a prefix, which is the case for the `Function` family and for all reflection families.


</div>

</div>
## Functions
### classId

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#classid"><span class="nf">classId</span></a><span class="p">(</span>arity<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span>ClassId
</span></code></pre></div>
</div>


<div markdown>

Returns the ClassId of the function type interface for the given [`arity`](index.md#classid).

For example, `classId(2)` on the `Function` family returns the ClassId for `kotlin.Function2`.


</div>

</div>
