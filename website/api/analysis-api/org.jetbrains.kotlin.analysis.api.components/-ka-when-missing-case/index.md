---
tags:
 - jvm
title: "KaWhenMissingCase"
---

# KaWhenMissingCase

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="index.html">KaWhenMissingCase</a>
</span></code></pre></div>Represents a missing case in a `when` expression.

#### See also


 - [`KaExpressionInformationProvider.computeMissingCases`](../-ka-expression-information-provider/index.md#computemissingcases)


#### Inheritors


 - [`ExpectTypeCase`](-expect-type-case/index.md)
 - [`NullCase`](-null-case/index.md)
 - [`BooleanCase`](-boolean-case/index.md)
 - [`TypeCase`](-type-case/index.md)
 - [`EnumEntryCase`](-enum-entry-case/index.md)
 - [`UnknownCase`](-unknown-case/index.md)



</div>

## Types
### [`BooleanCase`](-boolean-case/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-boolean-case/index.html">BooleanCase</a><span class="p">(</span><span class="kd">val </span>value<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span> : <a href="index.html">KaWhenMissingCase</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a missing boolean check.


</div>

</div>
### [`EnumEntryCase`](-enum-entry-case/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-enum-entry-case/index.html">EnumEntryCase</a><span class="p">(</span><span class="kd">val </span>callableId<span class="o">: </span>CallableId<span class="p">)</span> : <a href="index.html">KaWhenMissingCase</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a missing enum entry check.


</div>

</div>
### [`ExpectTypeCase`](-expect-type-case/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-expect-type-case/index.html">ExpectTypeCase</a> : <a href="index.html">KaWhenMissingCase</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a missing check for an `expect` declaration. Because `actual` types may define more cases (e.g., additional enum values), exhaustiveness checks are explicitly disabled for those. Also see KT-20306.


</div>

</div>
### [`NullCase`](-null-case/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-null-case/index.html">NullCase</a> : <a href="index.html">KaWhenMissingCase</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a missing `null` check.


</div>

</div>
### [`TypeCase`](-type-case/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-type-case/index.html">TypeCase</a><span class="p">(</span>
    <span class="kd">val </span>classId<span class="o">: </span>ClassId<span class="p">, </span>
    <span class="kd">val </span>isObject<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">val </span>ownTypeParameterCount<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
<span class="p">)</span> : <a href="index.html">KaWhenMissingCase</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a missing type check.


</div>

</div>
### [`UnknownCase`](-unknown-case/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-unknown-case/index.html">UnknownCase</a> : <a href="index.html">KaWhenMissingCase</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a missing case other than those mentioned above.


</div>

</div>
