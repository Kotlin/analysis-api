---
tags:
 - jvm
title: "collectPossibleReferenceShortenings"
---

# collectPossibleReferenceShortenings

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="collect-possible-reference-shortenings.html"><span class="nf">collectPossibleReferenceShortenings</span></a><span class="p">(</span>
    file<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>
    selection<span class="o">: </span>TextRange<span class="o"> = </span>file.textRange<span class="p">, </span>
    shortenOptions<span class="o">: </span><a href="-shorten-options/index.html">ShortenOptions</a><span class="o"> = </span>ShortenOptions.DEFAULT<span class="p">, </span>
    classShortenStrategy<span class="o">: </span><span class="p">(</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="-shorten-strategy/index.html">ShortenStrategy</a><span class="o"> = </span>defaultClassShortenStrategy<span class="p">, </span>
    callableShortenStrategy<span class="o">: </span><span class="p">(</span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">)</span><span class="o"> -> </span><a href="-shorten-strategy/index.html">ShortenStrategy</a><span class="o"> = </span>defaultCallableShortenStrategy
<span class="p">)</span><span class="o">: </span><a href="-shorten-command/index.html">ShortenCommand</a>
</span></code></pre></div>
</div>


<div markdown>

Collects possible references to shorten.

See [`defaultClassShortenStrategy`](-shorten-strategy/-companion/index.md#defaultclassshortenstrategy) and [`defaultCallableShortenStrategy`](-shorten-strategy/-companion/index.md#defaultcallableshortenstrategy) for the default shortening logic.

Also see `org.jetbrains.kotlin.idea.base.analysis.api.utils.shortenReferences` and functions around it.


</div>

</div>
