---
tags:
 - jvm
title: "KaDelegatedConstructorCall"
---

# KaDelegatedConstructorCall

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaDelegatedConstructorCall</a> : <a href="../-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">> </span>
</span></code></pre></div>A call to another constructor within the same class, or to a superclass constructor. This corresponds to the use of `this(...)` or `super(...)` within a constructor's body to delegate initialization to another constructor.

#### Example
```kotlin
open class SuperClass(i: Int)

class SubClass1 : SuperClass(1)      // a call to the constructor of `SuperClass` with a single argument `1`

class SubClass2 : SuperClass {
  constructor(i: Int) : super(i) {}  // a call to the constructor of `SuperClass` with a single argument `i`
  constructor() : this(2) {}         // a call to the constructor of `SubClass2` with a single argument `2`
}
```


</div>

## Types
### [`Kind`](-kind/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-kind/index.html">Kind</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-kind/index.html">KaDelegatedConstructorCall.Kind</a><span class="o">> </span>
</span></code></pre></div>
</div>

</div>
## Properties
### calls

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-call-info/index.html">KaCallInfo</a><span class="p">.</span><a href="../-ka-for-loop-call/index.html#calls">calls</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-call/index.html">KaCall</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The list of [`KaCall`](../-ka-call/index.md)s associated with the [`KaCallInfo`](../-ka-call-info/index.md). The list contains a single [`KaCall`](../-ka-call/index.md) in case of a [`successful call`](../-ka-success-call-info/index.md), but may contain multiple candidates in case of an [`error call`](../-ka-error-call-info/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-array-access-call-resolution-attempt/index.html#calls">calls</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The flattened list of resolved calls.

 - [`KaSimpleCallResolutionSuccess`](../-ka-simple-call-resolution-success/index.md): the resolved [`call`](../-ka-simple-call-resolution-success/index.md#call) as a single-element list.


 - [`KaSimpleCallResolutionError`](../-ka-simple-call-resolution-error/index.md): the [`candidate calls`](../-ka-simple-call-resolution-error/index.md#candidatecalls).


 - [`KaMultiCallResolutionAttempt`](../-ka-multi-call-resolution-attempt/index.md): the assembled [`call`](../-ka-multi-call-resolution-attempt/index.md#call) if all sub-calls succeeded, or the combined calls from individual [`simpleAttempts`](../-ka-compound-array-access-call-resolution-attempt/index.md#simpleattempts) otherwise.



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="p">.</span><a href="../-ka-for-loop-call/index.html#calls">calls</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The flattened list of [`KaSimpleCall`](../-ka-simple-call/index.md)s.

 - If [`this`](../-ka-simple-or-multi-call/index.md) is an instance of [`KaSimpleCall`](../-ka-simple-call/index.md), the list will contain only [`this`](../-ka-simple-or-multi-call/index.md) call


 - If [`this`](../-ka-simple-or-multi-call/index.md) is an instance of [`KaMultiCall`](../-ka-multi-call/index.md), the list will contain [`KaMultiCall.calls`](../-ka-for-loop-call/index.md#calls)



</div>

</div>
### combinedArgumentMapping

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#combinedargumentmapping">combinedArgumentMapping</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-variable-signature/index.html">KaVariableSignature</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-parameter-symbol/index.html">KaParameterSymbol</a><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A combined mapping from the call's argument expressions to their associated parameter symbols in a stable order. This includes both [`value arguments`](index.md#valueargumentmapping) and [`context arguments`](index.md#contextargumentmapping).

In case of `vararg` parameters, multiple arguments may be mapped to the same [`KaValueParameterSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.md).

**See also**



 - [`valueArgumentMapping`](index.md#valueargumentmapping)
 - [`contextArgumentMapping`](index.md#contextargumentmapping)



</div>

</div>
### constructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="p">.</span><a href="../-ka-for-loop-call/index.html#constructor">constructor</a><span class="o">: </span><a href="../-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

[`this`](../-ka-simple-or-multi-call/index.md) call as a call to a [`constructor`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md), or `null` if it is not a constructor call.

**Example**

```kotlin
annotation class Anno

class Foo

@Anno
fun usage() {
   Foo()
}
```

Both the `Foo()` call and the `@Anno` annotation entry are constructor calls, so [`constructor`](../-ka-for-loop-call/index.md#constructor) returns the call itself.

**See also**



 - [`KaConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md)
 - [`function`](../-ka-for-loop-call/index.md#function)



</div>

</div>
### contextArgumentMapping

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#contextargumentmapping">contextArgumentMapping</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-variable-signature/index.html">KaVariableSignature</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-context-parameter-symbol/index.html">KaContextParameterSymbol</a><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A mapping from the call's [explicit context argument](https://github.com/Kotlin/KEEP/blob/main/proposals/KEEP-0448-explicit-context-arguments.md) expressions to their associated context parameter symbols in a stable order.

**Example**

```kotlin
context(a: A, b: B)
fun foo() { ... }

fun test() {
    with(A()) {
        foo(b = B())  // explicit context argument `b = B()`
    }
}
```

For the `foo(b = B())` call, `contextArgumentMapping` contains a single entry mapping the `B()` expression to the context parameter `b: B`.

**See also**



 - [`valueArgumentMapping`](index.md#valueargumentmapping)
 - [`combinedArgumentMapping`](index.md#combinedargumentmapping)



</div>

</div>
### contextArguments

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-simple-call/index.html#contextarguments">contextArguments</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-receiver-value/index.html">KaReceiverValue</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The list of [context parameters](https://github.com/Kotlin/KEEP/issues/367) for this symbol access. The list is available if the callable is declared with context parameters.


</div>

</div>
### dispatchReceiver

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-simple-call/index.html#dispatchreceiver">dispatchReceiver</a><span class="o">: </span><a href="../-ka-receiver-value/index.html">KaReceiverValue</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [dispatch receiver](https://kotlin.github.io/analysis-api/receivers.html#types-of-receivers) for this symbol access. A dispatch receiver is available if the callable is declared inside a class or object.


</div>

</div>
### extensionReceiver

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-simple-call/index.html#extensionreceiver">extensionReceiver</a><span class="o">: </span><a href="../-ka-receiver-value/index.html">KaReceiverValue</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [extension receiver](https://kotlin.github.io/analysis-api/receivers.html#types-of-receivers) for this symbol access. An extension receiver is available if the callable is declared with an extension receiver.


</div>

</div>
### function

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="p">.</span><a href="../-ka-for-loop-call/index.html#function">function</a><span class="o">: </span><a href="../-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

[`this`](../-ka-simple-or-multi-call/index.md) call as a [`KaFunctionCall`](../-ka-function-call/index.md), or `null` if it is not a call to a function.

**Example**

```kotlin
class Foo {
   fun function() {}
   var int: Int = 1
}

fun Foo.usage() {
   function()
   int
}
```

For `function()`, [`function`](../-ka-for-loop-call/index.md#function) is the call to `function`. For `int`, which is a [`KaVariableAccessCall`](../-ka-variable-access-call/index.md), [`function`](../-ka-for-loop-call/index.md#function) is `null`.

**See also**



 - [`KaFunctionCall`](../-ka-function-call/index.md)
 - [`variable`](../-ka-for-loop-call/index.md#variable)



</div>

</div>
### kind

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#kind">kind</a><span class="o">: </span><a href="-kind/index.html">KaDelegatedConstructorCall.Kind</a>
</span></code></pre></div>
</div>


<div markdown>

Determines whether the constructor call is a [``super(...)``](-kind/-s-u-p-e-r_-c-a-l-l/index.md) call or a [``this(...)``](-kind/-t-h-i-s_-c-a-l-l/index.md) call.


</div>

</div>
### signature

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-simple-call/index.html#signature">signature</a><span class="o">: </span><a href="../-ka-simple-call/index.html">C</a>
</span></code></pre></div>
</div>


<div markdown>

The function or variable declaration.


</div>

</div>
### simple

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="p">.</span><a href="../-ka-for-loop-call/index.html#simple">simple</a><span class="o">: </span><a href="../-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

[`this`](../-ka-simple-or-multi-call/index.md) call as a [`KaSimpleCall`](../-ka-simple-call/index.md), or `null` if it is a [`KaMultiCall`](../-ka-multi-call/index.md).

**Example**

```kotlin
var int: Int = 1

fun usage() {
   int = 2
   int++
}
```

For `int = 2`, [`simple`](../-ka-for-loop-call/index.md#simple) is the write access to `int`. For `int++`, which is a [`KaMultiCall`](../-ka-multi-call/index.md), [`simple`](../-ka-for-loop-call/index.md#simple) is `null`.

**See also**



 - [`KaSimpleCall`](../-ka-simple-call/index.md)



</div>

</div>
### symbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><span class="o"><</span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">, </span><a href="../-ka-partially-applied-symbol/index.html#symbol">C</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a><span class="o">></span><span class="o">> </span><a href="../-ka-callable-member-call/index.html">KaCallableMemberCall</a><span class="o"><</span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a><span class="p">, </span><a href="../-ka-partially-applied-symbol/index.html#symbol">C</a><span class="o">></span><span class="p">.</span><a href="../-ka-partially-applied-symbol/index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) of the [`KaCallableMemberCall`](../-ka-callable-member-call/index.md)'s callee.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><span class="o"><</span><a href="../-ka-simple-call/index.html#symbol">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">, </span><a href="../-ka-simple-call/index.html#symbol">C</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="../-ka-simple-call/index.html#symbol">S</a><span class="o">></span><span class="o">> </span><a href="../-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><a href="../-ka-simple-call/index.html#symbol">S</a><span class="p">, </span><a href="../-ka-simple-call/index.html#symbol">C</a><span class="o">></span><span class="p">.</span><a href="../-ka-simple-call/index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-simple-call/index.html#symbol">S</a>
</span></code></pre></div>
</div>


<div markdown>

The resolved [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) of the [`KaSimpleCall`](../-ka-simple-call/index.md).

This is a short-cut for [`KaCallableSignature.symbol`](../../org.jetbrains.kotlin.analysis.api.signatures/-ka-variable-signature/index.md#symbol).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><span class="o"><</span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">, </span><a href="../-ka-partially-applied-symbol/index.html#symbol">C</a><span class="o"> : </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a><span class="o">></span><span class="o">> </span><a href="../-ka-partially-applied-symbol/index.html">KaPartiallyAppliedSymbol</a><span class="o"><</span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a><span class="p">, </span><a href="../-ka-partially-applied-symbol/index.html#symbol">C</a><span class="o">></span><span class="p">.</span><a href="../-ka-partially-applied-symbol/index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-partially-applied-symbol/index.html#symbol">S</a>
</span></code></pre></div>
</div>


<div markdown>

The [`callable symbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) which the [`KaPartiallyAppliedSymbol`](../-ka-partially-applied-symbol/index.md) represents. While the information contained in a partially applied symbol is not exhaustive (e.g. applied functions are missing value arguments), the symbol of the callable which is called is definite.


</div>

</div>
### symbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#symbols">symbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The flattened list of [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md)s for the resolved calls.

 - If [`this`](../-ka-simple-or-multi-call/index.md) is an instance of [`KaSimpleCall`](../-ka-simple-call/index.md), the list will contain only the [`KaSimpleCall.signature`](../-ka-simple-call/index.md#signature)'s symbol


 - If [`this`](../-ka-simple-or-multi-call/index.md) is an instance of [`KaMultiCall`](../-ka-multi-call/index.md), the list will contain symbols from all [`KaMultiCall.calls`](../-ka-for-loop-call/index.md#calls)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-symbol-resolution-attempt/index.html">KaSymbolResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#symbols">symbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md).

 - If [`this`](../-ka-symbol-resolution-attempt/index.md) is an instance of [`KaSimpleSymbolResolutionSuccess`](../-ka-simple-symbol-resolution-success/index.md), the list will contain [`KaSimpleSymbolResolutionSuccess.symbols`](../-ka-simple-symbol-resolution-success/index.md#symbols).


 - If [`this`](../-ka-symbol-resolution-attempt/index.md) is an instance of [`KaSimpleSymbolResolutionError`](../-ka-simple-symbol-resolution-error/index.md), the list will contain [`KaSimpleSymbolResolutionError.candidateSymbols`](../-ka-simple-symbol-resolution-error/index.md#candidatesymbols).


 - If [`this`](../-ka-symbol-resolution-attempt/index.md) is an instance of [`KaCompoundSymbolResolutionError`](../-ka-compound-symbol-resolution-error/index.md), the list will contain the combined symbols from all attempts.


**See also**



 - [`KaResolver.tryResolveSymbols`](../../org.jetbrains.kotlin.analysis.api.components/-ka-resolver/index.md#tryresolvesymbols)



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
### typeArgumentsMapping

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-simple-call/index.html#typeargumentsmapping">typeArgumentsMapping</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A map of inferred type arguments. If type placeholders were used, the actual inferred type will be used as a value. The keys for this map are from [`signature`](../-ka-simple-call/index.md#signature)'s type parameters.

In case of a resolution or inference error, the map might be empty.


</div>

</div>
### valueArgumentMapping

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#valueargumentmapping">valueArgumentMapping</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-variable-signature/index.html">KaVariableSignature</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.html">KaValueParameterSymbol</a><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A mapping from the call's argument expressions to their associated parameter symbols in a stable order. In case of `vararg` parameters, multiple arguments may be mapped to the same [`KaValueParameterSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.md).

**See also**



 - [`contextArgumentMapping`](index.md#contextargumentmapping)
 - [`combinedArgumentMapping`](index.md#combinedargumentmapping)



</div>

</div>
### variable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-simple-or-multi-call/index.html">KaSimpleOrMultiCall</a><span class="p">.</span><a href="../-ka-for-loop-call/index.html#variable">variable</a><span class="o">: </span><a href="../-ka-variable-access-call/index.html">KaVariableAccessCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

[`this`](../-ka-simple-or-multi-call/index.md) call as a [`KaVariableAccessCall`](../-ka-variable-access-call/index.md), or `null` if it is not an access to a variable.

**Example**

```kotlin
class Foo {
   fun function() {}
   var int: Int = 1
}

fun Foo.usage() {
   int
   function()
}
```

For `int`, [`variable`](../-ka-for-loop-call/index.md#variable) is the read access to `int`. For `function()`, which is a [`KaFunctionCall`](../-ka-function-call/index.md), [`variable`](../-ka-for-loop-call/index.md#variable) is `null`.

**See also**



 - [`KaVariableAccessCall`](../-ka-variable-access-call/index.md)
 - [`function`](../-ka-for-loop-call/index.md#function)



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
