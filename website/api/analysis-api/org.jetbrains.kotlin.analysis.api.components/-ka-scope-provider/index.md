---
tags:
 - jvm
title: "KaScopeProvider"
---

# KaScopeProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaScopeProvider</a> : <a href="../-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>#### Inheritors


 - [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)



</div>

## Properties
### combinedDeclaredMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="index.html#combineddeclaredmemberscope">combinedDeclaredMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing all members explicitly declared in the given [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md).

In contrast to [`declaredMemberScope`](index.md#declaredmemberscope) and [`staticDeclaredMemberScope`](index.md#staticdeclaredmemberscope), this scope contains both static and non-static members.


</div>

</div>
### combinedMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="index.html#combinedmemberscope">combinedMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing all members from [`memberScope`](index.md#memberscope) and [`staticMemberScope`](index.md#staticmemberscope).


</div>

</div>
### declarationScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.html">KaTypeScope</a><span class="p">.</span><a href="index.html#declarationscope">declarationScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing unsubstituted declarations from the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)'s underlying declaration.


</div>

</div>
### declaredMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="index.html#declaredmemberscope">declaredMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing the non-static callables (functions, properties, and constructors) and inner classes explicitly declared in the given [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md).

The declared member scope does not contain classifiers (including the companion object) except for inner classes. To retrieve the classifiers declared in this [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md), please use the static declared member scope provided by [`staticDeclaredMemberScope`](index.md#staticdeclaredmemberscope).

**See also**



 - [`staticDeclaredMemberScope`](index.md#staticdeclaredmemberscope)



</div>

</div>
### delegatedMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="index.html#delegatedmemberscope">delegatedMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing synthetic callables (functions and properties) created by interface delegation.

**Example**

```kotlin
interface I {
    val foo: Int get() = 2
    fun bar(): String
}

class A(
    private val p: I
) : I by p {
    val regularProperty: Int = 5
}
```

The delegated member scope for `A` has the following entries:

```
override val foo: kotlin.Int
  get()

override fun bar(): kotlin.String
```

`regularProperty` is not contained in the delegated member scope because it is not a delegated property.


</div>

</div>
### fileScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="p">.</span><a href="index.html#filescope">fileScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing the top-level declarations (such as classes, functions and properties) in the given [`KaFileSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md).


</div>

</div>
### importingScopeContext

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="index.html#importingscopecontext">importingScopeContext</a><span class="o">: </span><a href="../-ka-scope-context/index.html">KaScopeContext</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScopeContext`](../-ka-scope-context/index.md) formed from all imports in the [`KtFile`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md).

By default, the scope context also includes default importing scopes, which can be filtered by [`KaScopeKind`](../-ka-scope-kind/index.md).


</div>

</div>
### memberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="index.html#memberscope">memberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing non-static callable members (functions, properties, and constructors) and all classifier members (classes and objects) of the given [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md). The scope includes members inherited from the symbol's supertypes, in addition to members which are declared explicitly inside the symbol's body.

The member scope doesn't include [synthetic Java properties](https://kotlinlang.org/docs/java-interop.html#getters-and-setters). For a scope which contains synthetic properties, please refer to [`syntheticJavaPropertiesScope`](index.md#syntheticjavapropertiesscope).

**See also**



 - [`staticMemberScope`](index.md#staticmemberscope)



</div>

</div>
### packageScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-package-symbol/index.html">KaPackageSymbol</a><span class="p">.</span><a href="index.html#packagescope">packageScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing all members of the package represented by the given [`KaPackageSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-package-symbol/index.md), not including members of subpackages.


</div>

</div>
### scope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#scope">scope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.html">KaTypeScope</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.md) for the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md), or `null` if the type is [`erroneous`](../../org.jetbrains.kotlin.analysis.api.types/-ka-error-type/index.md). The scope includes all members which are callable on a given type. It also includes [synthetic Java properties](https://kotlinlang.org/docs/java-interop.html#getters-and-setters).

Comparing to [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md), the [`KaTypeScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.md) contains members whose use-site type parameters have been substituted.

**Example**

```kotlin
fun foo(list: List<String>) {
    list
}
```

We can get a [`KaTypeScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.md) for the [`expression type`](../-ka-expression-type-provider/index.md#expressiontype) of `list`. This scope contains a `get(index: Int): String` function, where the return type `E` from [`List.get`](../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-list/index.md#get) is substituted with the type argument `String`.

**See also**



 - [`KaTypeScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.md)
 - [`KaTypeProvider.type`](../-ka-type-provider/index.md#type)
 - [`KaExpressionTypeProvider.expressionType`](../-ka-expression-type-provider/index.md#expressiontype)



</div>

</div>
### staticDeclaredMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="index.html#staticdeclaredmemberscope">staticDeclaredMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing the static callables (functions and properties) and all classifiers (classes and objects) explicitly declared in the given [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md).

It is worth noting that, while Java classes may contain declarations of static callables freely, in Kotlin only enum classes define static callables. Hence, for non-enum Kotlin classes, it is not expected that the static declared member scope will contain any callables.

**See also**



 - [`declaredMemberScope`](index.md#declaredmemberscope)



</div>

</div>
### staticMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">.</span><a href="index.html#staticmemberscope">staticMemberScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing the static members of the given [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md).

The behavior of the scope differs based on whether the given [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md) is a Kotlin or Java class:

 - <strong>Kotlin class:</strong> The scope contains static callables (functions and properties) and classifiers (classes and objects) declared directly in the [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md). Hence, the static member scope for Kotlin classes is equivalent to [`staticDeclaredMemberScope`](index.md#staticdeclaredmemberscope).


 - <strong>Java class:</strong> The scope contains static callables (functions and properties) declared in the [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md) or any of its superclasses (excluding static callables from super-interfaces), and classes declared directly in the [`KaDeclarationContainerSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.md). This follows Kotlin's rules about static inheritance in Java classes, where static callables are propagated from superclasses, but nested classes are not.


**Kotlin Example**

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

**Java Example**

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

**See also**



 - [`memberScope`](index.md#memberscope)



</div>

</div>
### syntheticJavaPropertiesScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#syntheticjavapropertiesscope">syntheticJavaPropertiesScope</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.html">KaTypeScope</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.md) containing the [synthetic Java properties](https://kotlinlang.org/docs/java-interop.html#getters-and-setters) created for a given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md).


</div>

</div>
### [`token`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#token)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#token">token</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.html">KaLifetimeToken</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaLifetimeToken`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md) which determines the lifetime of the lifetime owner.


</div>

</div>
## Functions
### asCompositeScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a><span class="o">></span><span class="p">.</span><a href="index.html#ascompositescope"><span class="nf">asCompositeScope</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

Combines a list of [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md)s into a single composite [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md). The resulting scope contains all members of its constituent scopes.


</div>

</div>
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### compositeScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-ka-scope-context/index.html">KaScopeContext</a><span class="p">.</span><a href="index.html#compositescope"><span class="nf">compositeScope</span></a><span class="p">(</span>filter<span class="o">: </span><span class="p">(</span><a href="../-ka-scope-kind/index.html">KaScopeKind</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span>{ true }<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

Returns a single [`KaScope`](../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) that contains declarations from all scopes that satisfy [`filter`](index.md#compositescope).

The order of declarations corresponds to the order of their containing scopes, which are sorted according to their [`indices`](../-ka-scope-kind/-script-member-scope/index.md#indexintower) in the scope tower.


</div>

</div>
### [`isValid`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#isvalid)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#isvalid"><span class="nf">isValid</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the lifetime owner is still valid, i.e. we are still in the scope of the lifetime owner's regular lifetime.


</div>

</div>
### scopeContext

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="index.html#scopecontext"><span class="nf">scopeContext</span></a><span class="p">(</span>position<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="../-ka-scope-context/index.html">KaScopeContext</a>
</span></code></pre></div>
</div>


<div markdown>

Computes the lexical scope context for a given [`position`](index.md#scopecontext) in the [`KtFile`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md). The scope context includes all scopes that are relevant for the given position, together with all available implicit receivers.


</div>

</div>
### [`withValidityAssertion`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="o">> </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion"><span class="nf">withValidityAssertion</span></a><span class="p">(</span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#withvalidityassertion">R</a>
</span></code></pre></div>
</div>


<div markdown>

Executes [`action`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#withvalidityassertion) only if the [`KaLifetimeOwner`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.md) is still [`valid`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md#isvalid) and [`accessible`](../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-token/index.md#isaccessible). Otherwise, throws a validity exception based on the concrete violation.


</div>

</div>
