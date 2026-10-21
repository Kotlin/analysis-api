---
tags:
 - jvm
title: "KtPsiUtil"
---

# KtPsiUtil

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="index.html">KtPsiUtil</a>
</span></code></pre></div>A collection of static helper methods for working with the Kotlin PSI. 

The utilities here cover common low-level operations such as unwrapping parenthesized expressions ([`deparenthesize`](index.md#deparenthesize)), inspecting names and identifiers, and testing structural properties of elements (for example, whether a declaration is local). This class is not instantiable.


</div>

## Types
### [`KtExpressionWrapper`](-kt-expression-wrapper/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kt-expression-wrapper/index.html">KtExpressionWrapper</a>
</span></code></pre></div>
</div>


<div markdown>

An element that wraps a base expression, such as a parenthesized or annotated expression.

</div>

</div>
## Companion functions
### ascendIfPropertyAccessor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#ascendifpropertyaccessor"><span class="nf">ascendIfPropertyAccessor</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

If `#!java element` is a property accessor, returns its owning property; otherwise returns `#!java element` unchanged.


</div>

</div>
### checkVariableDeclarationInBlock

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#checkvariabledeclarationinblock"><span class="nf">checkVariableDeclarationInBlock</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> block<span class="o">: </span><a href="../-kt-block-expression/index.html">KtBlockExpression</a><span class="p">, </span><span class="se">@</span><span class="se">NotNull</span> varName<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java block` contains a variable declaration named `#!java varName`.


</div>

</div>
### checkWhenExpressionHasSingleElse

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#checkwhenexpressionhassingleelse"><span class="nf">checkWhenExpressionHasSingleElse</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> whenExpression<span class="o">: </span><a href="../-kt-when-expression/index.html">KtWhenExpression</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java whenExpression` has exactly one `#!java else` branch.


</div>

</div>
### deparenthesize

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#deparenthesize"><span class="nf">deparenthesize</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Recursively unwraps parentheses, labels, and annotations from the given `#!java expression`.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#deparenthesize"><span class="nf">deparenthesize</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">, </span>keepAnnotations<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Recursively unwraps parentheses and labels (and annotations unless `#!java keepAnnotations` is `#!java true`) from the given `#!java expression`, returning the innermost wrapped expression.


</div>

</div>
### deparenthesizeOnce

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#deparenthesizeonce"><span class="nf">deparenthesizeOnce</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Unwraps a single layer of parentheses, label, or annotation from the given `#!java expression`.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#deparenthesizeonce"><span class="nf">deparenthesizeOnce</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">, </span>keepAnnotations<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Unwraps a single layer of parentheses or label (and annotation unless `#!java keepAnnotations` is `#!java true`) from the given `#!java expression`.


</div>

</div>
### findChildByType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#findchildbytype"><span class="nf">findChildByType</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span>PsiElement<span class="p">, </span><span class="se">@</span><span class="se">NotNull</span> type<span class="o">: </span>IElementType<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Returns the first direct child of `#!java element` with the given node `#!java type`, or `#!java null` if there is none.


</div>

</div>
### findRootExpressions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#findrootexpressions"><span class="nf">findRootExpressions</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> unreachableElements<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html">Collection</a><span class="o"><</span><a href="../-kt-element/index.html">KtElement</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/Set.html">Set</a><span class="o"><</span><a href="../-kt-element/index.html">KtElement</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the subset of `#!java unreachableElements` that are not contained within any other element of the set.


</div>

</div>
### getClassIfParameterIsProperty

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getclassifparameterisproperty"><span class="nf">getClassIfParameterIsProperty</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> ktParameter<span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a><span class="p">)</span><span class="o">: </span><a href="../-kt-class-or-object/index.html">KtClassOrObject</a>
</span></code></pre></div>
</div>


<div markdown>

If `#!java ktParameter` is a primary-constructor `#!java val`/`#!java var` property parameter, returns the class or object that declares it; otherwise returns `#!java null`.


</div>

</div>
### getDirectParentOfTypeForBlock

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#getdirectparentoftypeforblock">T</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="index.html#getdirectparentoftypeforblock"><span class="nf">getDirectParentOfTypeForBlock</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> block<span class="o">: </span><a href="../-kt-block-expression/index.html">KtBlockExpression</a><span class="p">, </span><span class="se">@</span><span class="se">NotNull</span> aClass<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><a href="index.html#getdirectparentoftypeforblock">T</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="index.html#getdirectparentoftypeforblock">T</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the enclosing element of type `#!java aClass` for which `#!java block` is a direct body (an `#!java if` branch, a `#!java when` entry, a lambda body, or a `#!java try`/`#!java catch` body), or `#!java null` otherwise.


</div>

</div>
### getEnclosingElementForLocalDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getenclosingelementforlocaldeclaration"><span class="nf">getEnclosingElementForLocalDeclaration</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> declaration<span class="o">: </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="p">)</span><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the innermost element that scopes `#!java declaration` as a local declaration (a block, parameter, and so on), or `#!java null` if the declaration is not local. See [`getEnclosingElementForLocalDeclaration`](index.md#getenclosingelementforlocaldeclaration) with `#!java skipParameters`.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getenclosingelementforlocaldeclaration"><span class="nf">getEnclosingElementForLocalDeclaration</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> declaration<span class="o">: </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="p">, </span>skipParameters<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the innermost element that scopes `#!java declaration` as a local declaration, or `#!java null` if it is not local. When `#!java skipParameters` is `#!java true`, type and value parameters delegate to their owning declaration.


</div>

</div>
### getExpressionOrLastStatementInBlock

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getexpressionorlaststatementinblock"><span class="nf">getExpressionOrLastStatementInBlock</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the last statement of `#!java expression` if it is a block, otherwise `#!java expression` itself.


</div>

</div>
### getLastChildByType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/SafeVarargs.html"><span class="se">SafeVarargs</span></a>
<span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#getlastchildbytype">T</a><span class="o"> : </span>PsiElement<span class="o">?</span><span class="o">> </span><a href="index.html#getlastchildbytype"><span class="nf">getLastChildByType</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> root<span class="o">: </span>PsiElement<span class="p">, </span><span class="se">@</span><span class="se">NotNull</span> elementTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><span class="kd">out </span><a href="index.html#getlastchildbytype">T</a><span class="o">></span><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="index.html#getlastchildbytype">T</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the last direct child of `#!java root` whose type is one of `#!java elementTypes`, or `#!java null` if there is none.


</div>

</div>
### getLastElementDeparenthesized

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getlastelementdeparenthesized"><span class="nf">getLastElementDeparenthesized</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">, </span><span class="se">@</span><span class="se">NotNull</span> statementFilter<span class="o">: </span><a href="../../org.jetbrains.kotlin.resolve/-statement-filter/index.html">StatementFilter</a><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Deparenthesizes `#!java expression` and, if it is a block, recurses into the block's last statement (respecting `#!java statementFilter`), returning the innermost "result" expression.


</div>

</div>
### getLastReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getlastreference"><span class="nf">getLastReference</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> importedReference<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="../-kt-simple-name-expression/index.html">KtSimpleNameExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the last (rightmost) simple-name reference of the given qualified `#!java importedReference`, or `#!java null`.


</div>

</div>
### getLastStatementInABlock

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getlaststatementinablock"><span class="nf">getLastStatementInABlock</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> blockExpression<span class="o">: </span><a href="../-kt-block-expression/index.html">KtBlockExpression</a><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the last statement of the given block, or `#!java null` if the block is `#!java null` or empty.


</div>

</div>
### getNullableText

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getnullabletext"><span class="nf">getNullableText</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the text of `#!java element`, or `#!java null` if `#!java element` is `#!java null`.


</div>

</div>
### getOperationToken

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getoperationtoken"><span class="nf">getOperationToken</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-operation-expression/index.html">KtOperationExpression</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.lexer/-kt-token/index.html">KtToken</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the operation token of `#!java expression` (for example, `#!java PLUS`), or `#!java null` if unavailable.


</div>

</div>
### getOutermostClassOrObject

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getoutermostclassorobject"><span class="nf">getOutermostClassOrObject</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> classOrObject<span class="o">: </span><a href="../-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">)</span><span class="o">: </span><a href="../-kt-class-or-object/index.html">KtClassOrObject</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the outermost class that lexically encloses (and includes) the given class. 

Starting from `#!java classOrObject`, this repeatedly ascends to the enclosing class and returns the last one reached — the top of the class-nesting chain. 

The walk stops as soon as a declaration has no enclosing class; in particular: 

 - a top-level class is returned unchanged;
 - a nested or inner class resolves to the top-level class that contains it;
 - a local class (declared inside a code block) is returned unchanged, and the walk never crosses out of a local class into its surrounding block — so a class nested inside a local class resolves to that local class rather than to any top-level declaration.
 Note: a class declared inside a `#!java companion { }` block (which is invalid code) is treated as nested directly in the class that owns the block. **Example:**

```java

class Top {
    class Nested

    fun build() {
        class Local {
            inner class InsideLocal
        }
    }
}

```

For these declarations, `#!java getOutermostClassOrObject(nested)` returns `#!java top`, while calls for `#!java local` and `#!java insideLocal` both return `#!java local`. The search does not cross the local-class boundary.

**Return**

the outermost enclosing class; never `#!java null` — at minimum `#!java classOrObject` itself

**Parameters**



 - classOrObject: the class to start the search from





</div>

</div>
### getOutermostDescendantElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getoutermostdescendantelement"><span class="nf">getOutermostDescendantElement</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">Nullable</span> root<span class="o">: </span>PsiElement<span class="p">, </span>
    first<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NotNull</span> predicate<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/function/Predicate.html">Predicate</a><span class="o"><</span><a href="../-kt-element/index.html">KtElement</a><span class="o">></span>
<span class="p">)</span><span class="o">: </span><a href="../-kt-element/index.html">KtElement</a>
</span></code></pre></div>
</div>


<div markdown>

Traverses `#!java root` and its subtree, collecting the outermost elements that satisfy `#!java predicate` without descending into a match. Returns the first or last match in depth-first traversal order, as selected by `#!java first`, or `#!java null` if there is none. If `#!java root` matches, it is the only result. 

**Example:**

```java

class First {
    class Nested
}
class Second

```

Given the containing `#!java file`, the following searches return `#!java First` and `#!java Second`, respectively: 

```java

KtElement firstClass = getOutermostDescendantElement(file, true, element -> element instanceof KtClass);
KtElement lastClass = getOutermostDescendantElement(file, false, element -> element instanceof KtClass);

```

`#!java Nested` is not considered because the traversal does not descend into `#!java First` after it matches.


</div>

</div>
### getOutermostParent

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getoutermostparent"><span class="nf">getOutermostParent</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span>PsiElement<span class="p">, </span>
    <span class="se">@</span><span class="se">NotNull</span> upperBound<span class="o">: </span>PsiElement<span class="p">, </span>
    strict<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Returns the outermost ancestor of `#!java element` that is still a direct child of `#!java upperBound`, or `#!java null`. When `#!java strict` is `#!java false`, `#!java element` itself is considered.


</div>

</div>
### getPackageName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getpackagename"><span class="nf">getPackageName</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span><a href="../-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the dot-separated package name of the file containing `#!java element`, or `#!java null` if unavailable.


</div>

</div>
### getParentCallIfPresent

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getparentcallifpresent"><span class="nf">getParentCallIfPresent</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the nearest enclosing call-like expression that `#!java expression` is an operand or argument of, looking through parentheses, casts, argument lists, lambdas, and labels, or `#!java null` if there is none. 

**Example:**

```java

consume((value as String))
consume(left + right)

```

For the first statement, calling this method on the `#!java value` expression returns the `#!java consume(...)` call because casts and parentheses are skipped. For the second statement, calling it on `#!java left` returns the nearer binary expression `#!java left + right` rather than the outer `#!java consume(...)` call.


</div>

</div>
### getPreviousWord

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getpreviousword"><span class="nf">getPreviousWord</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span>PsiElement<span class="p">, </span><span class="se">@</span><span class="se">NotNull</span> word<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Returns the previous leaf if it is the identifier `#!java word` (skipping whitespace and comments), or `#!java null`.


</div>

</div>
### getScript

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getscript"><span class="nf">getScript</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> namedDeclaration<span class="o">: </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="p">)</span><span class="o">: </span><a href="../-kt-script/index.html">KtScript</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the script this declaration is a top-level member of, or `#!java null` if it is not in a script.


</div>

</div>
### getText

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#gettext"><span class="nf">getText</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the text of `#!java element`, or an empty string if `#!java element` is `#!java null`.


</div>

</div>
### getTopmostParentOfTypes

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="se">@</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/SafeVarargs.html"><span class="se">SafeVarargs</span></a>
<span class="se">@</span><span class="se">Contract</span><span class="p">(</span>value<span class="o"> = </span><span class="s">"null, _ -> null"</span><span class="p">)</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#gettopmostparentoftypes"><span class="nf">getTopmostParentOfTypes</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> element<span class="o">: </span>PsiElement<span class="p">, </span><span class="se">@</span><span class="se">NotNull</span> parentTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><span class="kd">out </span>PsiElement<span class="o">></span><span class="o">></span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Returns the topmost ancestor of `#!java element` (or the enclosing file) whose type is one of `#!java parentTypes`, or `#!java null` if there is none.


</div>

</div>
### isAbstract

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isabstract"><span class="nf">isAbstract</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> declaration<span class="o">: </span><a href="../-kt-declaration-with-body/index.html">KtDeclarationWithBody</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java declaration` has no body expression. This is a syntactic check; it does not inspect the `#!java abstract` modifier or determine whether the declaration is semantically abstract.


</div>

</div>
### isAssignment

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isassignment"><span class="nf">isAssignment</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java element` is an assignment (`#!java =` or an augmented assignment such as `#!java +=`).


</div>

</div>
### isBooleanConstant

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isbooleanconstant"><span class="nf">isBooleanConstant</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> condition<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java condition` is a boolean literal (`#!java true` or `#!java false`).


</div>

</div>
### isCast

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#iscast"><span class="nf">isCast</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-binary-expression-with-type-r-h-s/index.html">KtBinaryExpressionWithTypeRHS</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java expression` is a cast, whether safe (`#!java as?`) or unsafe (`#!java as`).


</div>

</div>
### isDeprecated

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isdeprecated"><span class="nf">isDeprecated</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> owner<span class="o">: </span><a href="../-kt-modifier-list-owner/index.html">KtModifierListOwner</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java owner` is syntactically annotated with `#!java @Deprecated` (by short name only).


</div>

</div>
### isFalseConstant

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isfalseconstant"><span class="nf">isFalseConstant</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> condition<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java condition` is the boolean literal `#!java false`.


</div>

</div>
### isInComment

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isincomment"><span class="nf">isInComment</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java element` is a comment or is inside a KDoc comment. 

isComment does not recognize elements <strong>inside</strong> a comment. KDoc tokens cannot be added to the general comment token set because the parser ignores every token in that set.


</div>

</div>
### isInOrNotInOperation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isinornotinoperation"><span class="nf">isInOrNotInOperation</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> binaryExpression<span class="o">: </span><a href="../-kt-binary-expression/index.html">KtBinaryExpression</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java binaryExpression` is an `#!java in` or `#!java !in` membership check.


</div>

</div>
### isLabeledFunctionLiteral

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#islabeledfunctionliteral"><span class="nf">isLabeledFunctionLiteral</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> functionLiteral<span class="o">: </span><a href="../-kt-function-literal/index.html">KtFunctionLiteral</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java functionLiteral`'s enclosing lambda expression carries a label.


</div>

</div>
### isLabelIdentifierExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#islabelidentifierexpression"><span class="nf">isLabelIdentifierExpression</span></a><span class="p">(</span>element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java element` is a label reference expression.


</div>

</div>
### isLHSOfDot

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#islhsofdot"><span class="nf">isLHSOfDot</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java expression` is on the left-hand side (the receiver) of a qualified `#!java .`/`#!java ?.` expression.


</div>

</div>
### isLocal

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#islocal"><span class="nf">isLocal</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> declaration<span class="o">: </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java declaration` is local (declared inside a function body or other local scope).


</div>

</div>
### isNotInOperation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isnotinoperation"><span class="nf">isNotInOperation</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> binaryExpression<span class="o">: </span><a href="../-kt-binary-expression/index.html">KtBinaryExpression</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java binaryExpression` is a `#!java !in` (not-in) membership check.


</div>

</div>
### isNullConstant

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isnullconstant"><span class="nf">isNullConstant</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java expression` (after deparenthesizing) is the `#!java null` literal.


</div>

</div>
### isOrdinaryAssignment

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isordinaryassignment"><span class="nf">isOrdinaryAssignment</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java element` is a plain assignment (`#!java =`), excluding augmented assignments.


</div>

</div>
### isRemovableVariableDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isremovablevariabledeclaration"><span class="nf">isRemovableVariableDeclaration</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> declaration<span class="o">: </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java declaration` has a PSI form supported by unused-variable cleanup: a property can be removed and a destructuring entry can be replaced with `#!java _`. This is a syntactic classification; it does not determine whether the declaration is unused or whether removing it preserves behavior.


</div>

</div>
### isSafeCast

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#issafecast"><span class="nf">isSafeCast</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-binary-expression-with-type-r-h-s/index.html">KtBinaryExpressionWithTypeRHS</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java expression` is a safe cast (`#!java as?`).


</div>

</div>
### isScriptDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isscriptdeclaration"><span class="nf">isScriptDeclaration</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> namedDeclaration<span class="o">: </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java namedDeclaration` is a top-level declaration of a script.


</div>

</div>
### isSelectorInQualified

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isselectorinqualified"><span class="nf">isSelectorInQualified</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> nameExpression<span class="o">: </span><a href="../-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java nameExpression` is the selector of a qualified expression or qualified user type.


</div>

</div>
### isStatement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isstatement"><span class="nf">isStatement</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java element` appears in a statement position (its parent is a [`statement container`](index.md#isstatementcontainer)).


</div>

</div>
### isStatementContainer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isstatementcontainer"><span class="nf">isStatementContainer</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> container<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java container` is an element whose children are statements (a block, control-structure body, or `#!java when` entry).


</div>

</div>
### isTrait

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#istrait"><span class="nf">isTrait</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> classOrObject<span class="o">: </span><a href="../-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java classOrObject` is an interface.


</div>

</div>
### isTrueConstant

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#istrueconstant"><span class="nf">isTrueConstant</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> condition<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java condition` is the boolean literal `#!java true`.


</div>

</div>
### isUnsafeCast

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isunsafecast"><span class="nf">isUnsafeCast</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-binary-expression-with-type-r-h-s/index.html">KtBinaryExpressionWithTypeRHS</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java true` if `#!java expression` is an unsafe cast (`#!java as`).


</div>

</div>
### prevLeafIgnoringWhitespaceAndComments

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#prevleafignoringwhitespaceandcomments"><span class="nf">prevLeafIgnoringWhitespaceAndComments</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Returns the previous leaf before `#!java element`, skipping whitespace and comments, or `#!java null`.


</div>

</div>
### safeDeparenthesize

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#safedeparenthesize"><span class="nf">safeDeparenthesize</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div><div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#safedeparenthesize"><span class="nf">safeDeparenthesize</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">, </span>keepAnnotations<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Like [`deparenthesize`](index.md#deparenthesize), but returns `#!java expression` itself if there is nothing to unwrap.


</div>

</div>
### safeName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#safename"><span class="nf">safeName</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> name<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="p">)</span><span class="o">: </span>Name
</span></code></pre></div>
</div>


<div markdown>

Returns `#!java name` as a Name, or the special "no name provided" name if `#!java name` is `#!java null`.


</div>

</div>
### skipSiblingsBackwardByPredicate

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#skipsiblingsbackwardbypredicate"><span class="nf">skipSiblingsBackwardByPredicate</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> element<span class="o">: </span>PsiElement<span class="p">, </span>elementsToSkip<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/util/function/Predicate.html">Predicate</a><span class="o"><</span>PsiElement<span class="o">></span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Returns the first preceding sibling of `#!java element` not matched by `#!java elementsToSkip`, or `#!java null`.


</div>

</div>
### skipTrailingWhitespacesAndComments

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">Nullable</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#skiptrailingwhitespacesandcomments"><span class="nf">skipTrailingWhitespacesAndComments</span></a><span class="p">(</span><span class="se">@</span><span class="se">Nullable</span> element<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Returns the first following sibling of `#!java element` that is neither whitespace nor a comment, or `#!java null`.


</div>

</div>
### unquoteIdentifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#unquoteidentifier"><span class="nf">unquoteIdentifier</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> quoted<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Removes surrounding backticks from a backtick-quoted identifier, returning `#!java quoted` unchanged if it has none.


</div>

</div>
### unquoteIdentifierOrFieldReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#unquoteidentifierorfieldreference"><span class="nf">unquoteIdentifierOrFieldReference</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> quoted<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Like [`unquoteIdentifier`](index.md#unquoteidentifier), but also handles a leading `#!java $` field-reference prefix.


</div>

</div>
### visitChildren

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#visitchildren">D</a><span class="o">> </span><a href="index.html#visitchildren"><span class="nf">visitChildren</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span><a href="../-kt-element/index.html">KtElement</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NotNull</span> visitor<span class="o">: </span><a href="../-kt-visitor/index.html">KtVisitor</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a><span class="p">, </span><a href="index.html#visitchildren">D</a><span class="o">></span><span class="p">, </span>
    data<span class="o">: </span><a href="index.html#visitchildren">D</a>
<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Dispatches each direct [`KtElement`](../-kt-element/index.md) child of the given `#!java element` to the `#!java visitor`.


</div>

</div>
