---
tags:
 - jvm
title: "KaRecommendedRendererCodeStyle"
---

# KaRecommendedRendererCodeStyle

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">KaRecommendedRendererCodeStyle</a> : <a href="../-ka-renderer-code-style/index.html">KaRendererCodeStyle</a>
</span></code></pre></div>
</div>

## Functions
### getIndentSize

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getindentsize"><span class="nf">getIndentSize</span></a><span class="p">(</span>analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### getSeparatorAfterContextReceivers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getseparatoraftercontextreceivers"><span class="nf">getSeparatorAfterContextReceivers</span></a><span class="p">(</span>analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### getSeparatorBetweenAnnotationAndOwner

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getseparatorbetweenannotationandowner"><span class="nf">getSeparatorBetweenAnnotationAndOwner</span></a><span class="p">(</span>analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### getSeparatorBetweenAnnotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getseparatorbetweenannotations"><span class="nf">getSeparatorBetweenAnnotations</span></a><span class="p">(</span>analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotated/index.html">KaAnnotated</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### getSeparatorBetweenMembers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getseparatorbetweenmembers"><span class="nf">getSeparatorBetweenMembers</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    first<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">, </span>
    second<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a>
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### getSeparatorBetweenModifiers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getseparatorbetweenmodifiers"><span class="nf">getSeparatorBetweenModifiers</span></a><span class="p">(</span>analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
