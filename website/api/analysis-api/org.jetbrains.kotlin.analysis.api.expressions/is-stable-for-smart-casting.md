---
tags:
 - jvm
title: "isStableForSmartCasting"
---

# isStableForSmartCasting

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="is-stable-for-smart-casting.html">isStableForSmartCasting</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
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

#### Example
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
