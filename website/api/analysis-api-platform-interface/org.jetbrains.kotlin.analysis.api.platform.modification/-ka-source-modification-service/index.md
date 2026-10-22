---
tags:
 - jvm
title: "KaSourceModificationService"
---

# KaSourceModificationService

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaSourceModificationService</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-ka-engine-service/index.html">KaEngineService</a>
</span></code></pre></div>[`KaSourceModificationService`](index.md) is an <strong>engine service</strong> which handles cache invalidation after source code changes:

 - For local changes (in-block modification and whitespace), the service invalidates local caches for, e.g., classes. This level of granularity cannot be reached by any module-level event (see [`KotlinModificationEvent`](../-kotlin-modification-event/index.md)), because the specific entity to invalidate needs to be discovered via the changed PsiElement.


 - For non-local changes (out-of-block modification), the service publishes a module out-of-block [`modification event`](../-kotlin-module-out-of-block-modification-event/index.md).


The service performs change locality detection to classify a change to a given PsiElement in terms of [`KaSourceModificationLocality`](../-ka-source-modification-locality/index.md).

An element may be submitted to consideration before or after the actual modification is performed, but service implementations don't guarantee that the invalidation behavior is the same for before/after instances of the same modification.

While out-of-block modification events can be published to the message bus directly, there is currently no infrastructure for publishing in-block modification. Hence, platforms will need to use [`KaSourceModificationService`](index.md) for more granular cache invalidation, or as a last resort publish out-of-block modification events for all changes.


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
### ancestorAffectedByInBlockModification

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#ancestoraffectedbyinblockmodification"><span class="nf">ancestorAffectedByInBlockModification</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the farthest ancestor PsiElement of [`element`](index.md#ancestoraffectedbyinblockmodification) which would be affected by an in-block modification to [`element`](index.md#ancestoraffectedbyinblockmodification), or `null` if it's uncertain.


</div>

</div>
### detectLocality

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#detectlocality"><span class="nf">detectLocality</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">, </span>modificationType<span class="o">: </span><a href="../-ka-element-modification-type/index.html">KaElementModificationType</a><span class="p">)</span><span class="o">: </span><a href="../-ka-source-modification-locality/index.html">KaSourceModificationLocality</a>
</span></code></pre></div>
</div>


<div markdown>

Classifies the modification of [`element`](index.md#detectlocality) and its [`modificationType`](index.md#detectlocality) in terms of [`KaSourceModificationLocality`](../-ka-source-modification-locality/index.md), as described in the KDoc of [`KaSourceModificationService`](index.md). The function may be called before and after [`element`](index.md#detectlocality)'s modification.

If [`KaElementModificationType.Unknown`](../-ka-element-modification-type/-unknown/index.md) is specified, the service must classify the modification pessimistically, so specifying a narrower modification type is usually beneficial.

Here are some examples for which [`element`](index.md#detectlocality) to pass:

 - [`element`](index.md#detectlocality) should be a [`KtNamedFunction`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-named-function/index.md) after dropping the function's [`body`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-block-expression/index.md).


 - [`element`](index.md#detectlocality) should be a [`KtBlockExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-block-expression/index.md) after replacing one body expression with another.


 - [`element`](index.md#detectlocality) should be a [`KtBlockExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-block-expression/index.md) after adding a body to a function without a body.


 - If [`element`](index.md#detectlocality) is the parent of an already removed element, [`KaElementModificationType.ElementRemoved`](../-ka-element-modification-type/-element-removed/index.md) should contain the removed element.


 - If [`element`](index.md#detectlocality) is the replacement, [`KaElementModificationType.ElementReplaced`](../-ka-element-modification-type/-element-replaced/index.md) should contain the replaced element.



</div>

</div>
### handleElementModification

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">KaSourceModificationService</a><span class="p">.</span><a href="index.html#handleelementmodification"><span class="nf">handleElementModification</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">, </span>modificationType<span class="o">: </span><a href="../-ka-element-modification-type/index.html">KaElementModificationType</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Detects the modification locality of [`element`](index.md#handleelementmodification) and handles the corresponding cache invalidation.

This is a convenience function that combines [`KaSourceModificationService.detectLocality`](index.md#detectlocality) and [`KaSourceModificationService.handleInvalidation`](index.md#handleinvalidation).

The function must be called from a write action.

**See also**



 - [`KaSourceModificationService.detectLocality`](index.md#detectlocality)
 - [`KaSourceModificationService.handleInvalidation`](index.md#handleinvalidation)



</div>

</div>
### handleInvalidation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#handleinvalidation"><span class="nf">handleInvalidation</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">, </span>modificationLocality<span class="o">: </span><a href="../-ka-source-modification-locality/index.html">KaSourceModificationLocality</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Handles the cache invalidation for [`element`](index.md#handleinvalidation)'s modification based on the detected [`modificationLocality`](index.md#handleinvalidation).

The function must be called from a write action.

**Parameters**



 - modificationLocality: The modification locality detected by [`detectLocality`](index.md#detectlocality). It must have been provided by this service. No other [`KaSourceModificationLocality`](../-ka-source-modification-locality/index.md) should be passed to the function.




**See also**



 - [`detectLocality`](index.md#detectlocality)



</div>

</div>
