---
tags:
 - jvm
title: "findLabelAndCall"
---

# findLabelAndCall

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-function-literal/index.html">KtFunctionLiteral</a><span class="p">.</span><a href="find-label-and-call.html"><span class="nf">findLabelAndCall</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/index.html">Pair</a><span class="o"><</span>Name<span class="o">?</span><span class="p">, </span><a href="../org.jetbrains.kotlin.psi/-kt-call-expression/index.html">KtCallExpression</a><span class="o">?</span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the label (explicit or the enclosing call's name) and the call that this lambda is passed to, as a pair. Either component may be `null` if it cannot be determined.

### Example:
```kotlin
items.forEach { println(it) }
items.forEach itemLoop@ { println(it) }
val standalone = { println("done") }
```

For the first function literal, this returns the inferred label `forEach` and its call. For the explicitly labeled literal, it returns `itemLoop` and the call. For the literal assigned to `standalone`, it returns `(null, null)`.


</div>

</div>
