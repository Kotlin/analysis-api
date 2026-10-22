---
tags:
 - jvm
title: "asPsiMethods"
---

# asPsiMethods

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="p">.</span><a href="as-psi-methods.html"><span class="nf">asPsiMethods</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>PsiMethod<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaFunctionSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md) to Java PsiMethods in the context of the [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md).

The resulting list is the view on the given Kotlin declaration from Java and contains all PsiMethods produced by [`this`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md).

[`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) for the current [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) is used to provide proper actualizations for `expect` declarations. Since the produced list is a JVM-specific representation, [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) is expected to be a JVM one.

If [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) is not a JVM module or the provided [`KaFunctionSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md) is not visible from Java, returns an empty list.

### Example:
The following Kotlin function:

```kotlin
// MyFile.kt
@JvmOverloads
@JvmName("jvmFoo")
fun foo(a: Int, b: Int = 1) {}
```

Is seen as the following PsiMethods from Java:

```java
public final class MyFileKt {
    @kotlin.jvm.JvmName(name = "jvmFoo")
    @kotlin.jvm.JvmOverloads()
    public static void jvmFoo(int);

    @kotlin.jvm.JvmName(name = "jvmFoo")
    @kotlin.jvm.JvmOverloads()
    public static void jvmFoo(int, int);
}
```


</div>

</div>
