---
tags:
 - jvm
title: "isFromCompanionBlock"
---

# isFromCompanionBlock

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="is-from-companion-block.html">isFromCompanionBlock</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether this declaration is declared inside a companion object block.

### Example:
```kotlin
class Foo {
  companion {
    fun static1() {} // true
  }

  fun regular() {} // false
}
```


</div>

</div>
