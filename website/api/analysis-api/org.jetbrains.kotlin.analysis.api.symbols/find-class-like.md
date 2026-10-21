---
tags:
 - jvm
title: "findClassLike"
---

# findClassLike

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="find-class-like.html"><span class="nf">findClassLike</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaClassLikeSymbol`](-ka-class-like-symbol/index.md) for the specified ClassId, or `null` if such a symbol cannot be found.

The function combines both class search (see [`findClass`](find-class.md)) and type alias search (see [`findTypeAlias`](find-type-alias.md)).


</div>

</div>
