---
tags:
 - jvm
title: "KaTypeScope"
---

# KaTypeScope

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaTypeScope</a> : <a href="../-ka-scope-like/index.html">KaScopeLike</a>
</span></code></pre></div>A scope which contains members whose use-site type parameters have been substituted with the type arguments of a concrete [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md). Callable declarations with substituted type parameters are represented as [`KaCallableSignature`](../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.md).

#### See also


 - [`KaScopeProvider.scope`](../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-provider/index.md#scope)



</div>

## Properties
### declarationScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="index.html">KaTypeScope</a><span class="p">.</span><a href="index.html#declarationscope">declarationScope</a><span class="o">: </span><a href="../-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../-ka-scope/index.md) containing unsubstituted declarations from the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)'s underlying declaration.


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
### getAllPossibleNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getallpossiblenames"><span class="nf">getAllPossibleNames</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the set of top-level declaration names contained in the scope. The set may contain false positives, i.e. names which aren't contained in the scope.


</div>

</div>
### getCallableSignatures

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getcallablesignatures"><span class="nf">getCallableSignatures</span></a><span class="p">(</span>nameFilter<span class="o">: </span><span class="p">(</span>Name<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns a sequence of [`KaCallableSignature`](../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.md)s contained in the scope which match the [`nameFilter`](index.md#getcallablesignatures).

The implementation of this function needs to retrieve a set of all possible names before processing callables. The overload with `Collection<Name>` should be used when the candidate name set is known.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getcallablesignatures"><span class="nf">getCallableSignatures</span></a><span class="p">(</span>names<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span>Name<span class="o">></span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">></span>
</span></code></pre></div><div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getcallablesignatures"><span class="nf">getCallableSignatures</span></a><span class="p">(</span><span class="kd">vararg </span>names<span class="o">: </span>Name<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.html">KaCallableSignature</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns a sequence of [`KaCallableSignature`](../../org.jetbrains.kotlin.analysis.api.signatures/-ka-callable-signature/index.md)s contained in the scope which match the given [`names`](index.md#getcallablesignatures).

The implementation of this function is optimized compared to using a name filter and should be used when the candidate name set is known.


</div>

</div>
### getClassifierSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getclassifiersymbols"><span class="nf">getClassifierSymbols</span></a><span class="p">(</span>nameFilter<span class="o">: </span><span class="p">(</span>Name<span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns a sequence of [`KaClassifierSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md)s contained in the scope which match the [`nameFilter`](index.md#getclassifiersymbols).

The result includes:

 - Nested classes


 - Inner classes


 - Nested type aliases for a class scope


 - Top-level classes and top-level type aliases for a file scope


The implementation of this function needs to retrieve a set of all possible names before processing classifiers. The overload with `Collection<Name>` should be used when the candidate name set is known.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getclassifiersymbols"><span class="nf">getClassifierSymbols</span></a><span class="p">(</span>names<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span>Name<span class="o">></span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">></span>
</span></code></pre></div><div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getclassifiersymbols"><span class="nf">getClassifierSymbols</span></a><span class="p">(</span><span class="kd">vararg </span>names<span class="o">: </span>Name<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.html">KaClassifierSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns a sequence of [`KaClassifierSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/index.md)s contained in the scope which match the given [`names`](index.md#getclassifiersymbols).

The result includes:

 - Nested classes


 - Inner classes


 - Nested type aliases for a class scope


 - Top-level classes and top-level type aliases for a file scope


The implementation of this function is optimized compared to using a name filter and should be used when the candidate name set is known.


</div>

</div>
### getConstructors

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getconstructors"><span class="nf">getConstructors</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns a sequence of [`KaConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md)s contained in the scope.


</div>

</div>
### getPossibleCallableNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getpossiblecallablenames"><span class="nf">getPossibleCallableNames</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the set of top-level callable names contained in the scope. The set may contain false positives, i.e. names which aren't contained in the scope.


</div>

</div>
### getPossibleClassifierNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getpossibleclassifiernames"><span class="nf">getPossibleClassifierNames</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the set of top-level classifier names contained in the scope. The set may contain false positives, i.e. names which aren't contained in the scope.


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
### mayContainName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#maycontainname"><span class="nf">mayContainName</span></a><span class="p">(</span>name<span class="o">: </span>Name<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether the scope might contain the given [`name`](index.md#maycontainname).

Since [`getPossibleCallableNames`](index.md#getpossiblecallablenames) and [`getPossibleClassifierNames`](index.md#getpossibleclassifiernames) admit false positives, the result may be `true` even if the scope doesn't contain a declaration with such a name. The reverse is not so: when [`mayContainName`](index.md#maycontainname) is `false`, the scope definitely doesn't contain a declaration with that name.


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
