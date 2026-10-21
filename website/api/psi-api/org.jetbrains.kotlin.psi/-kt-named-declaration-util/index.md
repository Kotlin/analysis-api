---
tags:
 - jvm
title: "KtNamedDeclarationUtil"
---

# KtNamedDeclarationUtil

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KtNamedDeclarationUtil</a>
</span></code></pre></div>Static helpers for computing fully qualified names of [`KtNamedDeclaration`](../-kt-named-declaration/index.md)s from their PSI structure. 

Prefer [`getFqName`](../-kt-function-not-stubbed/index.md#getfqname) in client code; these helpers back that computation by walking the enclosing declarations and package directive.


</div>

## Companion functions
### getParentFqName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getparentfqname"><span class="nf">getParentFqName</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> namedDeclaration<span class="o">: </span><a href="../-kt-named-declaration/index.html">KtNamedDeclaration</a><span class="p">)</span><span class="o">: </span>FqName
</span></code></pre></div>
</div>


<div markdown>

Returns the fully qualified name of the element that lexically encloses the given `#!java namedDeclaration` — its package for a top-level declaration, or the containing class, object, or script otherwise — or `#!java null` if it cannot be determined.


</div>

</div>
