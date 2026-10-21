---
tags:
 - jvm
title: "ClassMemberComparator"
---

# ClassMemberComparator

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">typealias </span><a href="index.html">ClassMemberComparator</a><span class="o"> = </span><span class="kd">context</span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span><a href="../../-ka-rendering-context/index.html">KaRenderingContext</a><span class="p">) </span><span class="p">(</span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">, </span><a href="../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>Orders [`KaSymbol`](../../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) members inside a class. Returns:

 - `-1` if the first symbol should be rendered before the second one;


 - `1` if the first symbol should be rendered after the next one;


 - `0` if member order should be kept intact.



</div>

