---
tags:
 - jvm
title: "KotlinAnalysisInWriteActionListener"
---

# KotlinAnalysisInWriteActionListener

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinAnalysisInWriteActionListener</a>
</span></code></pre></div>A listener for events which happen during an [`analyze`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.session/index.md) call in a write action.

Normally, analysis during write actions is not allowed. Nonetheless, it is possible, and such analysis poses some unique challenges to cache integrity, as analysis usually operates on an immutable context (read action) and not during or between modifications. The purpose of this listener is to allow components to react when a clean slate is required upon entering or leaving analysis.

#### See also


 - [`allowAnalysisFromWriteAction`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.permissions/index.md)



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
### afterLeavingAnalysisInWriteAction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#afterleavinganalysisinwriteaction"><span class="nf">afterLeavingAnalysisInWriteAction</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

This event is published after leaving analysis during a write action. It is published after the action of [`analyze`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.session/index.md) has been executed.

**See also**



 - [`KotlinAnalysisInWriteActionListener`](index.md)



</div>

</div>
### onEnteringAnalysisInWriteAction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#onenteringanalysisinwriteaction"><span class="nf">onEnteringAnalysisInWriteAction</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

This event is published when analysis is entered during a write action. It is published before the action of [`analyze`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.session/index.md) is executed.

**See also**



 - [`KotlinAnalysisInWriteActionListener`](index.md)



</div>

</div>
