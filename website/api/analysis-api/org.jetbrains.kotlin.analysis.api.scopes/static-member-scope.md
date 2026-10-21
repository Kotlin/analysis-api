---
tags:
 - jvm
title: "staticMemberScope"
---

# staticMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="static-member-scope.html">staticMemberScope</a><span class="o">: </span><a href="-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](-ka-scope/index.md) containing the static members of the given [`KaDeclarationContainerSymbol`](../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md).

The behavior of the scope differs based on whether the given [`KaDeclarationContainerSymbol`](../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md) is a Kotlin or Java class:

 - <strong>Kotlin class:</strong> The scope contains static callables (functions and properties) and classifiers (classes and objects) declared directly in the [`KaDeclarationContainerSymbol`](../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md). Hence, the static member scope for Kotlin classes is equivalent to [`staticDeclaredMemberScope`](static-declared-member-scope.md).


 - <strong>Java class:</strong> The scope contains static callables (functions and properties) declared in the [`KaDeclarationContainerSymbol`](../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md) or any of its superclasses (excluding static callables from super-interfaces), and classes declared directly in the [`KaDeclarationContainerSymbol`](../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md). This follows Kotlin's rules about static inheritance in Java classes, where static callables are propagated from superclasses, but nested classes are not.


#### Kotlin Example
```kotlin
abstract class A {
    class C1
    inner class D1
    object O1

    // There is no way to declare a static callable in an abstract class, as only enum classes define additional static callables.
}

class B : A() {
    class C2
    inner class D2
    object O2
    companion object {
        val baz: String = ""
    }
}
```

The static member scope of `B` contains the following symbols:

```
class C2
inner class D2
object O2
companion object
```

#### Java Example
```java
// SuperInterface.java
public interface SuperInterface {
    public static void fromSuperInterface() { }
}

// SuperClass.java
public abstract class SuperClass implements SuperInterface {
    static class NestedSuperClass { }
    class InnerSuperClass { }
    public static void fromSuperClass() { }
}

// FILE: JavaClass.java
public class JavaClass extends SuperClass {
    static class NestedClass { }
    class InnerClass { }
    public static void fromJavaClass() { }
}
```

The static member scope of `JavaClass` contains the following symbols:

```
public static void fromSuperClass()
public static void fromJavaClass()
static class NestedClass
class InnerClass
```

#### See also


 - [`memberScope`](member-scope.md)



</div>

</div>
