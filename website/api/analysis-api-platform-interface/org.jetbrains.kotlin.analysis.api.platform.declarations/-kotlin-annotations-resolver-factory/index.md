---
tags:
 - jvm
title: "KotlinAnnotationsResolverFactory"
---

# KotlinAnnotationsResolverFactory

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinAnnotationsResolverFactory</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Functions
### createAnnotationResolver

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createannotationresolver"><span class="nf">createAnnotationResolver</span></a><span class="p">(</span>searchScope<span class="o">: </span>GlobalSearchScope<span class="p">)</span><span class="o">: </span><a href="../-kotlin-annotations-resolver/index.html">KotlinAnnotationsResolver</a>
</span></code></pre></div>
</div>


<div markdown>

**Parameters**



 - searchScope: A scope in which the created [`KotlinAnnotationsResolver`](../-kotlin-annotations-resolver/index.md) will operate. Make sure that this scope contains all the annotations that you might want to resolve.





</div>

</div>
