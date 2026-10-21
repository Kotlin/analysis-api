---
tags:
 - jvm
title: "createCompilationOptions"
---

# createCompilationOptions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="create-compilation-options.html"><span class="nf">createCompilationOptions</span></a><span class="p">(</span>init<span class="o">: </span><a href="-ka-compilation-options-builder/index.html">KaCompilationOptionsBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="-ka-compilation-options/index.html">KaCompilationOptions</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a new [`KaCompilationOptions`](-ka-compilation-options/index.md) instance using the given DSL [`init`](create-compilation-options.md) block.

Example usage:

```kotlin
val options = createCompilationOptions {
    target(KaCompilationTarget.JVM)
    moduleName("myModule")
    languageVersionSettings(languageSettings)
    allowedErrorFilter { diagnostic -> diagnostic.factoryName in allowedErrors }
}
```

#### Parameters


 - init: A lambda that configures the [`KaCompilationOptionsBuilder`](-ka-compilation-options-builder/index.md).





</div>

</div>
