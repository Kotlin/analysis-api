---
tags:
 - jvm
title: "ExpectTypeCase"
---

# ExpectTypeCase

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="index.html">ExpectTypeCase</a> : <a href="../index.html">KaWhenMissingCase</a>
</span></code></pre></div>Represents a missing check for an `expect` declaration. Because `actual` types may define more cases (e.g., additional enum values), exhaustiveness checks are explicitly disabled for those. Also see KT-20306.

#### Inheritors


 - [`ExpectSealedClassCase`](-expect-sealed-class-case/index.md)
 - [`ExpectSealedInterfaceCase`](-expect-sealed-interface-case/index.md)
 - [`ExpectEnumCase`](-expect-enum-case/index.md)



</div>

## Types
### [`ExpectEnumCase`](-expect-enum-case/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-expect-enum-case/index.html">ExpectEnumCase</a> : <a href="index.html">KaWhenMissingCase.ExpectTypeCase</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a missing check for an `expect enum class`.


</div>

</div>
### [`ExpectSealedClassCase`](-expect-sealed-class-case/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-expect-sealed-class-case/index.html">ExpectSealedClassCase</a> : <a href="index.html">KaWhenMissingCase.ExpectTypeCase</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a missing check for an `expect sealed class`.


</div>

</div>
### [`ExpectSealedInterfaceCase`](-expect-sealed-interface-case/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-expect-sealed-interface-case/index.html">ExpectSealedInterfaceCase</a> : <a href="index.html">KaWhenMissingCase.ExpectTypeCase</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a missing check for an `expect sealed interface`.


</div>

</div>
