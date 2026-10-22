---
tags:
 - jvm
title: "createUseSiteVisibilityChecker"
---

# createUseSiteVisibilityChecker

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="create-use-site-visibility-checker.html"><span class="nf">createUseSiteVisibilityChecker</span></a><span class="p">(</span>
    useSiteFile<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="p">, </span>
    receiverExpression<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span><span class="p">, </span>
    position<span class="o">: </span>PsiElement
<span class="p">)</span><span class="o">: </span><a href="-ka-use-site-visibility-checker/index.html">KaUseSiteVisibilityChecker</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a visibility checker for the given use-site position.

#### Parameters


 - receiverExpression: The [dispatch receiver](https://kotlin.github.io/analysis-api/receivers.html#types-of-receivers) expression which the candidate symbol is called on, if applicable.




#### See also


 - [`KaUseSiteVisibilityChecker`](-ka-use-site-visibility-checker/index.md)



</div>

</div>
