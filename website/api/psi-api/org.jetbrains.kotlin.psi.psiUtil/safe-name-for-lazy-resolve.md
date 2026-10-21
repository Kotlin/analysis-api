---
tags:
 - jvm
title: "safeNameForLazyResolve"
---

# safeNameForLazyResolve

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-named-declaration/index.html">KtNamedDeclaration</a><span class="p">.</span><a href="safe-name-for-lazy-resolve.html"><span class="nf">safeNameForLazyResolve</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>Name
</span></code></pre></div>
</div>


<div markdown>

Returns this declaration's name, substituting the "no name provided" special name for a missing or special name.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>Name<span class="o">?</span><span class="p">.</span><a href="safe-name-for-lazy-resolve.html"><span class="nf">safeNameForLazyResolve</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>Name
</span></code></pre></div>
</div>


<div markdown>

Returns this name, or the "no name provided" special name if it is `null` or special.


</div>

</div>
