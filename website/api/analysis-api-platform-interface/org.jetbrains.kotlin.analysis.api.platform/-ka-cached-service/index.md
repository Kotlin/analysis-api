---
tags:
 - jvm
title: "KaCachedService"
---

# KaCachedService

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-i-e-l-d/index.html">AnnotationTarget.FIELD</a><span class="p">]</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="index.html">KaCachedService</a>
</span></code></pre></div>A property annotated with [`KaCachedService`](index.md) stores a cached IntelliJ project or application service, or an object with a reference to such a service.

Retrieving services via Project.getService and Application.getService can have an impact on performance when called frequently. While caching a service is generally not recommended, it can be beneficial for performance in hot spots, if done right.

The recommendation to avoid caching services is due to the risk of leaks. Properties annotated with [`KaCachedService`](index.md) should make sure that they don't leak the service: the lifetime of the property should be shorter or as long as the lifetime of the cached service.

When caching a service inside another service, the property should also be [`lazy`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/index.html) to avoid issues with cyclic service initialization and excessive class loading on startup.

The [`KaCachedService`](index.md) annotation itself is currently not enforced by any checkers or inspections, but it serves as an anchor for documentation and improves discoverability of cached services.


</div>

