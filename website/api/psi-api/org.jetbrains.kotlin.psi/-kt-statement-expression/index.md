---
tags:
 - jvm
title: "KtStatementExpression"
---

# KtStatementExpression

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KtStatementExpression</a>
</span></code></pre></div>This is an interface to show that [`KtExpression`](../-kt-expression/index.md) is not actually an expression (in the sense that this expression can be placed after "val x = "). This is a possibly redundant interface; all inheritors of this interface should be refactored so that they are not [`KtExpression`](../-kt-expression/index.md), after such refactoring, this interface can be removed.

#### Inheritors


 - [`KtFinallySection`](../-kt-finally-section/index.md)
 - [`KtSuperExpression`](../-kt-super-expression/index.md)
 - [`KtLoopExpression`](../-kt-loop-expression/index.md)
 - [`KtReturnExpression`](../-kt-return-expression/index.md)
 - [`KtBreakExpression`](../-kt-break-expression/index.md)
 - [`KtNamedDeclaration`](../-kt-named-declaration/index.md)
 - [`KtBlockExpression`](../-kt-block-expression/index.md)
 - [`KtContinueExpression`](../-kt-continue-expression/index.md)
 - [`KtThrowExpression`](../-kt-throw-expression/index.md)
 - [`KtAnonymousInitializer`](../-kt-anonymous-initializer/index.md)



</div>

