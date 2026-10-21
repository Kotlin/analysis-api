---
tags:
 - jvm
title: "NonLocalScope"
---

# NonLocalScope

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">NonLocalScope</a> : <a href="../index.html">KaScopeKind</a>
</span></code></pre></div>#### Inheritors


 - [`TypeParameterScope`](../-type-parameter-scope/index.md)
 - [`PackageMemberScope`](../-package-member-scope/index.md)
 - [`ImportingScope`](../-importing-scope/index.md)
 - [`StaticMemberScope`](../-static-member-scope/index.md)
 - [`ScriptMemberScope`](../-script-member-scope/index.md)



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
