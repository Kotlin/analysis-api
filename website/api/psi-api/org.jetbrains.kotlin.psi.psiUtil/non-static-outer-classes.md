---
tags:
 - jvm
title: "nonStaticOuterClasses"
---

# nonStaticOuterClasses

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="non-static-outer-classes.html"><span class="nf">nonStaticOuterClasses</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../org.jetbrains.kotlin.psi/-kt-class/index.html">KtClass</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the enclosing classes that this element can access an outer instance of, from innermost to outermost.

### Example:
Given `targetFunction` representing `target` in:

```kotlin
class Outer {
    class Boundary {
        inner class Inner {
            fun target() {}
        }
    }
}
```

`targetFunction.nonStaticOuterClasses().mapNotNull { it.name }.toList()` returns `listOf("Inner", "Boundary")`. The sequence stops at `Boundary` because it is not an `inner` class, so its instances do not retain an `Outer` instance.


</div>

</div>
