---
tags:
 - jvm
title: "ImportContent"
---

# ImportContent

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="index.html">ImportContent</a>
</span></code></pre></div>The imported reference, either as a resolved fully qualified name or as the raw reference expression.

#### Inheritors


 - [`ExpressionBased`](-expression-based/index.md)
 - [`FqNameBased`](-fq-name-based/index.md)



</div>

## Types
### [`ExpressionBased`](-expression-based/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-expression-based/index.html">ExpressionBased</a><span class="p">(</span><span class="kd">val </span>expression<span class="o">: </span><a href="../../-kt-expression/index.html">KtExpression</a><span class="p">)</span> : <a href="index.html">KtImportInfo.ImportContent</a>
</span></code></pre></div>
</div>


<div markdown>

The import is described by a reference [`expression`](-expression-based/index.md#expression) (the PSI-backed form).


</div>

</div>
### [`FqNameBased`](-fq-name-based/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-fq-name-based/index.html">FqNameBased</a><span class="p">(</span><span class="kd">val </span>fqName<span class="o">: </span>FqName<span class="p">)</span> : <a href="index.html">KtImportInfo.ImportContent</a>
</span></code></pre></div>
</div>


<div markdown>

The import is described directly by a [`fqName`](-fq-name-based/index.md#fqname) (the stub-backed form).


</div>

</div>
