---
tags:
 - jvm
title: "Companion"
---

# Companion

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">Companion</a>
</span></code></pre></div>
</div>

## Properties
### Annotation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#annotation">Annotation</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/index.html">Pair</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation/index.html">KaAnnotation</a><span class="p">, </span>AnnotationUseSiteTarget<span class="o">?</span><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A single annotation entry, e.g. `@Foo(bar)`. The annotation class name is rendered as [`ClassName`](index.md#classname), respecting [`KaRenderingOption.ClassTypeQualification`](../../-ka-rendering-option/-companion/index.md#classtypequalification).

The second component is the use-site target which the annotation is rendered with, e.g. `@get:Foo(bar)`, or `null` when it is rendered without one.


</div>

</div>
### Annotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#annotations">Annotations</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/index.html">Pair</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a><span class="p">, </span>AnnotationUseSiteTarget<span class="o">?</span><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The annotations of an annotated element, including the whitespace which separates them from what follows.

Which annotations are rendered is controlled by [`KaRenderingOption.Annotations`](../../-ka-rendering-option/-companion/index.md#annotations), and whether each is followed by a line break or a space by [`KaRenderingOption.AnnotationsOnNewLine`](../../-ka-rendering-option/-companion/index.md#annotationsonnewline).

The second component is the use-site target which the annotations are rendered with, e.g. `@receiver:Foo`, or `null` when they are rendered without one.


</div>

</div>
### AnnotationValue

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#annotationvalue">AnnotationValue</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-value/index.html">KaAnnotationValue</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A single annotation argument value (a constant, enum entry, class literal, nested annotation, or array).


</div>

</div>
### AnnotationValues

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#annotationvalues">AnnotationValues</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation/index.html">KaAnnotation</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The parenthesized argument list of an annotation, e.g. `(message = "Use bar")`. Nothing is rendered for an annotation without arguments.


</div>

</div>
### AnonymousFunction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#anonymousfunction">AnonymousFunction</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-anonymous-function-symbol/index.html">KaAnonymousFunctionSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

An anonymous function, e.g. `fun(x: Int): String { ... }`.


</div>

</div>
### AnonymousObject

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#anonymousobject">AnonymousObject</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-anonymous-object-symbol/index.html">KaAnonymousObjectSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

An anonymous object, e.g. `object : Runnable { ... }`.


</div>

</div>
### BackingField

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#backingfield">BackingField</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-backing-field-symbol/index.html">KaBackingFieldSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The declaration of a property's backing field, e.g. `field: MutableList<String>`.


</div>

</div>
### Callable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#callable">Callable</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Any [`org.jetbrains.kotlin.analysis.api.symbols.KaCallableSymbol`](../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md). Dispatches to [`Function`](index.md#function) for function-like declarations and to [`Variable`](index.md#variable) for variable-like declarations.


</div>

</div>
### CapturedType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#capturedtype">CapturedType</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-captured-type/index.html">KaCapturedType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A captured type produced by capturing a projection during type inference, rendered as `Captured(out Number)`.


</div>

</div>
### Class

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#class">Class</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Any class, object, or interface declaration ([`org.jetbrains.kotlin.analysis.api.symbols.KaClassSymbol`](../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md)). Dispatches to [`NamedClass`](index.md#namedclass) or [`AnonymousObject`](index.md#anonymousobject).


</div>

</div>
### ClassAnnotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#classannotations">ClassAnnotations</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The annotations of a class.


</div>

</div>
### ClassBody

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#classbody">ClassBody</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The body of a class, containing its member declarations, including the braces and the leading space, e.g. `{ ... }`. Nothing is rendered for an empty body. The rendered members and their layout are controlled by [`KaRenderingOption.ClassMembers`](../../-ka-rendering-option/-companion/index.md#classmembers), [`KaRenderingOption.ClassMemberOrdering`](../../-ka-rendering-option/-companion/index.md#classmemberordering), and [`KaRenderingOption.ExtraLineBetweenMembers`](../../-ka-rendering-option/-companion/index.md#extralinebetweenmembers).


</div>

</div>
### Classifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#classifier">Classifier</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Any classifier declaration ([`org.jetbrains.kotlin.analysis.api.symbols.KaClassifierSymbol`](../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md)). Dispatches to the piece of its kind: [`Class`](index.md#class), [`TypeAlias`](index.md#typealias), or [`TypeParameter`](index.md#typeparameter).


</div>

</div>
### ClassInitializer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#classinitializer">ClassInitializer</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-initializer-symbol/index.html">KaClassInitializerSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A class initializer block, rendered as `init`.


</div>

</div>
### ClassName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#classname">ClassName</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span>ClassId<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The qualified name of a class, rendered segment by segment, e.g. `Foo.Bar`. How qualified the name is rendered is controlled by [`KaRenderingOption.ClassTypeQualification`](../../-ka-rendering-option/-companion/index.md#classtypequalification). Each segment is linked to the classifier it names, when [`KaRenderingOption.LinkSymbols`](../../-ka-rendering-option/-companion/index.md#linksymbols) is enabled and it can be resolved.

The piece is used in positions which name a class without type arguments, such as annotations. The name of a class type, which includes the type arguments of each rendered qualifier segment, is [`ClassTypeName`](index.md#classtypename).


</div>

</div>
### ClassType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#classtype">ClassType</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.html">KaClassType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A class type, e.g. `List<String>?`, comprising its [`TypeAnnotations`](index.md#typeannotations), [`ClassTypeName`](index.md#classtypename), and [`TypeNullability`](index.md#typenullability).


</div>

</div>
### ClassTypeName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#classtypename">ClassTypeName</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-class-type/index.html">KaClassType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The name of a class type, e.g. `Foo.Bar` or `Int` for `Foo.Bar<Int>`. How the qualified name is rendered is controlled by [`KaRenderingOption.ClassTypeQualification`](../../-ka-rendering-option/-companion/index.md#classtypequalification).


</div>

</div>
### ConstantValue

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#constantvalue">ConstantValue</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.base/-ka-constant-value/index.html">KaConstantValue</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A constant value, e.g. `42`, `"text"`, or `null`.


</div>

</div>
### Constructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#constructor">Constructor</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A constructor declaration.


</div>

</div>
### ConstructorBody

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#constructorbody">ConstructorBody</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The body of a constructor, including whatever separates it from the signature, e.g. `{ ... }`. The body is not part of the symbol, so nothing is rendered by default.

The piece is not rendered for [`PrimaryConstructor`](index.md#primaryconstructor)s as they do not have a body.


</div>

</div>
### ContextParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#contextparameter">ContextParameter</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-context-parameter-symbol/index.html">KaContextParameterSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A single context parameter.


</div>

</div>
### ContextParameterAnnotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#contextparameterannotations">ContextParameterAnnotations</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-context-parameter-symbol/index.html">KaContextParameterSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The annotations of a context parameter.


</div>

</div>
### ContextParameterList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#contextparameterlist">ContextParameterList</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The `context(...)` clause of a callable, followed by a line break or a space (see [`KaRenderingOption.ContextParametersOnNewLine`](../../-ka-rendering-option/-companion/index.md#contextparametersonnewline)). Nothing is rendered when there are no context parameters.


</div>

</div>
### ContextParameterType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#contextparametertype">ContextParameterType</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-context-parameter-symbol/index.html">KaContextParameterSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The type of context parameter, including the leading colon, e.g. `: String`.


</div>

</div>
### Declaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#declaration">Declaration</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Any [`org.jetbrains.kotlin.analysis.api.symbols.KaDeclarationSymbol`](../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md). Dispatches to the piece of its kind: [`Callable`](index.md#callable), [`Classifier`](index.md#classifier), [`Script`](index.md#script), [`DestructuringDeclaration`](index.md#destructuringdeclaration), or [`ClassInitializer`](index.md#classinitializer).


</div>

</div>
### DefinitelyNotNullType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#definitelynotnulltype">DefinitelyNotNullType</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-definitely-not-null-type/index.html">KaDefinitelyNotNullType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A definitely non-nullable type, e.g. `T & Any`.


</div>

</div>
### DestructuringDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#destructuringdeclaration">DestructuringDeclaration</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-destructuring-declaration-symbol/index.html">KaDestructuringDeclarationSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A destructuring declaration, e.g. `val (a, b)`. The names of the created variables are rendered as [`SymbolName`](index.md#symbolname)s.

The declaration's own `val`/`var` keyword and its initializer expression are not part of the symbol: the keyword is taken from the entries, and nothing is rendered after the entry list.


</div>

</div>
### DynamicType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#dynamictype">DynamicType</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.html">KaDynamicType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The Kotlin/JS `dynamic` type.


</div>

</div>
### EnumEntry

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#enumentry">EnumEntry</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-enum-entry-symbol/index.html">KaEnumEntrySymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A single enum entry, including its anonymous object body when present, e.g. `ENTRY { ... }`.


</div>

</div>
### ErrorType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#errortype">ErrorType</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-error-type/index.html">KaErrorType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A type that could not be resolved. An unresolved class type is rendered in its written form, e.g. `C<String>`; other error types are rendered as an error marker.


</div>

</div>
### File

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#file">File</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A Kotlin file. As a file declares no header of its own, only the file's annotations are rendered, each with the `file` use-site target, e.g. `@file:JvmName("Foo")`.


</div>

</div>
### FlexibleType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#flexibletype">FlexibleType</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/index.html">KaFlexibleType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A flexible type spanning a lower and an upper bound, such as a platform type. With [`KaRenderingOption.FlexibleTypeShrinking`](../../-ka-rendering-option/-companion/index.md#flexibletypeshrinking) (the default), it is rendered compactly when possible, e.g. `String!`; otherwise as the `(lower..upper)` range of its bounds.


</div>

</div>
### Function

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#function">Function</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Any function-like declaration ([`org.jetbrains.kotlin.analysis.api.symbols.KaFunctionSymbol`](../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md)). Dispatches to the piece of its kind: [`NamedFunction`](index.md#namedfunction), [`Constructor`](index.md#constructor) (both primary and secondary), [`PropertyAccessor`](index.md#propertyaccessor), [`SamConstructor`](index.md#samconstructor), or [`AnonymousFunction`](index.md#anonymousfunction).


</div>

</div>
### FunctionAnnotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#functionannotations">FunctionAnnotations</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The annotations of a function.


</div>

</div>
### FunctionBody

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#functionbody">FunctionBody</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The body of a function, including whatever separates it from the signature, e.g. `{ ... }` or `= 42`. The body is not part of the symbol, so nothing is rendered by default.

The piece covers named functions, anonymous functions, SAM constructors, and property accessors. The body of a constructor is rendered as [`ConstructorBody`](index.md#constructorbody) instead.


</div>

</div>
### FunctionReturnType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#functionreturntype">FunctionReturnType</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The return type of function, including the leading colon, e.g. `: String`. The type is always rendered.


</div>

</div>
### FunctionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#functiontype">FunctionType</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.html">KaFunctionType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A function type rendered with function type syntax, e.g. `(Int) -> String`. A nullable or annotated function type is wrapped in parentheses, e.g. `((Int) -> String)?`.

By default, a [`reflection function type`](../../../org.jetbrains.kotlin.analysis.api.types/-ka-function-type/index.md#isreflecttype), such as `KFunction1<Int, String>`, is rendered as a [`ClassType`](index.md#classtype) as there is no type syntax for reflection types.


</div>

</div>
### FunctionTypeParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#functiontypeparameter">FunctionTypeParameter</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-function-value-parameter/index.html">KaFunctionValueParameter</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A single value parameter of a [`FunctionType`](index.md#functiontype), e.g. `x: Int` in `(x: Int) -> String`, or just `Int` for a parameter which has no name.

A function type parameter is named by a synthetic `@ParameterName` annotation on its type, so a parameter only has a name when that annotation is present.


</div>

</div>
### IntersectionType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#intersectiontype">IntersectionType</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-intersection-type/index.html">KaIntersectionType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

An intersection of several types, e.g. `A & B`.


</div>

</div>
### JavaField

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#javafield">JavaField</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-java-field-symbol/index.html">KaJavaFieldSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A field declared in Java.


</div>

</div>
### LocalVariable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#localvariable">LocalVariable</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-local-variable-symbol/index.html">KaLocalVariableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A local variable declaration.


</div>

</div>
### NamedClass

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#namedclass">NamedClass</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A named class, interface, or object declaration. The primary constructor is rendered in the class header when [`KaRenderingOption.PrimaryConstructorInClassHeader`](../../-ka-rendering-option/-companion/index.md#primaryconstructorinclassheader) is set (the default).


</div>

</div>
### NamedFunction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#namedfunction">NamedFunction</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A named function declaration.


</div>

</div>
### NamedFunctionReturnType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#namedfunctionreturntype">NamedFunctionReturnType</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The return type of named function, including the leading colon, e.g. `: String`. Nothing is rendered for an implicit `Unit` return type.


</div>

</div>
### Package

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#package">Package</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-package-symbol/index.html">KaPackageSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A package, e.g. `package kotlin.collections`.


</div>

</div>
### PackageName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#packagename">PackageName</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span>FqName<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The fully-qualified name of a package, rendered segment by segment, e.g. `org.example`.

Each segment is linked to the [`KaPackageSymbol`](../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-package-symbol/index.md) of the package it forms, when [`KaRenderingOption.LinkSymbols`](../../-ka-rendering-option/-companion/index.md#linksymbols) is enabled and that package can be resolved.

The piece renders the segments alone. A dot which separates the package name from what follows, such as the dot in a fully qualified class name, is rendered by the piece that requested it.


</div>

</div>
### Parameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#parameter">Parameter</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-parameter-symbol/index.html">KaParameterSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Any parameter ([`org.jetbrains.kotlin.analysis.api.symbols.KaParameterSymbol`](../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-parameter-symbol/index.md)). Dispatches to the piece of its kind: [`ValueParameter`](index.md#valueparameter), [`ContextParameter`](index.md#contextparameter), or [`ReceiverParameter`](index.md#receiverparameter).


</div>

</div>
### PrimaryConstructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#primaryconstructor">PrimaryConstructor</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The primary constructor of a class, as rendered in the class header, e.g. `(x: Int)` in `class Foo(x: Int)` (see [`KaRenderingOption.PrimaryConstructorInClassHeader`](../../-ka-rendering-option/-companion/index.md#primaryconstructorinclassheader)).

A primary constructor with annotations or an explicit visibility is rendered with a leading space and the `constructor` keyword, as in `class Foo private constructor(x: Int)`. Without parameters, the parentheses are omitted.


</div>

</div>
### Property

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#property">Property</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-property-symbol/index.html">KaPropertySymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A property declaration (`val` or `var`).


</div>

</div>
### PropertyAccessor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#propertyaccessor">PropertyAccessor</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-property-accessor-symbol/index.html">KaPropertyAccessorSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A property getter or setter.


</div>

</div>
### PropertyAccessors

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#propertyaccessors">PropertyAccessors</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-property-symbol/index.html">KaPropertySymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The accessors of a property which are rendered below it, each on its own indented line: the non-default accessors, and the default accessors carrying annotations.


</div>

</div>
### PropertyAnnotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#propertyannotations">PropertyAnnotations</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-property-symbol/index.html">KaPropertySymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The annotations of a property, including those of its backing field and default setter parameter, which have no rendered declaration of their own and so are rendered here with use-site targets, e.g. `@field:Foo`.


</div>

</div>
### PropertyInitializer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#propertyinitializer">PropertyInitializer</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-property-symbol/index.html">KaPropertySymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The initializer of a property, including the leading `=`, e.g. `= 42`.

Only the initializer of a `const` property is rendered by default, as it is a compile-time constant which is part of the property's declaration in source code.


</div>

</div>
### PropertyReturnType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#propertyreturntype">PropertyReturnType</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-property-symbol/index.html">KaPropertySymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The type of property, including the leading colon, e.g. `: String`.


</div>

</div>
### ReceiverParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#receiverparameter">ReceiverParameter</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-parameter-symbol/index.html">KaParameterSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The receiver of an extension callable, including the trailing dot, e.g. `String.` in `fun String.foo()`. A function type or definitely non-nullable receiver is parenthesized, e.g. `(() -> Unit).`.


</div>

</div>
### SamConstructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#samconstructor">SamConstructor</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-sam-constructor-symbol/index.html">KaSamConstructorSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A SAM constructor: the synthetic function which creates an instance of a functional interface from a lambda, e.g. `fun Runnable(function: () -> Unit): Runnable`.


</div>

</div>
### Script

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#script">Script</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-script-symbol/index.html">KaScriptSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A Kotlin script. Nothing is rendered by default.


</div>

</div>
### Supertype

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#supertype">Supertype</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A single supertype, including the constructor call parentheses of a class supertype, e.g. `Base()`.


</div>

</div>
### SupertypeList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#supertypelist">SupertypeList</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The supertype list of a class, including the leading colon, e.g. `: Base(), Runnable`. Nothing is rendered when there are no non-trivial supertypes (`Any` and the implicit `Enum`/`Annotation` supertypes are omitted).


</div>

</div>
### Symbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#symbol">Symbol</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Any [`org.jetbrains.kotlin.analysis.api.symbols.KaSymbol`](../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md). Dispatches to a more specific symbol piece depending on the symbol kind: [`Declaration`](index.md#declaration) for declarations, [`Package`](index.md#package) for packages, and [`File`](index.md#file) for files.


</div>

</div>
### SymbolModifiers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#symbolmodifiers">SymbolModifiers</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

All modifiers of a declaration in the canonical Kotlin order, each followed by a space, e.g. `private abstract `. The modifier list can be transformed with [`KaRenderingOption.Modifiers`](../../-ka-rendering-option/-companion/index.md#modifiers), and single modifiers filtered out with [`KaRenderingOption.AllowedKeywords`](../../-ka-rendering-option/-companion/index.md#allowedkeywords).


</div>

</div>
### SymbolName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#symbolname">SymbolName</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html">KaNamedSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The name of a declaration, as rendered in the declaration itself, e.g. `foo` in `fun foo()`.


</div>

</div>
### Type

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#type">Type</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Any [`org.jetbrains.kotlin.analysis.api.types.KaType`](../../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md). Applies [`KaRenderingOption.TypeTransformation`](../../-ka-rendering-option/-companion/index.md#typetransformation), [`KaRenderingOption.TypeApproximation`](../../-ka-rendering-option/-companion/index.md#typeapproximation), and [`KaRenderingOption.ClassTypeRenderingMode`](../../-ka-rendering-option/-companion/index.md#classtyperenderingmode) to the type (in the mentioned order), then dispatches to the piece of its kind.


</div>

</div>
### TypeAlias

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#typealias">TypeAlias</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-alias-symbol/index.html">KaTypeAliasSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A type alias declaration.


</div>

</div>
### TypeAnnotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#typeannotations">TypeAnnotations</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The annotations attached to a [`KaType`](../../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md), rendered as [`Annotations`](index.md#annotations) (each followed by a space by default).


</div>

</div>
### TypeArgumentList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#typeargumentlist">TypeArgumentList</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-type-projection/index.html">KaTypeProjection</a><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A comma-separated list of type arguments enclosed in angle brackets, e.g. `<Int, String>`.


</div>

</div>
### TypeNullability

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#typenullability">TypeNullability</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The nullability marker of a type, e.g. `?` in `String?`. Nothing is rendered for a non-nullable type or a flexible type.


</div>

</div>
### TypeParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#typeparameter">TypeParameter</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A single type parameter, including its `reified` modifier, variance, and a single upper bound, e.g. `in T : Number`. Multiple upper bounds are rendered in a [`WhereClause`](index.md#whereclause) instead.


</div>

</div>
### TypeParameterList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#typeparameterlist">TypeParameterList</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A comma-separated list of the declaration's type parameters enclosed in angle brackets, e.g. `<T : Number>`. Nothing is rendered when the declaration has no type parameters.


</div>

</div>
### TypeParameterType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#typeparametertype">TypeParameterType</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/index.html">KaTypeParameterType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A reference to a type parameter, e.g. `T`.


</div>

</div>
### TypeProjection

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#typeprojection">TypeProjection</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-type-projection/index.html">KaTypeProjection</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A type projection: an explicit type argument with its variance, e.g. `Number`, `out Number`, or a star projection `*`.


</div>

</div>
### Unknown

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#unknown">Unknown</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-pair/index.html">Pair</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="o">?</span><span class="p">, </span><a href="../index.html">KaPiece</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A dispatcher for [`KaPiece`](../index.md)s for which a renderer is not provided. As such a situation should never happen in correct code, the default implementation of [`Unknown`](index.md#unknown) posts an com.intellij.openapi.diagnostic.Logger.error.


</div>

</div>
### ValueParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#valueparameter">ValueParameter</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.html">KaValueParameterSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A single value parameter, including its modifiers, name, type, and default value. A parameter which declares a property in the primary constructor also carries the property's modifiers and its `val`/`var` (see [`KaRenderingOption.PrimaryConstructorInClassHeader`](../../-ka-rendering-option/-companion/index.md#primaryconstructorinclassheader)).


</div>

</div>
### ValueParameterAnnotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#valueparameterannotations">ValueParameterAnnotations</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.html">KaValueParameterSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The annotations of a value parameter. For a parameter which declares a property in the primary constructor, the annotations of the property and its components are also rendered here, with use-site targets, e.g. `@property:Foo`.


</div>

</div>
### ValueParameterDefaultValue

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#valueparameterdefaultvalue">ValueParameterDefaultValue</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.html">KaValueParameterSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The default value of a value parameter, including the leading `=`, e.g. `= ...`. Nothing is rendered for a parameter without a default value.


</div>

</div>
### ValueParameterDefaultValueExpression

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#valueparameterdefaultvalueexpression">ValueParameterDefaultValueExpression</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.html">KaValueParameterSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The default value expression of a value parameter, without the leading `=`.

The expression is not part of the symbol, so it is rendered as an `...` placeholder.


</div>

</div>
### ValueParameterList

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#valueparameterlist">ValueParameterList</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The parenthesized value parameter list of a function, e.g. `(a: Int, b: String)`.


</div>

</div>
### ValueParameterType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#valueparametertype">ValueParameterType</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.html">KaValueParameterSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The type of value parameter, including the leading colon, e.g. `: String`.


</div>

</div>
### Variable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#variable">Variable</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Any variable-like declaration ([`org.jetbrains.kotlin.analysis.api.symbols.KaVariableSymbol`](../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.md)). Dispatches to the piece of its kind: [`Property`](index.md#property), [`LocalVariable`](index.md#localvariable), [`JavaField`](index.md#javafield), [`BackingField`](index.md#backingfield), [`EnumEntry`](index.md#enumentry), or [`Parameter`](index.md#parameter).


</div>

</div>
### WhereClause

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#whereclause">WhereClause</a><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The `where` clause listing the bounds of type parameters that have more than one upper bound, including the leading space, e.g. `where T : A, T : B`. Nothing is rendered when no type parameter has multiple bounds.


</div>

</div>
## Functions
### create

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#create">T</a><span class="o">> </span><a href="index.html#create"><span class="nf">create</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../index.html">KaPiece</a><span class="o"><</span><a href="index.html#create">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Creates a new [`KaPiece`](../index.md).

Important: the Analysis API provides default [`KaPieceRenderer`](../../-ka-piece-renderer/index.md)s only for [`KaPiece`](../index.md)s listed in this object. For all custom pieces, you must provide the default renderer by yourself. If the renderer is not set for a custom piece, it will be dispatched to [`Unknown`](index.md#unknown).


</div>

</div>
