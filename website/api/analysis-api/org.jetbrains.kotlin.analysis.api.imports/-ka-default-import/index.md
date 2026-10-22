---
tags:
 - jvm
title: "KaDefaultImport"
---

# KaDefaultImport

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaDefaultImport</a>
</span></code></pre></div>Represents a default import that the Kotlin compiler adds to each file during resolution.

See [Kotlin Language Specification](https://kotlinlang.org/spec/packages-and-imports.html).

#### See also


 - [`KaDefaultImportsProvider`](../-ka-default-imports-provider/index.md)



</div>

## Properties
### importPath

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#importpath">importPath</a><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.resolve/-import-path/index.html">ImportPath</a>
</span></code></pre></div>
</div>


<div markdown>

The path that is imported by default.

It may be a star import if [`ImportPath.isAllUnder`](../../../psi-api/org.jetbrains.kotlin.resolve/-import-path/is-all-under.md) is `true`, or a non-star import if `false`.


</div>

</div>
### priority

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#priority">priority</a><span class="o">: </span><a href="../-ka-default-import-priority/index.html">KaDefaultImportPriority</a>
</span></code></pre></div>
</div>


<div markdown>

Represents the priority of the current default import.

**See also**



 - [`KaDefaultImportPriority`](../-ka-default-import-priority/index.md)



</div>

</div>
