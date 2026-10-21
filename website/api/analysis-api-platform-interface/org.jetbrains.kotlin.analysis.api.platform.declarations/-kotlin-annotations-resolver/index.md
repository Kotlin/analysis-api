---
tags:
 - jvm
title: "KotlinAnnotationsResolver"
---

# KotlinAnnotationsResolver

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinAnnotationsResolver</a>
</span></code></pre></div>[`KotlinAnnotationsResolver`](index.md) matches declarations with their annotations and vice versa.

This service can produce both false positives and false negatives, since it might not be allowed to use full resolution to understand the true FqName of a used annotation.

The next statement should be `true` for any `annotation`:

```
declarationsByAnnotation(annotation).all { declaration ->
  annotation in annotationsOnDeclaration(declaration)
}
```


</div>

## Functions
### annotationsOnDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#annotationsondeclaration"><span class="nf">annotationsOnDeclaration</span></a><span class="p">(</span>declaration<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-annotated/index.html">KtAnnotated</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>ClassId<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an approximate set of annotation ClassIds which have been applied to [`declaration`](index.md#annotationsondeclaration). The set may contain both false positives and false negatives.

**Parameters**



 - declaration: A [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md) or [`KtFile`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md) to resolve annotations on. Other [`KtElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md)s are not supported.





</div>

</div>
### declarationsByAnnotation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#declarationsbyannotation"><span class="nf">declarationsByAnnotation</span></a><span class="p">(</span>annotationClassId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-annotated/index.html">KtAnnotated</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an approximate set of [`KtAnnotated`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-annotated/index.md) declarations which have an annotation with the given [`annotationClassId`](index.md#declarationsbyannotation) applied to them. The set may contain both false positives and false negatives.


</div>

</div>
