---
tags:
 - jvm
title: "KaKDocProvider"
---

# KaKDocProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaKDocProvider</a> : <a href="../-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>Component that locates KDoc for [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md) and [`KaDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md).

This is part of a non-public API intended for use only by IDE and Dokka. Current implementation is based on the original `findKDoc` logic from Kotlin IDE Plugin.

#### Inheritors


 - [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)



</div>

## Properties
### [`token`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#token)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#token">token</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaLifetimeToken`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md) which determines the lifetime of the lifetime owner.


</div>

</div>
## Functions
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### findKDoc

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="index.html#findkdoc"><span class="nf">findKDoc</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.kdoc.psi.api/-k-doc-comment-descriptor/index.html">KDocCommentDescriptor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves KDoc for this [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md).

This is part of a non-public API intended for use only by IDE and Dokka. Current implementation is based on the original `findKDoc` logic from Kotlin IDE Plugin.

[`KDocCommentDescriptor`](../../../psi-api/org.jetbrains.kotlin.kdoc.psi.api/-k-doc-comment-descriptor/index.md) for the given [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md) is resolved using the following algorithm:

1. [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md) has its own KDoc, i.e. [`KtDeclaration.getDocComment`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/get-doc-comment.md) returns non-null value. In this case, [`KDocCommentDescriptor.primaryTag`](../../../psi-api/org.jetbrains.kotlin.kdoc.psi.api/-k-doc-comment-descriptor/primary-tag.md) is the KDoc's default section and [`KDocCommentDescriptor.additionalSections`](../../../psi-api/org.jetbrains.kotlin.kdoc.psi.api/-k-doc-comment-descriptor/additional-sections.md) contain all sections of that KDoc (including the default one).


1. [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md) does not have its own KDoc, but its documentation can be derived from its parent's KDoc. This rule is applied in four different cases:


1.  - [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md) is a primary constructor and the enclosing class KDoc has a `@constructor` section.     That section is used as KaKDocComment.primaryTag, and KaKDocComment.additionalSections contains     the sections that include `@param` tags from the class's KDoc.


 - [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md) is a KtParameter of the primary constructor. KaKDocComment.primaryTag is resolved     from the `@property` or `@param` tags of the class's KDoc. KaKDocComment.additionalSections is empty.


 - [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md) is a KtParameter or KtTypeParameter. KaKDocComment.primaryTag is resolved     from the `@param` tags of the parent's KDoc. KaKDocComment.additionalSections is empty.


 - [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md) is a KtProperty that is declared inside a class/object with a KDoc, but referenced     with a `@property` tag in the class/object KDoc. KaKDocComment.primaryTag is the `@property` tag,     and KaKDocComment.additionalSections is empty.



1. In all other cases this method returns `null`


Notes:

 - KDoc for an element can be resolved whenever we have sources for it. Including external libraries.


 - This method only resolves KDoc for Kotlin elements. Java elements and Javadoc are not supported.



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="index.html#findkdoc"><span class="nf">findKDoc</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.kdoc.psi.api/-k-doc-comment-descriptor/index.html">KDocCommentDescriptor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves KDoc for this [`KaDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md).

This is part of a non-public API intended for use only by IDE and Dokka. Current implementation is based on the original `findKDoc` logic from Kotlin IDE Plugin.

[`KDocCommentDescriptor`](../../../psi-api/org.jetbrains.kotlin.kdoc.psi.api/-k-doc-comment-descriptor/index.md) for the given [`KaDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) is resolved using the following algorithm:

1. Try resolving the KDoc of the symbol's PSI navigation element via [`KaKDocProvider.findKDoc`](index.md#findkdoc).


1. If the symbol is a callable, walk its [`KaCallableSymbol.allOverriddenSymbols`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/index.md) in order and recursively call [`findKDoc`](index.md#findkdoc) on each of them. Return the first non-null result.


1. Resolve the symbol's `expect` declarations via [`getExpectsForActual`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-receiver-parameter-symbol/index.md#getexpectsforactual). Recursively call [`findKDoc`](index.md#findkdoc) on the first (non-null) element of the list. Return the first non-null result.


1. In all other cases this method returns `null`.


Notes:

 - In case of ambiguity, the first match is returned; if nothing is found, `null` is returned;


 - KDoc for a [`KaDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) can only be resolved when it has a corresponding PSI element.


**See also**



 - [`KaKDocProvider.findKDoc`](index.md#findkdoc): for the implementation details.





</div>

</div>
### [`isValid`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#isvalid)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#isvalid"><span class="nf">isValid</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the lifetime owner is still valid, i.e. we are still in the scope of the lifetime owner's regular lifetime.


</div>

</div>
### [`withValidityAssertion`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion"><span class="nf">withValidityAssertion</span></a><span class="p">(</span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a>
</span></code></pre></div>
</div>


<div markdown>

Executes [`action`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion) only if the [`KaLifetimeOwner`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.md) is still [`valid`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md#isvalid) and [`accessible`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md#isaccessible). Otherwise, throws a validity exception based on the concrete violation.


</div>

</div>
