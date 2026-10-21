---
tags:
 - jvm
title: "KaTypeRelationChecker"
---

# KaTypeRelationChecker

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaTypeRelationChecker</a> : <a href="../-ka-session-component/index.html">KaSessionComponent</a>
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
### isSubtypeOf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>supertype<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>errorTypePolicy<span class="o">: </span><a href="../-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a><span class="o"> = </span>KaSubtypingErrorTypePolicy.STRICT<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a subtype of [`supertype`](index.md#issubtypeof). The relation is non-strict, i.e. any type `t` is a subtype of itself.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">, </span>errorTypePolicy<span class="o">: </span><a href="../-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a><span class="o"> = </span>KaSubtypingErrorTypePolicy.STRICT<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a subtype of a class called [`classId`](index.md#issubtypeof).

This function provides a convenient way to check if a class extends a certain base class or interface while disregarding type arguments. For example, one may check if this [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a subtype of StandardClassIds.Iterable.

The [`errorTypePolicy`](index.md#issubtypeof) is applied as such: If this [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is an error type, the [`LENIENT`](../-ka-subtyping-error-type-policy/-l-e-n-i-e-n-t/index.md) policy leads to a trivially `true` result. Errors in type arguments are not considered, as the subclass check is concerned with the applied class type and not its type arguments.

This function for ClassIds is a convenient dual to other [`isSubtypeOf`](index.md#issubtypeof) functions. As such, its result is the same as a call to [`isSubtypeOf`](index.md#issubtypeof) with the following right-hand [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md): `a.b.Class<*, *, ...>?` given a class ID `a.b.Class` with all type arguments instantiated to a star projection.

This has the following interesting implications:

 - If the [`classId`](index.md#issubtypeof) points to or actualizes to a type alias, subclassing is checked for the expanded type, as other [`isSubtypeOf`](index.md#issubtypeof) implementations also take expansion into account. If the type alias doesn't expand to a [`KaClassType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.md), [`isSubtypeOf`](index.md#issubtypeof) is trivially `false`.


 - If the [`classId`](index.md#issubtypeof) cannot be resolved, it effectively means that we would have an "unresolved symbol" error [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) on the right-hand side of [`isSubtypeOf`](index.md#issubtypeof). Hence, with a [`LENIENT`](../-ka-subtyping-error-type-policy/-l-e-n-i-e-n-t/index.md) error type policy, [`isSubtypeOf`](index.md#issubtypeof) is `true` for all unresolved class IDs.



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">, </span>errorTypePolicy<span class="o">: </span><a href="../-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a><span class="o"> = </span>KaSubtypingErrorTypePolicy.STRICT<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is a subtype of a class represented by [`symbol`](index.md#issubtypeof).

This function provides a convenient way to check if a class extends a certain base class or interface while disregarding type arguments.

The [`errorTypePolicy`](index.md#issubtypeof) is applied as such: If this [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is an error type, the [`LENIENT`](../-ka-subtyping-error-type-policy/-l-e-n-i-e-n-t/index.md) policy leads to a trivially `true` result. Errors in type arguments are not considered, as the subclass check is concerned with the applied class type and not its type arguments.

This function for [`KaClassLikeSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.md)s is a convenient dual to other [`isSubtypeOf`](index.md#issubtypeof) functions. As such, its result is the same as a call to [`isSubtypeOf`](index.md#issubtypeof) with the following right-hand [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md): `a.b.Class<*, *, ...>?` given a class called `a.b.Class` with all type arguments instantiated to a star projection.

This has the following interesting implication: If the [`symbol`](index.md#issubtypeof) points to or actualizes to a type alias, subclassing is checked for the expanded type, as other [`isSubtypeOf`](index.md#issubtypeof) implementations also take expansion into account. If the type alias doesn't expand to a [`KaClassType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.md), [`isSubtypeOf`](index.md#issubtypeof) is trivially `false`.


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
### semanticallyEquals

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#semanticallyequals"><span class="nf">semanticallyEquals</span></a><span class="p">(</span>other<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>errorTypePolicy<span class="o">: </span><a href="../-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a><span class="o"> = </span>KaSubtypingErrorTypePolicy.STRICT<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether this [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is semantically equal to [`other`](index.md#semanticallyequals).

Semantic equality stands in contrast to the structural equality implemented by [`KaType.equals`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/equals.html). See [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) for a detailed discussion about structural vs. semantic type equality.


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
