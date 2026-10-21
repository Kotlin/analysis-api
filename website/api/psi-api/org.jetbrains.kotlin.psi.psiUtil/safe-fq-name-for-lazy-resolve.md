---
tags:
 - jvm
title: "safeFqNameForLazyResolve"
---

# safeFqNameForLazyResolve

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-named-declaration/index.html">KtNamedDeclaration</a><span class="p">.</span><a href="safe-fq-name-for-lazy-resolve.html"><span class="nf">safeFqNameForLazyResolve</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>FqName<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns this declaration's fully qualified name using the safe name for lazy resolution, or `null` if unavailable.

Missing names of containing classes are replaced with the safe name as well, so the result matches the declaration's ClassId, e.g. `Outer.<no name provided>.Inner`.

Declarations without a ClassId are handled differently:

 - local declarations and everything nested in them have no fully qualified name;


 - enum entries are named using the real names of their containing classes, e.g. `MyEnum.Entry`, or `null` if any containing class has no name. Declarations in enum entry bodies are named after the entry.



</div>

</div>
