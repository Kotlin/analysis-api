---
tags:
 - jvm
title: "KtPsiInconsistencyHandling"
---

# KtPsiInconsistencyHandling

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a>
<span class="kd">annotation class </span><a href="index.html">KtPsiInconsistencyHandling</a>
</span></code></pre></div>Functions and classes annotated with [`KtPsiInconsistencyHandling`](index.md) are not intended for general-purpose use, but for working with possibly inconsistent PSI. The specific circumstances need to be described in the documentation of the annotated function/class.

Inconsistent PSI cannot be produced by the Kotlin parser. It occurs rarely, for example during modification of the PSI by the IDE. In general, it can be assumed that all PSI is consistent. Inconsistent PSI should only be assumed when there is sufficient proof.


</div>

