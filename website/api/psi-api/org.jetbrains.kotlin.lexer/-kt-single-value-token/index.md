---
tags:
 - jvm
title: "KtSingleValueToken"
---

# KtSingleValueToken

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="index.html">KtSingleValueToken</a> : <a href="../-kt-token/index.html">KtToken</a>
</span></code></pre></div>#### Inheritors


 - [`KtKeywordToken`](../-kt-keyword-token/index.md)



</div>

## Constructors
### KtSingleValueToken

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>
    <span class="se">@</span><span class="se">NotNull</span> <span class="se">@</span><span class="se">NonNls</span> debugName<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="p">, </span>
    <span class="se">@</span><span class="se">NotNull</span> <span class="se">@</span><span class="se">NonNls</span> value<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="p">, </span>
    tokenId<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Companion properties
### [`ARRAY_FACTORY`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#array_factory)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#array_factory">ARRAY_FACTORY</a><span class="o">: </span>ArrayFactory<span class="o"><</span>IElementType<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`EMPTY_ARRAY`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#empty_array)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#empty_array">EMPTY_ARRAY</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>IElementType<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`FIRST_TOKEN_INDEX`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#first_token_index)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#first_token_index">FIRST_TOKEN_INDEX</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/index.html">Short</a><span class="o"> = </span><span class="nb">1</span>
</span></code></pre></div>
</div>

</div>
### [`TRUE`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#true)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#true">TRUE</a><span class="o">: </span>IElementType.Predicate
</span></code></pre></div>
</div>

</div>
## Companion functions
### [`enumerate`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#enumerate)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#enumerate"><span class="nf">enumerate</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType.Predicate<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>IElementType<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`find`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#find)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#find"><span class="nf">find</span></a><span class="p">(</span>idx<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/index.html">Short</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType
</span></code></pre></div>
</div>

</div>
### [`getAllocatedTypesCount`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#getallocatedtypescount)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#getallocatedtypescount"><span class="nf">getAllocatedTypesCount</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/index.html">Short</a>
</span></code></pre></div>
</div>

</div>
### [`isTombstone`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#istombstone)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#istombstone"><span class="nf">isTombstone</span></a><span class="p">(</span>type<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`mapNotNull`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#mapnotnull)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#mapnotnull">R</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#mapnotnull"><span class="nf">mapNotNull</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <span class="p">(</span><span class="kd">in </span>IElementType<span class="p">)</span><span class="o"> -> </span><span class="kd">out </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#mapnotnull">R</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/util/List.html">List</a><span class="o"><</span><span class="se">@</span><span class="se">NotNull</span> <a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#mapnotnull">R</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`push`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#push)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#push"><span class="nf">push</span></a><span class="p">(</span>types<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>IElementType<span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>IElementType<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`unregisterElementTypes`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#unregisterelementtypes)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#unregisterelementtypes"><span class="nf">unregisterElementTypes</span></a><span class="p">(</span>loader<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/ClassLoader.html">ClassLoader</a><span class="p">, </span>pluginDescriptor<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PluginDescriptor<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### tokenId

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../org.jetbrains.kotlin.kdoc.lexer/-k-doc-token/index.html#tokenid">tokenId</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
## Functions
### [`getDebugName`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#getdebugname)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#getdebugname"><span class="nf">getDebugName</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NonNls</span> <span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`getIndex`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#getindex)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#getindex"><span class="nf">getIndex</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/index.html">Short</a>
</span></code></pre></div>
</div>

</div>
### [`getLanguage`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#getlanguage)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#getlanguage"><span class="nf">getLanguage</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Language
</span></code></pre></div>
</div>

</div>
### getValue

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><span class="se">NotNull</span>
<span class="se">@</span><span class="se">NonNls</span>
<span class="kd">open </span><span class="kd">fun </span><a href="index.html#getvalue"><span class="nf">getValue</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`hashCode`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#hashcode)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#hashcode"><span class="nf">hashCode</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`isLeftBound`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#isleftbound)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#isleftbound"><span class="nf">isLeftBound</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`toString`](../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.md#tostring)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.kdoc.parser/-k-doc-element-type/index.html#tostring"><span class="nf">toString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
