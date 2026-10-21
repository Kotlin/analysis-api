---
tags:
 - jvm
title: "KaSimpleOrMultiCall"
---

# KaSimpleOrMultiCall

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">KaSimpleOrMultiCall</a> : <a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>Represents a resolved call that can be either a simple call or a multi call.

It can be either a [`KaSimpleCall`](../-ka-simple-call/index.md) or a [`KaMultiCall`](../-ka-multi-call/index.md).

### Example
```kotlin
class Foo {
   fun function() {}
   var int: Int = 1
}

fun Foo.usage() {
   function()
   int++
}
```

`function()` call will be represented as a [`KaSimpleCall`](../-ka-simple-call/index.md) (the target is the function), and `int++` call as a [`KaMultiCall`](../-ka-multi-call/index.md) (with two targets: the `int` property and the `++` operator function)

#### See also


 - [`KaSimpleCall`](../-ka-simple-call/index.md)
 - [`KaMultiCall`](../-ka-multi-call/index.md)


#### Inheritors


 - [`KaSimpleCall`](../-ka-simple-call/index.md)
 - [`KaMultiCall`](../-ka-multi-call/index.md)



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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-call-resolution-attempt/index.html">KaCallResolutionAttempt</a><span class="p">.</span><a href="../-ka-compound-array-access-call-resolution-attempt/index.html#calls">calls</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">KaSimpleOrMultiCall</a><span class="o">></span>
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

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html">KaSimpleOrMultiCall</a><span class="p">.</span><a href="../-ka-for-loop-call/index.html#calls">calls</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The flattened list of [`KaSimpleCall`](../-ka-simple-call/index.md)s.

 - If [`this`](index.md) is an instance of [`KaSimpleCall`](../-ka-simple-call/index.md), the list will contain only [`this`](index.md) call


 - If [`this`](index.md) is an instance of [`KaMultiCall`](../-ka-multi-call/index.md), the list will contain [`KaMultiCall.calls`](../-ka-for-loop-call/index.md#calls)



</div>

</div>
### constructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html">KaSimpleOrMultiCall</a><span class="p">.</span><a href="../-ka-for-loop-call/index.html#constructor">constructor</a><span class="o">: </span><a href="../-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

[`this`](index.md) call as a call to a [`constructor`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md), or `null` if it is not a constructor call.

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
### function

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html">KaSimpleOrMultiCall</a><span class="p">.</span><a href="../-ka-for-loop-call/index.html#function">function</a><span class="o">: </span><a href="../-ka-function-call/index.html">KaFunctionCall</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

[`this`](index.md) call as a [`KaFunctionCall`](../-ka-function-call/index.md), or `null` if it is not a call to a function.

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
### simple

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html">KaSimpleOrMultiCall</a><span class="p">.</span><a href="../-ka-for-loop-call/index.html#simple">simple</a><span class="o">: </span><a href="../-ka-simple-call/index.html">KaSimpleCall</a><span class="o"><</span><span class="o">*</span><span class="p">, </span><span class="o">*</span><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

[`this`](index.md) call as a [`KaSimpleCall`](../-ka-simple-call/index.md), or `null` if it is a [`KaMultiCall`](../-ka-multi-call/index.md).

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
### symbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html">KaSimpleOrMultiCall</a><span class="p">.</span><a href="../-ka-compound-symbol-resolution-error/index.html#symbols">symbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The flattened list of [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md)s for the resolved calls.

 - If [`this`](index.md) is an instance of [`KaSimpleCall`](../-ka-simple-call/index.md), the list will contain only the [`KaSimpleCall.signature`](../-ka-simple-call/index.md#signature)'s symbol


 - If [`this`](index.md) is an instance of [`KaMultiCall`](../-ka-multi-call/index.md), the list will contain symbols from all [`KaMultiCall.calls`](../-ka-for-loop-call/index.md#calls)



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
### variable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html">KaSimpleOrMultiCall</a><span class="p">.</span><a href="../-ka-for-loop-call/index.html#variable">variable</a><span class="o">: </span><a href="../-ka-variable-access-call/index.html">KaVariableAccessCall</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

[`this`](index.md) call as a [`KaVariableAccessCall`](../-ka-variable-access-call/index.md), or `null` if it is not an access to a variable.

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
