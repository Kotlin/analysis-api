---
tags:
 - jvm
title: "staticDeclaredMemberScope"
---

# staticDeclaredMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="static-declared-member-scope.html">staticDeclaredMemberScope</a><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](-ka-scope/index.md) containing the static callables (functions and properties) and all classifiers (classes and objects) explicitly declared in the given [`KaDeclarationContainerSymbol`](../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md).

It is worth noting that, while Java classes may contain declarations of static callables freely, in Kotlin only enum classes define static callables. Hence, for non-enum Kotlin classes, it is not expected that the static declared member scope will contain any callables.

#### See also


 - [`declaredMemberScope`](declared-member-scope.md)



</div>

</div>
