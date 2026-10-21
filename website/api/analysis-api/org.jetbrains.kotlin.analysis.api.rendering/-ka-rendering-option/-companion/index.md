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
### AllowedKeywords

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#allowedkeywords">AllowedKeywords</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><span class="kd">context</span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span><a href="../../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">) </span><span class="p">(</span><a href="../../../../psi-api/org.jetbrains.kotlin.lexer/-kt-keyword-token/index.html">KtKeywordToken</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A function specifying which keywords are rendered. A keyword for which the predicate returns `false` is omitted, together with the whitespace which separates it from what follows.

The option covers the keywords of declarations and types, such as modifiers, `fun`, `class`, `constructor`, `where`, and `dynamic`. It does not affect keywords which are part of a value, such as `null`, `true`, and `false`.

By default, all keywords are rendered.


</div>

</div>
### Annotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#annotations">Annotations</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><span class="kd">context</span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span><a href="../../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">) </span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation/index.html">KaAnnotation</a><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Computes the annotations to render for an annotated element, in the order they are rendered. An omitted annotation is dropped together with the whitespace which separates it from what follows.

By default, all annotations of the element are rendered in their original order, except for `@ParameterName`. That annotation is how the name of a function type parameter is encoded, and the name is already rendered as part of the parameter itself (see [`KaPiece.FunctionTypeParameter`](../../-ka-piece/-companion/index.md#functiontypeparameter)), so rendering the annotation as well would duplicate it.


</div>

</div>
### AnnotationsOnNewLine

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#annotationsonnewline">AnnotationsOnNewLine</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><span class="kd">context</span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span><a href="../../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">) </span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Whether the annotations of the given element are placed on their own line rather than inline before it.


</div>

</div>
### ClassMemberOrdering

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#classmemberordering">ClassMemberOrdering</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><a href="../-class-member-comparator/index.html">KaRenderingOption.ClassMemberComparator</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A comparator establishing the order in which class members are rendered.


</div>

</div>
### ClassMembers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#classmembers">ClassMembers</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><span class="kd">context</span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span><a href="../../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">) </span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Computes the members to render for a [`KaClassSymbol`](../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md), in the order they are gathered.

By default, all declared members of a class, interface or an object are rendered, including both static and non-static ones.

The primary constructor and the properties which it declares are excluded when the primary constructor is rendered in the class header (see [`PrimaryConstructorInClassHeader`](index.md#primaryconstructorinclassheader)), as they are already rendered there.


</div>

</div>
### ClassTypeQualification

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#classtypequalification">ClassTypeQualification</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><a href="../../-ka-class-type-qualification/index.html">KaClassTypeQualification</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

How qualified class type names are rendered (with the package, with outer classifiers, or as a simple name).


</div>

</div>
### ClassTypeRenderingMode

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#classtyperenderingmode">ClassTypeRenderingMode</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><a href="../../-ka-class-type-rendering-mode/index.html">KaClassTypeRenderingMode</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

How a class type which involves a type alias is rendered: as the abbreviation (the type alias application), as its expansion, or as one of them with the other in a comment.

The mode is applied to each type as it is rendered, so it also affects nested types, such as type arguments. It runs after [`TypeTransformation`](index.md#typetransformation) and [`TypeApproximation`](index.md#typeapproximation).


</div>

</div>
### ContextParametersOnNewLine

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#contextparametersonnewline">ContextParametersOnNewLine</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><span class="kd">context</span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span><a href="../../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">) </span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Whether the `context(...)` parameters of the given element are placed on their own line rather than inline.


</div>

</div>
### ExcludedClassMemberOrigins

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#excludedclassmemberorigins">ExcludedClassMemberOrigins</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-origin/index.html">KaSymbolOrigin</a><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The symbol origins whose members are excluded from a rendered class body (e.g. inherited, generated, or delegated members).


</div>

</div>
### ExtraLineBetweenMembers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#extralinebetweenmembers">ExtraLineBetweenMembers</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Whether a blank line separates consecutive members within a class body.


</div>

</div>
### FlexibleTypeShrinking

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#flexibletypeshrinking">FlexibleTypeShrinking</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Whether a flexible type is shrunk to its compact form instead of being rendered as the `(lower..upper)` range of its bounds.

A flexible type whose bounds differ only in nullability is shrunk to its lower bound followed by `!`, so `String..String?` is rendered as `String!`. A flexible type between a mutable collection and its read-only counterpart is shrunk to the collection name carrying a `(Mutable)` marker, so `MutableList<String!>..List<String!>?` is rendered as `(Mutable)List<String!>!`. Any other flexible type has no compact form and is rendered as a range regardless of this option.

The option is applied to each type as it is rendered, so it also affects nested types, such as type arguments.

Flexible types are shrunk by default, as the range form exposes the bounds of a type which cannot be written in Kotlin source code in the first place.


</div>

</div>
### LinkSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#linksymbols">LinkSymbols</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Whether rendered identifiers are linked to the symbols they reference via [`KaTextAttribute.Symbol`](../../-ka-text-attribute/-symbol/index.md).

When disabled, renderers also skip the symbol resolution which is only needed for linking, such as resolving the segments of qualified class and package names. Disabled by default, as an output which produces plain text drops the links anyway.


</div>

</div>
### Modifiers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#modifiers">Modifiers</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><span class="kd">context</span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span><a href="../../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">) </span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../../psi-api/org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="o">></span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../../psi-api/org.jetbrains.kotlin.lexer/-kt-modifier-keyword-token/index.html">KtModifierKeywordToken</a><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Transforms the modifiers of a declaration. The transformer may drop, add, or reorder modifiers.

The default modifiers are given in the canonical Kotlin order (see [`KtTokens.MODIFIER_KEYWORDS_ARRAY`](../../../../psi-api/org.jetbrains.kotlin.lexer/-kt-tokens/-m-o-d-i-f-i-e-r_-k-e-y-w-o-r-d-s_-a-r-r-a-y.md)), and the returned modifiers are rendered in the order they are returned. As modifiers are keywords, [`AllowedKeywords`](index.md#allowedkeywords) is still applied to each of them afterward.

The option covers every modifier of every declaration, including the modifiers of value parameters (`vararg`, `crossinline`, `noinline`) and of type parameters (`reified`, and the declaration-site variance `in`/`out`). It does not cover keywords which are not modifiers, such as `fun`, `val`, `var`, `class`, or `constructor`.

By default, the declaration's own modifiers are rendered in the canonical order.


</div>

</div>
### MultilineValueParameterLists

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#multilinevalueparameterlists">MultilineValueParameterLists</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Whether a value parameter list with more than one parameter is rendered with each parameter on its own line, with the parentheses on lines of their own. A list with at most one parameter is rendered on a single line regardless of this option.

Disabled by default, so every value parameter list is rendered on a single line, e.g. `(a: Int, b: String)`.


</div>

</div>
### PrimaryConstructorInClassHeader

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#primaryconstructorinclassheader">PrimaryConstructorInClassHeader</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Whether the primary constructor is rendered in the class header (e.g. `class Foo(x: Int)`) rather than as a body member.


</div>

</div>
### TypeApproximation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#typeapproximation">TypeApproximation</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><a href="../../-ka-type-approximation/index.html">KaTypeApproximation</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Whether every rendered [`KaType`](../../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is approximated to a type that can be written in Kotlin source code, and in which direction.

The approximation is applied to each type as it is rendered, so it also affects nested types. It runs after [`TypeTransformation`](index.md#typetransformation).


</div>

</div>
### TypeTransformation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#typetransformation">TypeTransformation</a><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><span class="kd">context</span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span><a href="../../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">) </span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span><span class="o"> -> </span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A transformation applied to every rendered [`KaType`](../../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) before it is printed.

The transformation is applied to each type as it is rendered, so it also affects nested types, such as type arguments, upper bounds, and the components of flexible and intersection types. It runs before [`TypeApproximation`](index.md#typeapproximation).

By default, warning-level nullability annotations are treated as strict ones (see [`augmentedByWarningLevelAnnotations`](../../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.md#augmentedbywarninglevelannotations)), so `@RecentlyNullable X!` is rendered as `X?`.


</div>

</div>
## Functions
### create

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="index.html#create">T</a><span class="o">> </span><a href="index.html#create"><span class="nf">create</span></a><span class="p">(</span>defaultValue<span class="o">: </span><a href="index.html#create">T</a><span class="p">)</span><span class="o">: </span><a href="../index.html">KaRenderingOption</a><span class="o"><</span><a href="index.html#create">T</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Creates a rendering option with the provided [`defaultValue`](index.md#create).


</div>

</div>
