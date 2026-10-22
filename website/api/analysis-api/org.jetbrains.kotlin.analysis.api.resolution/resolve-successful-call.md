---
tags:
 - jvm
title: "resolveSuccessfulCall"
---

# resolveSuccessfulCall

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.html">KtResolvableCall</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the call for the given [`KtResolvableCall`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable-call/index.md).

### Usage Example:
```kotlin
context(session: KaSession)
fun resolveSymbol(expression: KtCallExpression): KaSymbol? {
  return expression.resolveSuccessfulCall()?.simple?.symbol
}
```

Returns the resolved [`KaSimpleOrMultiCall`](-ka-simple-or-multi-call/index.md) on success; otherwise, `null`

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`collectCallCandidates`](collect-call-candidates.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-annotation-call/index.html">KaAnnotationCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtAnnotationEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.md) to an annotation constructor call.

#### Example
```kotlin
annotation class Anno(val x: Int)

@Anno(42)
fun foo() {}
```

Returns the corresponding [`KaAnnotationCall`](-ka-annotation-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on annotation entries. Use [`collectCallCandidates`](collect-call-candidates.md) to inspect all candidates considered during overload resolution

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.html">KtSuperTypeCallEntry</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtSuperTypeCallEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.md) to a constructor call of the referenced supertype.

#### Example
```kotlin
open class Base(i: Int)

class Derived : Base(1)
//              ^^^^^^^
```

Returns the corresponding [`KaFunctionCall`](-ka-function-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on supertype constructor calls

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtConstructorDelegationCall`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.md) to a delegated constructor call.

#### Example
```kotlin
open class Base(val i: Int)

class Derived : Base {
    constructor() : this(0)
    //              ^^^^^^^

    constructor(x: Int) : super(x)
    //                    ^^^^^^^^
}
```

Returns the corresponding [`KaDelegatedConstructorCall`](-ka-delegated-constructor-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on constructor delegation calls

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.html">KtConstructorDelegationReferenceExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtConstructorDelegationReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.md) to a delegated constructor call.

#### Example
```kotlin
open class Base(val i: Int)

class Derived : Base {
    constructor() : this(0)
    //              ^^^^

    constructor(x: Int) : super(x)
    //                    ^^^^^
}
```

Returns the corresponding [`KaDelegatedConstructorCall`](-ka-delegated-constructor-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on constructor delegation calls

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.html">KtCallElement</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtCallElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.md) to a function call.

#### Example
```kotlin
fun foo(x: Int) {}

fun test() {
    foo(42)
//  ^^^^^^^
}
```

Returns the corresponding [`KaSimpleCall`](-ka-simple-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on call elements

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.html">KtCallableReferenceExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-callable-reference-call/index.html">KaCallableReferenceCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtCallableReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.md) to a callable member call.

#### Example
```kotlin
class A { fun foo() {} }

val ref = A::foo
//        ^^^^^^
```

Returns the corresponding [`KaCallableReferenceCall`](-ka-callable-reference-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on callable reference expressions

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.html">KtArrayAccessExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtArrayAccessExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.md) to a simple function call representing `get`/`set` operator invocation.

#### Example
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

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on array access operations.

<strong>Note</strong>: the `get` call is prefered in the case of a compound assignent

```kotlin
fun test(m: MyMap<String, Int>) {
    m["a"] += 1
//  ^^^^^^
}
```

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.html">KtCollectionLiteralExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtCollectionLiteralExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.md) to a simple function call representing the corresponding array factory invocation.

#### Example
```kotlin
annotation class Anno(val arr: IntArray)

@Anno([1, 2, 3])
//    ^^^^^^^^^ resolves to a call of `intArrayOf`
fun use() {}
```

Returns the corresponding KaSimpleFunctionCall if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on collection literal expressions

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.html">KtEnumEntrySuperclassReferenceExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-delegated-constructor-call/index.html">KaDelegatedConstructorCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtEnumEntrySuperclassReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md) to a delegated constructor call.

#### Example
```kotlin
enum class EnumWithConstructor(val x: Int) {
    Entry(1)
//      ^ resolves to the constructor of `EnumWithConstructor`
}
```

Returns the corresponding [`KaDelegatedConstructorCall`](-ka-delegated-constructor-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on enum entry superclass constructor calls

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.html">KtWhenConditionInRange</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtWhenConditionInRange`](../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.md) to a simple function call representing the corresponding `contains` operator invocation used by the `in`/`!in` branch condition.

#### Example
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

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on `in`/`!in` range conditions inside `when` entries

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtDestructuringDeclarationEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.md) to a call representing the `componentN` invocation (for positional destructuring) or the property access (for name-based destructuring).

#### Example
```kotlin
data class Point(val x: Int, val y: Int)

fun test(p: Point) {
    val (x, y) = p
//       ^ resolves to a call of `component1`
//          ^ resolves to a call of `component2`
}
```

Returns the corresponding [`KaSimpleCall`](-ka-simple-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on destructuring declaration entries

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtQualifiedExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.md) to a call representing the member or extension access.

#### Example
```kotlin
val len = str.length
//        ^________^
```

Calling `resolveSuccessfulCall()` on the [`KtQualifiedExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.md) (`str.length`) returns the corresponding [`KaSimpleCall`](-ka-simple-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on qualified expressions

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.html">KtForExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-for-loop-call/index.html">KaForLoopCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtForExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.md) to a [`KaForLoopCall`](-ka-for-loop-call/index.md) representing the desugared `for` loop.

A `for` loop desugars into three operator calls:

 - `iterator()` on the loop range expression


 - `hasNext()` on the iterator


 - `next()` on the iterator


#### Example
```kotlin
for (item in list) {
    println(item)
}
```

Calling `resolveSuccessfulCall()` on the [`KtForExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-for-expression/index.md) returns a [`KaForLoopCall`](-ka-for-loop-call/index.md) containing the three desugared operator calls if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on `for` loops

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.html">KtPropertyDelegate</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-delegated-property-call/index.html">KaDelegatedPropertyCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtPropertyDelegate`](../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.md) to a [`KaDelegatedPropertyCall`](-ka-delegated-property-call/index.md) representing the desugared delegated property.

A delegated property desugars into up to three operator calls:

 - `getValue()` on the delegate object


 - `setValue()` on the delegate object (only for `var` properties)


 - `provideDelegate()` on the delegate expression (if applicable)


#### Example
```kotlin
val name: String by lazy { "John" }
//               ^________________^
```

Calling `resolveSuccessfulCall()` on the [`KtPropertyDelegate`](../../psi-api/org.jetbrains.kotlin.psi/-kt-property-delegate/index.md) returns a [`KaDelegatedPropertyCall`](-ka-delegated-property-call/index.md) containing the desugared operator calls if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on delegated properties

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.html">KtConstructorCalleeExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtConstructorCalleeExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.md) to a constructor call.

#### Example
```kotlin
open class Base(i: Int)

class Derived : Base(1)
//              ^^^^
```

Returns the corresponding [`KaFunctionCall`](-ka-function-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on constructor callee expressions

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.html">KtNameReferenceExpression</a><span class="p">.</span><a href="resolve-successful-call.html"><span class="nf">resolveSuccessfulCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the given [`KtNameReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md) to a call representing the referenced declaration.

#### Example
```kotlin
fun foo() {}

val x = foo
//      ^^^
```

Calling `resolveSuccessfulCall()` on the [`KtNameReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md) (`foo`) returns the corresponding [`KaSimpleCall`](-ka-simple-call/index.md) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md) focused specifically on name reference expressions

#### See also


 - [`tryResolveCall`](try-resolve-call.md)
 - [`KtResolvableCall.resolveSuccessfulCall`](resolve-successful-call.md)



</div>

</div>
