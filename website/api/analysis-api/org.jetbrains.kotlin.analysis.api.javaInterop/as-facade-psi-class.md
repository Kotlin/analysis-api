---
tags:
 - jvm
title: "asFacadePsiClass"
---

# asFacadePsiClass

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="p">.</span><a href="as-facade-psi-class.html"><span class="nf">asFacadePsiClass</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiClass<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaFileSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md) to Java facade PsiClass in the context of the [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md).

The resulting PsiClass is the view on the given Kotlin file from Java. E.g., `main.kt` file is converted to `MainKt` class facade. [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) for the current [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) is used to provide proper actualizations for `expect` declarations. Since the produced PsiClass is a JVM-specific representation, [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) is expected to be a JVM one.

Note that the produced facade class only stores non-class declarations. Each Kotlin class is mapped to its own top-level PsiClass.

If [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) is not a JVM module or the provided [`KaFileSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md) is not supported, returns `null`.

Examples of non-supported files are:

 - Scripts


 - Files with no top-level callables


If the provided [`KaFileSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md) has a [`kotlin.jvm.JvmMultifileClass`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-multifile-class/index.html) annotation, the constructed PsiClass is a facade for all other files with [`kotlin.jvm.JvmMultifileClass`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-multifile-class/index.html) annotation and the same [`kotlin.jvm.JvmName`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-name/index.html).

### Example:
The following Kotlin file:

```kotlin
// MyFile.kt
class MyClass

fun foo(t: Int) {}

val x: Int = 0
```

Is seen as the following PsiClass from Java:

```java
public final class MyFileKt { // Doesn't contain `MyClass` declaration
    private static final int x = 0;

    public static int getX();

    public static void foo(int);
}
```

The following multifile class file `FirstFacadeClass`:

```kotlin
// FirstFacadeClass.kt
@file:JvmMultifileClass
@file:JvmName("SomeFacade")
package pkg

fun foo() = 42

val x = 24

// SecondFacadeClass.kt
@file:JvmMultifileClass
@file:JvmName("SomeFacade")
package pkg

private fun privateFoo(): Int = 3

const val myConst = 42
```

Is seen as the following PsiClass from Java:

```java
public final class SomeFacade {
  public static final int myConst = 42;

  public static final int foo();

  public static final int getX();
}
```

#### See also


 - [`KaScriptSymbol.asFacadePsiClass`](as-facade-psi-class.md)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-script-symbol/index.html">KaScriptSymbol</a><span class="p">.</span><a href="as-facade-psi-class.html"><span class="nf">asFacadePsiClass</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiClass<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaScriptSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-script-symbol/index.md) to Java facade PsiClass in the context of the [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md).

The resulting PsiClass is the view on the given Kotlin script from Java. [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) for the current [`KaSession`](../org.jetbrains.kotlin.analysis.api/-ka-session/index.md) is used to provide proper actualizations for `expect` declarations. Since the produced PsiClass is a JVM-specific representation, [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) is expected to be a JVM one.

In contrast to [`KaFileSymbol.asFacadePsiClass`](as-facade-psi-class.md), regular Kotlin classes in scripts are mapped to nested PsiClasses.

If [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md) is not a JVM module or the provided [`KaScriptSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-script-symbol/index.md) comes from a code fragment, returns `null`.

### Example:
The following Kotlin script:

```kotlin
// MyScript.kts
println("Hello, World!")

val x = 1

class MyClass {
    fun bar() {}
}
```

Is seen as the following PsiClass from Java:

```java
public final class MyScript extends kotlin.script.experimental.templates.ScriptWithArgs {
    public static void main(java.lang.String[]);

    public MyScript(java.lang.String[]);

    private final int x = 1;
    public int getX();

    public static final class MyClass {
        public MyClass();
        public void bar();
    }
}
```

#### See also


 - [`KaFileSymbol.asFacadePsiClass`](as-facade-psi-class.md)



</div>

</div>
