---
tags:
 - jvm
title: "PACKAGE_PROTECTED"
---

# PACKAGE_PROTECTED

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="index.html">PACKAGE_PROTECTED</a>

</span></code></pre></div>A package-protected Java declaration is visible in its class, package, and in all subclasses (even outside the package).

Unlike Kotlin, `protected` visibility in Java allows usages not only from inherited classes, but also from other classes in the same package. Effectively, it is a union of [`PROTECTED`](../-p-r-o-t-e-c-t-e-d/index.md) and [`PACKAGE_PRIVATE`](../-p-a-c-k-a-g-e_-p-r-i-v-a-t-e/index.md).

```java
public class JavaClass { // public
    protected void packageProtectedMember() { // package-protected
    }

    protected static void packageProtectedStaticMember() { // package-protected
    }
}
```


</div>

## Properties
### [`name`](../../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`ordinal`](../../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.md#ordinal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../../org.jetbrains.kotlin.analysis.api.types/-ka-unification-substitutor-policy/-a-s-s-i-g-n_-a-l-l/index.html#ordinal">ordinal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
