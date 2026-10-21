---
tags:
 - jvm
title: "KaDiagnostics"
---

# KaDiagnostics

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaDiagnostics</a> : <a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a>, <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-ka-diagnostic-with-psi/index.html">KaDiagnosticWithPsi</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">> </span>
</span></code></pre></div>A description of a diagnostic query, which yields the requested [`diagnostics`](../-ka-diagnostic-with-psi/index.md) on iteration.

[`KaDiagnostics`](index.md) is obtained from [`diagnostics`](../diagnostics.md). By default, the query yields diagnostics of [`common checkers`](../-ka-diagnostic-checker-kind/-companion/index.md#common) which are not [`suppressed`](../-ka-diagnostic-with-psi/index.md#issuppressed) at their use site recursively – in other words, exactly the diagnostics which the compiler reports:

```kotlin
for (diagnostic in file.diagnostics()) {
    handle(diagnostic)
}
```

The default can be adjusted before the iteration begins:

```kotlin
file.diagnostics()
    .withCheckers(KaDiagnosticCheckerKind.COMMON, KaDiagnosticCheckerKind.EXTENDED)
    .ignoreSuppressed(true)
    .directOnly(true)
    .forEach { handle(it) }
```

#### Laziness
[`KaDiagnostics`](index.md) is a [`Sequence`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html):

 - Calling `diagnostics()` itself doesn't trigger code analysis. The operation is intermediate and stateless.


 - Diagnostics are computed on-demand as the sequence is iterated over.


 - You can iterate over the same sequence multiple times.


#### See also


 - [`diagnostics`](../diagnostics.md)



</div>

## Properties
### [`token`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#token)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#token">token</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaLifetimeToken`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md) which determines the lifetime of the lifetime owner.


</div>

</div>
## Functions
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### directOnly

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#directonly"><span class="nf">directOnly</span></a><span class="p">(</span>direct<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaDiagnostics</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaDiagnostics`](index.md) which yields diagnostics only on the given [`KtElement`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md) itself depending on [`direct`](index.md#directonly) flag.

If [`direct`](index.md#directonly) is `true`, [`KaDiagnosticWithPsi`](../-ka-diagnostic-with-psi/index.md) of the element's children are <strong>not</strong> included, so the result is not the complete set of diagnostics which concern the element: a diagnostic about the element might be reported on one of its children, or on a containing element. Prefer `false` unless the diagnostics of the exact element are required.

The default behavior is `false`.


</div>

</div>
### ignoreSuppressed

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#ignoresuppressed"><span class="nf">ignoreSuppressed</span></a><span class="p">(</span>ignore<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaDiagnostics</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaDiagnostics`](index.md) which yields [`suppressed`](../-ka-diagnostic-with-psi/index.md#issuppressed) diagnostics depending on the value of [`ignore`](index.md#ignoresuppressed).

Suppressed diagnostics are not reported by the compiler, so they should not be presented to the user as is. They are useful for tooling which analyzes suppressions themselves, such as an inspection which detects redundant `@Suppress` annotations.

Collecting suppressed diagnostics does not require additional analysis.

The default behavior is `true`.


</div>

</div>
### [`isValid`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#isvalid)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#isvalid"><span class="nf">isValid</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the lifetime owner is still valid, i.e. we are still in the scope of the lifetime owner's regular lifetime.


</div>

</div>
### [`iterator`](index.md#iterator)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">operator </span><span class="kd">fun </span><a href="index.html#iterator"><span class="nf">iterator</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/index.html">Iterator</a><span class="o"><</span><a href="../-ka-diagnostic-with-psi/index.html">KaDiagnosticWithPsi</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### withCheckers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#withcheckers"><span class="nf">withCheckers</span></a><span class="p">(</span>kinds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../-ka-diagnostic-checker-kind/index.html">KaDiagnosticCheckerKind</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="index.html">KaDiagnostics</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaDiagnostics`](index.md) which yields diagnostics of the given checker [`kinds`](index.md#withcheckers).

The [`kinds`](index.md#withcheckers) <strong>replace</strong> the currently requested kinds, they are not added to them. An empty [`kinds`](index.md#withcheckers) set results in no diagnostics, and no checkers are run in that case.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#withcheckers"><span class="nf">withCheckers</span></a><span class="p">(</span><span class="kd">vararg </span>kinds<span class="o">: </span><a href="../-ka-diagnostic-checker-kind/index.html">KaDiagnosticCheckerKind</a><span class="p">)</span><span class="o">: </span><a href="index.html">KaDiagnostics</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaDiagnostics`](index.md) which yields diagnostics of the given checker [`kinds`](index.md#withcheckers).

The [`kinds`](index.md#withcheckers) <strong>replace</strong> the currently requested kinds, they are not added to them. Passing no kinds results in no diagnostics, and no checkers are run in that case.


</div>

</div>
### [`withValidityAssertion`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion"><span class="nf">withValidityAssertion</span></a><span class="p">(</span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a>
</span></code></pre></div>
</div>


<div markdown>

Executes [`action`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion) only if the [`KaLifetimeOwner`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.md) is still [`valid`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md#isvalid) and [`accessible`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md#isaccessible). Otherwise, throws a validity exception based on the concrete violation.


</div>

</div>
