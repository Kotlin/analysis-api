---
tags:
 - jvm
title: "KaDeclarationContainerSymbol"
---

# KaDeclarationContainerSymbol

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaDeclarationContainerSymbol</a> : <a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a>
</span></code></pre></div>A [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) which may contain declarations. These declarations may be accessed through the [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md)s provided by [`KaScopeProvider`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md).

#### Inheritors


 - [`KaClassSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md)
 - [`KaScriptSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-script-symbol/index.md)



</div>

## Properties
### [`anchorPsi`](../-ka-named-symbol/index.md#anchorpsi)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-named-symbol/index.html#anchorpsi">anchorPsi</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A PsiElement associated with the symbol. Usually, it is the best PsiElement representation for a particular [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md).


</div>

</div>
### [`combinedDeclaredMemberScope`](../../org.jetbrains.kotlin.analysis.api.scopes/combined-declared-member-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/combined-declared-member-scope.html">combinedDeclaredMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing all members explicitly declared in the given [`KaDeclarationContainerSymbol`](index.md).


</div>

</div>
### [`combinedMemberScope`](../../org.jetbrains.kotlin.analysis.api.scopes/combined-member-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/combined-member-scope.html">combinedMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing all members from [`memberScope`](../../org.jetbrains.kotlin.analysis.api.scopes/member-scope.md) and [`staticMemberScope`](../../org.jetbrains.kotlin.analysis.api.scopes/static-member-scope.md).


</div>

</div>
### [`containingDeclaration`](../-ka-named-symbol/index.md#containingdeclaration)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#containingdeclaration">containingDeclaration</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`KaDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) which contains this symbol, or `null` if there is no containing declaration:


</div>

</div>
### [`containingFile`](../-ka-named-symbol/index.md#containingfile)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#containingfile">containingFile</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`KaFileSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md) which contains this symbol, or `null` if this symbol is already a [`KaFileSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md), since it has no containing file. Also `null` for Java and library declarations.


</div>

</div>
### [`containingModule`](../-ka-named-symbol/index.md#containingmodule)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#containingmodule">containingModule</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaModule`](../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md) which contains this symbol.


</div>

</div>
### [`containingSymbol`](../-ka-named-symbol/index.md#containingsymbol)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#containingsymbol">containingSymbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) which contains this symbol, or `null` if there is no containing declaration:


</div>

</div>
### [`declaredMemberScope`](../../org.jetbrains.kotlin.analysis.api.scopes/declared-member-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/declared-member-scope.html">declaredMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing the non-static callables (functions, properties, and constructors) and inner classes explicitly declared in the given [`KaDeclarationContainerSymbol`](index.md).


</div>

</div>
### [`defaultAnnotationTargets`](../-ka-named-symbol/index.md#defaultannotationtargets)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#defaultannotationtargets">defaultAnnotationTargets</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-target/index.html">KaAnnotationTarget</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A set of annotation targets matching for the given symbol, or `null` if the symbol cannot be annotated. Annotations with one of targets from the returned set can be placed on the [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) without an explicit use-site target.


</div>

</div>
### [`delegatedMemberScope`](../../org.jetbrains.kotlin.analysis.api.scopes/delegated-member-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/delegated-member-scope.html">delegatedMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing synthetic callables (functions and properties) created by interface delegation.


</div>

</div>
### [`deprecation`](../-ka-named-symbol/index.md#deprecation)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#deprecation">deprecation</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-deprecation/index.html">KaDeprecation</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The deprecation status of the given symbol, or `null` if the symbol is not deprecated.


</div>

</div>
### [`importableFqName`](../-ka-named-symbol/index.md#importablefqname)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#importablefqname">importableFqName</a><span class="o">: </span>FqName<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A FqName which can be used to import the given symbol, or `null` if the symbol cannot be imported.


</div>

</div>
### [`isDeprecated`](../-ka-named-symbol/index.md#isdeprecated)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#isdeprecated">isDeprecated</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the symbol is deprecated at any level.


</div>

</div>
### [`isLocal`](../-ka-named-symbol/index.md#islocal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#islocal">isLocal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Indicates whether a symbol is defined locally within a body.


</div>

</div>
### [`isTopLevel`](../-ka-named-symbol/index.md#istoplevel)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#istoplevel">isTopLevel</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Indicates whether a [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) is at the top level.


</div>

</div>
### [`location`](../-ka-named-symbol/index.md#location)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-named-symbol/index.html#location">location</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-location/index.html">KaSymbolLocation</a>
</span></code></pre></div>
</div>


<div markdown>

The kind of location where a symbol is declared in code, e.g. [`KaSymbolLocation.TOP_LEVEL`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-location/-t-o-p_-l-e-v-e-l/index.md) for top-level declarations.


</div>

</div>
### [`memberScope`](../../org.jetbrains.kotlin.analysis.api.scopes/member-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/member-scope.html">memberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing non-static callable members (functions, properties, and constructors) and all classifier members (classes and objects) of the given [`KaDeclarationContainerSymbol`](index.md). The scope includes members inherited from the symbol's supertypes, in addition to members which are declared explicitly inside the symbol's body.


