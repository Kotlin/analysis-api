---
tags:
 - jvm
title: "ModificationTrackerWithInvalidationReason"
---

# ModificationTrackerWithInvalidationReason

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">ModificationTrackerWithInvalidationReason</a> : ModificationTracker
</span></code></pre></div>A ModificationTracker that provides a reason for invalidation since its creation.


</div>

## Properties
### [`modificationCount`](index.md#modificationcount)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#modificationcount">modificationCount</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>
</span></code></pre></div>
</div>

</div>
## Functions
### getInvalidationReason

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getinvalidationreason"><span class="nf">getInvalidationReason</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a human-readable representation of the invalidation reason if the tracker has been invalidated since its creation.

**Return**

the invalidation reason if it has been invalidated, or `null` otherwise.


</div>

</div>
