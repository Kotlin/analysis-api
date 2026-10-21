---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.symbols"
---

# org.jetbrains.kotlin.analysis.api.symbols
## Types
### [`KaAdditionalKDocResolutionProvider`](-ka-additional-k-doc-resolution-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-ka-additional-k-doc-resolution-provider/index.html">KaAdditionalKDocResolutionProvider</a>
</span></code></pre></div>
</div>


<div markdown>

An extension point to provide additional symbols for a KDoc reference. KDoc link resolution will use symbols returned by this extension point only if the real resolution was unsuccessful.


</div>

</div>
### [`KaAnonymousFunctionSymbol`](-ka-anonymous-function-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-anonymous-function-symbol/index.html">KaAnonymousFunctionSymbol</a> : <a href="-ka-function-symbol/index.html">KaFunctionSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaAnonymousFunctionSymbol`](-ka-anonymous-function-symbol/index.md) represents a [lambda or anonymous function declaration](https://kotlinlang.org/docs/lambdas.html#lambda-expressions-and-anonymous-functions).


</div>

</div>
### [`KaAnonymousObjectSymbol`](-ka-anonymous-object-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-anonymous-object-symbol/index.html">KaAnonymousObjectSymbol</a> : <a href="-ka-class-symbol/index.html">KaClassSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaAnonymousObjectSymbol`](-ka-anonymous-object-symbol/index.md) represents anonymous object declarations.


</div>

</div>
### [`KaBackingFieldSymbol`](-ka-backing-field-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-backing-field-symbol/index.html">KaBackingFieldSymbol</a> : <a href="-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaBackingFieldSymbol`](-ka-backing-field-symbol/index.md) represents the [backing field](https://kotlinlang.org/docs/properties.html#backing-fields) of a property.


</div>

</div>
### [`KaCallableImplementationState`](-ka-callable-implementation-state/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-callable-implementation-state/index.html">KaCallableImplementationState</a>
</span></code></pre></div>
</div>


<div markdown>

Describes the implementation state of a [`KaCallableSymbol`](-ka-callable-symbol/index.md) in the context of a specific [`KaClassSymbol`](-ka-class-symbol/index.md).


</div>

</div>
### [`KaCallableSymbol`](-ka-callable-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-callable-symbol/index.html">KaCallableSymbol</a> : <a href="-ka-declaration-symbol/index.html">KaDeclarationSymbol</a>, <a href="../org.jetbrains.kotlin.analysis.api.base/-ka-context-receivers-owner/index.html">KaContextReceiversOwner</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaCallableSymbol`](-ka-callable-symbol/index.md) represents callable declarations, such as functions and variables.


</div>

</div>
### [`KaClassifierSymbol`](-ka-classifier-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-classifier-symbol/index.html">KaClassifierSymbol</a> : <a href="-ka-declaration-symbol/index.html">KaDeclarationSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaClassifierSymbol`](-ka-classifier-symbol/index.md) represents a type declaration, including classes, objects, interfaces, type aliases, and type parameters.


</div>

</div>
### [`KaClassInitializerSymbol`](-ka-class-initializer-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-class-initializer-symbol/index.html">KaClassInitializerSymbol</a> : <a href="-ka-declaration-symbol/index.html">KaDeclarationSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaClassInitializerSymbol`](-ka-class-initializer-symbol/index.md) represents an [anonymous initializer declaration](https://kotlinlang.org/docs/reference/grammar.html#anonymousInitializer) in a class body.


</div>

</div>
### [`KaClassKind`](-ka-class-kind/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-class-kind/index.html">KaClassKind</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-class-kind/index.html">KaClassKind</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

The kind of class represented by a [`KaClassSymbol`](-ka-class-symbol/index.md).


</div>

</div>
### [`KaClassLikeSymbol`](-ka-class-like-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-class-like-symbol/index.html">KaClassLikeSymbol</a> : <a href="-ka-classifier-symbol/index.html">KaClassifierSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaClassLikeSymbol`](-ka-class-like-symbol/index.md) represents a class, object, interface, or type alias declaration.


</div>

</div>
### [`KaClassSymbol`](-ka-class-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-class-symbol/index.html">KaClassSymbol</a> : <a href="-ka-class-like-symbol/index.html">KaClassLikeSymbol</a>, <a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaClassSymbol`](-ka-class-symbol/index.md) represents a class, object, or interface declaration.


