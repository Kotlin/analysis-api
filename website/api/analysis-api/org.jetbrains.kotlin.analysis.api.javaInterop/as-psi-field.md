---
tags:
 - jvm
title: "asPsiField"
---

# asPsiField

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-backing-field-symbol/index.html">KaBackingFieldSymbol</a><span class="p">.</span><a href="as-psi-field.html"><span class="nf">asPsiField</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiField<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaBackingFieldSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-backing-field-symbol/index.md) to Java PsiField in the context of the [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md).

The resulting PsiField is the view on the given Kotlin backing field from Java. [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) for the current [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) is used to provide proper actualizations for `expect` declarations. Since the produced PsiField is a JVM-specific representation, [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) is expected to be a JVM one.

If [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) is not a JVM module or the provided [`KaBackingFieldSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-backing-field-symbol/index.md) is not visible from Java as a PsiField, returns `null`.

### Example:
The following Kotlin property with implicit backing field:

```kotlin
// MyFile.kt
val x: Int = 0 // implicit backing field
```

Is seen as the following PsiMethod getter and PsiField from Java:

```java
public final class MyFileKt {
    private static final int x = 0; // PsiField

    public static int getX();
}
```


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">.</span><a href="as-psi-field.html"><span class="nf">asPsiField</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiField<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaClassSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) to Java PsiField in the context of the [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md).

The resulting PsiField is the view on the given Kotlin declaration from Java. [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) for the current [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) is used to provide proper actualizations for `expect` declarations. Since the produced PsiField is a JVM-specific representation, [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) is expected to be a JVM one.

[`KaClassSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) has be mapped to PsiField in several cases:

 - `INSTANCE` field for object declarations


 - `Companion` (or the given name for named companions) field for companion objects


If [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) is not a JVM module or the provided [`KaClassSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) is not visible from Java as a PsiField, returns `null`.

### Example:
The following Kotlin companion object

```kotlin
package example

class MyClass {
    companion object {
        fun foo() {}
    }
}
```

Is seen as the following PsiField from Java:

```java
public final class MyClass {
    public static final example.MyClass.Companion Companion; // `Companion` instance field

    public MyClass();

    public static final class Companion {
        private  Companion();

        public final void foo();
    }
}
```

The following Kotlin object

```kotlin
package example

object MyObject {
    fun foo() {}
}
```

Is seen as the following PsiField from Java:

```java
public final class MyObject {
    public static final example.MyObject INSTANCE; // `INSTANCE` field

    private MyObject();

    public void foo();
}
```


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-enum-entry-symbol/index.html">KaEnumEntrySymbol</a><span class="p">.</span><a href="as-psi-field.html"><span class="nf">asPsiField</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiEnumConstant<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaEnumEntrySymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-enum-entry-symbol/index.md) to Java PsiEnumConstant in the context of the [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md).

The resulting PsiEnumConstant is the view on the given Kotlin enum entry from Java. [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) for the current [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) is used to provide proper actualizations for `expect` declarations. Since the produced PsiEnumConstant is a JVM-specific representation, [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) is expected to be a JVM one.

If [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) is not a JVM module or the provided [`KaEnumEntrySymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-enum-entry-symbol/index.md) is not visible from Java as a PsiEnumConstant, returns `null`.

### Example:
The following Kotlin enum entries

```kotlin
enum class MyEnum {
    A,
    B
}
```

Are seen as the following PsiEnumConstants from Java:

```java
public enum MyEnum {
    A, // PsiEnumConstant for MyEnum.A
    B; // PsiEnumConstant for MyEnum.B

    public static kotlin.enums.EnumEntries<example.MyEnum> getEntries();
    public static example.MyEnum [] values();
    public static example.MyEnum valueOf(java.lang.String) throws java.lang.IllegalArgumentException, java.lang.NullPointerException;
    private  MyEnum();
}
```


</div>

</div>
