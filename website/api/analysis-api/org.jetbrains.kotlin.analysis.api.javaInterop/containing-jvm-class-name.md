---
tags:
 - jvm
title: "containingJvmClassName"
---

# containingJvmClassName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="containing-jvm-class-name.html">containingJvmClassName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The containing JVM class name for the given [`KaCallableSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md).

The property works for both source and library declarations. The JVM class name is a fully qualified name separated by dots, such as `foo.bar.Baz.Companion`.

Applicable only to JVM modules, and common modules with JVM targets. [`containingJvmClassName`](containing-jvm-class-name.md) is always `null` all other kinds of modules.


</div>

</div>
