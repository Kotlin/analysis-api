---
tags:
 - jvm
title: "ElementReplaced"
---

# ElementReplaced

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">ElementReplaced</a><span class="p">(</span><span class="kd">val </span>replacedElement<span class="o">: </span>PsiElement<span class="p">)</span> : <a href="../index.html">KaElementModificationType</a>
</span></code></pre></div>The element passed is the replacement element. The replaced element itself is represented by [`replacedElement`](index.md#replacedelement). The replaced element itself cannot be the modification "anchor" because it has already been replaced and is not part of the [`KtFile`](../../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md) anymore, but it might still be used to determine the modification's change type.


</div>

## Constructors
### ElementReplaced

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>replacedElement<span class="o">: </span>PsiElement<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### replacedElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#replacedelement">replacedElement</a><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
