---
tags:
 - jvm
title: "contentRange"
---

# contentRange

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-block-expression/index.html">KtBlockExpression</a><span class="p">.</span><a href="content-range.html"><span class="nf">contentRange</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-psi-child-range/index.html">PsiChildRange</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the range of direct PSI children between this block's braces after excluding outer whitespace. The range may contain comments and other non-statement elements. Returns an empty range if either brace is missing or no non-whitespace content remains.


</div>

</div>
