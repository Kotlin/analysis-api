---
tags:
 - jvm
title: "isLegacyContractPresentPsiCheck"
---

# isLegacyContractPresentPsiCheck

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration-with-body/index.html">KtDeclarationWithBody</a><span class="p">.</span><a href="is-legacy-contract-present-psi-check.html"><span class="nf">isLegacyContractPresentPsiCheck</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the declaration may have a legacy contract (a contract defined inside the body).

In other words, <strong>false</strong> guarantees that the declaration cannot have a contract, but <strong>true</strong> does not guarantee that the declaration has a contract.


</div>

</div>
