---
tags:
 - jvm
title: "getParentOfTypeAndBranch"
---

# getParentOfTypeAndBranch

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="get-parent-of-type-and-branch.html">T</a><span class="o"> : </span>PsiElement<span class="o">> </span>PsiElement<span class="p">.</span><a href="get-parent-of-type-and-branch.html"><span class="nf">getParentOfTypeAndBranch</span></a><span class="p">(</span>strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span><span class="kd">noinline </span>branch<span class="o">: </span><a href="get-parent-of-type-and-branch.html">T</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="get-parent-of-type-and-branch.html">T</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Checks the nearest element of type [`T`](get-parent-of-type-and-branch.md) and returns it if this element lies within the subtree selected by [`branch`](get-parent-of-type-and-branch.md). If that candidate's branch does not contain this element, returns `null` without checking higher ancestors. When [`strict`](get-parent-of-type-and-branch.md) is `false`, this element itself is also considered as the candidate.

### Example:
Given the PSI for:

```kotlin
if (outerCondition) {
    if (innerCondition) {
        handleInner()
    } else {
        handleFallback()
    }
}
```

If `fallbackCall` is the [`KtCallExpression`](../org.jetbrains.kotlin.psi/-kt-call-expression/index.md) for `handleFallback()`, `fallbackCall.getParentOfTypeAndBranch<KtIfExpression> { getThen() }` returns `null`. The nearest [`KtIfExpression`](../org.jetbrains.kotlin.psi/-kt-if-expression/index.md) is the inner one, and `handleFallback()` is in its `else` branch. The search does not continue to the outer `if`, despite the call also being inside the outer `then` branch.


</div>

</div>
