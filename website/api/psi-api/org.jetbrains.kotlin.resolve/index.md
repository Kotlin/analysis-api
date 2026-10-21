---
tags:
 - jvm
title: "org.jetbrains.kotlin.resolve"
---

# org.jetbrains.kotlin.resolve
## Types
### [`StatementFilter`](-statement-filter/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">class </span><a href="-statement-filter/index.html">StatementFilter</a>
</span></code></pre></div>
</div>


<div markdown>

Selects which statements of a block should be taken into account (for example, during analysis). The base implementation applies no filtering; subclasses may restrict the considered statements by overriding [`filter`](-statement-filter/index.md#filter).


</div>

</div>
## Functions
