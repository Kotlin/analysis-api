---
tags:
 - jvm
title: "parameterIndex"
---

# parameterIndex

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="parameter-index.html"><span class="nf">parameterIndex</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the index of this parameter within its own parameter list (Kotlin or Java), or `-1` if it is not a parameter.

Ordinary parameters and context parameters live in separate lists, each indexed from zero, so the returned index does not correspond to the parameter's position in the JVM method signature or any combined ordering.

### Example:
Given the parameters in:

```kotlin
context(logger: Logger, transaction: Transaction)
fun process(first: String, second: Int) {}
```

`logger.parameterIndex()` and `first.parameterIndex()` both return `0`; `transaction.parameterIndex()` and `second.parameterIndex()` both return `1`.


</div>

</div>
