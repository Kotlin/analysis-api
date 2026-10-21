---
tags:
 - jvm
title: "KaInternalsReferenceShortener"
---

# KaInternalsReferenceShortener

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaInternalsReferenceShortener</a>
</span></code></pre></div>
</div>

## Functions
### collectPossibleReferenceShortenings

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#collectpossiblereferenceshortenings"><span class="nf">collectPossibleReferenceShortenings</span></a><span class="p">(</span>
    file<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>
    selection<span class="o">: </span>TextRange<span class="p">, </span>
    shortenOptions<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-options/index.html">ShortenOptions</a><span class="p">, </span>
    classShortenStrategy<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-strategy/index.html">ShortenStrategy</a><span class="p">, </span>
    callableShortenStrategy<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-strategy/index.html">ShortenStrategy</a>
<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-command/index.html">ShortenCommand</a>
</span></code></pre></div>
</div>

</div>
### collectPossibleReferenceShorteningsInElement

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#collectpossiblereferenceshorteningsinelement"><span class="nf">collectPossibleReferenceShorteningsInElement</span></a><span class="p">(</span>
    element<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">, </span>
    shortenOptions<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-options/index.html">ShortenOptions</a><span class="p">, </span>
    classShortenStrategy<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-strategy/index.html">ShortenStrategy</a><span class="p">, </span>
    callableShortenStrategy<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-strategy/index.html">ShortenStrategy</a>
<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-shorten-command/index.html">ShortenCommand</a>
</span></code></pre></div>
</div>

</div>