</div>

</div>
### [`name`](../-ka-named-symbol/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#name">name</a><span class="o">: </span>Name<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The name of the [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) if it has one.


</div>

</div>
### [`origin`](../-ka-named-symbol/index.md#origin)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-named-symbol/index.html#origin">origin</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-origin/index.html">KaSymbolOrigin</a>
</span></code></pre></div>
</div>


<div markdown>

The kind of data source or generation the symbol originates from (e.g. source files, libraries, compiler plugins).


</div>

</div>
### [`psi`](../-ka-named-symbol/index.md#psi)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-named-symbol/index.html#psi">psi</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

<strong>The API is obsolete and will be deprecated soon. Use </strong>[`<strong>realPsi</strong>`](../-ka-named-symbol/index.md#realpsi)<strong> or </strong>[`<strong>anchorPsi</strong>`](../-ka-named-symbol/index.md#anchorpsi)<strong> instead.</strong>


</div>

</div>
### [`realPsi`](../-ka-named-symbol/index.md#realpsi)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-named-symbol/index.html#realpsi">realPsi</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A PsiElement explicitly present in the code (source or library). This PsiElement is sufficient to restore the symbol via the [`symbol`](../../org.jetbrains.kotlin.analysis.api.symbols/symbol.md) API without any additional information.


</div>

</div>
### [`staticDeclaredMemberScope`](../../org.jetbrains.kotlin.analysis.api.scopes/static-declared-member-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/static-declared-member-scope.html">staticDeclaredMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing the static callables (functions and properties) and all classifiers (classes and objects) explicitly declared in the given [`KaDeclarationContainerSymbol`](index.md).


</div>

</div>
### [`staticMemberScope`](../../org.jetbrains.kotlin.analysis.api.scopes/static-member-scope.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/static-member-scope.html">staticMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing the static members of the given [`KaDeclarationContainerSymbol`](index.md).


</div>

</div>
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
### createPointer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#createpointer"><span class="nf">createPointer</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.pointers/-ka-symbol-pointer/index.html">KaSymbolPointer</a><span class="o"><</span><a href="index.html">KaDeclarationContainerSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSymbolPointer`](../../org.jetbrains.kotlin.analysis.api.symbols.pointers/-ka-symbol-pointer/index.md) which can be used to retrieve the symbol in a different [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) block (i.e. a different [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)).


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
### [`psi`](../-ka-named-symbol/index.md#psi)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../-ka-named-symbol/index.html#psi">PSI</a><span class="o"> : </span>PsiElement<span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#psi"><span class="nf">psi</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-named-symbol/index.html#psi">PSI</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The API is obsolete and will be deprecated soon. Use </strong>[`<strong>realPsi</strong>`](../-ka-named-symbol/index.md#realpsi)<strong> or </strong>[`<strong>anchorPsi</strong>`](../-ka-named-symbol/index.md#anchorpsi)<strong> instead.</strong>


</div>

</div>
### [`psiSafe`](../-ka-named-symbol/index.md#psisafe)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../-ka-named-symbol/index.html#psisafe">PSI</a><span class="o"> : </span>PsiElement<span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#psisafe"><span class="nf">psiSafe</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-named-symbol/index.html#psisafe">PSI</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

<strong>The API is obsolete and will be deprecated soon. Use </strong>[`<strong>realPsi</strong>`](../-ka-named-symbol/index.md#realpsi)<strong> or </strong>[`<strong>anchorPsi</strong>`](../-ka-named-symbol/index.md#anchorpsi)<strong> instead.</strong>


</div>

</div>
### [`sourcePsi`](../-ka-named-symbol/index.md#sourcepsi)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../-ka-named-symbol/index.html#sourcepsi">PSI</a><span class="o"> : </span>PsiElement<span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#sourcepsi"><span class="nf">sourcePsi</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-named-symbol/index.html#sourcepsi">PSI</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

<strong>The API is obsolete and will be deprecated soon. Use </strong>[`<strong>realPsi</strong>`](../-ka-named-symbol/index.md#realpsi)<strong> or </strong>[`<strong>anchorPsi</strong>`](../-ka-named-symbol/index.md#anchorpsi)<strong> instead.</strong>


</div>

</div>
### [`sourcePsiSafe`](../-ka-named-symbol/index.md#sourcepsisafe)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../-ka-named-symbol/index.html#sourcepsisafe">PSI</a><span class="o"> : </span>PsiElement<span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../-ka-named-symbol/index.html#sourcepsisafe"><span class="nf">sourcePsiSafe</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-named-symbol/index.html#sourcepsisafe">PSI</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

<strong>The API is obsolete and will be deprecated soon. Use </strong>[`<strong>realPsi</strong>`](../-ka-named-symbol/index.md#realpsi)<strong> or </strong>[`<strong>anchorPsi</strong>`](../-ka-named-symbol/index.md#anchorpsi)<strong> instead.</strong>


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
