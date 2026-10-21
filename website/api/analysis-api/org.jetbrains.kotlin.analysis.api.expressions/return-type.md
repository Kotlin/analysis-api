---
tags:
 - jvm
title: "returnType"
---

# returnType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration-with-return-type/index.html">KtDeclarationWithReturnType</a><span class="p">.</span><a href="return-type.html">returnType</a><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The return type of the given [`KtDeclarationWithReturnType`](../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration-with-return-type/index.md), either declared explicitly or inferred.

Depending on the declaration kind, the return type is:

 - The return type for a function, including anonymous functions and function literals (lambdas). A function with a block body and without a declared return type returns [`Unit`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html).


 - The constructed class type for a constructor, e.g., `Foo<T>` for a constructor of `class Foo<T>`.


 - The property type for a property and its getter, and [`Unit`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html) for its setter.


 - The field type for an explicit backing field, which may differ from the property type.


 - The parameter type for a value, context, lambda, `for` loop, `catch`, or function type parameter.


 - The type of the destructured value for a destructuring declaration, and the component type for its entries.


 - The enum class type for an enum entry.


If the type cannot be resolved or inferred (e.g., it refers to an unresolved class, or implicit types depend on each other recursively), the result is a [`KaErrorType`](../org.jetbrains.kotlin.analysis.api.types/-ka-error-type/index.md).

### `vararg` parameters
For a `vararg foo: T` parameter, the resulting type is the full `Array<out T>` type, or a primitive array type such as `IntArray` for a primitive `T` (unlike [`KaValueParameterSymbol.returnType`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-receiver-parameter-symbol/index.md#returntype), which is `T`).

The reasoning behind this is that [`KaCallableSymbol.returnType`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-receiver-parameter-symbol/index.md#returntype) sees the parameter from the declaration's semantic perspective, representing the signature of the parameter, which contains just the element type. In this paradigm, `vararg` arrays are constructed separately under the hood.

At the same time, [`returnType`](return-type.md) represents a use-site perspective, which has to desugar `vararg` parameters because they are consumed as array types.

Apart from `vararg` parameters, the result is the same as the return type of the declaration's [`KaCallableSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) if there is one (function type parameters have no symbol, and destructuring declarations have a non-callable symbol).


</div>

</div>
