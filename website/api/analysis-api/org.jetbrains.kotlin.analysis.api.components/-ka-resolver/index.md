---
tags:
 - jvm
title: "KaResolver"
---

# KaResolver

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaResolver</a> : <a href="../-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>#### Inheritors


 - [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)



</div>

## Properties
### contextSensitiveResolutionStatus

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="index.html#contextsensitiveresolutionstatus">contextSensitiveResolutionStatus</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-context-sensitive-resolution-status/index.html">KaContextSensitiveResolutionStatus</a>
</span></code></pre></div>
</div>


<div markdown>

The [context-sensitive resolution](https://github.com/Kotlin/KEEP/issues/379) status of the [`KtSimpleNameExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.md): whether the name is already resolved through context-sensitive resolution, and whether a redundant explicit qualifier or import could be removed in favor of it.

The information is available even when the `-Xcontext-sensitive-resolution` feature is not enabled.

**Example**

```
enum class Foo { BAR }

fun usage(): Foo {
    return Foo.BAR // the 'Foo.' qualifier can be removed -> KaContextSensitiveResolutionStatus.QualifierCanBeRemoved
}
```

**See also**



 - [`KaContextSensitiveResolutionStatus`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-context-sensitive-resolution-status/index.md)



</div>

</div>
### isImplicitReferenceToCompanion

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">.</span><a href="index.html#isimplicitreferencetocompanion">isImplicitReferenceToCompanion</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks if the [`KtSimpleNameExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.md) is an implicit reference to a companion object via the containing class.

**Example**

```
class A {
   companion object {
      fun foo() {}
   }
}
```

Given a call `A.foo()`, `A` is an implicit reference to the companion object, so `isImplicitReferenceToCompanion` returns `true`.


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
### collectCallCandidates

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">.</span><a href="index.html#collectcallcandidates"><span class="nf">collectCallCandidates</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-candidate/index.html">KaCallCandidate</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all candidates considered during [overload resolution](https://kotlinlang.org/spec/overload-resolution.html) for the call corresponding to the given [`KtResolvableCall`](../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md).

In contrast, [`resolveCall`](index.md#resolvecall) returns only the final result, i.e., the most specific callable that passes all compatibility checks.

**See also**



 - [`resolveCall`](index.md#resolvecall)



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
### resolveCall

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the call for the given [`KtResolvableCall`](../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md).

**Usage Example:**

```kotlin
fun KaSession.resolveSymbol(expression: KtCallExpression): KaSymbol? {
  return expression.resolveCall()?.simple?.symbol
}
```

Returns the resolved [`KaSimpleOrMultiCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-or-multi-call/index.md) on success; otherwise, `null`

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`collectCallCandidates`](index.md#collectcallcandidates)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-annotation-call/index.html">KaAnnotationCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtAnnotationEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.md) to an annotation constructor call.

**Example**

```kotlin
annotation class Anno(val x: Int)

@Anno(42)
fun foo() {}
```

Returns the corresponding [`KaAnnotationCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-annotation-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on annotation entries. Use [`collectCallCandidates`](index.md#collectcallcandidates) to inspect all candidates considered during overload resolution

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.html">KtSuperTypeCallEntry</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtSuperTypeCallEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.md) to a constructor call of the referenced supertype.

**Example**

```kotlin
open class Base(i: Int)

class Derived : Base(1)
//              ^^^^^^^
```

Returns the corresponding [`KaFunctionCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on supertype constructor calls

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtConstructorDelegationCall`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.md) to a delegated constructor call.

**Example**

```kotlin
open class Base(val i: Int)

class Derived : Base {
    constructor() : this(0)
    //              ^^^^^^^

    constructor(x: Int) : super(x)
    //                    ^^^^^^^^
}
```

Returns the corresponding [`KaDelegatedConstructorCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-constructor-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on constructor delegation calls

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.html">KtConstructorDelegationReferenceExpression</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtConstructorDelegationReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.md) to a delegated constructor call.

**Example**

```kotlin
open class Base(val i: Int)

class Derived : Base {
    constructor() : this(0)
    //              ^^^^

    constructor(x: Int) : super(x)
    //                    ^^^^^
}
```

Returns the corresponding [`KaDelegatedConstructorCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-constructor-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on constructor delegation calls

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.html">KtCallElement</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtCallElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.md) to a function call.

**Example**

```kotlin
fun foo(x: Int) {}

fun test() {
    foo(42)
//  ^^^^^^^
}
```

Returns the corresponding [`KaSimpleCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on call elements

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.html">KtCallableReferenceExpression</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-callable-reference-call/index.html">KaCallableReferenceCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtCallableReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.md) to a callable member call.

**Example**

```kotlin
class A { fun foo() {} }

val ref = A::foo
//        ^^^^^^
```

Returns the corresponding [`KaCallableReferenceCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-callable-reference-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on callable reference expressions

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.html">KtArrayAccessExpression</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtArrayAccessExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.md) to a simple function call representing `get`/`set` operator invocation.

**Example**

```kotlin
class A {
    operator fun get(i: Int): Int = i
    operator fun set(i: Int, value: Int) {}
}

fun test(a: A) {
    a[0]
//  ^^^^  resolves to `get`
    a[0] = 1
//  ^^^^ resolves to `set`
}
```

Returns the corresponding KaSimpleFunctionCall if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on array access operations.

<strong>Note</strong>: the `get` call is prefered in the case of a compound assignent

```kotlin
fun test(m: MyMap<String, Int>) {
    m["a"] += 1
//  ^^^^^^
}
```

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.html">KtCollectionLiteralExpression</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtCollectionLiteralExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.md) to a simple function call representing the corresponding array factory invocation.

**Example**

```kotlin
annotation class Anno(val arr: IntArray)

@Anno([1, 2, 3])
//    ^^^^^^^^^ resolves to a call of `intArrayOf`
fun use() {}
```

Returns the corresponding KaSimpleFunctionCall if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on collection literal expressions

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.html">KtEnumEntrySuperclassReferenceExpression</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtEnumEntrySuperclassReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md) to a delegated constructor call.

**Example**

```kotlin
enum class EnumWithConstructor(val x: Int) {
    Entry(1)
//      ^ resolves to the constructor of `EnumWithConstructor`
}
```

Returns the corresponding [`KaDelegatedConstructorCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-constructor-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on enum entry superclass constructor calls

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.html">KtWhenConditionInRange</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtWhenConditionInRange`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.md) to a simple function call representing the corresponding `contains` operator invocation used by the `in`/`!in` branch condition.

**Example**

```kotlin
fun test(x: Int) {
    when (x) {
        in 1..10 -> {}
//      ^^^^^^^^ resolves to a call of `IntRange.contains`

        !in setOf(1, 2, 3) -> {}
//      ^^^^^^^^^^^^^^^^^^ resolves to a call of `Set<Int>.contains`
    }
}
```

Returns the corresponding KaSimpleFunctionCall if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on `in`/`!in` range conditions inside `when` entries

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtDestructuringDeclarationEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.md) to a call representing the `componentN` invocation (for positional destructuring) or the property access (for name-based destructuring).

**Example**

```kotlin
data class Point(val x: Int, val y: Int)

fun test(p: Point) {
    val (x, y) = p
//       ^ resolves to a call of `component1`
//          ^ resolves to a call of `component2`
}
```

Returns the corresponding [`KaSimpleCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on destructuring declaration entries

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtQualifiedExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.md) to a call representing the member or extension access.

**Example**

```kotlin
val len = str.length
//        ^________^
```

Calling `resolveCall()` on the [`KtQualifiedExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.md) (`str.length`) returns the corresponding [`KaSimpleCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on qualified expressions

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.html">KtForExpression</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-for-loop-call/index.html">KaForLoopCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtForExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.md) to a [`KaForLoopCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-for-loop-call/index.md) representing the desugared `for` loop.

A `for` loop desugars into three operator calls:

 - `iterator()` on the loop range expression


 - `hasNext()` on the iterator


 - `next()` on the iterator


**Example**

```kotlin
for (item in list) {
    println(item)
}
```

Calling `resolveCall()` on the [`KtForExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.md) returns a [`KaForLoopCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-for-loop-call/index.md) containing the three desugared operator calls if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on `for` loops

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.html">KtPropertyDelegate</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-property-call/index.html">KaDelegatedPropertyCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtPropertyDelegate`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.md) to a [`KaDelegatedPropertyCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-property-call/index.md) representing the desugared delegated property.

A delegated property desugars into up to three operator calls:

 - `getValue()` on the delegate object


 - `setValue()` on the delegate object (only for `var` properties)


 - `provideDelegate()` on the delegate expression (if applicable)


**Example**

```kotlin
val name: String by lazy { "John" }
//               ^________________^
```

Calling `resolveCall()` on the [`KtPropertyDelegate`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.md) returns a [`KaDelegatedPropertyCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-property-call/index.md) containing the desugared operator calls if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on delegated properties

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.html">KtConstructorCalleeExpression</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtConstructorCalleeExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.md) to a constructor call.

**Example**

```kotlin
open class Base(i: Int)

class Derived : Base(1)
//              ^^^^
```

Returns the corresponding [`KaFunctionCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on constructor callee expressions

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.html">KtNameReferenceExpression</a><span class="p">.</span><a href="index.html#resolvecall"><span class="nf">resolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtNameReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md) to a call representing the referenced declaration.

**Example**

```kotlin
fun foo() {}

val x = foo
//      ^^^
```

Calling `resolveCall()` on the [`KtNameReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md) (`foo`) returns the corresponding [`KaSimpleCall`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveCall`](index.md#resolvecall) focused specifically on name reference expressions

**See also**



 - [`tryResolveCall`](index.md#tryresolvecall)
 - [`KtResolvableCall.resolveCall`](index.md#resolvecall)



</div>

</div>
### resolveSymbol { data-search-exclude }

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves a single symbol for the given [`KtResolvable`](../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md).

Returns the [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) if there is exactly one target; otherwise, `null`

In contract to [`resolveCall`](index.md#resolvecall), it could represent any [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md), not only [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md).

In most cases, a not-null result of [`resolveCall`](index.md#resolvecall) will represent the same symbol. The only exceptions are:

 - [`KtNameReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md)


 - [`KtOperationReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-operation-reference-expression/index.md)


 - [`KtEnumEntrySuperclassReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md)


For which the behavior could be different depending on the context.

The main idea is that [`resolveSymbol`](index.md#resolvesymbol) could represent more cases, so it prefers exactly the referenced symbol and not the parent call. For more details, see the mentioned elements.

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`resolveSymbols`](index.md#resolvesymbols)
 - [`KaSimpleSymbolResolutionSuccess`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-symbol-resolution-success/index.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol of the annotation referenced by the given [`KtAnnotationEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.md).

**Example**

```kotlin
annotation class Anno(val x: Int)

@Anno(42)
fun foo() {}
```

Calling `resolveSymbol()` on the [`KtAnnotationEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.md) (`@Anno(42)`) returns the [`KaConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) of `Anno`'s annotation constructor if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on annotation entries

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.html">KtSuperTypeCallEntry</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol by the given [`KtSuperTypeCallEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.md).

**Example**

```kotlin
open class Base(i: Int)

class Derived : Base(1)
//              ^^^^^^^
```

Calling `resolveSymbol()` on the [`KtSuperTypeCallEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.md) (`Base(1)`) returns the [`KaConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) of `Base`'s constructor if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on supertype constructor calls

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol referenced by the given [`KtConstructorDelegationCall`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.md).

**Example**

```kotlin
open class Base(val i: Int)

class Derived : Base {
    constructor() : this(0)
    //              ^^^^^^^

    constructor(x: Int) : super(x)
    //                    ^^^^^^^^
}
```

Calling `resolveSymbol()` on a [`KtConstructorDelegationCall`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.md) (either `this(...)` or `super(...)`) returns the [`KaConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) of the target constructor if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on constructor delegation calls

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.html">KtConstructorDelegationReferenceExpression</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol referenced by the given [`KtConstructorDelegationReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.md).

**Example**

```kotlin
open class Base(val i: Int)

class Derived : Base {
    constructor() : this(0)
    //              ^^^^

    constructor(x: Int) : super(x)
    //                    ^^^^^
}
```

Calling `resolveSymbol()` on a [`KtConstructorDelegationReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.md) (either `this` or `super`) returns the [`KaConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) of the target constructor if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on constructor delegation calls

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.html">KtCallElement</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the function symbol targeted by the given [`KtCallElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.md).

**Example**

```kotlin
fun foo(x: Int) {}

fun test() {
    foo(42)
//  ^^^^^^^
}
```

Calling `resolveSymbol()` on the [`KtCallElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.md) (`foo(42)`) returns the [`KaFunctionSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md) of `foo` if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on call elements

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.html">KtCallableReferenceExpression</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the callable symbol targeted by the given [`KtCallableReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.md).

**Example**

```kotlin
fun foo(x: Int) {}

val ref = ::foo
//        ^^^^^
```

Calling `resolveSymbol()` on the [`KtCallableReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.md) (`::foo`) returns the [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) of `foo` if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on callable reference expressions

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.html">KtArrayAccessExpression</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the operator function symbol targeted by the given [`KtArrayAccessExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.md).

**Example**

```kotlin
class A {
    operator fun get(i: Int): Int = i
    operator fun set(i: Int, value: Int) {}
}

fun test(a: A) {
    a[0]
//  ^^^^  resolves to `get`
    a[0] = 1
//  ^^^^ resolves to `set`
}
```

Calling `resolveSymbol()` on a [`KtArrayAccessExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.md) (`a[0]`) returns the [`KaNamedFunctionSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.md) of the corresponding `get`/`set` operator if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on array access operations.

<strong>Note</strong>: the `get` call is prefered in the case of a compound assignent

```kotlin
fun test(m: MyMap<String, Int>) {
    m["a"] += 1
//  ^^^^^^
}
```

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.html">KtCollectionLiteralExpression</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the function symbol targeted by the given [`KtCollectionLiteralExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.md).

**Example**

```kotlin
annotation class Anno(val arr: IntArray)

@Anno([1, 2, 3])
//    ^^^^^^^^^ resolves to the `intArrayOf` function
fun use() {}
```

Calling `resolveSymbol()` on a [`KtCollectionLiteralExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.md) (`[1, 2, 3]`) returns the [`KaNamedFunctionSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.md) of the corresponding array factory (e.g., `arrayOf`, `intArrayOf`) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on collection literal expressions

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.html">KtEnumEntrySuperclassReferenceExpression</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the enum class symbol referenced by the given [`KtEnumEntrySuperclassReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md).

**Example**

```kotlin
enum class EnumWithConstructor(val x: Int) {
    Entry(1)
//      ^ resolves to the enum class `EnumWithConstructor`
}
```

Calling `resolveSymbol()` on a [`KtEnumEntrySuperclassReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md) returns the [`KaNamedClassSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.md) of the enclosing enum class if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

Mirrors how [`KtNameReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md) prefers the class over the constructor: while the surrounding super-type call ([`resolveCall`](index.md#resolvecall)) maps to the constructor, the reference itself denotes the class.

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on enum entry super-type references

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-label-reference-expression/index.html">KtLabelReferenceExpression</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the declaration symbol targeted by the given [`KtLabelReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-label-reference-expression/index.md).

**Example**

```kotlin
fun myAction(action: () -> Unit) {
    action {
        return@action // resolves to the anonymous function
//            ^^^^^^^
    }

    return@main
//        ^^^^^
}
```

Calling `resolveSymbol()` on a [`KtLabelReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-label-reference-expression/index.md) (`@action` and `@main`) returns the corresponding [`KaDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) of the labeled declaration if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on label references

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-return-expression/index.html">KtReturnExpression</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the function symbol targeted by the given [`KtReturnExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-return-expression/index.md).

**Example**

```kotlin
fun foo() {
    return
//  ^^^^^^ resolves to `foo`
}

fun main() {
    listOf(1).forEach label@{
        if (it == 0) return@label
//                   ^^^^^^^^^^^^ resolves to the anonymous function of this lambda
    }
}
```

Calling `resolveSymbol()` on a [`KtReturnExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-return-expression/index.md) (`return` or `return@label`) returns the [`KaFunctionSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md) of the enclosing function (for unlabeled returns) or of the labeled target (for `return@label`) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on return expressions

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.html">KtWhenConditionInRange</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the operator function symbol targeted by the given [`KtWhenConditionInRange`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.md).

**Example**

```kotlin
fun test(x: Int) {
    when (x) {
        in 1..10 -> {}
//      ^^^^^^^^ resolves to a call of `IntRange.contains`

        !in setOf(1, 2, 3) -> {}
//      ^^^^^^^^^^^^^^^^^^ resolves to a call of `Set<Int>.contains`
    }
}
```

Calling `resolveSymbol()` on a [`KtWhenConditionInRange`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.md) (`in 1..10` or `!in setOf(1, 2, 3)`) returns the [`KaNamedFunctionSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.md) of the labeled declaration if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on `in`/`!in` range conditions inside `when` entries

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the callable symbol targeted by the given [`KtDestructuringDeclarationEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.md).

**Example**

```kotlin
data class Point(val x: Int, val y: Int)

fun test(p: Point) {
    val (x, y) = p
//       ^ resolves to `component1`
//          ^ resolves to `component2`
}
```

Calling `resolveSymbol()` on a [`KtDestructuringDeclarationEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.md) returns the [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) of the corresponding `componentN` function (for positional destructuring) or the accessed property (for name-based destructuring) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on destructuring declaration entries

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the callable symbol targeted by the given [`KtQualifiedExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.md).

**Example**

```kotlin
val len = str.length
//        ^________^
```

Calling `resolveSymbol()` on the [`KtQualifiedExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.md) (`str.length`) returns the [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) of `length` if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on qualified expressions

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.html">KtConstructorCalleeExpression</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol referenced by the given [`KtConstructorCalleeExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.md).

**Example**

```kotlin
open class Base(i: Int)

class Derived : Base(1)
//              ^^^^
```

Calling `resolveSymbol()` on the [`KtConstructorCalleeExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.md) (`Base`) returns the [`KaConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) of `Base`'s constructor if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on constructor callee expressions

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-instance-expression-with-label/index.html">KtInstanceExpressionWithLabel</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the declaration symbol referenced by the given [`KtInstanceExpressionWithLabel`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-instance-expression-with-label/index.md).

**Example**

```kotlin
class Foo {
    fun bar() = this
//              ^^^^  resolves to the class `Foo`
}

fun String.ext() = this
//                 ^^^^  resolves to the receiver parameter of `ext`

open class Base {
    open fun baz() {}
}

class Derived : Base() {
    override fun baz() {
        super.baz()
//      ^^^^^  resolves to the class `Base`
    }
}
```

Calling `resolveSymbol()` on a [`KtInstanceExpressionWithLabel`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-instance-expression-with-label/index.md) (`this` or `super`) returns the [`KaDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) of the referenced class, receiver, or other target declaration if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on instance expressions

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-nullable-type/index.html">KtNullableType</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtNullableType`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-nullable-type/index.md).

**Example**

```kotlin
val name: String? = null
//        ^^^^^^^  resolves to `kotlin.String`
```

Resolution unwraps the nullability marker and recurses into the inner type element. The result is the [`KaClassifierSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) of the underlying class, type alias, or type parameter if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or when the inner element has no single classifier).

Unlike [`KtUserType`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-user-type/index.md), a [`KtNullableType`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-nullable-type/index.md) cannot stand for a package qualifier, so the result is always a classifier when present.

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on nullable types

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-function-type/index.html">KtFunctionType</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the synthetic function class symbol referenced by the given [`KtFunctionType`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-function-type/index.md).

**Example**

```kotlin
val a: (Int, String) -> Boolean = TODO()
//     ^^^^^^^^^^^^^^^^^^^^^^^   resolves to `kotlin.Function2`

val b: suspend () -> Unit = TODO()
//     ^^^^^^^^^^^^^^^^^   resolves to `kotlin.coroutines.SuspendFunction0`
```

Returns the [`KaClassSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) of the corresponding `FunctionN`/`SuspendFunctionN` class (the receiver and context parameters count as parameters towards the arity), or `null` if resolution fails.

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on function types

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.html">KtTypeReference</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtTypeReference`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.md).

**Example**

```kotlin
val a: String = ""
//     ^^^^^^  resolves to `kotlin.String`

val b: List<Int>? = null
//     ^^^^^^^^^^  resolves to `kotlin.collections.List`

val c: (Int) -> Int = { it }
//     ^^^^^^^^^^^^  resolves to `kotlin.Function1`
```

Resolution delegates to the inner [`KtTypeReference.typeElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/type-element.md) and returns the underlying [`KaClassifierSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) (a class, type alias, or type parameter), or `null` for type elements that don't denote a single classifier (e.g. `dynamic` and intersection types).

Unlike [`KtUserType`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-user-type/index.md), a [`KtTypeReference`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.md) never stands for the package portion of a qualified path: the inner qualifier chain is built from raw `KtUserType` nodes and is never wrapped in its own type reference, so the result is always a classifier when present.

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on type references

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-literal-expression/index.html">KtClassLiteralExpression</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtClassLiteralExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-literal-expression/index.md) (`Foo::class`).

**Example**

```kotlin
val a = String::class
//      ^^^^^^^^^^^^^   resolves to `kotlin.String`

val b = kotlin.String::class
//      ^^^^^^^^^^^^^^^^^^^^   resolves to `kotlin.String`
```

Resolution delegates to the receiver expression on the left of `::class`. Returns the underlying [`KaClassifierSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) of the referenced class, type alias, or type parameter if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on class literal expressions

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-entry/index.html">KtSuperTypeEntry</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtSuperTypeEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-entry/index.md) (the no-parens form `class Foo : Bar`).

**Example**

```kotlin
class Foo : Runnable
//          ^^^^^^^^  resolves to `java.lang.Runnable`
```

Resolution delegates to the entry's [`KtSuperTypeEntry.getTypeReference`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-list-entry/get-type-reference.md). Returns the underlying [`KaClassifierSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) of the supertype if resolution succeeds; otherwise, it returns `null`.

Companion to [`KtSuperTypeCallEntry.resolveSymbol`](index.md#resolvesymbol), which returns the [`KaConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) for the `class Foo : Bar()` form.

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on supertype entries

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-delegated-super-type-entry/index.html">KtDelegatedSuperTypeEntry</a><span class="p">.</span><a href="index.html#resolvesymbol"><span class="nf">resolveSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtDelegatedSuperTypeEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-delegated-super-type-entry/index.md) (`class Foo : Bar by baz`).

**Example**

```kotlin
class Foo(b: Base) : Base by b
//                   ^^^^      resolves to `Base`
```

Resolution delegates to the entry's [`KtDelegatedSuperTypeEntry.getTypeReference`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-list-entry/get-type-reference.md) — the supertype side of the `by` clause, not the delegate expression. Returns the underlying [`KaClassifierSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) if resolution succeeds; otherwise, it returns `null`.

This is a specialized counterpart of [`KtResolvable.resolveSymbol`](index.md#resolvesymbol) focused specifically on delegated supertype entries

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvable.resolveSymbol`](index.md#resolvesymbol)



</div>

</div>
### resolveSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">.</span><a href="index.html#resolvesymbols"><span class="nf">resolveSymbols</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Resolves symbols for the given [`KtResolvable`](../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md).

Returns all resolved [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md)s if successful; otherwise, an empty list. Might contain multiple symbols for a compound case

In contract to [`resolveCall`](index.md#resolvecall), it could represent any [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md), not only [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md).

In most cases, a not-null result of [`resolveCall`](index.md#resolvecall) will represent the same symbol. The only exceptions are:

 - [`KtNameReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md)


 - [`KtOperationReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-operation-reference-expression/index.md)


 - [`KtEnumEntrySuperclassReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md)


For which the behavior could be different depending on the context.

The main idea is that [`resolveSymbols`](index.md#resolvesymbols) could represent more cases, so it prefers exactly the referenced symbol and not the parent call. For more details, see the mentioned elements.

**See also**



 - [`tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`resolveSymbol`](index.md#resolvesymbol)
 - [`KaSimpleSymbolResolutionSuccess`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-symbol-resolution-success/index.md)



</div>

</div>
### resolveToCall

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="index.html#resolvetocall"><span class="nf">resolveToCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/index.html">KaCallInfo</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md) to a [`KaCallInfo`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/index.md) object. [`KaCallInfo`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/index.md) either contains a successfully resolved call or an error with a list of candidate calls and a diagnostic.

Returns `null` if the element does not correspond to a call.

Consider using the [new resolution API](https://kotlin.github.io/analysis-api/migrating-resolution-api.html).

**See also**



 - [`KtResolvableCall.tryResolveCall`](index.md#tryresolvecall)



</div>

</div>
### resolveToCallCandidates

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="index.html#resolvetocallcandidates"><span class="nf">resolveToCallCandidates</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-candidate-info/index.html">KaCallCandidateInfo</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns all candidates considered during [overload resolution](https://kotlinlang.org/spec/overload-resolution.html) for the call corresponding to this [`KtElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md).

To compare, the [`resolveToCall`](index.md#resolvetocall) function only returns the final result of overload resolution, i.e. the most specific callable passing all compatibility checks.

Consider using the [new resolution API](https://kotlin.github.io/analysis-api/migrating-resolution-api.html).

**See also**



 - [`KtResolvableCall.collectCallCandidates`](index.md#collectcallcandidates)



</div>

</div>
### resolveToSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.html">KtReference</a><span class="p">.</span><a href="index.html#resolvetosymbol"><span class="nf">resolveToSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtReference`](../../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.md) to a symbol.

Returns `null` if the reference cannot be resolved, or resolves to multiple symbols due to being ambiguous.

Consider using the [new resolution API](https://kotlin.github.io/analysis-api/migrating-resolution-api.html).

**See also**



 - [`KtResolvable.tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvableCall.tryResolveCall`](index.md#tryresolvecall)



</div>

</div>
### resolveToSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.html">KtReference</a><span class="p">.</span><a href="index.html#resolvetosymbols"><span class="nf">resolveToSymbols</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtReference`](../../../psi-api/org.jetbrains.kotlin.idea.references/-kt-reference/index.md) to symbols.

Returns an empty collection if the reference cannot be resolved, or multiple symbols if the reference is ambiguous.

Consider using the [new resolution API](https://kotlin.github.io/analysis-api/migrating-resolution-api.html).

**See also**



 - [`KtResolvable.tryResolveSymbols`](index.md#tryresolvesymbols)
 - [`KtResolvableCall.tryResolveCall`](index.md#tryresolvecall)



</div>

</div>
### tryResolveCall

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">.</span><a href="index.html#tryresolvecall"><span class="nf">tryResolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve the call for the given [`KtResolvableCall`](../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md).

**Usage Example:**

```kotlin
fun KaSession.findResolutionDiagnostic(expression: KtCallExpression): KaDiagnostic? {
  val attempt = expression.tryResolveCall() ?: return null
  return attempt.errors.firstOrNull()?.diagnostic
}
```

Returns a [`KaCallResolutionAttempt`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-call-resolution-attempt/index.md), or `null` when there is no call to resolve: the element is not call-shaped, or its reference resolves to something non-callable, such as a qualifier, an import, or a type. Broken code can end up here as well.

A non-null result describes the outcome of an actual resolution. Check it with [`errors`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-compound-symbol-resolution-error/index.md#errors) or [`isSuccessful`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-compound-symbol-resolution-error/index.md#issuccessful) rather than with a type check, which only covers simple attempts. A reported error may carry an empty [`candidateCalls`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call-resolution-error/index.md#candidatecalls) list.

See [References and Calls](https://kotlin.github.io/analysis-api/references-and-calls.html) for a top-level overview.

**See also**



 - [`resolveCall`](index.md#resolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.html">KtForExpression</a><span class="p">.</span><a href="index.html#tryresolvecall"><span class="nf">tryResolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-for-loop-call-resolution-attempt/index.html">KaForLoopCallResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve the given [`KtForExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.md) to a [`KaForLoopCallResolutionAttempt`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-for-loop-call-resolution-attempt/index.md) containing the individual resolution results for each desugared operator call (`iterator`, `hasNext`, `next`).

This is a specialized counterpart of [`KtResolvableCall.tryResolveCall`](index.md#tryresolvecall) focused specifically on `for` loops.

**See also**



 - [`KtForExpression.resolveCall`](index.md#resolvecall)
 - [`KtResolvableCall.tryResolveCall`](index.md#tryresolvecall)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.html">KtPropertyDelegate</a><span class="p">.</span><a href="index.html#tryresolvecall"><span class="nf">tryResolveCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-property-call-resolution-attempt/index.html">KaDelegatedPropertyCallResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve the given [`KtPropertyDelegate`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.md) to a [`KaDelegatedPropertyCallResolutionAttempt`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-property-call-resolution-attempt/index.md) containing the individual resolution results for each desugared operator call (`getValue`, `setValue`, `provideDelegate`).

This is a specialized counterpart of [`KtResolvableCall.tryResolveCall`](index.md#tryresolvecall) focused specifically on delegated properties.

**See also**



 - [`KtPropertyDelegate.resolveCall`](index.md#resolvecall)
 - [`KtResolvableCall.tryResolveCall`](index.md#tryresolvecall)



</div>

</div>
### tryResolveSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">.</span><a href="index.html#tryresolvesymbols"><span class="nf">tryResolveSymbols</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.resolution/-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Attempts to resolve a symbol for the given [`KtResolvable`](../../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md).

**Usage Example:**

```kotlin
fun KaSession.findSymbol(reference: KtNameReferenceExpression): KaSymbol? {
  val attempt = reference.tryResolveSymbols() ?: return null
  return attempt.fold(
    onSuccess = { symbols -> symbols.singleOrNull() },
    onFailure = { errors ->
      val name = reference.getReferencedName()
      errors.forEach { println("Cannot resolve '$name': ${it.diagnostic.defaultMessage}") }
      null
    },
  )
}
```

Returns a [`KaSymbolResolutionAttempt`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-symbol-resolution-attempt/index.md) that describes either success ([`KaSimpleSymbolResolutionSuccess`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-symbol-resolution-success/index.md)) or failure ([`KaSimpleSymbolResolutionError`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-symbol-resolution-error/index.md), or [`KaCompoundSymbolResolutionError`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-compound-symbol-resolution-error/index.md) for a compound call), or `null` when there is nothing to resolve: the element carries no resolvable reference, such as a type reference to a dynamic or intersection type, or the engine has no result for it, which broken code can cause.

A non-null result describes the outcome of an actual resolution. Check it with [`errors`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-compound-symbol-resolution-error/index.md#errors) or [`isSuccessful`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-compound-symbol-resolution-error/index.md#issuccessful) rather than with a type check, which only covers simple attempts. A reported error may carry an empty [`candidateSymbols`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-symbol-resolution-error/index.md#candidatesymbols) list.

In contract to [`tryResolveCall`](index.md#tryresolvecall), it could represent any [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md), not only [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md).

In most cases, a not-null result of [`tryResolveCall`](index.md#tryresolvecall) will represent the same symbol. The only exceptions are:

 - [`KtNameReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md)


 - [`KtOperationReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-operation-reference-expression/index.md)


 - [`KtEnumEntrySuperclassReferenceExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md)


For which the behavior could be different depending on the context.

The main idea is that [`tryResolveSymbols`](index.md#tryresolvesymbols) could represent more cases, so it prefers exactly the referenced symbol and not the parent call. For more details, see the mentioned elements.

See [References and Calls](https://kotlin.github.io/analysis-api/references-and-calls.html) for a top-level overview.

**See also**



 - [`KaSimpleSymbolResolutionSuccess`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-symbol-resolution-success/index.md)
 - [`KaSimpleSymbolResolutionError`](../../org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-symbol-resolution-error/index.md)



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
