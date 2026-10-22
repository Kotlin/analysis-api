---
tags:
 - jvm
title: "createSubtypingUnificationSubstitutor"
---

# createSubtypingUnificationSubstitutor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="create-subtyping-unification-substitutor.html"><span class="nf">createSubtypingUnificationSubstitutor</span></a><span class="p">(</span>leftTypesToRightTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/index.html">Pair</a><span class="o"><</span><a href="-ka-type/index.html">KaType</a><span class="p">, </span><a href="-ka-type/index.html">KaType</a><span class="o">></span><span class="o">></span><span class="p">, </span>isFreeTypeParameter<span class="o">: </span><span class="p">(</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="-ka-substitutor/index.html">KaSubstitutor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSubstitutor`](-ka-substitutor/index.md) which assigns type arguments such that, for each pair in [`leftTypesToRightTypes`](create-subtyping-unification-substitutor.md), the substituted left type is a subtype of the substituted right type. Returns `null` if such an assignment is not possible.

Note that when one type parameter is shared across several constraint pairs, all these pairs affect the resulting substitution for this parameter.

[`createSubtypingUnificationSubstitutor`](create-subtyping-unification-substitutor.md) creates a constraint system, adds all the required bounds for 'leftType <: rightType' from each [`leftTypesToRightTypes`](create-subtyping-unification-substitutor.md) pair and tries to solve the given constraint system:

 - If there were no contradictions found in the constraint system, the resulting substitutor is non-null. Otherwise, `null` is returned.


 - If there are no type parameters involved in the provided types and every left type is a subtype of its right type, [`KaSubstitutor.Empty`](-ka-substitutor/-empty/index.md) is returned.


 - If [`leftTypesToRightTypes`](create-subtyping-unification-substitutor.md) is empty, [`KaSubstitutor.Empty`](-ka-substitutor/-empty/index.md) is returned as there can be no contradictions with no constraints.


[`isFreeTypeParameter`](create-subtyping-unification-substitutor.md) is called on every type parameter involved in the provided types and controls the set of free type parameters registered in the constraint system. Only affects the construction when at least one of the involved types is generic, i.e., depends on a type parameter. The constraint system will only adjust the values of these free type parameters, and the produced substitutor will only contain mappings for these parameters.


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

[`createSubtypingUnificationSubstitutor`](create-subtyping-unification-substitutor.md) creates a constraint system, adds all the required bounds for '[`leftType`](create-subtyping-unification-substitutor.md)<: [`rightType`](create-subtyping-unification-substitutor.md)' and tries to solve the given constraint system:

 - If there were no contradictions found in the constraint system, the resulting substitutor is non-null. Otherwise, `null` is returned.


 - If there are no type parameters involved in the provided types and [`leftType`](create-subtyping-unification-substitutor.md) is a subtype of [`rightType`](create-subtyping-unification-substitutor.md), [`KaSubstitutor.Empty`](-ka-substitutor/-empty/index.md) is returned.


[`constructionPolicy`](create-subtyping-unification-substitutor.md) controls the way the unification substitutor is constructed. Only affects the construction when at least one of the involved types is generic, i.e., depends on a type parameter. See [`KaUnificationSubstitutorPolicy`](-ka-unification-substitutor-policy/index.md) for more information and code examples.

#### Examples:
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


#### See also


 - [`KaUnificationSubstitutorPolicy.ASSIGN_LEFT`](-ka-unification-substitutor-policy/-a-s-s-i-g-n_-l-e-f-t/index.md)
 - [`KaUnificationSubstitutorPolicy.ASSIGN_RIGHT`](-ka-unification-substitutor-policy/-a-s-s-i-g-n_-r-i-g-h-t/index.md)
 - [`KaUnificationSubstitutorPolicy.ASSIGN_ALL`](-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md)



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

Note that when one type parameter is shared across several constraint pairs, all these pairs affect the resulting substitution for this parameter.

[`createSubtypingUnificationSubstitutor`](create-subtyping-unification-substitutor.md) creates a constraint system, adds all the required bounds for 'leftType <: rightType' from each [`leftTypesToRightTypes`](create-subtyping-unification-substitutor.md) pair and tries to solve the given constraint system:

 - If there were no contradictions found in the constraint system, the resulting substitutor is non-null. Otherwise, `null` is returned.


 - If there are no type parameters involved in the provided types and every left type is a subtype of its right type, [`KaSubstitutor.Empty`](-ka-substitutor/-empty/index.md) is returned.


 - If [`leftTypesToRightTypes`](create-subtyping-unification-substitutor.md) is empty, [`KaSubstitutor.Empty`](-ka-substitutor/-empty/index.md) is returned as there can be no contradictions with no constraints.


[`constructionPolicy`](create-subtyping-unification-substitutor.md) controls the way the unification substitutor is constructed. Only affects the construction when at least one of the involved types is generic, i.e., depends on a type parameter. See [`KaUnificationSubstitutorPolicy`](-ka-unification-substitutor-policy/index.md) for more information and code examples.

#### Examples:
```
fun <X> rights(right1: List<X>, right2: List<X>) {}

fun lefts(left1: List<Int>, left2: List<String>) {}
```

 - `createSubtypingUnificationSubstitutor(listOf(List<Int> to List<X>, List<String> to List<X>), KaUnificationSubstitutorPolicy.ASSIGN_LEFT)` returns `null` as the left types contain no type parameters and the concrete left types are not subtypes of their generic right types.


 - `createSubtypingUnificationSubstitutor(listOf(List<Int> to List<X>, List<String> to List<X>), KaUnificationSubstitutorPolicy.ASSIGN_RIGHT)` returns `KaSubstitutor { X -> intersection(kotlin/Comparable<*> & java/io/Serializable) }`.


 - `createSubtypingUnificationSubstitutor(listOf(List<Int> to List<X>, List<String> to List<X>), KaUnificationSubstitutorPolicy.ASSIGN_ALL)` returns the same substitutor `KaSubstitutor { X -> intersection(kotlin/Comparable<*> & java/io/Serializable) }`.


#### See also


 - [`KaUnificationSubstitutorPolicy.ASSIGN_LEFT`](-ka-unification-substitutor-policy/-a-s-s-i-g-n_-l-e-f-t/index.md)
 - [`KaUnificationSubstitutorPolicy.ASSIGN_RIGHT`](-ka-unification-substitutor-policy/-a-s-s-i-g-n_-r-i-g-h-t/index.md)
 - [`KaUnificationSubstitutorPolicy.ASSIGN_ALL`](-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md)



</div>

</div>
