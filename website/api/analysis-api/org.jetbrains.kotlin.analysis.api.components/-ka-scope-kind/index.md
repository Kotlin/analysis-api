---
tags:
 - jvm
title: "KaScopeKind"
---

# KaScopeKind

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">KaScopeKind</a>
</span></code></pre></div>#### Inheritors


 - [`LocalScope`](-local-scope/index.md)
 - [`TypeScope`](-type-scope/index.md)
 - [`NonLocalScope`](-non-local-scope/index.md)



</div>

## Types
### [`DefaultSimpleImportingScope`](-default-simple-importing-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-default-simple-importing-scope/index.html">DefaultSimpleImportingScope</a> : <a href="-importing-scope/index.html">KaScopeKind.ImportingScope</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing declarations from non-star imports which are not declared explicitly and are added by default.


</div>

</div>
### [`DefaultStarImportingScope`](-default-star-importing-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-default-star-importing-scope/index.html">DefaultStarImportingScope</a> : <a href="-importing-scope/index.html">KaScopeKind.ImportingScope</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing declarations from star imports which are not declared explicitly and are added by default.


</div>

</div>
### [`ExplicitSimpleImportingScope`](-explicit-simple-importing-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-explicit-simple-importing-scope/index.html">ExplicitSimpleImportingScope</a> : <a href="-importing-scope/index.html">KaScopeKind.ImportingScope</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing declarations from explicit non-star imports.


</div>

</div>
### [`ExplicitStarImportingScope`](-explicit-star-importing-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-explicit-star-importing-scope/index.html">ExplicitStarImportingScope</a> : <a href="-importing-scope/index.html">KaScopeKind.ImportingScope</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing declarations from explicit star imports.


</div>

</div>
### [`ImportingScope`](-importing-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-importing-scope/index.html">ImportingScope</a> : <a href="-non-local-scope/index.html">KaScopeKind.NonLocalScope</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing declarations from imports.


</div>

</div>
### [`LocalScope`](-local-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-local-scope/index.html">LocalScope</a> : <a href="index.html">KaScopeKind</a>
</span></code></pre></div>
</div>

</div>
### [`NonLocalScope`](-non-local-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-non-local-scope/index.html">NonLocalScope</a> : <a href="index.html">KaScopeKind</a>
</span></code></pre></div>
</div>

</div>
### [`PackageMemberScope`](-package-member-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-package-member-scope/index.html">PackageMemberScope</a> : <a href="-non-local-scope/index.html">KaScopeKind.NonLocalScope</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing declarations from a package.


</div>

</div>
### [`ScriptMemberScope`](-script-member-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-script-member-scope/index.html">ScriptMemberScope</a> : <a href="-non-local-scope/index.html">KaScopeKind.NonLocalScope</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing the members of a script.


</div>

</div>
### [`StaticMemberScope`](-static-member-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-static-member-scope/index.html">StaticMemberScope</a> : <a href="-non-local-scope/index.html">KaScopeKind.NonLocalScope</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing the static members of a classifier.


</div>

</div>
### [`TypeParameterScope`](-type-parameter-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-type-parameter-scope/index.html">TypeParameterScope</a> : <a href="-non-local-scope/index.html">KaScopeKind.NonLocalScope</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing type parameters.


</div>

</div>
### [`TypeScope`](-type-scope/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-type-scope/index.html">TypeScope</a> : <a href="index.html">KaScopeKind</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) for a type, which includes [synthetic Java properties](https://kotlinlang.org/docs/java-interop.html#getters-and-setters) of that type.


</div>

</div>
## Properties
### indexInTower

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="-script-member-scope/index.html#indexintower">indexInTower</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>


<div markdown>

An index in the scope tower. The lower the index, the closer the scope is to the context position.

**Example**

```kotlin
fun f(a: A, b: B) {      // local scope:       indexInTower = 2
    with(a) {            // type scope for A:  indexInTower = 1
        with(b) {        // type scope for B:  indexInTower = 0
            <caret>
        }
    }
}
```


</div>

</div>
