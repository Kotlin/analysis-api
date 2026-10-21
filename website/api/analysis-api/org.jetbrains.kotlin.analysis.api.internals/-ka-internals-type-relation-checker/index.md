---
tags:
 - jvm
title: "KaInternalsTypeRelationChecker"
---

# KaInternalsTypeRelationChecker

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaInternalsTypeRelationChecker</a>
</span></code></pre></div>
</div>

## Functions
### isSubtypeOf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>
    type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    supertype<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    errorTypePolicy<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a>
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>
    type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    classId<span class="o">: </span>ClassId<span class="p">, </span>
    errorTypePolicy<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a>
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#issubtypeof"><span class="nf">isSubtypeOf</span></a><span class="p">(</span>
    type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">, </span>
    errorTypePolicy<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a>
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### semanticallyEquals

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#semanticallyequals"><span class="nf">semanticallyEquals</span></a><span class="p">(</span>
    type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    other<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    errorTypePolicy<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-subtyping-error-type-policy/index.html">KaSubtypingErrorTypePolicy</a>
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
