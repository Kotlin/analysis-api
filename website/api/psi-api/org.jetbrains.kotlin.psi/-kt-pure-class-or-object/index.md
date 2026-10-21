---
tags:
 - jvm
title: "KtPureClassOrObject"
---

# KtPureClassOrObject

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KtPureClassOrObject</a> : <a href="../-kt-pure-element/index.html">KtPureElement</a>, <a href="../-kt-declaration-container/index.html">KtDeclarationContainer</a>
</span></code></pre></div>A minimal interface that [`KtClassOrObject`](../-kt-class-or-object/index.md) implements for the purpose of code-generation that does not need the full power of PSI. This interface can be easily implemented by synthetic elements to generate code for them.

#### Inheritors


 - [`KtClassOrObject`](../-kt-class-or-object/index.md)



</div>

## Properties
### [`pureEndOffset`](../../org.jetbrains.kotlin.psi.psiUtil/pure-end-offset.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-kt-pure-element/index.html">KtPureElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/pure-end-offset.html">pureEndOffset</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

The end offset of this element's source.


</div>

</div>
### [`pureStartOffset`](../../org.jetbrains.kotlin.psi.psiUtil/pure-start-offset.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-kt-pure-element/index.html">KtPureElement</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.psi.psiUtil/pure-start-offset.html">pureStartOffset</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

The start offset of this element's source, excluding any leading comments.


</div>

</div>
## Functions
### getBody

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getbody"><span class="nf">getBody</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-class-body/index.html">KtClassBody</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the body of this class or object (the part enclosed in braces), or `#!java null` if it has no body.


</div>

</div>
### getCompanionObjects

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="se">@</span><span class="se">ReadOnly</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getcompanionobjects"><span class="nf">getCompanionObjects</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/List.html">List</a><span class="o"><</span><a href="../-kt-object-declaration/index.html">KtObjectDeclaration</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the companion objects declared in this class or object body, or an empty list if there are none.


</div>

</div>
### getContainingKtFile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="../-kt-pure-element/index.html#getcontainingktfile"><span class="nf">getContainingKtFile</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-file/index.html">KtFile</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KtFile`](../-kt-file/index.md) this element belongs to.


</div>

</div>
### getContextReceivers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="se">@</span><span class="se">ReadOnly</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getcontextreceivers"><span class="nf">getContextReceivers</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/List.html">List</a><span class="o"><</span><a href="../-kt-context-receiver/index.html">KtContextReceiver</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the unnamed context receivers declared on this class or object, or an empty list if there are none. This is the legacy context-receiver API; named context parameters are exposed by [`KtContextParameterList`](../-kt-context-parameter-list/index.md).


</div>

</div>
### getDeclarations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="se">@</span><span class="se">ReadOnly</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getdeclarations"><span class="nf">getDeclarations</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/List.html">List</a><span class="o"><</span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the declarations directly contained in this element, in their source order. Returns an empty list if there are none.


</div>

</div>
### getName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getname"><span class="nf">getName</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the simple name of this class or object, or `#!java null` if it has none (for example, an object literal).


</div>

</div>
### getParent

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-kt-throw-expression/index.html#getparent"><span class="nf">getParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Returns parent source element.


</div>

</div>
### getPrimaryConstructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getprimaryconstructor"><span class="nf">getPrimaryConstructor</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-primary-constructor/index.html">KtPrimaryConstructor</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the primary constructor, or `#!java null` if there is no explicitly written primary constructor.


</div>

</div>
### getPrimaryConstructorModifierList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getprimaryconstructormodifierlist"><span class="nf">getPrimaryConstructorModifierList</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-modifier-list/index.html">KtModifierList</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the modifier list of the primary constructor (for example, its visibility modifiers), or `#!java null` if there is no explicitly written primary constructor or it has no modifiers.


</div>

</div>
### getPrimaryConstructorParameters

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="se">@</span><span class="se">ReadOnly</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getprimaryconstructorparameters"><span class="nf">getPrimaryConstructorParameters</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/List.html">List</a><span class="o"><</span><a href="../-kt-parameter/index.html">KtParameter</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the value parameters of the primary constructor, or an empty list if there are none.


</div>

</div>
### getPsiOrParent

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="../-kt-pure-element/index.html#getpsiorparent"><span class="nf">getPsiOrParent</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Returns this or parent source element (for synthetic element declarations). Use it only for the purposes of source attribution.


</div>

</div>
### getSecondaryConstructors

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="se">@</span><span class="se">ReadOnly</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getsecondaryconstructors"><span class="nf">getSecondaryConstructors</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/List.html">List</a><span class="o"><</span><a href="../-kt-secondary-constructor/index.html">KtSecondaryConstructor</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the secondary constructors declared in this class or object body, or an empty list if there are none.


</div>

</div>
### getSuperTypeListEntries

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="se">@</span><span class="se">ReadOnly</span>
<span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getsupertypelistentries"><span class="nf">getSuperTypeListEntries</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/List.html">List</a><span class="o"><</span><a href="../-kt-super-type-list-entry/index.html">KtSuperTypeListEntry</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the supertype list entries (the types and delegations written after the `#!java :`), or an empty list if there are none.


</div>

</div>
### hasExplicitPrimaryConstructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#hasexplicitprimaryconstructor"><span class="nf">hasExplicitPrimaryConstructor</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if this class or object has an explicitly written primary constructor.


</div>

</div>
### hasPrimaryConstructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#hasprimaryconstructor"><span class="nf">hasPrimaryConstructor</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if this class or object has an explicit primary constructor or has no secondary constructors. Consequently, this can be `#!java true` for an object and when [`getPrimaryConstructor`](index.md#getprimaryconstructor) is `#!java null`.


</div>

</div>
### isLocal

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#islocal"><span class="nf">isLocal</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if this class or object is declared in a local scope (inside a function body or another block) rather than as a top-level or member declaration.


</div>

</div>
