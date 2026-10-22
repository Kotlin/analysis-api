---
tags:
 - jvm
title: "IfNotParsed"
---

# IfNotParsed

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/annotation/Retention.html"><span class="se">Retention</span></a><span class="p">(</span>value<span class="o"> = </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/annotation/RetentionPolicy.html">RetentionPolicy.RUNTIME</a><span class="p">)</span>
<span class="se">@</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/annotation/Target.html"><span class="se">Target</span></a><span class="p">(</span>value<span class="o"> = </span><span class="p">[</span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/annotation/ElementType.html">ElementType.METHOD</a><span class="p">]</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="index.html">IfNotParsed</a>
</span></code></pre></div>Comes along with @Nullable to indicate null is only possible if parsing error present


</div>

## Functions
### [`annotationType`](index.md#annotationtype)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#annotationtype"><span class="nf">annotationType</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html">Class</a><span class="o"><</span><span class="kd">out </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/annotation/Annotation.html">Annotation</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### [`equals`](index.md#equals)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#equals"><span class="nf">equals</span></a><span class="p">(</span>p<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### [`hashCode`](index.md#hashcode)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#hashcode"><span class="nf">hashCode</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### [`toString`](index.md#tostring)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#tostring"><span class="nf">toString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://docs.oracle.com/javase/8/docs/api/java/lang/String.html">String</a>
</span></code></pre></div>
</div>

</div>
