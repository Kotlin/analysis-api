---
tags:
 - jvm
title: "KtPsiFactory"
---

# KtPsiFactory

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KtPsiFactory</a>
</span></code></pre></div>A factory for creating Kotlin PSI elements programmatically, usually by parsing a snippet of source text.

Most methods follow a `createX(text)` shape: they build a throwaway [`KtFile`](../-kt-file/index.md) containing the given text and return the requested element from it. Unless noted otherwise, the text must be a syntactically valid form of the requested element, and the method throws if it cannot be produced; `...IfPossible` variants return `null` instead.

The created elements are detached from any real file and are not meant to be analyzed, unless the factory is created with a context via [`contextual`](-companion/index.md#contextual).

#### Parameters


 - markGenerated: This needs to be set to true if the `KtPsiFactory` is going to be used for creating elements that are going to be inserted in the user source code (this ensures that the elements will be formatted correctly). In other cases, `markGenerated` should be false, which saves time and memory.





</div>

## Constructors
### KtPsiFactory

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html"><span class="se">JvmOverloads</span></a>
<span class="kd">constructor</span><span class="p">(</span>project<span class="o">: </span>Project<span class="p">, </span>markGenerated<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>
    project<span class="o">: </span>Project<span class="p">, </span>
    markGenerated<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">, </span>
    eventSystemEnabled<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Types
### [`CallableBuilder`](-callable-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-callable-builder/index.html">CallableBuilder</a><span class="p">(</span>target<span class="o">: </span><a href="-callable-builder/-target/index.html">KtPsiFactory.CallableBuilder.Target</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

A fluent builder for a function, constructor, or read-only property declaration string. The available steps and their order depend on the [`Target`](-callable-builder/-target/index.md); call [`asString`](-callable-builder/index.md#asstring) to obtain the resulting text, then pass it to the matching `create*` method.


</div>

</div>
### [`ClassHeaderBuilder`](-class-header-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-class-header-builder/index.html">ClassHeaderBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

A fluent builder for a class header string, assembled in a fixed order: modifiers, name, type parameters, base class, and type constraints. Call [`asString`](-class-header-builder/index.md#asstring) to obtain the resulting header text, then pass it to [`createClass`](index.md#createclass) to build the PSI.


</div>

</div>
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Functions
### buildDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">KtPsiFactory</a><span class="p">.</span><a href="index.html#builddeclaration"><span class="nf">buildDeclaration</span></a><span class="p">(</span>build<span class="o">: </span><a href="../-builder-by-pattern/index.html">BuilderByPattern</a><span class="o"><</span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="o">></span><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../-kt-declaration/index.html">KtDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a declaration using a [`BuilderByPattern`](../-builder-by-pattern/index.md) configured by [`build`](index.md#builddeclaration).


</div>

</div>
### buildDestructuringDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">KtPsiFactory</a><span class="p">.</span><a href="index.html#builddestructuringdeclaration"><span class="nf">buildDestructuringDeclaration</span></a><span class="p">(</span>build<span class="o">: </span><a href="../-builder-by-pattern/index.html">BuilderByPattern</a><span class="o"><</span><a href="../-kt-destructuring-declaration/index.html">KtDestructuringDeclaration</a><span class="o">></span><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../-kt-destructuring-declaration/index.html">KtDestructuringDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a destructuring declaration using a [`BuilderByPattern`](../-builder-by-pattern/index.md) configured by [`build`](index.md#builddestructuringdeclaration).


</div>

</div>
### buildExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">KtPsiFactory</a><span class="p">.</span><a href="index.html#buildexpression"><span class="nf">buildExpression</span></a><span class="p">(</span>reformat<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">, </span>build<span class="o">: </span><a href="../-builder-by-pattern/index.html">BuilderByPattern</a><span class="o"><</span><a href="../-kt-expression/index.html">KtExpression</a><span class="o">></span><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Builds an expression using a [`BuilderByPattern`](../-builder-by-pattern/index.md) configured by [`build`](index.md#buildexpression).


</div>

</div>
### buildValueArgumentList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">KtPsiFactory</a><span class="p">.</span><a href="index.html#buildvalueargumentlist"><span class="nf">buildValueArgumentList</span></a><span class="p">(</span>build<span class="o">: </span><a href="../-builder-by-pattern/index.html">BuilderByPattern</a><span class="o"><</span><a href="../-kt-value-argument-list/index.html">KtValueArgumentList</a><span class="o">></span><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="../-kt-value-argument-list/index.html">KtValueArgumentList</a>
</span></code></pre></div>
</div>


<div markdown>

Builds a value argument list using a [`BuilderByPattern`](../-builder-by-pattern/index.md) configured by [`build`](index.md#buildvalueargumentlist).


</div>

</div>
### creareDelegatedSuperTypeEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#crearedelegatedsupertypeentry"><span class="nf">creareDelegatedSuperTypeEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-constructor-delegation-call/index.html">KtConstructorDelegationCall</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a constructor delegation call from the given [`text`](index.md#crearedelegatedsupertypeentry) (for example, `"super(1)"` or `"this()"`).


</div>

</div>
### createAnnotationEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createannotationentry"><span class="nf">createAnnotationEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-annotation-entry/index.html">KtAnnotationEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an annotation entry from the given [`text`](index.md#createannotationentry) (for example, `"@Suppress(\"x\")"`).


</div>

</div>
### createAnonymousInitializer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createanonymousinitializer"><span class="nf">createAnonymousInitializer</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-anonymous-initializer/index.html">KtAnonymousInitializer</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an empty `init` block.


</div>

</div>
### createArgument

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createargument"><span class="nf">createArgument</span></a><span class="p">(</span>
    expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="o">?</span><span class="p">, </span>
    name<span class="o">: </span>Name<span class="o">?</span><span class="o"> = </span>null<span class="p">, </span>
    isSpread<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span>
    reformat<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span>
<span class="p">)</span><span class="o">: </span><a href="../-kt-value-argument/index.html">KtValueArgument</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a value argument wrapping the given [`expression`](index.md#createargument), optionally named ([`name`](index.md#createargument)) and/or spread ([`isSpread`](index.md#createargument)).

**Parameters**



 - reformat: whether to reformat the created argument





</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createargument"><span class="nf">createArgument</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-value-argument/index.html">KtValueArgument</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a value argument from the given [`text`](index.md#createargument) (for example, `"x = 1"` or `"*array"`).


</div>

</div>
### createBlock

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createblock"><span class="nf">createBlock</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> bodyText<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-block-expression/index.html">KtBlockExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a function body block wrapping the given [`bodyText`](index.md#createblock).


</div>

</div>
### createBlockCodeFragment

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createblockcodefragment"><span class="nf">createBlockCodeFragment</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>context<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-kt-block-code-fragment/index.html">KtBlockCodeFragment</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KtBlockCodeFragment`](../-kt-block-code-fragment/index.md) for the given [`text`](index.md#createblockcodefragment), resolved in the given [`context`](index.md#createblockcodefragment).


</div>

</div>
### createBlockStringTemplateEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createblockstringtemplateentry"><span class="nf">createBlockStringTemplateEntry</span></a><span class="p">(</span>expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="../-kt-string-template-entry-with-expression/index.html">KtStringTemplateEntryWithExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a block string-template entry (`${...}`) wrapping the given [`expression`](index.md#createblockstringtemplateentry).


</div>

</div>
### createCallableReferenceExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createcallablereferenceexpression"><span class="nf">createCallableReferenceExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-callable-reference-expression/index.html">KtCallableReferenceExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates an expression from [`text`](index.md#createcallablereferenceexpression) and returns it if it is a callable reference, or `null` if it is another kind of expression. Failure to parse an expression is handled as described by [`createExpression`](index.md#createexpression).


</div>

</div>
### createCallArguments

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createcallarguments"><span class="nf">createCallArguments</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-value-argument-list/index.html">KtValueArgumentList</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a value argument list from the given parenthesized [`text`](index.md#createcallarguments) (for example, `"(1, x = 2)"`).


</div>

</div>
### createClass

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createclass"><span class="nf">createClass</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-class/index.html">KtClass</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a class or interface declaration from the given [`text`](index.md#createclass).


</div>

</div>
### createClassKeyword

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createclasskeyword"><span class="nf">createClassKeyword</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a `class` keyword token.


</div>

</div>
### createColon

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createcolon"><span class="nf">createColon</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a colon (`:`) token.


</div>

</div>
### createComma

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createcomma"><span class="nf">createComma</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a comma token.


</div>

</div>
### createComment

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createcomment"><span class="nf">createComment</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span>PsiComment
</span></code></pre></div>
</div>


<div markdown>

Creates a comment (line or block) from the given [`text`](index.md#createcomment); the text must be a single comment.


</div>

</div>
### createCompanionBlock

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createcompanionblock"><span class="nf">createCompanionBlock</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-companion-block/index.html">KtCompanionBlock</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an empty companion block.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createcompanionblock"><span class="nf">createCompanionBlock</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-companion-block/index.html">KtCompanionBlock</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a companion block from the given [`text`](index.md#createcompanionblock) (for example, `"companion { ... }"`). The text must contain exactly one complete companion block and no other class-body elements.


</div>

</div>
### createCompanionObject

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createcompanionobject"><span class="nf">createCompanionObject</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-object-declaration/index.html">KtObjectDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an empty companion object.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createcompanionobject"><span class="nf">createCompanionObject</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-object-declaration/index.html">KtObjectDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a companion object from the given [`text`](index.md#createcompanionobject) (for example, `"companion object { ... }"`).


</div>

</div>
### createConstructorKeyword

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createconstructorkeyword"><span class="nf">createConstructorKeyword</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a `constructor` keyword token.


</div>

</div>
### createDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#createdeclaration">TDeclaration</a><span class="o"> : </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="o">> </span><a href="index.html#createdeclaration"><span class="nf">createDeclaration</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html#createdeclaration">TDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a top-level declaration from the given [`text`](index.md#createdeclaration), cast to the expected type [`TDeclaration`](index.md#createdeclaration). The text must contain exactly one declaration.


</div>

</div>
### createDeclarationByPattern

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#createdeclarationbypattern">TDeclaration</a><span class="o"> : </span><a href="../-kt-declaration/index.html">KtDeclaration</a><span class="o">> </span><a href="index.html">KtPsiFactory</a><span class="p">.</span><a href="index.html#createdeclarationbypattern"><span class="nf">createDeclarationByPattern</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NonNls</span> pattern<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> <span class="kd">vararg </span>args<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span>
    reformat<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span>
<span class="p">)</span><span class="o">: </span><a href="index.html#createdeclarationbypattern">TDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a declaration from the given [`pattern`](index.md#createdeclarationbypattern) with placeholders substituted by [`args`](index.md#createdeclarationbypattern). See [`createByPattern`](../create-by-pattern.md).


</div>

</div>
### createDestructuringDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createdestructuringdeclaration"><span class="nf">createDestructuringDeclaration</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-destructuring-declaration/index.html">KtDestructuringDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a destructuring declaration from the given [`text`](index.md#createdestructuringdeclaration) (for example, `"val (x, y) = pair"`).


</div>

</div>
### createDestructuringDeclarationByPattern

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">KtPsiFactory</a><span class="p">.</span><a href="index.html#createdestructuringdeclarationbypattern"><span class="nf">createDestructuringDeclarationByPattern</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NonNls</span> pattern<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> <span class="kd">vararg </span>args<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span>
    reformat<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span>
<span class="p">)</span><span class="o">: </span><a href="../-kt-destructuring-declaration/index.html">KtDestructuringDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a destructuring declaration from the given [`pattern`](index.md#createdestructuringdeclarationbypattern) with placeholders substituted by [`args`](index.md#createdestructuringdeclarationbypattern). See [`createByPattern`](../create-by-pattern.md).


</div>

</div>
### createDestructuringParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createdestructuringparameter"><span class="nf">createDestructuringParameter</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a destructuring lambda parameter from the given [`text`](index.md#createdestructuringparameter) (for example, `"(x, y)"`).


</div>

</div>
### createDot

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createdot"><span class="nf">createDot</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a dot (`.`) token.


</div>

</div>
### createEmptyBody

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createemptybody"><span class="nf">createEmptyBody</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-block-expression/index.html">KtBlockExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an empty function body block (`{}`).


</div>

</div>
### createEmptyClassBody

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createemptyclassbody"><span class="nf">createEmptyClassBody</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-class-body/index.html">KtClassBody</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an empty class body (`{}`).


</div>

</div>
### createEmptyModifierList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createemptymodifierlist"><span class="nf">createEmptyModifierList</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-modifier-list/index.html">KtModifierList</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an empty modifier list.


</div>

</div>
### createEnumEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createenumentry"><span class="nf">createEnumEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-enum-entry/index.html">KtEnumEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an enum entry from the given [`text`](index.md#createenumentry) (for example, `"RED"` or `"RED(0xFF0000)"`).


</div>

</div>
### createEnumEntryInitializerList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createenumentryinitializerlist"><span class="nf">createEnumEntryInitializerList</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-initializer-list/index.html">KtInitializerList</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an enum entry initializer list holding a single set of constructor arguments.


</div>

</div>
### createEQ

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createeq"><span class="nf">createEQ</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates an equals (`=`) token.


</div>

</div>
### createExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createexpression"><span class="nf">createExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an expression from the given [`text`](index.md#createexpression). Throws if no expression can be parsed. When JVM assertions are enabled, also fails if the parsed expression's text does not match [`text`](index.md#createexpression) exactly; use [`createExpressionIfPossible`](index.md#createexpressionifpossible) for unconditional validation and a `null` result on failure.


</div>

</div>
### createExpressionByPattern

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">KtPsiFactory</a><span class="p">.</span><a href="index.html#createexpressionbypattern"><span class="nf">createExpressionByPattern</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NonNls</span> pattern<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> <span class="kd">vararg </span>args<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span>
    reformat<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span>
<span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an expression from the given [`pattern`](index.md#createexpressionbypattern) with `$0`, `$1`, … placeholders substituted by [`args`](index.md#createexpressionbypattern). See [`createByPattern`](../create-by-pattern.md).


</div>

</div>
### createExpressionCodeFragment

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createexpressioncodefragment"><span class="nf">createExpressionCodeFragment</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>context<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-kt-expression-code-fragment/index.html">KtExpressionCodeFragment</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KtExpressionCodeFragment`](../-kt-expression-code-fragment/index.md) for the given [`text`](index.md#createexpressioncodefragment), resolved in the given [`context`](index.md#createexpressioncodefragment).


</div>

</div>
### createExpressionIfPossible

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createexpressionifpossible"><span class="nf">createExpressionIfPossible</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates an expression from the given [`text`](index.md#createexpressionifpossible), or returns `null` if the text cannot be parsed as a single expression whose text matches [`text`](index.md#createexpressionifpossible) exactly.


</div>

</div>
### createFile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createfile"><span class="nf">createFile</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-file/index.html">KtFile</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KtFile`](../-kt-file/index.md) with the given [`text`](index.md#createfile) and a dummy file name.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createfile"><span class="nf">createFile</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> fileName<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-file/index.html">KtFile</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KtFile`](../-kt-file/index.md) with the given [`fileName`](index.md#createfile) and [`text`](index.md#createfile). If this factory has a context, the file is marked analyzable in that context; otherwise it is marked as [`do-not-analyze`](../-kt-type-code-fragment/index.md#donotanalyze).


</div>

</div>
### createFileAnnotation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createfileannotation"><span class="nf">createFileAnnotation</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> annotationText<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-annotation-entry/index.html">KtAnnotationEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a file-level annotation entry from the given [`annotationText`](index.md#createfileannotation) (without the `@file:` prefix).


</div>

</div>
### createFileAnnotationListWithAnnotation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createfileannotationlistwithannotation"><span class="nf">createFileAnnotationListWithAnnotation</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> annotationText<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-file-annotation-list/index.html">KtFileAnnotationList</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a file annotation list containing a single `@file:` annotation from the given [`annotationText`](index.md#createfileannotationlistwithannotation).


</div>

</div>
### createFunction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createfunction"><span class="nf">createFunction</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> funDecl<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-named-function/index.html">KtNamedFunction</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a named function from the given declaration text [`funDecl`](index.md#createfunction).


</div>

</div>
### createFunctionTypeParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createfunctiontypeparameter"><span class="nf">createFunctionTypeParameter</span></a><span class="p">(</span>typeReference<span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="p">)</span><span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a function-type parameter whose type is the given [`typeReference`](index.md#createfunctiontypeparameter).


</div>

</div>
### createFunctionTypeReceiver

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createfunctiontypereceiver"><span class="nf">createFunctionTypeReceiver</span></a><span class="p">(</span>typeReference<span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="p">)</span><span class="o">: </span><a href="../-kt-function-type-receiver/index.html">KtFunctionTypeReceiver</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a function-type receiver (the `T.` in `T.() -> R`) wrapping the given [`typeReference`](index.md#createfunctiontypereceiver).


</div>

</div>
### createIdentifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createidentifier"><span class="nf">createIdentifier</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a bare identifier token for the given [`name`](index.md#createidentifier).


</div>

</div>
### createIf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createif"><span class="nf">createIf</span></a><span class="p">(</span>
    condition<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">, </span>
    thenExpr<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">, </span>
    elseExpr<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="o">?</span><span class="o"> = </span>null
<span class="p">)</span><span class="o">: </span><a href="../-kt-if-expression/index.html">KtIfExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an `if` expression with the given [`condition`](index.md#createif), [`thenExpr`](index.md#createif), and optional [`elseExpr`](index.md#createif).


</div>

</div>
### createImportDirective

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createimportdirective"><span class="nf">createImportDirective</span></a><span class="p">(</span>importPath<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.resolve/-import-path/index.html">ImportPath</a><span class="p">)</span><span class="o">: </span><a href="../-kt-import-directive/index.html">KtImportDirective</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an `import` directive for the given [`importPath`](index.md#createimportdirective) (including its all-under flag and alias).

**Throws**



[`IllegalArgumentException`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html)

:   if the import path is empty (the root package)





</div>

</div>
### createLabeledExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createlabeledexpression"><span class="nf">createLabeledExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> labelName<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-labeled-expression/index.html">KtLabeledExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a labeled expression from a label [`labelName`](index.md#createlabeledexpression) such as `"loop"`; the resulting expression is `loop@ 1`.


</div>

</div>
### createLambdaExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createlambdaexpression"><span class="nf">createLambdaExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> parameters<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span><span class="se">@</span><span class="se">NonNls</span> body<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-lambda-expression/index.html">KtLambdaExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a lambda expression with the given [`parameters`](index.md#createlambdaexpression) and [`body`](index.md#createlambdaexpression) text.


</div>

</div>
### createLambdaParameterList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createlambdaparameterlist"><span class="nf">createLambdaParameterList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-parameter-list/index.html">KtParameterList</a>
</span></code></pre></div>
</div>


<div markdown>

Creates the parameter list of a lambda with the given parameter [`text`](index.md#createlambdaparameterlist).


</div>

</div>
### createLambdaParameterListIfAny

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createlambdaparameterlistifany"><span class="nf">createLambdaParameterListIfAny</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-parameter-list/index.html">KtParameterList</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates the parameter list of a lambda with the given parameter [`text`](index.md#createlambdaparameterlistifany), or `null` if the lambda declares none.


</div>

</div>
### createLiteralStringTemplateEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createliteralstringtemplateentry"><span class="nf">createLiteralStringTemplateEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> literal<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-literal-string-template-entry/index.html">KtLiteralStringTemplateEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a literal (plain text) string-template entry for the given [`literal`](index.md#createliteralstringtemplateentry) text.


</div>

</div>
### createLoopParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createloopparameter"><span class="nf">createLoopParameter</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a `for`-loop parameter from the given [`text`](index.md#createloopparameter).


</div>

</div>
### createModifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createmodifier"><span class="nf">createModifier</span></a><span class="p">(</span>modifier<span class="o">: </span><a href="../../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a single modifier keyword token.


</div>

</div>
### createModifierList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createmodifierlist"><span class="nf">createModifierList</span></a><span class="p">(</span>modifier<span class="o">: </span><a href="../../org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="p">)</span><span class="o">: </span><a href="../-kt-modifier-list/index.html">KtModifierList</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a modifier list containing the single given [`modifier`](index.md#createmodifierlist) keyword.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createmodifierlist"><span class="nf">createModifierList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-modifier-list/index.html">KtModifierList</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a modifier list from the given [`text`](index.md#createmodifierlist) (a space-separated sequence of modifiers).


</div>

</div>
### createMultiDollarBlockStringTemplateEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createmultidollarblockstringtemplateentry"><span class="nf">createMultiDollarBlockStringTemplateEntry</span></a><span class="p">(</span>expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">, </span>prefixLength<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span><a href="../-kt-string-template-entry-with-expression/index.html">KtStringTemplateEntryWithExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a block string-template entry (`${...}`) wrapping the given [`expression`](index.md#createmultidollarblockstringtemplateentry), for a string template whose interpolation prefix is [`prefixLength`](index.md#createmultidollarblockstringtemplateentry) dollar signs (for example, `$${...}` when [`prefixLength`](index.md#createmultidollarblockstringtemplateentry) is `2`).

**Throws**



[`IllegalStateException`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-state-exception/index.html)

:   if [`prefixLength`](index.md#createmultidollarblockstringtemplateentry) is not positive





</div>

</div>
### createMultiDollarSimpleNameStringTemplateEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createmultidollarsimplenamestringtemplateentry"><span class="nf">createMultiDollarSimpleNameStringTemplateEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>prefixLength<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span><a href="../-kt-simple-name-string-template-entry/index.html">KtSimpleNameStringTemplateEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a simple-name string-template entry (`$name`) for the given [`name`](index.md#createmultidollarsimplenamestringtemplateentry), for a string template whose interpolation prefix is [`prefixLength`](index.md#createmultidollarsimplenamestringtemplateentry) dollar signs (for example, `$$name` when [`prefixLength`](index.md#createmultidollarsimplenamestringtemplateentry) is `2`).

**Throws**



[`IllegalStateException`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-state-exception/index.html)

:   if [`prefixLength`](index.md#createmultidollarsimplenamestringtemplateentry) is not positive





</div>

</div>
### createMultiDollarStringTemplate

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createmultidollarstringtemplate"><span class="nf">createMultiDollarStringTemplate</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NonNls</span> content<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    prefixLength<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">, </span>
    forceMultiQuoted<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span>
<span class="p">)</span><span class="o">: </span><a href="../-kt-string-template-expression/index.html">KtStringTemplateExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a string template with the given [`content`](index.md#createmultidollarstringtemplate) whose interpolation prefix is [`prefixLength`](index.md#createmultidollarstringtemplate) dollar signs. A raw (triple-quoted) template is used when [`content`](index.md#createmultidollarstringtemplate) spans multiple lines or [`forceMultiQuoted`](index.md#createmultidollarstringtemplate) is `true`, and a regular (double-quoted) one otherwise.

**Throws**



[`IllegalStateException`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-state-exception/index.html)

:   if [`prefixLength`](index.md#createmultidollarstringtemplate) is not positive





</div>

</div>
### createNameIdentifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createnameidentifier"><span class="nf">createNameIdentifier</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a name identifier token for the given [`name`](index.md#createnameidentifier). Throws if [`name`](index.md#createnameidentifier) is not a valid identifier.


</div>

</div>
### createNameIdentifierIfPossible

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createnameidentifierifpossible"><span class="nf">createNameIdentifierIfPossible</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a name identifier token for the given [`name`](index.md#createnameidentifierifpossible), or returns `null` if [`name`](index.md#createnameidentifierifpossible) is not a valid identifier.


</div>

</div>
### createNewLine

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createnewline"><span class="nf">createNewLine</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a whitespace element containing a single line break.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createnewline"><span class="nf">createNewLine</span></a><span class="p">(</span>lineBreaks<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a whitespace element containing [`lineBreaks`](index.md#createnewline) line breaks.


</div>

</div>
### createObject

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createobject"><span class="nf">createObject</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-object-declaration/index.html">KtObjectDeclaration</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an object declaration from the given [`text`](index.md#createobject).


</div>

</div>
### createOperationName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createoperationname"><span class="nf">createOperationName</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-simple-name-expression/index.html">KtSimpleNameExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an operation-reference expression for the given operator [`name`](index.md#createoperationname) (for example, `"+"`).


</div>

</div>
### createPackageDirective

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createpackagedirective"><span class="nf">createPackageDirective</span></a><span class="p">(</span>fqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="../-kt-package-directive/index.html">KtPackageDirective</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a `package` directive for the given [`fqName`](index.md#createpackagedirective).


</div>

</div>
### createPackageDirectiveIfNeeded

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createpackagedirectiveifneeded"><span class="nf">createPackageDirectiveIfNeeded</span></a><span class="p">(</span>fqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="../-kt-package-directive/index.html">KtPackageDirective</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a `package` directive for the given [`fqName`](index.md#createpackagedirectiveifneeded), or returns `null` for the root package.


</div>

</div>
### createParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createparameter"><span class="nf">createParameter</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-parameter/index.html">KtParameter</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a value parameter from the given [`text`](index.md#createparameter) (for example, `"x: Int = 0"`).


</div>

</div>
### createParameterList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createparameterlist"><span class="nf">createParameterList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-parameter-list/index.html">KtParameterList</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a parameter list from the given parenthesized [`text`](index.md#createparameterlist) (for example, `"(x: Int, y: Int)"`).


</div>

</div>
### createPhysicalFile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createphysicalfile"><span class="nf">createPhysicalFile</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> fileName<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-file/index.html">KtFile</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a physical (event-system-enabled) [`KtFile`](../-kt-file/index.md) with the given [`fileName`](index.md#createphysicalfile) and [`text`](index.md#createphysicalfile). Unlike [`createFile`](index.md#createfile), the resulting file participates in the PSI event system and supports light classes.


</div>

</div>
### createPrimaryConstructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createprimaryconstructor"><span class="nf">createPrimaryConstructor</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o"> = </span><span class="s">""</span><span class="p">)</span><span class="o">: </span><a href="../-kt-primary-constructor/index.html">KtPrimaryConstructor</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a primary constructor from the given [`text`](index.md#createprimaryconstructor) (for example, `"constructor(x: Int)"`), defaulting to an empty one.


</div>

</div>
### createPrimaryConstructorWithModifiers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createprimaryconstructorwithmodifiers"><span class="nf">createPrimaryConstructorWithModifiers</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> modifiers<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-kt-primary-constructor/index.html">KtPrimaryConstructor</a>
</span></code></pre></div>
</div>


<div markdown>

Creates an empty primary constructor carrying the given [`modifiers`](index.md#createprimaryconstructorwithmodifiers).


</div>

</div>
### createProperty

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createproperty"><span class="nf">createProperty</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NonNls</span> modifiers<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> type<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">, </span>
    isVar<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> initializer<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="../-kt-property/index.html">KtProperty</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a property from its parts: optional [`modifiers`](index.md#createproperty), [`name`](index.md#createproperty), optional [`type`](index.md#createproperty), mutability ([`isVar`](index.md#createproperty)), and optional [`initializer`](index.md#createproperty).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createproperty"><span class="nf">createProperty</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> type<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">, </span>
    isVar<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> initializer<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="../-kt-property/index.html">KtProperty</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a property from its parts, without modifiers.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createproperty"><span class="nf">createProperty</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> type<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">, </span>
    isVar<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
<span class="p">)</span><span class="o">: </span><a href="../-kt-property/index.html">KtProperty</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a property with the given [`name`](index.md#createproperty) and optional [`type`](index.md#createproperty) and no initializer.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createproperty"><span class="nf">createProperty</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-property/index.html">KtProperty</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a property from the given full declaration [`text`](index.md#createproperty) (for example, `"val x: Int = 1"`).


</div>

</div>
### createPropertyDelegate

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createpropertydelegate"><span class="nf">createPropertyDelegate</span></a><span class="p">(</span>expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="../-kt-property-delegate/index.html">KtPropertyDelegate</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a property delegate (`by ...`) whose delegate expression is the given [`expression`](index.md#createpropertydelegate).


</div>

</div>
### createPropertyGetter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createpropertygetter"><span class="nf">createPropertyGetter</span></a><span class="p">(</span>expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="../-kt-property-accessor/index.html">KtPropertyAccessor</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a property getter whose body is the given [`expression`](index.md#createpropertygetter) (a block or a single expression).


</div>

</div>
### createPropertySetter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createpropertysetter"><span class="nf">createPropertySetter</span></a><span class="p">(</span>expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="../-kt-property-accessor/index.html">KtPropertyAccessor</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a property setter whose body is the given [`expression`](index.md#createpropertysetter) (a block or a single expression).


</div>

</div>
### createRawStringTemplate

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createrawstringtemplate"><span class="nf">createRawStringTemplate</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> content<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-string-template-expression/index.html">KtStringTemplateExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a raw (triple-quoted) string template with the given [`content`](index.md#createrawstringtemplate).


</div>

</div>
### createReplSnippet

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createreplsnippet"><span class="nf">createReplSnippet</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-script/index.html">KtScript</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a REPL snippet [`KtScript`](../-kt-script/index.md) from the specified text content.


</div>

</div>
### createSecondaryConstructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createsecondaryconstructor"><span class="nf">createSecondaryConstructor</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> decl<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-secondary-constructor/index.html">KtSecondaryConstructor</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a secondary constructor from the given declaration text [`decl`](index.md#createsecondaryconstructor).


</div>

</div>
### createSemicolon

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createsemicolon"><span class="nf">createSemicolon</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a semicolon token.


</div>

</div>
### createSimpleName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createsimplename"><span class="nf">createSimpleName</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-simple-name-expression/index.html">KtSimpleNameExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a simple name reference expression for the given [`name`](index.md#createsimplename).


</div>

</div>
### createSimpleNameStringTemplateEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createsimplenamestringtemplateentry"><span class="nf">createSimpleNameStringTemplateEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-simple-name-string-template-entry/index.html">KtSimpleNameStringTemplateEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a simple-name string-template entry (`$name`) for the given [`name`](index.md#createsimplenamestringtemplateentry).


</div>

</div>
### createSingleStatementBlock

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createsinglestatementblock"><span class="nf">createSingleStatementBlock</span></a><span class="p">(</span>
    statement<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> prevComment<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="o"> = </span>null<span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> nextComment<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="o"> = </span>null
<span class="p">)</span><span class="o">: </span><a href="../-kt-block-expression/index.html">KtBlockExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a block containing the single given [`statement`](index.md#createsinglestatementblock), optionally preceded by [`prevComment`](index.md#createsinglestatementblock) and followed by [`nextComment`](index.md#createsinglestatementblock).


</div>

</div>
### createStar

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createstar"><span class="nf">createStar</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a `*` (star projection) token.


</div>

</div>
### createStringTemplate

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createstringtemplate"><span class="nf">createStringTemplate</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> content<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-string-template-expression/index.html">KtStringTemplateExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a regular (double-quoted) string template with the given [`content`](index.md#createstringtemplate).


</div>

</div>
### createSuperTypeCallEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createsupertypecallentry"><span class="nf">createSuperTypeCallEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-super-type-call-entry/index.html">KtSuperTypeCallEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a superclass constructor call entry from the given [`text`](index.md#createsupertypecallentry) (for example, `"Base(1)"`).


</div>

</div>
### createSuperTypeEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createsupertypeentry"><span class="nf">createSuperTypeEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-super-type-entry/index.html">KtSuperTypeEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a plain supertype entry from the given [`text`](index.md#createsupertypeentry) (for example, an interface name `"Runnable"`).


</div>

</div>
### createThisExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createthisexpression"><span class="nf">createThisExpression</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-kt-this-expression/index.html">KtThisExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a `this` expression.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createthisexpression"><span class="nf">createThisExpression</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> qualifier<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-this-expression/index.html">KtThisExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a labeled `this` expression (`this@qualifier`).


</div>

</div>
### createType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createtype"><span class="nf">createType</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> type<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a type reference from the given [`type`](index.md#createtype) text. Throws if the text cannot be parsed as a type whose text matches [`type`](index.md#createtype) exactly; use [`createTypeIfPossible`](index.md#createtypeifpossible) to get `null` instead.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createtype"><span class="nf">createType</span></a><span class="p">(</span>typeElement<span class="o">: </span><a href="../-kt-type-element/index.html">KtTypeElement</a><span class="p">)</span><span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a type reference wrapping the given [`typeElement`](index.md#createtype).


</div>

</div>
### createTypeAlias

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createtypealias"><span class="nf">createTypeAlias</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    typeParameters<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">></span><span class="p">, </span>
    typeElement<span class="o">: </span><a href="../-kt-type-element/index.html">KtTypeElement</a>
<span class="p">)</span><span class="o">: </span><a href="../-kt-type-alias/index.html">KtTypeAlias</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a type alias with the given [`name`](index.md#createtypealias) and [`typeParameters`](index.md#createtypealias), aliasing the given [`typeElement`](index.md#createtypealias).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createtypealias"><span class="nf">createTypeAlias</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    typeParameters<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">></span><span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> body<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
<span class="p">)</span><span class="o">: </span><a href="../-kt-type-alias/index.html">KtTypeAlias</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a type alias with the given [`name`](index.md#createtypealias) and [`typeParameters`](index.md#createtypealias), aliasing the type in [`body`](index.md#createtypealias).


</div>

</div>
### createTypeArgument

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createtypeargument"><span class="nf">createTypeArgument</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-type-projection/index.html">KtTypeProjection</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a single type argument (projection) from the given [`text`](index.md#createtypeargument).


</div>

</div>
### createTypeArguments

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createtypearguments"><span class="nf">createTypeArguments</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-type-argument-list/index.html">KtTypeArgumentList</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a type argument list from the given angle-bracketed [`text`](index.md#createtypearguments) (for example, `"<Int, String>"`).


</div>

</div>
### createTypeCodeFragment

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createtypecodefragment"><span class="nf">createTypeCodeFragment</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>context<span class="o">: </span>PsiElement<span class="o">?</span><span class="p">)</span><span class="o">: </span><a href="../-kt-type-code-fragment/index.html">KtTypeCodeFragment</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KtTypeCodeFragment`](../-kt-type-code-fragment/index.md) for the given [`text`](index.md#createtypecodefragment), resolved in the given [`context`](index.md#createtypecodefragment).


</div>

</div>
### createTypeIfPossible

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createtypeifpossible"><span class="nf">createTypeIfPossible</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> type<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-type-reference/index.html">KtTypeReference</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Creates a type reference from the given [`type`](index.md#createtypeifpossible) text, or returns `null` if it cannot be parsed as such.


</div>

</div>
### createTypeParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createtypeparameter"><span class="nf">createTypeParameter</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-type-parameter/index.html">KtTypeParameter</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a single type parameter from the given [`text`](index.md#createtypeparameter) (for example, `"T : Comparable<T>"`).


</div>

</div>
### createTypeParameterList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createtypeparameterlist"><span class="nf">createTypeParameterList</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-type-parameter-list/index.html">KtTypeParameterList</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a type parameter list from the given angle-bracketed [`text`](index.md#createtypeparameterlist) (for example, `"<T, R>"`).


</div>

</div>
### createValKeyword

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createvalkeyword"><span class="nf">createValKeyword</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a `val` keyword token.


</div>

</div>
### createValueArgumentListByPattern

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html">KtPsiFactory</a><span class="p">.</span><a href="index.html#createvalueargumentlistbypattern"><span class="nf">createValueArgumentListByPattern</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NonNls</span> pattern<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NonNls</span> <span class="kd">vararg </span>args<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">, </span>
    reformat<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span>
<span class="p">)</span><span class="o">: </span><a href="../-kt-value-argument-list/index.html">KtValueArgumentList</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a value argument list from the given [`pattern`](index.md#createvalueargumentlistbypattern) with placeholders substituted by [`args`](index.md#createvalueargumentlistbypattern). See [`createByPattern`](../create-by-pattern.md).


</div>

</div>
### createVarKeyword

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createvarkeyword"><span class="nf">createVarKeyword</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a `var` keyword token.


</div>

</div>
### createWhenCondition

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createwhencondition"><span class="nf">createWhenCondition</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> conditionText<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-when-condition/index.html">KtWhenCondition</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a `when` condition from the given [`conditionText`](index.md#createwhencondition) (for example, `"in 1..10"` or `"is String"`).


</div>

</div>
### createWhenEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createwhenentry"><span class="nf">createWhenEntry</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> entryText<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="../-kt-when-entry/index.html">KtWhenEntry</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a `when` entry from the given [`entryText`](index.md#createwhenentry) (for example, `"1 -> \"one\""`). Throws if the produced entry's text does not match [`entryText`](index.md#createwhenentry).


</div>

</div>
### createWhiteSpace

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createwhitespace"><span class="nf">createWhiteSpace</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a single-space whitespace element.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createwhitespace"><span class="nf">createWhiteSpace</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> text<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>


<div markdown>

Creates a whitespace element with the exact given [`text`](index.md#createwhitespace).


</div>

</div>
### createWhitespaceAndArrow

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#createwhitespaceandarrow"><span class="nf">createWhitespaceAndArrow</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/index.html">Pair</a><span class="o"><</span>PsiElement<span class="p">, </span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Creates a whitespace-then-arrow pair; the returned pair holds the first and last elements of that range.


</div>

</div>
### wrapInABlockWrapper

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#wrapinablockwrapper"><span class="nf">wrapInABlockWrapper</span></a><span class="p">(</span>expression<span class="o">: </span><a href="../-kt-expression/index.html">KtExpression</a><span class="p">)</span><span class="o">: </span><a href="../-kt-block-expression/index.html">KtBlockExpression</a>
</span></code></pre></div>
</div>


<div markdown>

Wraps the given [`expression`](index.md#wrapinablockwrapper) in a synthetic single-statement block. If [`expression`](index.md#wrapinablockwrapper) is already a block, it is returned unchanged. Intended for internal compiler use.


</div>

</div>
