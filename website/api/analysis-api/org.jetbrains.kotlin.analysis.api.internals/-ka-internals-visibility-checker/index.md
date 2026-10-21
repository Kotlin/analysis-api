---
tags:
 - jvm
title: "KaInternalsVisibilityChecker"
---

# KaInternalsVisibilityChecker

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaInternalsVisibilityChecker</a>
</span></code></pre></div>
</div>

## Functions
### createUseSiteVisibilityChecker

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createusesitevisibilitychecker"><span class="nf">createUseSiteVisibilityChecker</span></a><span class="p">(</span>
    useSiteFile<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="p">, </span>
    receiverExpression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span><span class="p">, </span>
    position<span class="o">: </span>PsiElement
<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html">KaUseSiteVisibilityChecker</a>
</span></code></pre></div>
</div>

</div>
### isPublicApi

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#ispublicapi"><span class="nf">isPublicApi</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### isVisibleInClass

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#isvisibleinclass"><span class="nf">isVisibleInClass</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">, </span>classSymbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
