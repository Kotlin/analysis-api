---
tags:
 - jvm
title: "containingClassOrObject"
---

# containingClassOrObject

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="containing-class-or-object.html">containingClassOrObject</a><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The class or object that declares this declaration as a member (including constructors and nested classes), or `null` if it is not a class member — for example, a member function's parameter or local, or a property accessor.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-class-body/index.html">KtClassBody</a><span class="p">.</span><a href="containing-class-or-object.html">containingClassOrObject</a><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The containing class for the body.

<strong>Note</strong>: it bypasses [`KtCompanionBlock`](../org.jetbrains.kotlin.psi/-kt-companion-block/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-companion-block/index.html">KtCompanionBlock</a><span class="p">.</span><a href="containing-class-or-object.html">containingClassOrObject</a><span class="o">: </span><a href="../org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The containing class for the companion block.


</div>

</div>
