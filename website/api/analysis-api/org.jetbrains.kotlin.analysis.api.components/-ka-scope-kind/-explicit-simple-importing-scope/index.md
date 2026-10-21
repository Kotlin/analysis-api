---
tags:
 - jvm
title: "ExplicitSimpleImportingScope"
---

# ExplicitSimpleImportingScope

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">ExplicitSimpleImportingScope</a> : <a href="../-importing-scope/index.html">KaScopeKind.ImportingScope</a>
</span></code></pre></div>Represents a [`KaScope`](../../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing declarations from explicit non-star imports.

#### Inheritors


 - [`ExplicitSimpleImportingScope`](../../-ka-scope-kinds/-explicit-simple-importing-scope/index.md)



</div>

## Properties
### indexInTower

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-script-member-scope/index.html#indexintower">indexInTower</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
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
