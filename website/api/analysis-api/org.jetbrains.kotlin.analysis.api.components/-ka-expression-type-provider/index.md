---
tags:
 - jvm
title: "KaExpressionTypeProvider"
---

# KaExpressionTypeProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaExpressionTypeProvider</a> : <a href="../-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>#### Inheritors


 - [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)



</div>

## Properties
### expectedType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span>PsiElement<span class="p">.</span><a href="index.html#expectedtype">expectedType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The expected [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) for the given PsiElement if it is an expression, or `null` if the element does not have an expected type. The expected type represents the type that is expected for an expression at a specific location in the code.

See [`expressionType`](index.md#expressiontype) for a discussion about the expression type vs. the expected type.


</div>

</div>
### expressionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="index.html#expressiontype">expressionType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The type of the given [`KtExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md), or `null` if it does not have a type.

In particular:

 - A not-null type for valued expressions (e.g., a variable, a function call, a lambda expression).


 - [`Unit`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html) for statements (e.g., assignments, loops).


 - `null` for [`KtExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md)s that are not a part of the expression tree (e.g., expressions in import or package statements).


**Expression vs. expected type**

The Analysis API distinguishes between an expression's type and its expected type, which represent different aspects of the Kotlin type system.

The expression type represents the actual type of an expression after it has been resolved. It reflects the result of type inference, smart casts, and implicit conversions.

The expected type represents the type that is expected for an expression at a specific location in the code. This is determined by the context in which the expression appears, such as a variable type for its initializer, or a parameter type for a function call.


</div>

</div>
### functionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-function/index.html">KtFunction</a><span class="p">.</span><a href="index.html#functiontype">functionType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The function type of the given [`KtFunction`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-function/index.md).

For a regular function, the result is a `kotlin.FunctionN<P1, P2, ..., R>` type where:

 - `N` is the number of value parameters in the function.


 - `Px` is the type of the x-th value parameter.


 - `R` is the return type of the function.


Depending on the function's attributes, such as `suspend` or reflective access, a different functional type such as `SuspendFunction`, `KFunction`, or `KSuspendFunction` will be constructed.


</div>

</div>
### isDefinitelyNotNull

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="index.html#isdefinitelynotnull">isDefinitelyNotNull</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether this expression is definitely not null.

**See also**



 - [`isDefinitelyNull`](index.md#isdefinitelynull)



</div>

</div>
### isDefinitelyNull

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="index.html#isdefinitelynull">isDefinitelyNull</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether this expression is definitely null, based on the declared nullability and smart cast types derived from data-flow analysis facts.

Only nullability from stable smart casts is considered. See the [smart cast sink stability](https://kotlinlang.org/spec/type-inference.html#smart-cast-sink-stability) section of the Kotlin specification for more information.

**Examples**

```
public fun <T : Any> foo(t: T, nt: T?, s: String, ns: String?) {
  t     // t.isDefinitelyNull()  == false && t.isDefinitelyNotNull()  == true
  nt    // nt.isDefinitelyNull() == false && nt.isDefinitelyNotNull() == false
  s     // s.isDefinitelyNull()  == false && s.isDefinitelyNotNull()  == true
  ns    // ns.isDefinitelyNull() == false && ns.isDefinitelyNotNull() == false

  if (ns != null) {
    ns  // ns.isDefinitelyNull() == false && ns.isDefinitelyNotNull() == true
  } else {
    ns  // ns.isDefinitelyNull() == true  && ns.isDefinitelyNotNull() == false
  }

  ns!!  // From this point on: ns.isDefinitelyNull() == false && ns.isDefinitelyNotNull() == true
}
```


</div>

</div>
### returnType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration-with-return-type/index.html">KtDeclarationWithReturnType</a><span class="p">.</span><a href="index.html#returntype">returnType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The return type of the given [`KtDeclarationWithReturnType`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration-with-return-type/index.md).

Note: For a `vararg foo: T` parameter, the resulting type is the full `Array<out T>` type (unlike [`KaValueParameterSymbol.returnType`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-receiver-parameter-symbol/index.md#returntype), which is `T`).

The reasoning behind this is that [`KaCallableSymbol.returnType`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-receiver-parameter-symbol/index.md#returntype) sees the parameter from the declaration's semantic perspective, representing the signature of the parameter, which contains just the element type. In this paradigm, `vararg` arrays are constructed separately under the hood.

At the same time, [`KtDeclaration.returnType`](index.md#returntype) from [`KaExpressionTypeProvider`](index.md#returntype) represents a use-site perspective, which has to desugar `vararg` parameters because they are consumed as array types.


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
