---
tags:
 - jvm
title: "KaCodeFragmentCapturedValue"
---

# KaCodeFragmentCapturedValue

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="index.html">KaCodeFragmentCapturedValue</a>
</span></code></pre></div>#### Inheritors


 - [`Local`](-local/index.md)
 - [`LocalDelegate`](-local-delegate/index.md)
 - [`BackingField`](-backing-field/index.md)
 - [`ContainingClass`](-containing-class/index.md)
 - [`SuperClass`](-super-class/index.md)
 - [`ExtensionReceiver`](-extension-receiver/index.md)
 - [`ContextReceiver`](-context-receiver/index.md)
 - [`ForeignValue`](-foreign-value/index.md)
 - [`CoroutineContext`](-coroutine-context/index.md)



</div>

## Types
### [`BackingField`](-backing-field/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-backing-field/index.html">BackingField</a><span class="p">(</span>
    name<span class="o">: </span>Name<span class="p">, </span>
    isMutated<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    isCrossingInlineBounds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    depthRelativeToCurrentFrame<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
<span class="p">)</span> : <a href="index.html">KaCodeFragmentCapturedValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a backing field (a `field` variable inside a property accessor).


</div>

</div>
### [`ContainingClass`](-containing-class/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-containing-class/index.html">ContainingClass</a><span class="p">(</span>
    classId<span class="o">: </span>ClassId<span class="p">, </span>
    isCrossingInlineBounds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    depthRelativeToCurrentFrame<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
<span class="p">)</span> : <a href="index.html">KaCodeFragmentCapturedValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a captured outer class.


</div>

</div>
### [`ContextReceiver`](-context-receiver/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-context-receiver/index.html">ContextReceiver</a><span class="p">(</span>
    <span class="kd">val </span>index<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">, </span>
    labelName<span class="o">: </span>Name<span class="p">, </span>
    isCrossingInlineBounds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    depthRelativeToCurrentFrame<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
<span class="p">)</span> : <a href="index.html">KaCodeFragmentCapturedValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a context receiver.


</div>

</div>
### [`CoroutineContext`](-coroutine-context/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-coroutine-context/index.html">CoroutineContext</a><span class="p">(</span>isCrossingInlineBounds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>depthRelativeToCurrentFrame<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="p">)</span> : <a href="index.html">KaCodeFragmentCapturedValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a `coroutineContext` call.


</div>

</div>
### [`ExtensionReceiver`](-extension-receiver/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-extension-receiver/index.html">ExtensionReceiver</a><span class="p">(</span>
    labelName<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">, </span>
    isCrossingInlineBounds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    depthRelativeToCurrentFrame<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
<span class="p">)</span> : <a href="index.html">KaCodeFragmentCapturedValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an extension receiver.


</div>

</div>
### [`ForeignValue`](-foreign-value/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-foreign-value/index.html">ForeignValue</a><span class="p">(</span>
    name<span class="o">: </span>Name<span class="p">, </span>
    isCrossingInlineBounds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    depthRelativeToCurrentFrame<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
<span class="p">)</span> : <a href="index.html">KaCodeFragmentCapturedValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents an externally provided value.


</div>

</div>
### [`Local`](-local/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-local/index.html">Local</a><span class="p">(</span>
    name<span class="o">: </span>Name<span class="p">, </span>
    isMutated<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    isCrossingInlineBounds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    depthRelativeToCurrentFrame<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
<span class="p">)</span> : <a href="index.html">KaCodeFragmentCapturedValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a local variable or a parameter.


</div>

</div>
### [`LocalDelegate`](-local-delegate/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-local-delegate/index.html">LocalDelegate</a><span class="p">(</span>
    name<span class="o">: </span>Name<span class="p">, </span>
    isMutated<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    isCrossingInlineBounds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    depthRelativeToCurrentFrame<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
<span class="p">)</span> : <a href="index.html">KaCodeFragmentCapturedValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a delegated local variable (`val local by...`).


</div>

</div>
### [`SuperClass`](-super-class/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-super-class/index.html">SuperClass</a><span class="p">(</span>
    classId<span class="o">: </span>ClassId<span class="p">, </span>
    isCrossingInlineBounds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    depthRelativeToCurrentFrame<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
<span class="p">)</span> : <a href="index.html">KaCodeFragmentCapturedValue</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a captured super class (`super.foo()`).


</div>

</div>
## Properties
### depthRelativeToCurrentFrame

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="-coroutine-context/index.html#depthrelativetocurrentframe">depthRelativeToCurrentFrame</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
### displayText

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="-coroutine-context/index.html#displaytext">displayText</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### isCrossingInlineBounds

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="-coroutine-context/index.html#iscrossinginlinebounds">isCrossingInlineBounds</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### isMutated

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="-coroutine-context/index.html#ismutated">isMutated</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### name

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="-coroutine-context/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
## Functions
### toString

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="-coroutine-context/index.html#tostring"><span class="nf">toString</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
