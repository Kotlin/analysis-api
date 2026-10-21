---
tags:
 - jvm
title: "computeMissingCases"
---

# computeMissingCases

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-when-expression/index.html">KtWhenExpression</a><span class="p">.</span><a href="compute-missing-cases.html"><span class="nf">computeMissingCases</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-ka-when-missing-case/index.html">KaWhenMissingCase</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Computes the missing cases of the given [`KtWhenExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-when-expression/index.md).

The computed missing cases are not affected by the existence or absence of an `else` branch.

#### Example
In the following code, `Direction.WEST` and `Direction.EAST` are missing branches:

```
enum class Direction {
  NORTH, SOUTH, WEST, EAST
}

foo = when(direction) {
  Direction.NORTH -> 1
  Direction.SOUTH -> 2
  else -> 3
}
```

If the [`KtWhenExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-when-expression/index.md) has no subject, then the `else` is reported as missing even if it is explicitly present:

```
fun test() {
    when {
        true -> {}
        else -> {}
    }
}
```


</div>

</div>
