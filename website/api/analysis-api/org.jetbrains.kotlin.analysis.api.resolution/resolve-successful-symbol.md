---
tags:
 - jvm
title: "resolveSuccessfulSymbol"
---

# resolveSuccessfulSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.html">KtResolvable</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves a single symbol for the given [`KtResolvable`](../../psi-api/org.jetbrains.kotlin.resolution/-kt-resolvable/index.md).

Returns the [`KaSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) if there is exactly one target; otherwise, `null`

In contract to [`resolveSuccessfulCall`](resolve-successful-call.md), it could represent any [`KaSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md), not only [`KaCallableSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md).

In most cases, a not-null result of [`resolveSuccessfulCall`](resolve-successful-call.md) will represent the same symbol. The only exceptions are:

 - [`KtNameReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md)


 - [`KtOperationReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-operation-reference-expression/index.md)


 - [`KtEnumEntrySuperclassReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md)


For which the behavior could be different depending on the context.

The main idea is that [`resolveSuccessfulSymbol`](resolve-successful-symbol.md) could represent more cases, so it prefers exactly the referenced symbol and not the parent call. For more details, see the mentioned elements.

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`resolveSuccessfulSymbols`](resolve-successful-symbols.md)
 - [`KaSimpleSymbolResolutionSuccess`](-ka-simple-symbol-resolution-success/index.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol of the annotation referenced by the given [`KtAnnotationEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.md).

#### Example
```kotlin
annotation class Anno(val x: Int)

@Anno(42)
fun foo() {}
```

Calling `resolveSuccessfulSymbol()` on the [`KtAnnotationEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-annotation-entry/index.md) (`@Anno(42)`) returns the [`KaConstructorSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) of `Anno`'s annotation constructor if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on annotation entries

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.html">KtSuperTypeCallEntry</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol by the given [`KtSuperTypeCallEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.md).

#### Example
```kotlin
open class Base(i: Int)

class Derived : Base(1)
//              ^^^^^^^
```

Calling `resolveSuccessfulSymbol()` on the [`KtSuperTypeCallEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-call-entry/index.md) (`Base(1)`) returns the [`KaConstructorSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) of `Base`'s constructor if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on supertype constructor calls

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol referenced by the given [`KtConstructorDelegationCall`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.md).

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

Calling `resolveSuccessfulSymbol()` on a [`KtConstructorDelegationCall`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-call/index.md) (either `this(...)` or `super(...)`) returns the [`KaConstructorSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) of the target constructor if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on constructor delegation calls

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.html">KtConstructorDelegationReferenceExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol referenced by the given [`KtConstructorDelegationReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.md).

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

Calling `resolveSuccessfulSymbol()` on a [`KtConstructorDelegationReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-delegation-reference-expression/index.md) (either `this` or `super`) returns the [`KaConstructorSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) of the target constructor if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on constructor delegation calls

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.html">KtCallElement</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the function symbol targeted by the given [`KtCallElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.md).

#### Example
```kotlin
fun foo(x: Int) {}

fun test() {
    foo(42)
//  ^^^^^^^
}
```

Calling `resolveSuccessfulSymbol()` on the [`KtCallElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-call-element/index.md) (`foo(42)`) returns the [`KaFunctionSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md) of `foo` if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on call elements

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.html">KtCallableReferenceExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the callable symbol targeted by the given [`KtCallableReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.md).

#### Example
```kotlin
fun foo(x: Int) {}

val ref = ::foo
//        ^^^^^
```

Calling `resolveSuccessfulSymbol()` on the [`KtCallableReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-callable-reference-expression/index.md) (`::foo`) returns the [`KaCallableSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) of `foo` if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on callable reference expressions

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.html">KtArrayAccessExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the operator function symbol targeted by the given [`KtArrayAccessExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.md).

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

Calling `resolveSuccessfulSymbol()` on a [`KtArrayAccessExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-array-access-expression/index.md) (`a[0]`) returns the [`KaNamedFunctionSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.md) of the corresponding `get`/`set` operator if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on array access operations.

<strong>Note</strong>: the `get` call is prefered in the case of a compound assignent

```kotlin
fun test(m: MyMap<String, Int>) {
    m["a"] += 1
//  ^^^^^^
}
```

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.html">KtCollectionLiteralExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the function symbol targeted by the given [`KtCollectionLiteralExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.md).

#### Example
```kotlin
annotation class Anno(val arr: IntArray)

@Anno([1, 2, 3])
//    ^^^^^^^^^ resolves to the `intArrayOf` function
fun use() {}
```

Calling `resolveSuccessfulSymbol()` on a [`KtCollectionLiteralExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-collection-literal-expression/index.md) (`[1, 2, 3]`) returns the [`KaNamedFunctionSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.md) of the corresponding array factory (e.g., `arrayOf`, `intArrayOf`) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on collection literal expressions

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.html">KtEnumEntrySuperclassReferenceExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the enum class symbol referenced by the given [`KtEnumEntrySuperclassReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md).

#### Example
```kotlin
enum class EnumWithConstructor(val x: Int) {
    Entry(1)
//      ^ resolves to the enum class `EnumWithConstructor`
}
```

Calling `resolveSuccessfulSymbol()` on a [`KtEnumEntrySuperclassReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry-superclass-reference-expression/index.md) returns the [`KaNamedClassSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.md) of the enclosing enum class if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

Mirrors how [`KtNameReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-name-reference-expression/index.md) prefers the class over the constructor: while the surrounding super-type call ([`resolveSuccessfulCall`](resolve-successful-call.md)) maps to the constructor, the reference itself denotes the class.

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on enum entry super-type references

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-label-reference-expression/index.html">KtLabelReferenceExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the declaration symbol targeted by the given [`KtLabelReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-label-reference-expression/index.md).

#### Example
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

Calling `resolveSuccessfulSymbol()` on a [`KtLabelReferenceExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-label-reference-expression/index.md) (`@action` and `@main`) returns the corresponding [`KaDeclarationSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) of the labeled declaration if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on label references

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-return-expression/index.html">KtReturnExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the function symbol targeted by the given [`KtReturnExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-return-expression/index.md).

#### Example
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

Calling `resolveSuccessfulSymbol()` on a [`KtReturnExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-return-expression/index.md) (`return` or `return@label`) returns the [`KaFunctionSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md) of the enclosing function (for unlabeled returns) or of the labeled target (for `return@label`) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on return expressions

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.html">KtWhenConditionInRange</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the operator function symbol targeted by the given [`KtWhenConditionInRange`](../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.md).

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

Calling `resolveSuccessfulSymbol()` on a [`KtWhenConditionInRange`](../../psi-api/org.jetbrains.kotlin.psi/-kt-when-condition-in-range/index.md) (`in 1..10` or `!in setOf(1, 2, 3)`) returns the [`KaNamedFunctionSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.md) of the labeled declaration if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on `in`/`!in` range conditions inside `when` entries

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the callable symbol targeted by the given [`KtDestructuringDeclarationEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.md).

#### Example
```kotlin
data class Point(val x: Int, val y: Int)

fun test(p: Point) {
    val (x, y) = p
//       ^ resolves to `component1`
//          ^ resolves to `component2`
}
```

Calling `resolveSuccessfulSymbol()` on a [`KtDestructuringDeclarationEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.md) returns the [`KaCallableSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) of the corresponding `componentN` function (for positional destructuring) or the accessed property (for name-based destructuring) if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on destructuring declaration entries

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the callable symbol targeted by the given [`KtQualifiedExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.md).

#### Example
```kotlin
val len = str.length
//        ^________^
```

Calling `resolveSuccessfulSymbol()` on the [`KtQualifiedExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-qualified-expression/index.md) (`str.length`) returns the [`KaCallableSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) of `length` if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on qualified expressions

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.html">KtConstructorCalleeExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the constructor symbol referenced by the given [`KtConstructorCalleeExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.md).

#### Example
```kotlin
open class Base(i: Int)

class Derived : Base(1)
//              ^^^^
```

Calling `resolveSuccessfulSymbol()` on the [`KtConstructorCalleeExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor-callee-expression/index.md) (`Base`) returns the [`KaConstructorSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) of `Base`'s constructor if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on constructor callee expressions

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-instance-expression-with-label/index.html">KtInstanceExpressionWithLabel</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the declaration symbol referenced by the given [`KtInstanceExpressionWithLabel`](../../psi-api/org.jetbrains.kotlin.psi/-kt-instance-expression-with-label/index.md).

#### Example
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

Calling `resolveSuccessfulSymbol()` on a [`KtInstanceExpressionWithLabel`](../../psi-api/org.jetbrains.kotlin.psi/-kt-instance-expression-with-label/index.md) (`this` or `super`) returns the [`KaDeclarationSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) of the referenced class, receiver, or other target declaration if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on instance expressions

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-nullable-type/index.html">KtNullableType</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtNullableType`](../../psi-api/org.jetbrains.kotlin.psi/-kt-nullable-type/index.md).

#### Example
```kotlin
val name: String? = null
//        ^^^^^^^  resolves to `kotlin.String`
```

Resolution unwraps the nullability marker and recurses into the inner type element. The result is the [`KaClassifierSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) of the underlying class, type alias, or type parameter if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or when the inner element has no single classifier).

Unlike [`KtUserType`](../../psi-api/org.jetbrains.kotlin.psi/-kt-user-type/index.md), a [`KtNullableType`](../../psi-api/org.jetbrains.kotlin.psi/-kt-nullable-type/index.md) cannot stand for a package qualifier, so the result is always a classifier when present.

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on nullable types

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-function-type/index.html">KtFunctionType</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the synthetic function class symbol referenced by the given [`KtFunctionType`](../../psi-api/org.jetbrains.kotlin.psi/-kt-function-type/index.md).

#### Example
```kotlin
val a: (Int, String) -> Boolean = TODO()
//     ^^^^^^^^^^^^^^^^^^^^^^^   resolves to `kotlin.Function2`

val b: suspend () -> Unit = TODO()
//     ^^^^^^^^^^^^^^^^^   resolves to `kotlin.coroutines.SuspendFunction0`
```

Returns the [`KaClassSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) of the corresponding `FunctionN`/`SuspendFunctionN` class (the receiver and context parameters count as parameters towards the arity), or `null` if resolution fails.

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on function types

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.html">KtTypeReference</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtTypeReference`](../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.md).

#### Example
```kotlin
val a: String = ""
//     ^^^^^^  resolves to `kotlin.String`

val b: List<Int>? = null
//     ^^^^^^^^^^  resolves to `kotlin.collections.List`

val c: (Int) -> Int = { it }
//     ^^^^^^^^^^^^  resolves to `kotlin.Function1`
```

Resolution delegates to the inner [`KtTypeReference.typeElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/type-element.md) and returns the underlying [`KaClassifierSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) (a class, type alias, or type parameter), or `null` for type elements that don't denote a single classifier (e.g. `dynamic` and intersection types).

Unlike [`KtUserType`](../../psi-api/org.jetbrains.kotlin.psi/-kt-user-type/index.md), a [`KtTypeReference`](../../psi-api/org.jetbrains.kotlin.psi/-kt-type-reference/index.md) never stands for the package portion of a qualified path: the inner qualifier chain is built from raw `KtUserType` nodes and is never wrapped in its own type reference, so the result is always a classifier when present.

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on type references

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-class-literal-expression/index.html">KtClassLiteralExpression</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtClassLiteralExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-class-literal-expression/index.md) (`Foo::class`).

#### Example
```kotlin
val a = String::class
//      ^^^^^^^^^^^^^   resolves to `kotlin.String`

val b = kotlin.String::class
//      ^^^^^^^^^^^^^^^^^^^^   resolves to `kotlin.String`
```

Resolution delegates to the receiver expression on the left of `::class`. Returns the underlying [`KaClassifierSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) of the referenced class, type alias, or type parameter if resolution succeeds; otherwise, it returns `null` (e.g., when unresolved or ambiguous).

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on class literal expressions

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-entry/index.html">KtSuperTypeEntry</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtSuperTypeEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-entry/index.md) (the no-parens form `class Foo : Bar`).

#### Example
```kotlin
class Foo : Runnable
//          ^^^^^^^^  resolves to `java.lang.Runnable`
```

Resolution delegates to the entry's [`KtSuperTypeEntry.getTypeReference`](../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-list-entry/get-type-reference.md). Returns the underlying [`KaClassifierSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) of the supertype if resolution succeeds; otherwise, it returns `null`.

Companion to [`KtSuperTypeCallEntry.resolveSuccessfulSymbol`](resolve-successful-symbol.md), which returns the [`KaConstructorSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) for the `class Foo : Bar()` form.

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on supertype entries

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-delegated-super-type-entry/index.html">KtDelegatedSuperTypeEntry</a><span class="p">.</span><a href="resolve-successful-symbol.html"><span class="nf">resolveSuccessfulSymbol</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves the classifier symbol referenced by the given [`KtDelegatedSuperTypeEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-delegated-super-type-entry/index.md) (`class Foo : Bar by baz`).

#### Example
```kotlin
class Foo(b: Base) : Base by b
//                   ^^^^      resolves to `Base`
```

Resolution delegates to the entry's [`KtDelegatedSuperTypeEntry.getTypeReference`](../../psi-api/org.jetbrains.kotlin.psi/-kt-super-type-list-entry/get-type-reference.md) — the supertype side of the `by` clause, not the delegate expression. Returns the underlying [`KaClassifierSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md) if resolution succeeds; otherwise, it returns `null`.

This is a specialized counterpart of [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md) focused specifically on delegated supertype entries

#### See also


 - [`tryResolveSymbols`](try-resolve-symbols.md)
 - [`KtResolvable.resolveSuccessfulSymbol`](resolve-successful-symbol.md)



</div>

</div>
