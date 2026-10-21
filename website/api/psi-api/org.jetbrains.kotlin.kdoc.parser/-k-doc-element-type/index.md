---
tags:
 - jvm
title: "KDocElementType"
---

# KDocElementType

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="index.html">KDocElementType</a> : IElementType
</span></code></pre></div>
</div>

## Constructors
### KDocElementType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>debugName<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a><span class="p">, </span><span class="se">@</span><span class="se">NotNull</span> psiClass<span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><span class="kd">out </span>PsiElement<span class="o">></span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Companion properties
### [`ARRAY_FACTORY`](index.md#array_factory)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#array_factory">ARRAY_FACTORY</a><span class="o">: </span>ArrayFactory<span class="o"><</span>IElementType<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`EMPTY_ARRAY`](index.md#empty_array)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#empty_array">EMPTY_ARRAY</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>IElementType<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`FIRST_TOKEN_INDEX`](index.md#first_token_index)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#first_token_index">FIRST_TOKEN_INDEX</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/index.html">Short</a><span class="o"> = </span><span class="nb">1</span>
</span></code></pre></div>
</div>

</div>
### [`TRUE`](index.md#true)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#true">TRUE</a><span class="o">: </span>IElementType.Predicate
</span></code></pre></div>
</div>

</div>
## Companion functions
### [`enumerate`](index.md#enumerate)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#enumerate"><span class="nf">enumerate</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType.Predicate<span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>IElementType<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`find`](index.md#find)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#find"><span class="nf">find</span></a><span class="p">(</span>idx<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/index.html">Short</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType
</span></code></pre></div>
</div>

</div>
### [`getAllocatedTypesCount`](index.md#getallocatedtypescount)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getallocatedtypescount"><span class="nf">getAllocatedTypesCount</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/index.html">Short</a>
</span></code></pre></div>
</div>

</div>
### [`isTombstone`](index.md#istombstone)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#istombstone"><span class="nf">isTombstone</span></a><span class="p">(</span>type<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> IElementType<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`mapNotNull`](index.md#mapnotnull)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#mapnotnull">R</a><span class="o">> </span><a href="index.html#mapnotnull"><span class="nf">mapNotNull</span></a><span class="p">(</span>p<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <span class="p">(</span><span class="kd">in </span>IElementType<span class="p">)</span><span class="o"> -> </span><span class="kd">out </span><a href="index.html#mapnotnull">R</a><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/util/List.html">List</a><span class="o"><</span><span class="se">@</span><span class="se">NotNull</span> <a href="index.html#mapnotnull">R</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`push`](index.md#push)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#push"><span class="nf">push</span></a><span class="p">(</span>types<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>IElementType<span class="o">></span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="o"><</span>IElementType<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`unregisterElementTypes`](index.md#unregisterelementtypes)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#unregisterelementtypes"><span class="nf">unregisterElementTypes</span></a><span class="p">(</span>loader<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/ClassLoader.html">ClassLoader</a><span class="p">, </span>pluginDescriptor<span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> PluginDescriptor<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Functions
### createPsi

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#createpsi"><span class="nf">createPsi</span></a><span class="p">(</span>node<span class="o">: </span>ASTNode<span class="p">)</span><span class="o">: </span>PsiElement
</span></code></pre></div>
</div>

</div>
### [`getDebugName`](index.md#getdebugname)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getdebugname"><span class="nf">getDebugName</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NonNls</span> <span class="se">@</span><span class="se">NotNull</span> <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`getIndex`](index.md#getindex)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#getindex"><span class="nf">getIndex</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/index.html">Short</a>
</span></code></pre></div>
</div>

</div>
### [`getLanguage`](index.md#getlanguage)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#getlanguage"><span class="nf">getLanguage</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><span class="se">@</span><span class="se">NotNull</span> Language
</span></code></pre></div>
</div>

</div>
### [`hashCode`](index.md#hashcode)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#hashcode"><span class="nf">hashCode</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`isLeftBound`](index.md#isleftbound)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#isleftbound"><span class="nf">isLeftBound</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`toString`](index.md#tostring)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="index.html#tostring"><span class="nf">toString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
