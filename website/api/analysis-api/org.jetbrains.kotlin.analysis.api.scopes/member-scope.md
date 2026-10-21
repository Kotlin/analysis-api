---
tags:
 - jvm
title: "memberScope"
---

# memberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="member-scope.html">memberScope</a><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](-ka-scope/index.md) containing non-static callable members (functions, properties, and constructors) and all classifier members (classes and objects) of the given [`KaDeclarationContainerSymbol`](../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md). The scope includes members inherited from the symbol's supertypes, in addition to members which are declared explicitly inside the symbol's body.

The member scope doesn't include [synthetic Java properties](https://kotlinlang.org/docs/java-interop.html#getters-and-setters). For a scope which contains synthetic properties, please refer to [`syntheticJavaPropertiesScope`](synthetic-java-properties-scope.md).

#### See also


 - [`staticMemberScope`](static-member-scope.md)



</div>

</div>
