---
tags:
 - jvm
title: "KaRestrictedAnalysisException"
---

# KaRestrictedAnalysisException

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KaRestrictedAnalysisException</a><span class="p">(</span>cause<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="p">)</span> : <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html">Exception</a>
</span></code></pre></div>An exception which occurred during [`restricted analysis`](../-kotlin-restricted-analysis-service/index.md).

The Analysis API wraps exceptions which occur during restricted analysis in [`KaRestrictedAnalysisException`](index.md). Due to the incomplete, inconsistent, and potentially changing information available during restricted analysis mode, the Analysis API's resolution and caches might run into inconsistent states. This can trigger exceptions from Analysis API and Kotlin compiler internals. Similar to how Analysis API results might not be as expected during restricted analysis, there might be exceptions which usually couldn't occur with a consistent project state.

Distinguishing between regular exceptions and those that occurred during restricted analysis supports diagnostic efforts and even allows the platform to suppress such exceptions if needed.


</div>

## Constructors
### KaRestrictedAnalysisException

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>cause<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### [`cause`](index.md#cause)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="index.html#cause">cause</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html">Throwable</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### [`message`](index.md#message)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="index.html#message">message</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
