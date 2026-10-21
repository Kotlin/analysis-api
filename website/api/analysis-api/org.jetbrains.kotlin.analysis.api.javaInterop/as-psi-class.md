---
tags:
 - jvm
title: "asPsiClass"
---

# asPsiClass

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">.</span><a href="as-psi-class.html"><span class="nf">asPsiClass</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiClass<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaClassSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) to Java PsiClass in the context of the [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md).

The resulting PsiClass is the view on the given Kotlin class from Java. [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) for the current [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) is used to provide proper actualizations for `expect` declarations. Since the produced PsiClass is a JVM-specific representation, [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) is expected to be a JVM one.

If [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) is not a JVM module or the provided [`KaClassSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) is not visible from Java, returns `null`.

### Example:
The following Kotlin class:

```kotlin
interface MyInterface {
    val property: String

    fun function(argument: Int): Int
}
```

Is seen as the following PsiClass from Java:

```java
public interface MyInterface {
    @org.jetbrains.annotations.NotNull()
    java.lang.String getProperty();

    int function(int argument);
}
```

The following Kotlin enum class:

```kotlin
package example

enum class MyEnum {
    A {
        fun foo() {}
    },
    B,
}
```

Is seen as the following PsiClass from Java:

```java
public enum MyEnum {
    A // PsiField
    {
        A();                     // Anonymous initializer PsiClass
        public final void foo(); //
    },

    B; // Does not have an anonymous initializer class, just PsiField

    public static kotlin.enums.EnumEntries<example.MyEnum> getEntries();
    public static example.MyEnum [] values();
    public static example.MyEnum valueOf(java.lang.String) throws java.lang.IllegalArgumentException, java.lang.NullPointerException;
    private  MyEnum();
}
```


</div>

</div>
