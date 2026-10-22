---
tags:
 - jvm
title: "KtVisitorVoidWithParameter"
---

# KtVisitorVoidWithParameter

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="index.html">KtVisitorVoidWithParameter</a><span class="o"><</span><a href="index.html">P</a><span class="o">></span> : <a href="../-kt-visitor/index.html">KtVisitor</a><span class="o"><</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a><span class="p">, </span><a href="index.html">P</a><span class="o">> </span>
</span></code></pre></div>A convenience [`KtVisitor`](../-kt-visitor/index.md) for visitors that return nothing but still thread a data parameter through the traversal. 

Its `#!java visit*Void` methods take the data parameter but no result. The `#!java Void` suffix distinguishes them from the two-argument `#!java visit*` methods inherited from [`KtVisitor`](../-kt-visitor/index.md), which they cannot override because of the differing return type.

#### Parameters


 - <P>: the type of the data threaded through the traversal





</div>

## Constructors
### KtVisitorVoidWithParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Companion properties
### [`EMPTY_VISITOR`](index.md#empty_visitor)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#empty_visitor">EMPTY_VISITOR</a><span class="o">: </span>PsiElementVisitor
</span></code></pre></div>
</div>

</div>
## Functions
### visitAnnotatedExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitannotatedexpression"><span class="nf">visitAnnotatedExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-annotated-expression/index.html">KtAnnotatedExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitAnnotatedExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitannotatedexpressionvoid"><span class="nf">visitAnnotatedExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-annotated-expression/index.html">KtAnnotatedExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitAnnotation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitannotation"><span class="nf">visitAnnotation</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> annotation<span class="o">: </span><a href="../-kt-annotation/index.html">KtAnnotation</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitAnnotationEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitannotationentry"><span class="nf">visitAnnotationEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> annotationEntry<span class="o">: </span><a href="../-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitAnnotationEntryVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitannotationentryvoid"><span class="nf">visitAnnotationEntryVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> annotationEntry<span class="o">: </span><a href="../-kt-annotation-entry/index.html">KtAnnotationEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitAnnotationUseSiteTarget

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitannotationusesitetarget"><span class="nf">visitAnnotationUseSiteTarget</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> annotationTarget<span class="o">: </span><a href="../-kt-annotation-use-site-target/index.html">KtAnnotationUseSiteTarget</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitAnnotationVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitannotationvoid"><span class="nf">visitAnnotationVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> annotation<span class="o">: </span><a href="../-kt-annotation/index.html">KtAnnotation</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitAnonymousInitializer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitanonymousinitializer"><span class="nf">visitAnonymousInitializer</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> initializer<span class="o">: </span><a href="../-kt-anonymous-initializer/index.html">KtAnonymousInitializer</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitAnonymousInitializerVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitanonymousinitializervoid"><span class="nf">visitAnonymousInitializerVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> initializer<span class="o">: </span><a href="../-kt-anonymous-initializer/index.html">KtAnonymousInitializer</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitArgument

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitargument"><span class="nf">visitArgument</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> argument<span class="o">: </span><a href="../-kt-value-argument/index.html">KtValueArgument</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitArgumentVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitargumentvoid"><span class="nf">visitArgumentVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> argument<span class="o">: </span><a href="../-kt-value-argument/index.html">KtValueArgument</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitArrayAccessExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitarrayaccessexpression"><span class="nf">visitArrayAccessExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-array-access-expression/index.html">KtArrayAccessExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitArrayAccessExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitarrayaccessexpressionvoid"><span class="nf">visitArrayAccessExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-array-access-expression/index.html">KtArrayAccessExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitBackingField

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitbackingfield"><span class="nf">visitBackingField</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> accessor<span class="o">: </span><a href="../-kt-backing-field/index.html">KtBackingField</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitBinaryExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitbinaryexpression"><span class="nf">visitBinaryExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-binary-expression/index.html">KtBinaryExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>


<div markdown>

Visits the input expression using a stack if it's a string literals concatenation expression (to prevent potential stack overflow exception), otherwise visits the expression using regular recursive calls. If you need to handle nested binary expressions inside string literals concatenation, you have to override this method and write the necessary logic there.


</div>

