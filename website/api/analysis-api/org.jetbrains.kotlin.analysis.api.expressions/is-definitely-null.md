---
tags:
 - jvm
title: "isDefinitelyNull"
---

# isDefinitelyNull

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">.</span><a href="is-definitely-null.html">isDefinitelyNull</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether this expression is definitely null, based on the declared nullability and smart cast types derived from data-flow analysis facts.

Only nullability from stable smart casts is considered. See the [smart cast sink stability](https://kotlinlang.org/spec/type-inference.html#smart-cast-sink-stability) section of the Kotlin specification for more information.

#### Examples
```
public fun <T : Any> foo(t: T, nt: T?, s: String, ns: String?) {
  t     // t.isDefinitelyNull()  == false && t.isDefinitelyNotNull()  == true
  nt    // nt.isDefinitelyNull() == false && nt.isDefinitelyNotNull() == false
  s     // s.isDefinitelyNull()  == false && s.isDefinitelyNotNull()  == true
  ns    // ns.isDefinitelyNull() == false && ns.isDefinitelyNotNull() == false

  if (ns != null) {
    ns  // ns.isDefinitelyNull() == false && ns.isDefinitelyNotNull() == true
  } else {
    ns  // ns.isDefinitelyNull() == true  && ns.isDefinitelyNotNull() == false
  }

  ns!!  // From this point on: ns.isDefinitelyNull() == false && ns.isDefinitelyNotNull() == true
}
```


</div>

</div>
