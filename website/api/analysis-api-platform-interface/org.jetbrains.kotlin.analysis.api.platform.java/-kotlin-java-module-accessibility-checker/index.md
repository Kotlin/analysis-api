---
tags:
 - jvm
title: "KotlinJavaModuleAccessibilityChecker"
---

# KotlinJavaModuleAccessibilityChecker

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinJavaModuleAccessibilityChecker</a>
</span></code></pre></div>Allows checking whether one Java module has access to another Java module.


</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Functions
### checkAccessibility

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#checkaccessibility"><span class="nf">checkAccessibility</span></a><span class="p">(</span>
    useSiteFile<span class="o">: </span>VirtualFile<span class="o">?</span><span class="p">, </span>
    referencedFile<span class="o">: </span>VirtualFile<span class="p">, </span>
    referencedPackage<span class="o">: </span>FqName<span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="../-kotlin-java-module-accessibility-error/index.html">KotlinJavaModuleAccessibilityError</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Checks whether the Java module of [`referencedFile`](index.md#checkaccessibility) is accessible from the Java module of [`useSiteFile`](index.md#checkaccessibility). If [`referencedPackage`](index.md#checkaccessibility) is specified, additionally checks that the Java module of [`referencedFile`](index.md#checkaccessibility) exports the given package.

**Return**

`null` if the use-site module can access the referenced module (and the [`referencedPackage`](index.md#checkaccessibility) is exported), or an accessibility error otherwise.


</div>

</div>
