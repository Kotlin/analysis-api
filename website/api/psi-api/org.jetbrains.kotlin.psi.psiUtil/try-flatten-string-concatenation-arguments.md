---
tags:
 - jvm
title: "tryFlattenStringConcatenationArguments"
---

# tryFlattenStringConcatenationArguments

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-binary-expression/index.html">KtBinaryExpression</a><span class="p">.</span><a href="try-flatten-string-concatenation-arguments.html"><span class="nf">tryFlattenStringConcatenationArguments</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi/-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the string-template arguments of this expression if it is a string-literal concatenation; otherwise, returns `null`.

For example, for `"a0" /* comment before plus */ + /* comment after plus */ "a1"`, this returns `"a0"` and `"a1"`.

#### See also


 - [`tryFlattenStringConcatenation`](../../psi-api/org.jetbrains.kotlin.psi.psiUtil/index.md)



</div>

</div>
