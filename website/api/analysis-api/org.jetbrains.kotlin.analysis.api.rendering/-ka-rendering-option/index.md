---
tags:
 - jvm
title: "KaRenderingOption"
---

# KaRenderingOption

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KaRenderingOption</a><span class="o"><</span><a href="index.html">T</a><span class="o">></span>
</span></code></pre></div>A typed configuration flag that influences rendering. Its [`defaultValue`](index.md#defaultvalue) is used unless overridden via [`KaRendererBuilder.set`](../-ka-renderer-builder/index.md#set).

The available options are defined as properties of the companion object.


</div>

## Types
### [`ClassMemberComparator`](-class-member-comparator/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">typealias </span><a href="-class-member-comparator/index.html">ClassMemberComparator</a><span class="o"> = </span><span class="kd">context</span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span><a href="../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">) </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

Orders [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) members inside a class. Returns:


</div>

</div>
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Properties
### defaultValue

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#defaultvalue">defaultValue</a><span class="o">: </span><a href="index.html">T</a>
</span></code></pre></div>
</div>

</div>
