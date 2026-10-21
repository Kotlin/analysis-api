---
tags:
 - jvm
title: "TypeParameterScope"
---

# TypeParameterScope

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">TypeParameterScope</a><span class="p">(</span><span class="kd">val </span>indexInTower<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span> : <a href="../../-ka-scope-kind/-type-parameter-scope/index.html">KaScopeKind.TypeParameterScope</a>
</span></code></pre></div>
</div>

## Constructors
### TypeParameterScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>indexInTower<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### indexInTower

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#indexintower">indexInTower</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
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