</div>
### visitBinaryExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitbinaryexpressionvoid"><span class="nf">visitBinaryExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-binary-expression/index.html">KtBinaryExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`visitBinaryFile`](index.md#visitbinaryfile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitbinaryfile"><span class="nf">visitBinaryFile</span></a><span class="p">(</span>file<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiBinaryFile<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitBinaryWithTypeRHSExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitbinarywithtyperhsexpression"><span class="nf">visitBinaryWithTypeRHSExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-binary-expression-with-type-r-h-s/index.html">KtBinaryExpressionWithTypeRHS</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitBinaryWithTypeRHSExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitbinarywithtyperhsexpressionvoid"><span class="nf">visitBinaryWithTypeRHSExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-binary-expression-with-type-r-h-s/index.html">KtBinaryExpressionWithTypeRHS</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitBlockExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitblockexpression"><span class="nf">visitBlockExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-block-expression/index.html">KtBlockExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitBlockExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitblockexpressionvoid"><span class="nf">visitBlockExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-block-expression/index.html">KtBlockExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitBlockStringTemplateEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitblockstringtemplateentry"><span class="nf">visitBlockStringTemplateEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> entry<span class="o">: </span><a href="../-kt-block-string-template-entry/index.html">KtBlockStringTemplateEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitBlockStringTemplateEntryVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitblockstringtemplateentryvoid"><span class="nf">visitBlockStringTemplateEntryVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> entry<span class="o">: </span><a href="../-kt-block-string-template-entry/index.html">KtBlockStringTemplateEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitBreakExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitbreakexpression"><span class="nf">visitBreakExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-break-expression/index.html">KtBreakExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitBreakExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitbreakexpressionvoid"><span class="nf">visitBreakExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-break-expression/index.html">KtBreakExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitCallableReferenceExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitcallablereferenceexpression"><span class="nf">visitCallableReferenceExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-callable-reference-expression/index.html">KtCallableReferenceExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitCallableReferenceExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitcallablereferenceexpressionvoid"><span class="nf">visitCallableReferenceExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-callable-reference-expression/index.html">KtCallableReferenceExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitCallExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitcallexpression"><span class="nf">visitCallExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-call-expression/index.html">KtCallExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitCallExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitcallexpressionvoid"><span class="nf">visitCallExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-call-expression/index.html">KtCallExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitCatchSection

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitcatchsection"><span class="nf">visitCatchSection</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> catchClause<span class="o">: </span><a href="../-kt-catch-clause/index.html">KtCatchClause</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitCatchSectionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitcatchsectionvoid"><span class="nf">visitCatchSectionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> catchClause<span class="o">: </span><a href="../-kt-catch-clause/index.html">KtCatchClause</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitClass

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitclass"><span class="nf">visitClass</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> klass<span class="o">: </span><a href="../-kt-class/index.html">KtClass</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitClassBody

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitclassbody"><span class="nf">visitClassBody</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> classBody<span class="o">: </span><a href="../-kt-class-body/index.html">KtClassBody</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitClassBodyVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitclassbodyvoid"><span class="nf">visitClassBodyVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> classBody<span class="o">: </span><a href="../-kt-class-body/index.html">KtClassBody</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitClassInitializer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitclassinitializer"><span class="nf">visitClassInitializer</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> initializer<span class="o">: </span><a href="../-kt-class-initializer/index.html">KtClassInitializer</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitClassLiteralExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitclassliteralexpression"><span class="nf">visitClassLiteralExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-class-literal-expression/index.html">KtClassLiteralExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitClassLiteralExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitclassliteralexpressionvoid"><span class="nf">visitClassLiteralExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-class-literal-expression/index.html">KtClassLiteralExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitClassOrObject

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitclassorobject"><span class="nf">visitClassOrObject</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> classOrObject<span class="o">: </span><a href="../-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitClassVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitclassvoid"><span class="nf">visitClassVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> klass<span class="o">: </span><a href="../-kt-class/index.html">KtClass</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitCollectionLiteralExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitcollectionliteralexpression"><span class="nf">visitCollectionLiteralExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-collection-literal-expression/index.html">KtCollectionLiteralExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitCollectionLiteralExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitcollectionliteralexpressionvoid"><span class="nf">visitCollectionLiteralExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-collection-literal-expression/index.html">KtCollectionLiteralExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`visitComment`](index.md#visitcomment)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitcomment"><span class="nf">visitComment</span></a><span class="p">(</span>comment<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiComment<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitCompanionBlock

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitcompanionblock"><span class="nf">visitCompanionBlock</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> companionBlock<span class="o">: </span><a href="../-kt-companion-block/index.html">KtCompanionBlock</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitCompanionBlockVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitcompanionblockvoid"><span class="nf">visitCompanionBlockVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> companionBlock<span class="o">: </span><a href="../-kt-companion-block/index.html">KtCompanionBlock</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitConstantExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitconstantexpression"><span class="nf">visitConstantExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-constant-expression/index.html">KtConstantExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitConstantExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitconstantexpressionvoid"><span class="nf">visitConstantExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-constant-expression/index.html">KtConstantExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitConstructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitconstructor"><span class="nf">visitConstructor</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> constructor<span class="o">: </span><a href="../-kt-constructor/index.html">KtConstructor</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitConstructorCalleeExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitconstructorcalleeexpression"><span class="nf">visitConstructorCalleeExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> constructorCalleeExpression<span class="o">: </span><a href="../-kt-constructor-callee-expression/index.html">KtConstructorCalleeExpression</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitConstructorCalleeExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitconstructorcalleeexpressionvoid"><span class="nf">visitConstructorCalleeExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> constructorCalleeExpression<span class="o">: </span><a href="../-kt-constructor-callee-expression/index.html">KtConstructorCalleeExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitConstructorDelegationCall

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitconstructordelegationcall"><span class="nf">visitConstructorDelegationCall</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> call<span class="o">: </span><a href="../-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitConstructorDelegationCallVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitconstructordelegationcallvoid"><span class="nf">visitConstructorDelegationCallVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> call<span class="o">: </span><a href="../-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitContextParameterList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitcontextparameterlist"><span class="nf">visitContextParameterList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> contextParameterList<span class="o">: </span><a href="../-kt-context-parameter-list/index.html">KtContextParameterList</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitContextReceiver

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitcontextreceiver"><span class="nf">visitContextReceiver</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> contextReceiver<span class="o">: </span><a href="../-kt-context-receiver/index.html">KtContextReceiver</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitContextReceiverList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitcontextreceiverlist"><span class="nf">visitContextReceiverList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> contextReceiverList<span class="o">: </span><a href="../-kt-context-receiver-list/index.html">KtContextReceiverList</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

The visitor returns null since [`KtContextReceiverList`](../-kt-context-receiver-list/index.md) invoke both [`visitContextParameterList`](index.md#visitcontextparameterlist) and [`visitContextReceiverList`](index.md#visitcontextreceiverlist). Because of this, the visitor implementation must not implement both methods at the same time.


</div>

</div>
### visitContinueExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitcontinueexpression"><span class="nf">visitContinueExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-continue-expression/index.html">KtContinueExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitContinueExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitcontinueexpressionvoid"><span class="nf">visitContinueExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-continue-expression/index.html">KtContinueExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitdeclaration"><span class="nf">visitDeclaration</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> dcl<span class="o">: </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitDeclarationVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitdeclarationvoid"><span class="nf">visitDeclarationVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> dcl<span class="o">: </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitDelegatedSuperTypeEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitdelegatedsupertypeentry"><span class="nf">visitDelegatedSuperTypeEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> specifier<span class="o">: </span><a href="../-kt-delegated-super-type-entry/index.html">KtDelegatedSuperTypeEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitDelegatedSuperTypeEntryVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitdelegatedsupertypeentryvoid"><span class="nf">visitDelegatedSuperTypeEntryVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> specifier<span class="o">: </span><a href="../-kt-delegated-super-type-entry/index.html">KtDelegatedSuperTypeEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitDestructuringDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitdestructuringdeclaration"><span class="nf">visitDestructuringDeclaration</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> multiDeclaration<span class="o">: </span><a href="../-kt-destructuring-declaration/index.html">KtDestructuringDeclaration</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitDestructuringDeclarationEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitdestructuringdeclarationentry"><span class="nf">visitDestructuringDeclarationEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> multiDeclarationEntry<span class="o">: </span><a href="../-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitDestructuringDeclarationEntryVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitdestructuringdeclarationentryvoid"><span class="nf">visitDestructuringDeclarationEntryVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> multiDeclarationEntry<span class="o">: </span><a href="../-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitDestructuringDeclarationVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitdestructuringdeclarationvoid"><span class="nf">visitDestructuringDeclarationVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> multiDeclaration<span class="o">: </span><a href="../-kt-destructuring-declaration/index.html">KtDestructuringDeclaration</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`visitDirectory`](index.md#visitdirectory)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitdirectory"><span class="nf">visitDirectory</span></a><span class="p">(</span>dir<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiDirectory<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitDotQualifiedExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitdotqualifiedexpression"><span class="nf">visitDotQualifiedExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-dot-qualified-expression/index.html">KtDotQualifiedExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitDotQualifiedExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitdotqualifiedexpressionvoid"><span class="nf">visitDotQualifiedExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-dot-qualified-expression/index.html">KtDotQualifiedExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitDoubleColonExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitdoublecolonexpression"><span class="nf">visitDoubleColonExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-double-colon-expression/index.html">KtDoubleColonExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitDoubleColonExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitdoublecolonexpressionvoid"><span class="nf">visitDoubleColonExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-double-colon-expression/index.html">KtDoubleColonExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitDoWhileExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitdowhileexpression"><span class="nf">visitDoWhileExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-do-while-expression/index.html">KtDoWhileExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitDoWhileExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitdowhileexpressionvoid"><span class="nf">visitDoWhileExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-do-while-expression/index.html">KtDoWhileExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitDynamicType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitdynamictype"><span class="nf">visitDynamicType</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> type<span class="o">: </span><a href="../-kt-dynamic-type/index.html">KtDynamicType</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitDynamicTypeVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitdynamictypevoid"><span class="nf">visitDynamicTypeVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> type<span class="o">: </span><a href="../-kt-dynamic-type/index.html">KtDynamicType</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`visitElement`](index.md#visitelement)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitelement"><span class="nf">visitElement</span></a><span class="p">(</span>element<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiElement<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitEnumEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitenumentry"><span class="nf">visitEnumEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> enumEntry<span class="o">: </span><a href="../-kt-enum-entry/index.html">KtEnumEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitEnumEntryVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitenumentryvoid"><span class="nf">visitEnumEntryVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> enumEntry<span class="o">: </span><a href="../-kt-enum-entry/index.html">KtEnumEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`visitErrorElement`](index.md#visiterrorelement)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visiterrorelement"><span class="nf">visitErrorElement</span></a><span class="p">(</span>element<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiErrorElement<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitErrorSafeQualifiedExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visiterrorsafequalifiedexpression"><span class="nf">visitErrorSafeQualifiedExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-error-safe-qualified-expression/index.html">KtErrorSafeQualifiedExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitErrorSafeQualifiedExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visiterrorsafequalifiedexpressionvoid"><span class="nf">visitErrorSafeQualifiedExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-error-safe-qualified-expression/index.html">KtErrorSafeQualifiedExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitEscapeStringTemplateEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitescapestringtemplateentry"><span class="nf">visitEscapeStringTemplateEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> entry<span class="o">: </span><a href="../-kt-escape-string-template-entry/index.html">KtEscapeStringTemplateEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitEscapeStringTemplateEntryVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitescapestringtemplateentryvoid"><span class="nf">visitEscapeStringTemplateEntryVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> entry<span class="o">: </span><a href="../-kt-escape-string-template-entry/index.html">KtEscapeStringTemplateEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitexpression"><span class="nf">visitExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitexpressionvoid"><span class="nf">visitExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitExpressionWithLabel

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitexpressionwithlabel"><span class="nf">visitExpressionWithLabel</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-expression-with-label/index.html">KtExpressionWithLabel</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitExpressionWithLabelVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitexpressionwithlabelvoid"><span class="nf">visitExpressionWithLabelVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-expression-with-label/index.html">KtExpressionWithLabel</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`visitFile`](index.md#visitfile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitfile"><span class="nf">visitFile</span></a><span class="p">(</span>psiFile<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiFile<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitFileAnnotationList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitfileannotationlist"><span class="nf">visitFileAnnotationList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> fileAnnotationList<span class="o">: </span><a href="../-kt-file-annotation-list/index.html">KtFileAnnotationList</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitFinallySection

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitfinallysection"><span class="nf">visitFinallySection</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> finallySection<span class="o">: </span><a href="../-kt-finally-section/index.html">KtFinallySection</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitFinallySectionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitfinallysectionvoid"><span class="nf">visitFinallySectionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> finallySection<span class="o">: </span><a href="../-kt-finally-section/index.html">KtFinallySection</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitForExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitforexpression"><span class="nf">visitForExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-for-expression/index.html">KtForExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitForExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitforexpressionvoid"><span class="nf">visitForExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-for-expression/index.html">KtForExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitFunctionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitfunctiontype"><span class="nf">visitFunctionType</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> type<span class="o">: </span><a href="../-kt-function-type/index.html">KtFunctionType</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitFunctionTypeVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitfunctiontypevoid"><span class="nf">visitFunctionTypeVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> type<span class="o">: </span><a href="../-kt-function-type/index.html">KtFunctionType</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitIfExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitifexpression"><span class="nf">visitIfExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-if-expression/index.html">KtIfExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitIfExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitifexpressionvoid"><span class="nf">visitIfExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-if-expression/index.html">KtIfExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitImportAlias

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitimportalias"><span class="nf">visitImportAlias</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> importAlias<span class="o">: </span><a href="../-kt-import-alias/index.html">KtImportAlias</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitImportAliasVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitimportaliasvoid"><span class="nf">visitImportAliasVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> importAlias<span class="o">: </span><a href="../-kt-import-alias/index.html">KtImportAlias</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitImportDirective

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitimportdirective"><span class="nf">visitImportDirective</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> importDirective<span class="o">: </span><a href="../-kt-import-directive/index.html">KtImportDirective</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitImportDirectiveVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitimportdirectivevoid"><span class="nf">visitImportDirectiveVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> importDirective<span class="o">: </span><a href="../-kt-import-directive/index.html">KtImportDirective</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitImportList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitimportlist"><span class="nf">visitImportList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> importList<span class="o">: </span><a href="../-kt-import-list/index.html">KtImportList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitImportListVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitimportlistvoid"><span class="nf">visitImportListVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> importList<span class="o">: </span><a href="../-kt-import-list/index.html">KtImportList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitInitializerList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitinitializerlist"><span class="nf">visitInitializerList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> list<span class="o">: </span><a href="../-kt-initializer-list/index.html">KtInitializerList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitInitializerListVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitinitializerlistvoid"><span class="nf">visitInitializerListVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> list<span class="o">: </span><a href="../-kt-initializer-list/index.html">KtInitializerList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitIntersectionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitintersectiontype"><span class="nf">visitIntersectionType</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> definitelyNotNullType<span class="o">: </span><a href="../-kt-intersection-type/index.html">KtIntersectionType</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitIsExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitisexpression"><span class="nf">visitIsExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-is-expression/index.html">KtIsExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitIsExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitisexpressionvoid"><span class="nf">visitIsExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-is-expression/index.html">KtIsExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitKtCommonFile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitktcommonfile"><span class="nf">visitKtCommonFile</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> file<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-common-file/index.html">KtCommonFile</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

Required for [`KtCommonFile`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-common-file/index.md) implementation. It is not expected to be used, because [`KtCommonFile`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-common-file/index.md) should not be used directly.


</div>

</div>
### visitKtElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitktelement"><span class="nf">visitKtElement</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span><a href="../-kt-element/index.html">KtElement</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitKtElementVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitktelementvoid"><span class="nf">visitKtElementVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> element<span class="o">: </span><a href="../-kt-element/index.html">KtElement</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitKtFile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitktfile"><span class="nf">visitKtFile</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> file<span class="o">: </span><a href="../-kt-file/index.html">KtFile</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitKtFileVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitktfilevoid"><span class="nf">visitKtFileVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> file<span class="o">: </span><a href="../-kt-file/index.html">KtFile</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitLabeledExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitlabeledexpression"><span class="nf">visitLabeledExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-labeled-expression/index.html">KtLabeledExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitLabeledExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitlabeledexpressionvoid"><span class="nf">visitLabeledExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-labeled-expression/index.html">KtLabeledExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitLambdaExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitlambdaexpression"><span class="nf">visitLambdaExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-lambda-expression/index.html">KtLambdaExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitLambdaExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitlambdaexpressionvoid"><span class="nf">visitLambdaExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-lambda-expression/index.html">KtLambdaExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitLiteralStringTemplateEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitliteralstringtemplateentry"><span class="nf">visitLiteralStringTemplateEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> entry<span class="o">: </span><a href="../-kt-literal-string-template-entry/index.html">KtLiteralStringTemplateEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitLiteralStringTemplateEntryVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitliteralstringtemplateentryvoid"><span class="nf">visitLiteralStringTemplateEntryVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> entry<span class="o">: </span><a href="../-kt-literal-string-template-entry/index.html">KtLiteralStringTemplateEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitLoopExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitloopexpression"><span class="nf">visitLoopExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> loopExpression<span class="o">: </span><a href="../-kt-loop-expression/index.html">KtLoopExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitLoopExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitloopexpressionvoid"><span class="nf">visitLoopExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> loopExpression<span class="o">: </span><a href="../-kt-loop-expression/index.html">KtLoopExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitModifierList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitmodifierlist"><span class="nf">visitModifierList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> list<span class="o">: </span><a href="../-kt-modifier-list/index.html">KtModifierList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitModifierListVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitmodifierlistvoid"><span class="nf">visitModifierListVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> list<span class="o">: </span><a href="../-kt-modifier-list/index.html">KtModifierList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitNamedDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitnameddeclaration"><span class="nf">visitNamedDeclaration</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> declaration<span class="o">: </span><a href="../-kt-named-declaration/index.html">KtNamedDeclaration</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitNamedDeclarationVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitnameddeclarationvoid"><span class="nf">visitNamedDeclarationVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> declaration<span class="o">: </span><a href="../-kt-named-declaration/index.html">KtNamedDeclaration</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitNamedFunction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitnamedfunction"><span class="nf">visitNamedFunction</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> function<span class="o">: </span><a href="../-kt-named-function/index.html">KtNamedFunction</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitNamedFunctionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitnamedfunctionvoid"><span class="nf">visitNamedFunctionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> function<span class="o">: </span><a href="../-kt-named-function/index.html">KtNamedFunction</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitNullableType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitnullabletype"><span class="nf">visitNullableType</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> nullableType<span class="o">: </span><a href="../-kt-nullable-type/index.html">KtNullableType</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitNullableTypeVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitnullabletypevoid"><span class="nf">visitNullableTypeVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> nullableType<span class="o">: </span><a href="../-kt-nullable-type/index.html">KtNullableType</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitObjectDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitobjectdeclaration"><span class="nf">visitObjectDeclaration</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> declaration<span class="o">: </span><a href="../-kt-object-declaration/index.html">KtObjectDeclaration</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitObjectDeclarationVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitobjectdeclarationvoid"><span class="nf">visitObjectDeclarationVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> declaration<span class="o">: </span><a href="../-kt-object-declaration/index.html">KtObjectDeclaration</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitObjectLiteralExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitobjectliteralexpression"><span class="nf">visitObjectLiteralExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-object-literal-expression/index.html">KtObjectLiteralExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitObjectLiteralExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitobjectliteralexpressionvoid"><span class="nf">visitObjectLiteralExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-object-literal-expression/index.html">KtObjectLiteralExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`visitOuterLanguageElement`](index.md#visitouterlanguageelement)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitouterlanguageelement"><span class="nf">visitOuterLanguageElement</span></a><span class="p">(</span>element<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> OuterLanguageElement<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitPackageDirective

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitpackagedirective"><span class="nf">visitPackageDirective</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> directive<span class="o">: </span><a href="../-kt-package-directive/index.html">KtPackageDirective</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitparameter"><span class="nf">visitParameter</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> parameter<span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitParameterList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitparameterlist"><span class="nf">visitParameterList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> list<span class="o">: </span><a href="../-kt-parameter-list/index.html">KtParameterList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitParameterListVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitparameterlistvoid"><span class="nf">visitParameterListVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> list<span class="o">: </span><a href="../-kt-parameter-list/index.html">KtParameterList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitParameterVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitparametervoid"><span class="nf">visitParameterVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> parameter<span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitParenthesizedExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitparenthesizedexpression"><span class="nf">visitParenthesizedExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-parenthesized-expression/index.html">KtParenthesizedExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitParenthesizedExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitparenthesizedexpressionvoid"><span class="nf">visitParenthesizedExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-parenthesized-expression/index.html">KtParenthesizedExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`visitPlainText`](index.md#visitplaintext)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitplaintext"><span class="nf">visitPlainText</span></a><span class="p">(</span>content<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiPlainText<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`visitPlainTextFile`](index.md#visitplaintextfile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitplaintextfile"><span class="nf">visitPlainTextFile</span></a><span class="p">(</span>file<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiPlainTextFile<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitPostfixExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitpostfixexpression"><span class="nf">visitPostfixExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-postfix-expression/index.html">KtPostfixExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitPostfixExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitpostfixexpressionvoid"><span class="nf">visitPostfixExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-postfix-expression/index.html">KtPostfixExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitPrefixExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitprefixexpression"><span class="nf">visitPrefixExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-prefix-expression/index.html">KtPrefixExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitPrefixExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitprefixexpressionvoid"><span class="nf">visitPrefixExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-prefix-expression/index.html">KtPrefixExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitPrimaryConstructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitprimaryconstructor"><span class="nf">visitPrimaryConstructor</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> constructor<span class="o">: </span><a href="../-kt-primary-constructor/index.html">KtPrimaryConstructor</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitPrimaryConstructorVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitprimaryconstructorvoid"><span class="nf">visitPrimaryConstructorVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> constructor<span class="o">: </span><a href="../-kt-primary-constructor/index.html">KtPrimaryConstructor</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitProperty

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitproperty"><span class="nf">visitProperty</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> property<span class="o">: </span><a href="../-kt-property/index.html">KtProperty</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitPropertyAccessor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitpropertyaccessor"><span class="nf">visitPropertyAccessor</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> accessor<span class="o">: </span><a href="../-kt-property-accessor/index.html">KtPropertyAccessor</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitPropertyAccessorVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitpropertyaccessorvoid"><span class="nf">visitPropertyAccessorVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> accessor<span class="o">: </span><a href="../-kt-property-accessor/index.html">KtPropertyAccessor</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitPropertyDelegate

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitpropertydelegate"><span class="nf">visitPropertyDelegate</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> delegate<span class="o">: </span><a href="../-kt-property-delegate/index.html">KtPropertyDelegate</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitPropertyDelegateVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitpropertydelegatevoid"><span class="nf">visitPropertyDelegateVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> delegate<span class="o">: </span><a href="../-kt-property-delegate/index.html">KtPropertyDelegate</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitPropertyVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitpropertyvoid"><span class="nf">visitPropertyVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> property<span class="o">: </span><a href="../-kt-property/index.html">KtProperty</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitQualifiedExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitqualifiedexpression"><span class="nf">visitQualifiedExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitQualifiedExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitqualifiedexpressionvoid"><span class="nf">visitQualifiedExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-qualified-expression/index.html">KtQualifiedExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitReferenceExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitreferenceexpression"><span class="nf">visitReferenceExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-reference-expression/index.html">KtReferenceExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitReferenceExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitreferenceexpressionvoid"><span class="nf">visitReferenceExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-reference-expression/index.html">KtReferenceExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitReturnExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitreturnexpression"><span class="nf">visitReturnExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-return-expression/index.html">KtReturnExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitReturnExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitreturnexpressionvoid"><span class="nf">visitReturnExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-return-expression/index.html">KtReturnExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitSafeQualifiedExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitsafequalifiedexpression"><span class="nf">visitSafeQualifiedExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-safe-qualified-expression/index.html">KtSafeQualifiedExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitSafeQualifiedExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitsafequalifiedexpressionvoid"><span class="nf">visitSafeQualifiedExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-safe-qualified-expression/index.html">KtSafeQualifiedExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitScript

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitscript"><span class="nf">visitScript</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> script<span class="o">: </span><a href="../-kt-script/index.html">KtScript</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitScriptInitializer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitscriptinitializer"><span class="nf">visitScriptInitializer</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> initializer<span class="o">: </span><a href="../-kt-script-initializer/index.html">KtScriptInitializer</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitScriptVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitscriptvoid"><span class="nf">visitScriptVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> script<span class="o">: </span><a href="../-kt-script/index.html">KtScript</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitSecondaryConstructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitsecondaryconstructor"><span class="nf">visitSecondaryConstructor</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> constructor<span class="o">: </span><a href="../-kt-secondary-constructor/index.html">KtSecondaryConstructor</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitSecondaryConstructorVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitsecondaryconstructorvoid"><span class="nf">visitSecondaryConstructorVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> constructor<span class="o">: </span><a href="../-kt-secondary-constructor/index.html">KtSecondaryConstructor</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitSimpleNameExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitsimplenameexpression"><span class="nf">visitSimpleNameExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitSimpleNameExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitsimplenameexpressionvoid"><span class="nf">visitSimpleNameExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitSimpleNameStringTemplateEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitsimplenamestringtemplateentry"><span class="nf">visitSimpleNameStringTemplateEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> entry<span class="o">: </span><a href="../-kt-simple-name-string-template-entry/index.html">KtSimpleNameStringTemplateEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitSimpleNameStringTemplateEntryVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitsimplenamestringtemplateentryvoid"><span class="nf">visitSimpleNameStringTemplateEntryVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> entry<span class="o">: </span><a href="../-kt-simple-name-string-template-entry/index.html">KtSimpleNameStringTemplateEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitStringInterpolationPrefix

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitstringinterpolationprefix"><span class="nf">visitStringInterpolationPrefix</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> prefix<span class="o">: </span><a href="../-kt-string-interpolation-prefix/index.html">KtStringInterpolationPrefix</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>


<div markdown>

**See also**



 - [`KtStringInterpolationPrefix`](../-kt-string-interpolation-prefix/index.md)



</div>

</div>
### visitStringTemplateEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitstringtemplateentry"><span class="nf">visitStringTemplateEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> entry<span class="o">: </span><a href="../-kt-string-template-entry/index.html">KtStringTemplateEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitStringTemplateEntryVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitstringtemplateentryvoid"><span class="nf">visitStringTemplateEntryVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> entry<span class="o">: </span><a href="../-kt-string-template-entry/index.html">KtStringTemplateEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitStringTemplateEntryWithExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitstringtemplateentrywithexpression"><span class="nf">visitStringTemplateEntryWithExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> entry<span class="o">: </span><a href="../-kt-string-template-entry-with-expression/index.html">KtStringTemplateEntryWithExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitStringTemplateEntryWithExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitstringtemplateentrywithexpressionvoid"><span class="nf">visitStringTemplateEntryWithExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> entry<span class="o">: </span><a href="../-kt-string-template-entry-with-expression/index.html">KtStringTemplateEntryWithExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitStringTemplateExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitstringtemplateexpression"><span class="nf">visitStringTemplateExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitStringTemplateExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitstringtemplateexpressionvoid"><span class="nf">visitStringTemplateExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-string-template-expression/index.html">KtStringTemplateExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitSuperExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitsuperexpression"><span class="nf">visitSuperExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-super-expression/index.html">KtSuperExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitSuperExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitsuperexpressionvoid"><span class="nf">visitSuperExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-super-expression/index.html">KtSuperExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitSuperTypeCallEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitsupertypecallentry"><span class="nf">visitSuperTypeCallEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> call<span class="o">: </span><a href="../-kt-super-type-call-entry/index.html">KtSuperTypeCallEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitSuperTypeCallEntryVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitsupertypecallentryvoid"><span class="nf">visitSuperTypeCallEntryVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> call<span class="o">: </span><a href="../-kt-super-type-call-entry/index.html">KtSuperTypeCallEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitSuperTypeEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitsupertypeentry"><span class="nf">visitSuperTypeEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> specifier<span class="o">: </span><a href="../-kt-super-type-entry/index.html">KtSuperTypeEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitSuperTypeEntryVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitsupertypeentryvoid"><span class="nf">visitSuperTypeEntryVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> specifier<span class="o">: </span><a href="../-kt-super-type-entry/index.html">KtSuperTypeEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitSuperTypeList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitsupertypelist"><span class="nf">visitSuperTypeList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> list<span class="o">: </span><a href="../-kt-super-type-list/index.html">KtSuperTypeList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitSuperTypeListEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitsupertypelistentry"><span class="nf">visitSuperTypeListEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> specifier<span class="o">: </span><a href="../-kt-super-type-list-entry/index.html">KtSuperTypeListEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitSuperTypeListEntryVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitsupertypelistentryvoid"><span class="nf">visitSuperTypeListEntryVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> specifier<span class="o">: </span><a href="../-kt-super-type-list-entry/index.html">KtSuperTypeListEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitSuperTypeListVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitsupertypelistvoid"><span class="nf">visitSuperTypeListVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> list<span class="o">: </span><a href="../-kt-super-type-list/index.html">KtSuperTypeList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitThisExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitthisexpression"><span class="nf">visitThisExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-this-expression/index.html">KtThisExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitThisExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitthisexpressionvoid"><span class="nf">visitThisExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-this-expression/index.html">KtThisExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitThrowExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitthrowexpression"><span class="nf">visitThrowExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-throw-expression/index.html">KtThrowExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitThrowExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitthrowexpressionvoid"><span class="nf">visitThrowExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-throw-expression/index.html">KtThrowExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitTryExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visittryexpression"><span class="nf">visitTryExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-try-expression/index.html">KtTryExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitTryExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visittryexpressionvoid"><span class="nf">visitTryExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-try-expression/index.html">KtTryExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitTypeAlias

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visittypealias"><span class="nf">visitTypeAlias</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> typeAlias<span class="o">: </span><a href="../-kt-type-alias/index.html">KtTypeAlias</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitTypeArgumentList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visittypeargumentlist"><span class="nf">visitTypeArgumentList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> typeArgumentList<span class="o">: </span><a href="../-kt-type-argument-list/index.html">KtTypeArgumentList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitTypeArgumentListVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visittypeargumentlistvoid"><span class="nf">visitTypeArgumentListVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> typeArgumentList<span class="o">: </span><a href="../-kt-type-argument-list/index.html">KtTypeArgumentList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitTypeConstraint

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visittypeconstraint"><span class="nf">visitTypeConstraint</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> constraint<span class="o">: </span><a href="../-kt-type-constraint/index.html">KtTypeConstraint</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitTypeConstraintList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visittypeconstraintlist"><span class="nf">visitTypeConstraintList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> list<span class="o">: </span><a href="../-kt-type-constraint-list/index.html">KtTypeConstraintList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitTypeConstraintListVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visittypeconstraintlistvoid"><span class="nf">visitTypeConstraintListVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> list<span class="o">: </span><a href="../-kt-type-constraint-list/index.html">KtTypeConstraintList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitTypeConstraintVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visittypeconstraintvoid"><span class="nf">visitTypeConstraintVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> constraint<span class="o">: </span><a href="../-kt-type-constraint/index.html">KtTypeConstraint</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitTypeParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visittypeparameter"><span class="nf">visitTypeParameter</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> parameter<span class="o">: </span><a href="../-kt-type-parameter/index.html">KtTypeParameter</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitTypeParameterList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visittypeparameterlist"><span class="nf">visitTypeParameterList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> list<span class="o">: </span><a href="../-kt-type-parameter-list/index.html">KtTypeParameterList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitTypeParameterListVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visittypeparameterlistvoid"><span class="nf">visitTypeParameterListVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> list<span class="o">: </span><a href="../-kt-type-parameter-list/index.html">KtTypeParameterList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitTypeParameterVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visittypeparametervoid"><span class="nf">visitTypeParameterVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> parameter<span class="o">: </span><a href="../-kt-type-parameter/index.html">KtTypeParameter</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitTypeProjection

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visittypeprojection"><span class="nf">visitTypeProjection</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> typeProjection<span class="o">: </span><a href="../-kt-type-projection/index.html">KtTypeProjection</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitTypeProjectionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visittypeprojectionvoid"><span class="nf">visitTypeProjectionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> typeProjection<span class="o">: </span><a href="../-kt-type-projection/index.html">KtTypeProjection</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitTypeReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visittypereference"><span class="nf">visitTypeReference</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> typeReference<span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitTypeReferenceVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visittypereferencevoid"><span class="nf">visitTypeReferenceVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> typeReference<span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitUnaryExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitunaryexpression"><span class="nf">visitUnaryExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-unary-expression/index.html">KtUnaryExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitUnaryExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitunaryexpressionvoid"><span class="nf">visitUnaryExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-unary-expression/index.html">KtUnaryExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitUnionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visituniontype"><span class="nf">visitUnionType</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> unionType<span class="o">: </span><a href="../-kt-union-type/index.html">KtUnionType</a><span class="p">, </span>data<span class="o">: </span><a href="../-kt-visitor/index.html">D</a><span class="p">)</span><span class="o">: </span><a href="../-kt-visitor/index.html">R</a>
</span></code></pre></div>
</div>

</div>
### visitUserType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitusertype"><span class="nf">visitUserType</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> type<span class="o">: </span><a href="../-kt-user-type/index.html">KtUserType</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitUserTypeVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitusertypevoid"><span class="nf">visitUserTypeVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> type<span class="o">: </span><a href="../-kt-user-type/index.html">KtUserType</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitValueArgumentList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitvalueargumentlist"><span class="nf">visitValueArgumentList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> list<span class="o">: </span><a href="../-kt-value-argument-list/index.html">KtValueArgumentList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitValueArgumentListVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitvalueargumentlistvoid"><span class="nf">visitValueArgumentListVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> list<span class="o">: </span><a href="../-kt-value-argument-list/index.html">KtValueArgumentList</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitWhenConditionInRange

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitwhenconditioninrange"><span class="nf">visitWhenConditionInRange</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> condition<span class="o">: </span><a href="../-kt-when-condition-in-range/index.html">KtWhenConditionInRange</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitWhenConditionInRangeVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitwhenconditioninrangevoid"><span class="nf">visitWhenConditionInRangeVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> condition<span class="o">: </span><a href="../-kt-when-condition-in-range/index.html">KtWhenConditionInRange</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitWhenConditionIsPattern

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitwhenconditionispattern"><span class="nf">visitWhenConditionIsPattern</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> condition<span class="o">: </span><a href="../-kt-when-condition-is-pattern/index.html">KtWhenConditionIsPattern</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitWhenConditionIsPatternVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitwhenconditionispatternvoid"><span class="nf">visitWhenConditionIsPatternVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> condition<span class="o">: </span><a href="../-kt-when-condition-is-pattern/index.html">KtWhenConditionIsPattern</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitWhenConditionWithExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitwhenconditionwithexpression"><span class="nf">visitWhenConditionWithExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> condition<span class="o">: </span><a href="../-kt-when-condition-with-expression/index.html">KtWhenConditionWithExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitWhenConditionWithExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitwhenconditionwithexpressionvoid"><span class="nf">visitWhenConditionWithExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> condition<span class="o">: </span><a href="../-kt-when-condition-with-expression/index.html">KtWhenConditionWithExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitWhenEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitwhenentry"><span class="nf">visitWhenEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> ktWhenEntry<span class="o">: </span><a href="../-kt-when-entry/index.html">KtWhenEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitWhenEntryVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitwhenentryvoid"><span class="nf">visitWhenEntryVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> ktWhenEntry<span class="o">: </span><a href="../-kt-when-entry/index.html">KtWhenEntry</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitWhenExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitwhenexpression"><span class="nf">visitWhenExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-when-expression/index.html">KtWhenExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitWhenExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitwhenexpressionvoid"><span class="nf">visitWhenExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-when-expression/index.html">KtWhenExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### visitWhileExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#visitwhileexpression"><span class="nf">visitWhileExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-while-expression/index.html">KtWhileExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html">Void</a>
</span></code></pre></div>
</div>

</div>
### visitWhileExpressionVoid

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitwhileexpressionvoid"><span class="nf">visitWhileExpressionVoid</span></a><span class="p">(</span><span class="se">@</span><span class="se">NotNull</span> expression<span class="o">: </span><a href="../-kt-while-expression/index.html">KtWhileExpression</a><span class="p">, </span>data<span class="o">: </span><a href="index.html">P</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`visitWhiteSpace`](index.md#visitwhitespace)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#visitwhitespace"><span class="nf">visitWhiteSpace</span></a><span class="p">(</span>space<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PsiWhiteSpace<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
