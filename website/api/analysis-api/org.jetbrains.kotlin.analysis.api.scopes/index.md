---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.scopes"
---

# org.jetbrains.kotlin.analysis.api.scopes
## Types
### [`KaScope`](-ka-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-scope/index.html">KaScope</a> : <a href="-ka-scope-like/index.html">KaScopeLike</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](-ka-scope/index.md) provides access to the declarations contained in a specific [`declaration`](../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md), file, or package, such as classes, type aliases, functions, properties, and constructors.


</div>

</div>
### [`KaScopeLike`](-ka-scope-like/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-scope-like/index.html">KaScopeLike</a> : <a href="../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>
</span></code></pre></div>
</div>

</div>
### [`KaTypeScope`](-ka-type-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-type-scope/index.html">KaTypeScope</a> : <a href="-ka-scope-like/index.html">KaScopeLike</a>
</span></code></pre></div>
</div>


<div markdown>

A scope which contains members whose use-site type parameters have been substituted with the type arguments of a concrete [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md). Callable declarations with substituted type parameters are represented as [`KaCallableSignature`](../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.md).


</div>

</div>
## Properties
### [`combinedDeclaredMemberScope`](combined-declared-member-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="combined-declared-member-scope.html">combinedDeclaredMemberScope</a><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](-ka-scope/index.md) containing all members explicitly declared in the given [`KaDeclarationContainerSymbol`](../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md).


</div>

</div>
### [`combinedMemberScope`](combined-member-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="combined-member-scope.html">combinedMemberScope</a><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](-ka-scope/index.md) containing all members from [`memberScope`](member-scope.md) and [`staticMemberScope`](static-member-scope.md).


</div>

</div>
### [`declaredMemberScope`](declared-member-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="declared-member-scope.html">declaredMemberScope</a><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](-ka-scope/index.md) containing the non-static callables (functions, properties, and constructors) and inner classes explicitly declared in the given [`KaDeclarationContainerSymbol`](../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md).


</div>

</div>
### [`delegatedMemberScope`](delegated-member-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="delegated-member-scope.html">delegatedMemberScope</a><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](-ka-scope/index.md) containing synthetic callables (functions and properties) created by interface delegation.


</div>

</div>
### [`fileScope`](file-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="p">.</span><a href="file-scope.html">fileScope</a><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](-ka-scope/index.md) containing the top-level declarations (such as classes, functions and properties) in the given [`KaFileSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md).


</div>

</div>
### [`memberScope`](member-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="member-scope.html">memberScope</a><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](-ka-scope/index.md) containing non-static callable members (functions, properties, and constructors) and all classifier members (classes and objects) of the given [`KaDeclarationContainerSymbol`](../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md). The scope includes members inherited from the symbol's supertypes, in addition to members which are declared explicitly inside the symbol's body.


</div>

</div>
### [`packageScope`](package-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-package-symbol/index.html">KaPackageSymbol</a><span class="p">.</span><a href="package-scope.html">packageScope</a><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](-ka-scope/index.md) containing all members of the package represented by the given [`KaPackageSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-package-symbol/index.md), not including members of subpackages.


</div>

</div>
### [`scope`](scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="scope.html">scope</a><span class="o">: </span><a href="-ka-type-scope/index.html">KaTypeScope</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeScope`](-ka-type-scope/index.md) for the given [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md), or `null` if the type is [`erroneous`](../org.jetbrains.kotlin.analysis.api.types/-ka-error-type/index.md). The scope includes all members which are callable on a given type. It also includes [synthetic Java properties](https://kotlinlang.org/docs/java-interop.html#getters-and-setters).


</div>

</div>
### [`staticDeclaredMemberScope`](static-declared-member-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="static-declared-member-scope.html">staticDeclaredMemberScope</a><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](-ka-scope/index.md) containing the static callables (functions and properties) and all classifiers (classes and objects) explicitly declared in the given [`KaDeclarationContainerSymbol`](../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md).


</div>

</div>
### [`staticMemberScope`](static-member-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="static-member-scope.html">staticMemberScope</a><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](-ka-scope/index.md) containing the static members of the given [`KaDeclarationContainerSymbol`](../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md).


</div>

</div>
### [`syntheticJavaPropertiesScope`](synthetic-java-properties-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="synthetic-java-properties-scope.html">syntheticJavaPropertiesScope</a><span class="o">: </span><a href="-ka-type-scope/index.html">KaTypeScope</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeScope`](-ka-type-scope/index.md) containing the [synthetic Java properties](https://kotlinlang.org/docs/java-interop.html#getters-and-setters) created for a given [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).


</div>

</div>
## Functions
### [`asCompositeScope`](as-composite-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-ka-scope/index.html">KaScope</a><span class="o">></span><span class="p">.</span><a href="as-composite-scope.html"><span class="nf">asCompositeScope</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

Combines a list of [`KaScope`](-ka-scope/index.md)s into a single composite [`KaScope`](-ka-scope/index.md). The resulting scope contains all members of its constituent scopes.


</div>

</div>
