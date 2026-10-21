---
tags:
 - jvm
title: "allowAnalysisFromWriteAction"
---

# allowAnalysisFromWriteAction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="allow-analysis-from-write-action.html">T</a><span class="o">> </span><a href="allow-analysis-from-write-action.html"><span class="nf">allowAnalysisFromWriteAction</span></a><span class="p">(</span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="allow-analysis-from-write-action.html">T</a><span class="p">)</span><span class="o">: </span><a href="allow-analysis-from-write-action.html">T</a>
</span></code></pre></div>
</div>


<div markdown>

Allows [`analyze`](../org.jetbrains.kotlin.analysis.api.session/analyze.md) to be called from a write action in the given [`action`](allow-analysis-from-write-action.md), which is normally not allowed.

Analysis is not supposed to be called from a write action. Such actions can lead to IDE freezes and incorrect behavior in some cases.

There is no guarantee that PSI changes will be reflected in an Analysis API world inside one [`analyze`](../org.jetbrains.kotlin.analysis.api.session/analyze.md) session. Example:

```
// code to be analyzed
fun foo(): Int = 0

// use case code
fun useCase() {
  analyse(function) {
   // 'getConstantFromExpressionBody' is an imaginary function
   val valueBefore = function.getConstantFromExpressionBody() // valueBefore is 0

   changeExpressionBodyTo(1) // now function will looks like `fun foo(): Int = 1`
   val valueAfter = function.getConstantFromExpressionBody() // Wrong way: valueAfter is not guaranteed to be '1'
  }

  analyse(function) {
   val valueAfter = function.getConstantFromExpressionBody() // OK: valueAfter is guaranteed to be '1'
  }
}
```


</div>

</div>
