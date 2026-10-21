---
tags:
 - jvm
title: "ClassHeaderBuilder"
---

# ClassHeaderBuilder

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">ClassHeaderBuilder</a>
</span></code></pre></div>A fluent builder for a class header string, assembled in a fixed order: modifiers, name, type parameters, base class, and type constraints. Call [`asString`](index.md#asstring) to obtain the resulting header text, then pass it to [`createClass`](../index.md#createclass) to build the PSI.

Calls are expected in that order. Order violations are checked only when JVM assertions are enabled.


</div>

## Constructors
### ClassHeaderBuilder

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Types
### [`State`](-state/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">enum class </span><a href="-state/index.html">State</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="o"><</span><a href="-state/index.html">KtPsiFactory.ClassHeaderBuilder.State</a><span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

The stages in the expected order for building a class header.


</div>

</div>
## Functions
### asString

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#asstring"><span class="nf">asString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Returns the assembled class header text.


</div>

</div>
### baseClass

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#baseclass"><span class="nf">baseClass</span></a><span class="p">(</span>
    <span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    typeArguments<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">></span><span class="p">, </span>
    isInterface<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
<span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.ClassHeaderBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends the base class or interface: its [`name`](index.md#baseclass) and [`typeArguments`](index.md#baseclass). When [`isInterface`](index.md#baseclass) is `false`, an empty constructor call `()` is appended.


</div>

</div>
### modifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#modifier"><span class="nf">modifier</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> modifier<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.ClassHeaderBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends [`modifier`](index.md#modifier) verbatim. No separator is added between repeated calls, so callers must include any required whitespace. This is expected to be called before [`name`](index.md#name).


</div>

</div>
### name

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#name"><span class="nf">name</span></a><span class="p">(</span><span class="se">@</span><span class="se">NonNls</span> name<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.ClassHeaderBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends the `class` keyword and the class [`name`](index.md#name). Ends the modifiers stage.


</div>

</div>
### transform

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#transform"><span class="nf">transform</span></a><span class="p">(</span>f<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/-string-builder/index.html">StringBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Applies an arbitrary transformation to the underlying text buffer.


</div>

</div>
### typeConstraints

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#typeconstraints"><span class="nf">typeConstraints</span></a><span class="p">(</span>values<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.ClassHeaderBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends the `where` clause type constraints, if any.


</div>

</div>
### typeParameters

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#typeparameters"><span class="nf">typeParameters</span></a><span class="p">(</span>values<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="index.html">KtPsiFactory.ClassHeaderBuilder</a>
</span></code></pre></div>
</div>


<div markdown>

Appends the type parameters, if any.


</div>

</div>
