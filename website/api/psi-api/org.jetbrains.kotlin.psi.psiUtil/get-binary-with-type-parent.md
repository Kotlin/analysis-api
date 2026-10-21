---
tags:
 - jvm
title: "getBinaryWithTypeParent"
---

# getBinaryWithTypeParent

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="get-binary-with-type-parent.html"><span class="nf">getBinaryWithTypeParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-binary-expression-with-type-r-h-s/index.html">KtBinaryExpressionWithTypeRHS</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the `as`/`as?` expression whose left-hand side is a call with this expression as its direct child, normally its callee. The call may be the selector of a qualified expression, and the call or qualified expression may be parenthesized. Returns `null` otherwise.

### Example:
Given the PSI for:

```kotlin
val result = (service.load()) as Result
```

Calling this function on the `load` callee reference returns the full `(service.load()) as Result` cast expression. Calling it on the `service` receiver returns `null` because the receiver is not a direct child of the call expression.


</div>

</div>
