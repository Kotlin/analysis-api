---
tags:
 - jvm
title: "ElementRemoved"
---

# ElementRemoved

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">ElementRemoved</a><span class="p">(</span><span class="kd">val </span>removedElement<span class="o">: </span>PsiElement<span class="p">)</span> : <a href="../index.html">KaElementModificationType</a>
</span></code></pre></div>The element passed is the parent of a removed element, which is additionally provided as [`removedElement`](index.md#removedelement). The removed element itself cannot be the modification "anchor" because it has already been removed and is not part of the [`KtFile`](../../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md) anymore, but it might still be used to determine the modification's change type.


</div>

## Constructors
### ElementRemoved

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>removedElement<span class="o">: </span>PsiElement<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### removedElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#removedelement">removedElement</a><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