</div>

</div>
### [`KaConstructorSymbol`](-ka-constructor-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-constructor-symbol/index.html">KaConstructorSymbol</a> : <a href="-ka-function-symbol/index.html">KaFunctionSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaConstructorSymbol`](-ka-constructor-symbol/index.md) represents a class [constructor declaration](https://kotlinlang.org/docs/classes.html#constructors).


</div>

</div>
### [`KaContextParameterSymbol`](-ka-context-parameter-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-context-parameter-symbol/index.html">KaContextParameterSymbol</a> : <a href="-ka-parameter-symbol/index.html">KaParameterSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaContextParameterSymbol`](-ka-context-parameter-symbol/index.md) represents a context parameter of a [`KaNamedFunctionSymbol`](-ka-named-function-symbol/index.md), [`KaAnonymousFunctionSymbol`](-ka-anonymous-function-symbol/index.md), or [`KaKotlinPropertySymbol`](-ka-kotlin-property-symbol/index.md).


</div>

</div>
### [`KaDebugRenderer`](-ka-debug-renderer/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-debug-renderer/index.html">KaDebugRenderer</a><span class="p">(</span>
    <span class="kd">val </span>renderExtra<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span>
    <span class="kd">val </span>renderTypeByProperties<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span>
    <span class="kd">val </span>renderExpandedTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span>
    <span class="kd">val </span>renderIsPublicApi<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`KaDeclarationSymbol`](-ka-declaration-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-ka-declaration-symbol/index.html">KaDeclarationSymbol</a> : <a href="-ka-symbol/index.html">KaSymbol</a>, <a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-annotated-symbol/index.html">KaAnnotatedSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a source-representable declaration such as a class, function, or property.


</div>

</div>
### [`KaDeprecation`](-ka-deprecation/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-deprecation/index.html">KaDeprecation</a>
</span></code></pre></div>
</div>


<div markdown>

Represents the deprecation status of a symbol.


</div>

</div>
### [`KaDeprecationLevel`](-ka-deprecation-level/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-ka-deprecation-level/index.html">KaDeprecationLevel</a>
</span></code></pre></div>
</div>


<div markdown>

Deprecation severity levels, corresponding to [`DeprecationLevel`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-deprecation-level/index.html) in the Kotlin standard library.


</div>

</div>
### [`KaDestructuringDeclarationSymbol`](-ka-destructuring-declaration-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-destructuring-declaration-symbol/index.html">KaDestructuringDeclarationSymbol</a> : <a href="-ka-declaration-symbol/index.html">KaDeclarationSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaSymbol`](-ka-symbol/index.md) created from a [`destructuring declaration`](../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration/index.md) (possibly from a lambda parameter).


</div>

</div>
### [`KaEnumEntrySymbol`](-ka-enum-entry-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-enum-entry-symbol/index.html">KaEnumEntrySymbol</a> : <a href="-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaEnumEntrySymbol`](-ka-enum-entry-symbol/index.md) represents an [enum entry declaration](https://kotlinlang.org/docs/enum-classes.html).


</div>

</div>
### [`KaFileSymbol`](-ka-file-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-file-symbol/index.html">KaFileSymbol</a> : <a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-annotated-symbol/index.html">KaAnnotatedSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaFileSymbol`](-ka-file-symbol/index.md) represents a [`KtFile`](../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md).


</div>

</div>
### [`KaFunctionSymbol`](-ka-function-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-function-symbol/index.html">KaFunctionSymbol</a> : <a href="-ka-callable-symbol/index.html">KaCallableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaFunctionSymbol`](-ka-function-symbol/index.md) represents a function-like declaration, including named and anonymous functions, constructors, and property accessors.


</div>

</div>
### [`KaJavaFieldSymbol`](-ka-java-field-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-java-field-symbol/index.html">KaJavaFieldSymbol</a> : <a href="-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaJavaFieldSymbol`](-ka-java-field-symbol/index.md) represents a [Java field declaration](https://docs.oracle.com/javase/specs/jls/se23/html/jls-8.html#jls-8.3).


</div>

</div>
### [`KaKotlinPropertySymbol`](-ka-kotlin-property-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-kotlin-property-symbol/index.html">KaKotlinPropertySymbol</a> : <a href="-ka-property-symbol/index.html">KaPropertySymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaKotlinPropertySymbol`](-ka-kotlin-property-symbol/index.md) represents a Kotlin property symbol, in contrast to [`KaSyntheticJavaPropertySymbol`](-ka-synthetic-java-property-symbol/index.md).


</div>

</div>
### [`KaLocalVariableSymbol`](-ka-local-variable-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-local-variable-symbol/index.html">KaLocalVariableSymbol</a> : <a href="-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaLocalVariableSymbol`](-ka-local-variable-symbol/index.md) represents a local variable.


</div>

</div>
### [`KaNamedClassSymbol`](-ka-named-class-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-named-class-symbol/index.html">KaNamedClassSymbol</a> : <a href="-ka-class-symbol/index.html">KaClassSymbol</a>, <a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html">KaNamedSymbol</a>, <a href="../org.jetbrains.kotlin.analysis.api.base/-ka-context-receivers-owner/index.html">KaContextReceiversOwner</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaNamedClassSymbol`](-ka-named-class-symbol/index.md) represents a named class, object, or interface declaration. The symbol covers most class declarations except for anonymous objects, which are represented by [`KaAnonymousObjectSymbol`](-ka-anonymous-object-symbol/index.md).


</div>

</div>
### [`KaNamedFunctionSymbol`](-ka-named-function-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a> : <a href="-ka-function-symbol/index.html">KaFunctionSymbol</a>, <a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html">KaNamedSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaNamedFunctionSymbol`](-ka-named-function-symbol/index.md) represents a named [function declaration](https://kotlinlang.org/docs/functions.html), such as a top-level function, a class method, or a named local function.


</div>

</div>
### [`KaPackageSymbol`](-ka-package-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-package-symbol/index.html">KaPackageSymbol</a> : <a href="-ka-symbol/index.html">KaSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaPackageSymbol`](-ka-package-symbol/index.md) represents a package as a symbol.


</div>

</div>
### [`KaParameterSymbol`](-ka-parameter-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-parameter-symbol/index.html">KaParameterSymbol</a> : <a href="-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaParameterSymbol`](-ka-parameter-symbol/index.md) represents a value parameter, context parameter, or receiver parameter.


</div>

</div>
### [`KaPropertyAccessorSymbol`](-ka-property-accessor-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-property-accessor-symbol/index.html">KaPropertyAccessorSymbol</a> : <a href="-ka-function-symbol/index.html">KaFunctionSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaPropertyAccessorSymbol`](-ka-property-accessor-symbol/index.md) represents a [getter or setter declaration](https://kotlinlang.org/docs/properties.html#getters-and-setters) of a property.


</div>

</div>
### [`KaPropertyGetterSymbol`](-ka-property-getter-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-property-getter-symbol/index.html">KaPropertyGetterSymbol</a> : <a href="-ka-property-accessor-symbol/index.html">KaPropertyAccessorSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaPropertyGetterSymbol`](-ka-property-getter-symbol/index.md) represents a property getter.


</div>

</div>
### [`KaPropertySetterSymbol`](-ka-property-setter-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-property-setter-symbol/index.html">KaPropertySetterSymbol</a> : <a href="-ka-property-accessor-symbol/index.html">KaPropertyAccessorSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaPropertyGetterSymbol`](-ka-property-getter-symbol/index.md) represents a property setter.


</div>

</div>
### [`KaPropertySymbol`](-ka-property-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-property-symbol/index.html">KaPropertySymbol</a> : <a href="-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaPropertySymbol`](-ka-property-symbol/index.md) represents a [property declaration](https://kotlinlang.org/docs/properties.html).


</div>

</div>
### [`KaReceiverParameterSymbol`](-ka-receiver-parameter-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-receiver-parameter-symbol/index.html">KaReceiverParameterSymbol</a> : <a href="-ka-parameter-symbol/index.html">KaParameterSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A symbol for a receiver parameter of an [extension function or property](https://kotlinlang.org/docs/extensions.html).


</div>

</div>
### [`KaReturnValueStatus`](-ka-return-value-status/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-return-value-status/index.html">KaReturnValueStatus</a>
</span></code></pre></div>
</div>


<div markdown>

The return value status of the function (should it be used, or can it be ignored).


</div>

</div>
### [`KaSamConstructorSymbol`](-ka-sam-constructor-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-sam-constructor-symbol/index.html">KaSamConstructorSymbol</a> : <a href="-ka-function-symbol/index.html">KaFunctionSymbol</a>, <a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html">KaNamedSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaSamConstructorSymbol`](-ka-sam-constructor-symbol/index.md) represents constructors used to build instances of [SAM interfaces](https://kotlinlang.org/docs/fun-interfaces.html#sam-conversions).


</div>

</div>
### [`KaScriptSymbol`](-ka-script-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-script-symbol/index.html">KaScriptSymbol</a> : <a href="-ka-declaration-symbol/index.html">KaDeclarationSymbol</a>, <a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html">KaNamedSymbol</a>, <a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaScriptSymbol`](-ka-script-symbol/index.md) represents a [Kotlin script](https://kotlinlang.org/docs/custom-script-deps-tutorial.html).


</div>

</div>
### [`KaSymbol`](-ka-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-symbol/index.html">KaSymbol</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaSymbol`](-ka-symbol/index.md)s are a core concept in the Analysis API, representing declarations visible to Kotlin. Symbols represent not only declarations in source files, but also declarations from libraries, and those generated by compiler plugins and the compiler itself.


</div>

</div>
### [`KaSymbolLocation`](-ka-symbol-location/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-symbol-location/index.html">KaSymbolLocation</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-symbol-location/index.html">KaSymbolLocation</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Describes the location where a [`KaSymbol`](-ka-symbol/index.md) is declared in code.


</div>

</div>
### [`KaSymbolModality`](-ka-symbol-modality/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-symbol-modality/index.html">KaSymbolModality</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-symbol-modality/index.html">KaSymbolModality</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

A symbol's modality defines its ability to be [inherited](https://kotlinlang.org/docs/inheritance.html).


</div>

</div>
### [`KaSymbolOrigin`](-ka-symbol-origin/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-symbol-origin/index.html">KaSymbolOrigin</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-symbol-origin/index.html">KaSymbolOrigin</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

[`KaSymbolOrigin`](-ka-symbol-origin/index.md) describes the kind of data source (sources, libraries, etc.) or generation (SAM constructors, compiler plugins, etc.) the symbol originates from.


</div>

</div>
### [`KaSymbolProvider`](-ka-symbol-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-symbol-provider/index.html">KaSymbolProvider</a> : <a href="../org.jetbrains.kotlin.analysis.api.components/-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaSymbolProvider`](-ka-symbol-provider/index.md) provides [`KaSymbol`](-ka-symbol/index.md)s for given PSI elements.


</div>

</div>
### [`KaSymbolVisibility`](-ka-symbol-visibility/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-ka-symbol-visibility/index.html">KaSymbolVisibility</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-ka-symbol-visibility/index.html">KaSymbolVisibility</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

The [visibility](https://kotlinlang.org/docs/visibility-modifiers.html) of a [`KaSymbol`](-ka-symbol/index.md). As symbols can represent both Kotlin and Java declarations, [`KaSymbolVisibility`](-ka-symbol-visibility/index.md) covers both visibility definitions.


</div>

</div>
### [`KaSyntheticJavaPropertySymbol`](-ka-synthetic-java-property-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-synthetic-java-property-symbol/index.html">KaSyntheticJavaPropertySymbol</a> : <a href="-ka-property-symbol/index.html">KaPropertySymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaSyntheticJavaPropertySymbol`](-ka-synthetic-java-property-symbol/index.md) represents a synthetic property generated by the compiler for a Java field associated with a getter or setter. This allows Java fields to be accessed like Kotlin properties.


</div>

</div>
### [`KaTypeAliasSymbol`](-ka-type-alias-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-type-alias-symbol/index.html">KaTypeAliasSymbol</a> : <a href="-ka-class-like-symbol/index.html">KaClassLikeSymbol</a>, <a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html">KaNamedSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaTypeAliasSymbol`](-ka-type-alias-symbol/index.md) represents a type alias declaration.


</div>

</div>
### [`KaTypeParameterSymbol`](-ka-type-parameter-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a> : <a href="-ka-classifier-symbol/index.html">KaClassifierSymbol</a>, <a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html">KaNamedSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaTypeParameterSymbol`](-ka-type-parameter-symbol/index.md) represents a type parameter of a class, function, property, or type alias.


</div>

</div>
### [`KaValueParameterSymbol`](-ka-value-parameter-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="-ka-value-parameter-symbol/index.html">KaValueParameterSymbol</a> : <a href="-ka-parameter-symbol/index.html">KaParameterSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaValueParameterSymbol`](-ka-value-parameter-symbol/index.md) represents a value parameter of a function, constructor, or property setter.


</div>

</div>
### [`KaVariableSymbol`](-ka-variable-symbol/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-ka-variable-symbol/index.html">KaVariableSymbol</a> : <a href="-ka-callable-symbol/index.html">KaCallableSymbol</a>, <a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html">KaNamedSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

[`KaVariableSymbol`](-ka-variable-symbol/index.md) represents a variable-like declaration, including properties, local variables, and value parameters.


</div>

</div>
## Properties
### [`classSymbol`](class-symbol.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">.</span><a href="class-symbol.html">classSymbol</a><span class="o">: </span><a href="-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaClassSymbol`](-ka-class-symbol/index.md) for the given [`KtClassOrObject`](../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.md), or `null` for [`KtEnumEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry/index.md) declarations.


</div>

</div>
### [`namedClassSymbol`](named-class-symbol.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">.</span><a href="named-class-symbol.html">namedClassSymbol</a><span class="o">: </span><a href="-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaNamedClassSymbol`](-ka-named-class-symbol/index.md) for the given named [`KtClassOrObject`](../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.md), or `null` for [`KtEnumEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry/index.md) declarations and object literals.


</div>

</div>
### [`rootPackageSymbol`](root-package-symbol.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="root-package-symbol.html">rootPackageSymbol</a><span class="o">: </span><a href="-ka-package-symbol/index.html">KaPackageSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaPackageSymbol`](-ka-package-symbol/index.md) for the root package, which is the special package with an empty fully-qualified name.


</div>

</div>
### [`symbol`](symbol.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-backing-field/index.html">KtBackingField</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-backing-field-symbol/index.html">KaBackingFieldSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaBackingFieldSymbol`](-ka-backing-field-symbol/index.md) for the given [`KtBackingField`](../../psi-api/org.jetbrains.kotlin.psi/-kt-backing-field/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-class-initializer/index.html">KtClassInitializer</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-class-initializer-symbol/index.html">KaClassInitializerSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaClassInitializerSymbol`](-ka-class-initializer-symbol/index.md) for the given [`KtClassInitializer`](../../psi-api/org.jetbrains.kotlin.psi/-kt-class-initializer/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor/index.html">KtConstructor</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-constructor-symbol/index.html">KaConstructorSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaConstructorSymbol`](-ka-constructor-symbol/index.md) for the given [`KtConstructor`](../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-context-receiver/index.html">KtContextReceiver</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-context-parameter-symbol/index.html">KaContextParameterSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

Represents [`KtContextReceiver`](../../psi-api/org.jetbrains.kotlin.psi/-kt-context-receiver/index.md) as a [`KaContextParameterSymbol`](-ka-context-parameter-symbol/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-declaration-symbol/index.html">KaDeclarationSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaDeclarationSymbol`](-ka-declaration-symbol/index.md) for the given [`KtDeclaration`](../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration/index.html">KtDestructuringDeclaration</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-destructuring-declaration-symbol/index.html">KaDestructuringDeclarationSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaDestructuringDeclarationSymbol`](-ka-destructuring-declaration-symbol/index.md) for the given [`KtDestructuringDeclaration`](../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaVariableSymbol`](-ka-variable-symbol/index.md) that corresponds to the local variable introduced by the given [`KtDestructuringDeclarationEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry/index.html">KtEnumEntry</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-enum-entry-symbol/index.html">KaEnumEntrySymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaEnumEntrySymbol`](-ka-enum-entry-symbol/index.md) for the given [`KtEnumEntry`](../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-file-symbol/index.html">KaFileSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaFileSymbol`](-ka-file-symbol/index.md) for a [`KtFile`](../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-function-literal/index.html">KtFunctionLiteral</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-anonymous-function-symbol/index.html">KaAnonymousFunctionSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaAnonymousFunctionSymbol`](-ka-anonymous-function-symbol/index.md) for the given [`KtFunctionLiteral`](../../psi-api/org.jetbrains.kotlin.psi/-kt-function-literal/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-named-function/index.html">KtNamedFunction</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-function-symbol/index.html">KaFunctionSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaFunctionSymbol`](-ka-function-symbol/index.md) for the given [`KtNamedFunction`](../../psi-api/org.jetbrains.kotlin.psi/-kt-named-function/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-object-declaration/index.html">KtObjectDeclaration</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-class-symbol/index.html">KaClassSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaClassSymbol`](-ka-class-symbol/index.md) for the given [`KtObjectDeclaration`](../../psi-api/org.jetbrains.kotlin.psi/-kt-object-declaration/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-object-literal-expression/index.html">KtObjectLiteralExpression</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-anonymous-object-symbol/index.html">KaAnonymousObjectSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaAnonymousObjectSymbol`](-ka-anonymous-object-symbol/index.md) for the given [`KtObjectLiteralExpression`](../../psi-api/org.jetbrains.kotlin.psi/-kt-object-literal-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-parameter/index.html">KtParameter</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaVariableSymbol`](-ka-variable-symbol/index.md) for the given [`KtParameter`](../../psi-api/org.jetbrains.kotlin.psi/-kt-parameter/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-property/index.html">KtProperty</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaVariableSymbol`](-ka-variable-symbol/index.md) for the given [`KtProperty`](../../psi-api/org.jetbrains.kotlin.psi/-kt-property/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-property-accessor/index.html">KtPropertyAccessor</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-property-accessor-symbol/index.html">KaPropertyAccessorSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaPropertyAccessorSymbol`](-ka-property-accessor-symbol/index.md) for the given [`KtPropertyAccessor`](../../psi-api/org.jetbrains.kotlin.psi/-kt-property-accessor/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-script/index.html">KtScript</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-script-symbol/index.html">KaScriptSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScriptSymbol`](-ka-script-symbol/index.md) for a [`KtScript`](../../psi-api/org.jetbrains.kotlin.psi/-kt-script/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-type-alias/index.html">KtTypeAlias</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-type-alias-symbol/index.html">KaTypeAliasSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeAliasSymbol`](-ka-type-alias-symbol/index.md) for the given [`KtTypeAlias`](../../psi-api/org.jetbrains.kotlin.psi/-kt-type-alias/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-type-parameter/index.html">KtTypeParameter</a><span class="p">.</span><a href="symbol.html">symbol</a><span class="o">: </span><a href="-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeParameterSymbol`](-ka-type-parameter-symbol/index.md) for the given [`KtTypeParameter`](../../psi-api/org.jetbrains.kotlin.psi/-kt-type-parameter/index.md).


</div>

</div>
## Functions
### [`findClass`](find-class.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="find-class.html"><span class="nf">findClass</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaNamedClassSymbol`](-ka-named-class-symbol/index.md) for the specified ClassId, or `null` if such a symbol cannot be found.


</div>

</div>
### [`findClassLike`](find-class-like.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="find-class-like.html"><span class="nf">findClassLike</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaClassLikeSymbol`](-ka-class-like-symbol/index.md) for the specified ClassId, or `null` if such a symbol cannot be found.


</div>

</div>
### [`findPackage`](find-package.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="find-package.html"><span class="nf">findPackage</span></a><span class="p">(</span>fqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="-ka-package-symbol/index.html">KaPackageSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaPackageSymbol`](-ka-package-symbol/index.md) corresponding to the given [`fqName`](find-package.md) if that package exists and is visible from the current use site, or `null` otherwise.


</div>

</div>
### [`findTopLevelCallables`](find-top-level-callables.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="find-top-level-callables.html"><span class="nf">findTopLevelCallables</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">, </span>name<span class="o">: </span>Name<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Finds top-level functions and properties called [`name`](find-top-level-callables.md) in the package called [`packageFqName`](find-top-level-callables.md). Returns only symbols that are visible from the current use-site module.


</div>

</div>
### [`findTypeAlias`](find-type-alias.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="find-type-alias.html"><span class="nf">findTypeAlias</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="-ka-type-alias-symbol/index.html">KaTypeAliasSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaTypeAliasSymbol`](-ka-type-alias-symbol/index.md) for the specified ClassId, or `null` if such a symbol cannot be found.


</div>

</div>
