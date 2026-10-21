---
tags:
 - jvm
title: "KaSubstitutorProvider"
---

# KaSubstitutorProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaSubstitutorProvider</a> : <a href="../-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>#### Inheritors


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
## Functions
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### createInheritanceTypeSubstitutor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createinheritancetypesubstitutor"><span class="nf">createInheritanceTypeSubstitutor</span></a><span class="p">(</span>subClass<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">, </span>superClass<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md) based on the inheritance relationship between [`subClass`](index.md#createinheritancetypesubstitutor) and [`superClass`](index.md#createinheritancetypesubstitutor). [`subClass`](index.md#createinheritancetypesubstitutor) must inherit from [`superClass`](index.md#createinheritancetypesubstitutor) and there may not be any error types in the inheritance path. Otherwise, `null` is returned.

The semantics of the resulting [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md) are as follows: When applied to a member of [`superClass`](index.md#createinheritancetypesubstitutor), such as a function, its type parameters are substituted in such a way that the resulting member can be used with an instance of [`subClass`](index.md#createinheritancetypesubstitutor).

In other words, the substitutor is a composition of inheritance-based substitutions incorporating the whole inheritance chain.

**Example**

```
class A : B<String>
class B<T> : C<T, Int>
class C<X, Y>
```

 - `createInheritanceTypeSubstitutor(A, B)` returns `KaSubstitutor { T -> String }`


 - `createInheritanceTypeSubstitutor(B, C)` returns `KaSubstitutor { X -> T, Y -> Int }`


 - `createInheritanceTypeSubstitutor(A, C)` returns `KaSubstitutor { X -> T, Y -> Int } and then KaSubstitutor { T -> String }`



</div>

</div>
### createSubstitutor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createsubstitutor"><span class="nf">createSubstitutor</span></a><span class="p">(</span>mappings<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md) based on the given [`mappings`](index.md#createsubstitutor).

Usually, [`buildSubstitutor`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/index.md) should be preferred to build a new substitutor from scratch.

**See also**



 - [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md)



</div>

</div>
### createSubtypingUnificationSubstitutor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createsubtypingunificationsubstitutor"><span class="nf">createSubtypingUnificationSubstitutor</span></a><span class="p">(</span>leftTypesToRightTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/index.html">Pair</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span><span class="o">></span><span class="p">, </span>isFreeTypeParameter<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md) which assigns type arguments such that, for each pair in [`leftTypesToRightTypes`](index.md#createsubtypingunificationsubstitutor), the substituted left type is a subtype of the substituted right type. Returns `null` if such an assignment is not possible.

Note that when one type parameter is shared across several constraint pairs, all these pairs affect the resulting substitution for this parameter.

[`createSubtypingUnificationSubstitutor`](index.md#createsubtypingunificationsubstitutor) creates a constraint system, adds all the required bounds for 'leftType <: rightType' from each [`leftTypesToRightTypes`](index.md#createsubtypingunificationsubstitutor) pair and tries to solve the given constraint system:

 - If there were no contradictions found in the constraint system, the resulting substitutor is non-null. Otherwise, `null` is returned.


 - If there are no type parameters involved in the provided types and every left type is a subtype of its right type, [`KaSubstitutor.Empty`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/-empty/index.md) is returned.


 - If [`leftTypesToRightTypes`](index.md#createsubtypingunificationsubstitutor) is empty, [`KaSubstitutor.Empty`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/-empty/index.md) is returned as there can be no contradictions with no constraints.


[`isFreeTypeParameter`](index.md#createsubtypingunificationsubstitutor) is called on every type parameter involved in the provided types and controls the set of free type parameters registered in the constraint system. Only affects the construction when at least one of the involved types is generic, i.e., depends on a type parameter. The constraint system will only adjust the values of these free type parameters, and the produced substitutor will only contain mappings for these parameters.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createsubtypingunificationsubstitutor"><span class="nf">createSubtypingUnificationSubstitutor</span></a><span class="p">(</span>
    leftType<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    rightType<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    constructionPolicy<span class="o">: </span><a href="../-ka-unification-substitutor-policy/index.html">KaUnificationSubstitutorPolicy</a>
<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md) which assigns type arguments such that the substituted [`leftType`](index.md#createsubtypingunificationsubstitutor) is a subtype of the substituted [`rightType`](index.md#createsubtypingunificationsubstitutor). Returns `null` if such an assignment is not possible.

[`createSubtypingUnificationSubstitutor`](index.md#createsubtypingunificationsubstitutor) creates a constraint system, adds all the required bounds for '[`leftType`](index.md#createsubtypingunificationsubstitutor)<: [`rightType`](index.md#createsubtypingunificationsubstitutor)' and tries to solve the given constraint system:

 - If there were no contradictions found in the constraint system, the resulting substitutor is non-null. Otherwise, `null` is returned.


 - If there are no type parameters involved in the provided types and [`leftType`](index.md#createsubtypingunificationsubstitutor) is a subtype of [`rightType`](index.md#createsubtypingunificationsubstitutor), [`KaSubstitutor.Empty`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/-empty/index.md) is returned.


[`constructionPolicy`](index.md#createsubtypingunificationsubstitutor) controls the way the unification substitutor is constructed. Only affects the construction when at least one of the involved types is generic, i.e., depends on a type parameter. See [`KaUnificationSubstitutorPolicy`](../-ka-unification-substitutor-policy/index.md) for more information and code examples.

**Examples:**

```
interface MyClass<A>

fun <T: X, X: R, R: Number> someFun(leftType: MyClass<Int>, rightType: MyClass<T>) {}
```

 - `createSubtypingUnificationSubstitutor(MyClass<Int>, MyClass<T>, KaUnificationSubstitutorPolicy.ASSIGN_LEFT)` returns `null`, as `T` is fixed and not guaranteed to be exactly `Int` to satisfy the constraint.


 - `createSubtypingUnificationSubstitutor(MyClass<Int>, MyClass<T>, KaUnificationSubstitutorPolicy.ASSIGN_RIGHT)` returns `KaSubstitutor { T -> kotlin/Int, X -> kotlin/Int, R -> kotlin/Int }`.


 - `createSubtypingUnificationSubstitutor(MyClass<Int>, MyClass<T>, KaUnificationSubstitutorPolicy.ASSIGN_ALL)` returns the exact same substitutor `KaSubstitutor { T -> kotlin/Int, X -> kotlin/Int, R -> kotlin/Int }`.


```
fun <C: Any, T: Int> foo(leftType: List<C>, rightType: List<T>) {}
```

 - `createSubtypingUnificationSubstitutor(List<C>, List<T>, KaUnificationSubstitutorPolicy.ASSIGN_LEFT)` returns `KaSubstitutor { C -> T }`.


 - `createSubtypingUnificationSubstitutor(List<C>, List<T>, KaUnificationSubstitutorPolicy.ASSIGN_RIGHT)` returns `null`, as `C` is fixed and there is no assignment for `T` to satisfy the constraint (e.g., with `C = kotlin/Any`, while `T` is bounded by `kotlin/Int`).


 - `createSubtypingUnificationSubstitutor(List<C>, List<T>, KaUnificationSubstitutorPolicy.ASSIGN_ALL)` returns `KaSubstitutor { C -> kotlin/Int, T -> kotlin/Int }`, as with such a substitution, `List<C>` is a subtype of `List<T>`.


**See also**



 - [`KaUnificationSubstitutorPolicy.ASSIGN_LEFT`](../-ka-unification-substitutor-policy/-a-s-s-i-g-n_-l-e-f-t/index.md)
 - [`KaUnificationSubstitutorPolicy.ASSIGN_RIGHT`](../-ka-unification-substitutor-policy/-a-s-s-i-g-n_-r-i-g-h-t/index.md)
 - [`KaUnificationSubstitutorPolicy.ASSIGN_ALL`](../-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createsubtypingunificationsubstitutor"><span class="nf">createSubtypingUnificationSubstitutor</span></a><span class="p">(</span>leftTypesToRightTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/index.html">Pair</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span><span class="o">></span><span class="p">, </span>constructionPolicy<span class="o">: </span><a href="../-ka-unification-substitutor-policy/index.html">KaUnificationSubstitutorPolicy</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.html">KaSubstitutor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/index.md) which assigns type arguments such that, for each pair in [`leftTypesToRightTypes`](index.md#createsubtypingunificationsubstitutor), the substituted left type is a subtype of the substituted right type. Returns `null` if such an assignment is not possible.

Note that when one type parameter is shared across several constraint pairs, all these pairs affect the resulting substitution for this parameter.

[`createSubtypingUnificationSubstitutor`](index.md#createsubtypingunificationsubstitutor) creates a constraint system, adds all the required bounds for 'leftType <: rightType' from each [`leftTypesToRightTypes`](index.md#createsubtypingunificationsubstitutor) pair and tries to solve the given constraint system:

 - If there were no contradictions found in the constraint system, the resulting substitutor is non-null. Otherwise, `null` is returned.


 - If there are no type parameters involved in the provided types and every left type is a subtype of its right type, [`KaSubstitutor.Empty`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/-empty/index.md) is returned.


 - If [`leftTypesToRightTypes`](index.md#createsubtypingunificationsubstitutor) is empty, [`KaSubstitutor.Empty`](../../org.jetbrains.kotlin.analysis.api.types/-ka-substitutor/-empty/index.md) is returned as there can be no contradictions with no constraints.


[`constructionPolicy`](index.md#createsubtypingunificationsubstitutor) controls the way the unification substitutor is constructed. Only affects the construction when at least one of the involved types is generic, i.e., depends on a type parameter. See [`KaUnificationSubstitutorPolicy`](../-ka-unification-substitutor-policy/index.md) for more information and code examples.

**Examples:**

```
fun <X> rights(right1: List<X>, right2: List<X>) {}

fun lefts(left1: List<Int>, left2: List<String>) {}
```

 - `createSubtypingUnificationSubstitutor(listOf(List<Int> to List<X>, List<String> to List<X>), KaUnificationSubstitutorPolicy.ASSIGN_LEFT)` returns `null` as the left types contain no type parameters and the concrete left types are not subtypes of their generic right types.


 - `createSubtypingUnificationSubstitutor(listOf(List<Int> to List<X>, List<String> to List<X>), KaUnificationSubstitutorPolicy.ASSIGN_RIGHT)` returns `KaSubstitutor { X -> intersection(kotlin/Comparable<*> & java/io/Serializable) }`.


 - `createSubtypingUnificationSubstitutor(listOf(List<Int> to List<X>, List<String> to List<X>), KaUnificationSubstitutorPolicy.ASSIGN_ALL)` returns the same substitutor `KaSubstitutor { X -> intersection(kotlin/Comparable<*> & java/io/Serializable) }`.


**See also**



 - [`KaUnificationSubstitutorPolicy.ASSIGN_LEFT`](../-ka-unification-substitutor-policy/-a-s-s-i-g-n_-l-e-f-t/index.md)
 - [`KaUnificationSubstitutorPolicy.ASSIGN_RIGHT`](../-ka-unification-substitutor-policy/-a-s-s-i-g-n_-r-i-g-h-t/index.md)
 - [`KaUnificationSubstitutorPolicy.ASSIGN_ALL`](../-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md)



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
