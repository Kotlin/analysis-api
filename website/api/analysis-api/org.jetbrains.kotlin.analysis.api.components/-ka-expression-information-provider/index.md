---
tags:
 - jvm
title: "KaExpressionInformationProvider"
---

# KaExpressionInformationProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaExpressionInformationProvider</a> : <a href="../-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>#### Inheritors


 - [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)



</div>

## Properties
### isStableForSmartCasting

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="index.html#isstableforsmartcasting">isStableForSmartCasting</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether this expression can be used as a stable smart-cast sink at the current program point.

Stability is only one prerequisite for applying a smart cast. A `true` result does not mean that the expression is currently smart-cast to a more specific type. It only means that data-flow facts about this expression may be applied if such facts are available.

This property is meaningful for expressions that can be represented as data-flow variables, such as local variables, parameters, receivers, and property accesses. It returns `false` for expressions that are not smart-cast sinks, such as literals, function calls, and other types of expressions.

Stable smart-cast sinks generally include:

 - Local `val`s, value parameters, and stable receivers.


 - Local `var`s that the compiler can treat as effectively immutable at this program point.


 - `val` properties without delegation or custom getters, accessed through a stable receiver and declared in the      current module.


Unstable smart-cast sinks generally include:

 - Non-local `var` properties.


 - Delegated properties.


 - Properties with custom getters.


 - Properties from separately compiled modules.


 - `open` properties whose receiver is not known to have a final type.


 - Local `var`s whose captured writes may invalidate the relevant data-flow facts.


See the Kotlin specification section on [smart cast sink stability](https://kotlinlang.org/spec/type-inference.html#smart-cast-sink-stability).

**Example**

```kotlin
class Container(val value: Any?)

open class OpenContainer(open val value: Any?)

fun source(): Any? = ""

fun test(container: Container, openContainer: OpenContainer) {
    val local: Any? = ""
    var mutableLocal: Any? = ""
    mutableLocal = "tracked assignment"

    // local.isStableForSmartCasting == true
    // mutableLocal.isStableForSmartCasting == true
    // container.value.isStableForSmartCasting == true
    // openContainer.value.isStableForSmartCasting == false
    // source().isStableForSmartCasting == false
}
```


</div>

</div>
### isUsedAsExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="index.html#isusedasexpression">isUsedAsExpression</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the value of the given [`KtExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md) is used. In other words, `true` if the value of the expression is not safe to discard.

[`isUsedAsExpression`](index.md#isusedasexpression) performs a <strong>conservative check</strong> instead of exhaustive control-flow analysis. For example, `x` in the following example is possibly used, even though the value is never consumed at runtime: `x + try { throw Exception() } finally { return }`.

**Example**

In the following examples, `x` is used as a value (`x.isUsedAsExpression == true`):

 - `if (x) { ... } else { ... }`


 - `val a = x`


 - `x + 8`


 - `when (x) { 1 -> ...; else -> ... }`


In these expressions, `x` is not used as a value (`x.isUsedAsExpression == false`)

 - `run { x; println(50) }`


 - `when (x) { else -> ... }`



</div>

</div>
### isUsedAsResultOfLambda

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="index.html#isusedasresultoflambda">isUsedAsResultOfLambda</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the value of the given [`KtExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md) is used as the resulting expression of some lambda block.

Note that [`isUsedAsResultOfLambda`](index.md#isusedasresultoflambda) performs a <strong>conservative check</strong> instead of exhaustive control-flow analysis and `isUsedAsResultOfLambda` being `true` doesn't imply that the containing lambda itself is used.

It's also vital to not confuse lambda expressions with regular scope blocks (like `if` branches).

**Example**

In the following examples, `x` is used as a result of a lambda (`x.isUsedAsResultOfLambda == true`):

 - `{ x -> println(0); x }`


 - `{ { x }; 5 }`


In these expressions, `x` is not used as a result of a lambda (`x.isUsedAsResultOfLambda == false`)

 - `{ x -> println(0); x + 1 }`


 - `{ x; println(50) }`


 - `{ if (true) { x } else { x } }`


 - `fun(x: Int) = x`



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
### computeMissingCases

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-expression/index.html">KtWhenExpression</a><span class="p">.</span><a href="index.html#computemissingcases"><span class="nf">computeMissingCases</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-when-missing-case/index.html">KaWhenMissingCase</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Computes the missing cases of the given [`KtWhenExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-expression/index.md).

The computed missing cases are not affected by the existence or absence of an `else` branch.

**Example**

In the following code, `Direction.WEST` and `Direction.EAST` are missing branches:

```
enum class Direction {
  NORTH, SOUTH, WEST, EAST
}

foo = when(direction) {
  Direction.NORTH -> 1
  Direction.SOUTH -> 2
  else -> 3
}
```

If the [`KtWhenExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-expression/index.md) has no subject, then the `else` is reported as missing even if it is explicitly present:

```
fun test() {
    when {
        true -> {}
        else -> {}
    }
}
```


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
