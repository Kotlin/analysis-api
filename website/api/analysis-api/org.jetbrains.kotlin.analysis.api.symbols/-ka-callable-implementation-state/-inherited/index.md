---
tags:
 - jvm
title: "Inherited"
---

# Inherited

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">Inherited</a> : <a href="../index.html">KaCallableImplementationState</a>
</span></code></pre></div>The declaration has the implementation provided by a supertype or multiple supertypes, and <strong>does not</strong> have explicit implementation in the target class.


</div>

## Properties
### isAmbiguous

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#isambiguous">isAmbiguous</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether multiple supertypes provide implementations. As the compiler cannot decide which implementation to choose, the declaration must be overridden explicitly. E.g.:

```kotlin
interface ColoredEntity {
    val color: String
}

interface GreenEntity : ColoredEntity {
    override val color get() = "green"
}

interface BlueEntity : ColoredEntity {
    override val color get() = "blue"
}

// Interface 'SeaColorEntity' must override 'color' because it inherits multiple interface methods for it
interface SeaColorEntity : GreenEntity, BlueEntity
```


</div>

</div>
### isOverridable

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#isoverridable">isOverridable</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the declaration can be overridden in the target class (e.g., it is not marked as `final` in a supertype).


</div>

</div>
