---
tags:
 - jvm
title: "withStatsCounter"
---

# withStatsCounter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><span class="o"><</span><a href="with-stats-counter.html">K</a><span class="p">, </span><a href="with-stats-counter.html">V</a><span class="o">> </span>Caffeine<span class="o"><</span><a href="with-stats-counter.html">K</a><span class="p">, </span><a href="with-stats-counter.html">V</a><span class="o">></span><span class="p">.</span><a href="with-stats-counter.html"><span class="nf">withStatsCounter</span></a><span class="p">(</span>statsCounter<span class="o">: </span>StatsCounter<span class="o">?</span><span class="p">)</span><span class="o">: </span>Caffeine<span class="o"><</span><a href="with-stats-counter.html">K</a><span class="p">, </span><a href="with-stats-counter.html">V</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Applies the StatsCounter to the Caffeine cache builder if it's non-null, or otherwise doesn't register it.

[`withStatsCounter`](with-stats-counter.md) exists because Caffeine.recordStats itself doesn't handle `null` stats counters.

Beware: Some operations of Cache.asMap do not record stats, so it's recommended to use the Caffeine cache directly.


</div>

</div>
