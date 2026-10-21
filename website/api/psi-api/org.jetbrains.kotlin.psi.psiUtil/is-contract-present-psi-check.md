---
tags:
 - jvm
title: "isContractPresentPsiCheck"
---

# isContractPresentPsiCheck

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-named-function/index.html">KtNamedFunction</a><span class="p">.</span><a href="is-contract-present-psi-check.html"><span class="nf">isContractPresentPsiCheck</span></a><span class="p">(</span>isAllowedOnMembers<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Best-effort PSI check for whether this function's body begins with a `contract { ... }` call, taking into account whether contracts are allowed on member functions via [`isAllowedOnMembers`](is-contract-present-psi-check.md). `false` is definitive; `true` is not a guarantee.

### Example:
```kotlin
@OptIn(kotlin.contracts.ExperimentalContracts::class)
fun declaredContract() {
    kotlin.contracts.contract { returns() }
}

private fun contract() {}

fun sameNameOnly() {
    contract()
}
```

This check returns `true` for both `declaredContract` and `sameNameOnly`: it recognizes the first call by its PSI shape and name without resolving which `contract` function is called.


</div>

</div>
