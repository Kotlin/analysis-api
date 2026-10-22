---
tags:
 - jvm
title: "getAssignmentLhsIfUnwrappable"
---

# getAssignmentLhsIfUnwrappable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span>PsiElement<span class="p">.</span><a href="get-assignment-lhs-if-unwrappable.html"><span class="nf">getAssignmentLhsIfUnwrappable</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the operand this operation applies to, but only when that operand is wrapped in parentheses, a label, or annotations; returns `null` otherwise.

The operand is the left-hand side of an assignment or augmented-assignment operator call (`(x) = ...`, `(x) += ...`), the base of a postfix increment or decrement (`(x)++`), or the operand of a prefix increment or decrement (`++(x)`).

This should only be called for a source element corresponding to one of those constructs.


</div>

</div>
