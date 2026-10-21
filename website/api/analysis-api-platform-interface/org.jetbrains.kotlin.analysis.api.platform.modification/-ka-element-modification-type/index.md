---
tags:
 - jvm
title: "KaElementModificationType"
---

# KaElementModificationType

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">KaElementModificationType</a>
</span></code></pre></div>[`KaElementModificationType`](index.md) describes which kind of modification was applied to a changed PsiElement. [`KaSourceModificationService`](../-ka-source-modification-service/index.md) uses this information to perform change locality detection.

#### Inheritors


 - [`ElementAdded`](-element-added/index.md)
 - [`ElementRemoved`](-element-removed/index.md)
 - [`ElementReplaced`](-element-replaced/index.md)
 - [`Unknown`](-unknown/index.md)



</div>

## Types
### [`ElementAdded`](-element-added/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-element-added/index.html">ElementAdded</a> : <a href="index.html">KaElementModificationType</a>
</span></code></pre></div>
</div>


<div markdown>

The element has been added as a new element.


</div>

</div>
### [`ElementRemoved`](-element-removed/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-element-removed/index.html">ElementRemoved</a><span class="p">(</span><span class="kd">val </span>removedElement<span class="o">: </span>PsiElement<span class="p">)</span> : <a href="index.html">KaElementModificationType</a>
</span></code></pre></div>
</div>


<div markdown>

The element passed is the parent of a removed element, which is additionally provided as [`removedElement`](-element-removed/index.md#removedelement). The removed element itself cannot be the modification "anchor" because it has already been removed and is not part of the [`KtFile`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md) anymore, but it might still be used to determine the modification's change type.


</div>

</div>
### [`ElementReplaced`](-element-replaced/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-element-replaced/index.html">ElementReplaced</a><span class="p">(</span><span class="kd">val </span>replacedElement<span class="o">: </span>PsiElement<span class="p">)</span> : <a href="index.html">KaElementModificationType</a>
</span></code></pre></div>
</div>


<div markdown>

The element passed is the replacement element. The replaced element itself is represented by [`replacedElement`](-element-replaced/index.md#replacedelement). The replaced element itself cannot be the modification "anchor" because it has already been replaced and is not part of the [`KtFile`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md) anymore, but it might still be used to determine the modification's change type.


</div>

</div>
### [`Unknown`](-unknown/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-unknown/index.html">Unknown</a> : <a href="index.html">KaElementModificationType</a>
</span></code></pre></div>
</div>


<div markdown>

Which kind of modification was applied to the element is unknown.


</div>

</div>
