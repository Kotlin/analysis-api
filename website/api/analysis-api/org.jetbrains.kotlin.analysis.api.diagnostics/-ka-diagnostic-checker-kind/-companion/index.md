---
tags:
 - jvm
title: "Companion"
---

# Companion

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">Companion</a>
</span></code></pre></div>
</div>

## Properties
### ALL

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#all">ALL</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../index.html">KaDiagnosticCheckerKind</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

All checker kinds supported by the current version of the Analysis API.

<strong>Caution:</strong> The set may grow in future versions, so by requesting [`ALL`](index.md#all), the client opts in to diagnostics and performance costs of checker kinds which do not exist yet. Prefer listing the required kinds explicitly.


</div>

</div>
### COMMON

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#common">COMMON</a><span class="o">: </span><a href="../index.html">KaDiagnosticCheckerKind</a>
</span></code></pre></div>
</div>


<div markdown>

The compiler's common checkers. Their diagnostics are exactly the ones reported during compilation.


</div>

</div>
### EXPERIMENTAL

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#experimental">EXPERIMENTAL</a><span class="o">: </span><a href="../index.html">KaDiagnosticCheckerKind</a>
</span></code></pre></div>
</div>


<div markdown>

Experimental checkers. Their role is the same as of [`EXTENDED`](index.md#extended) checkers, with the following differences:

 - They might have false positives.


 - They might be slow.



</div>

</div>
### EXTENDED

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#extended">EXTENDED</a><span class="o">: </span><a href="../index.html">KaDiagnosticCheckerKind</a>
</span></code></pre></div>
</div>


<div markdown>

Extended checkers, which typically run only in the IDE. They report additional diagnostics which are not a part of the compilation, such as reports about redundant code.


</div>

</div>
