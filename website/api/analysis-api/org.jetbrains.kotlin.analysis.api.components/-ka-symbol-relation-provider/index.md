---
tags:
 - jvm
title: "KaSymbolRelationProvider"
---

# KaSymbolRelationProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaSymbolRelationProvider</a> : <a href="../-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>#### Inheritors


 - [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)



</div>

## Properties
### allOverriddenSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="index.html#alloverriddensymbols">allOverriddenSymbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

All explicitly declared (non-fake) callable symbols overridden by this callable symbol.

The sequence implicitly unwraps substituted and intersection override symbols (see [`INTERSECTION_OVERRIDE`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-origin/-i-n-t-e-r-s-e-c-t-i-o-n_-o-v-e-r-r-i-d-e/index.md) and [`SUBSTITUTION_OVERRIDE`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-origin/-s-u-b-s-t-i-t-u-t-i-o-n_-o-v-e-r-r-i-d-e/index.md)).

The sequence doesn't include the original overridden declaration of a delegated symbol (for that, use [`fakeOverrideOriginal`](index.md#fakeoverrideoriginal)).

Depending on this callable symbol, the sequence contains:

 - Regular [`KaNamedFunctionSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.md) that is not a Java accessor method of a synthetic Java property: overridden function symbols.


 - Java [`KaNamedFunctionSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.md) that corresponds to the getter or setter of a [`KaSyntheticJavaPropertySymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-synthetic-java-property-symbol/index.md): the same property symbols as the corresponding synthetic property accessor, not Java accessor methods.


 - [`KaPropertySymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-property-symbol/index.md), including [`KaSyntheticJavaPropertySymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-synthetic-java-property-symbol/index.md): overridden property symbols.


 - [`KaPropertyGetterSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-property-getter-symbol/index.md): overridden properties of the containing property, not getter symbols.


 - [`KaPropertySetterSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-property-setter-symbol/index.md): overridden mutable properties whose setters are overridden by this setter.


 - [`KaValueParameterSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.md) with [`KaValueParameterSymbol.primaryConstructorProperty`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.md#primaryconstructorproperty): overridden symbols of that generated property.


 - Other callable kinds: an empty sequence.


The sequence may include [`KaSyntheticJavaPropertySymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-synthetic-java-property-symbol/index.md)s in Java/Kotlin hierarchies.

**Example**

```kotlin
abstract class C {
    open fun foo() { ... }
}

abstract class B : C() {
    override fun foo() { ... }
}

class A : B() {
    override fun foo() { ... }
}
```

For `A.foo`, [`allOverriddenSymbols`](index.md#alloverriddensymbols) contains both overridden super-declarations, `B.foo` and `C.foo`.

**See also**



 - [`directlyOverriddenSymbols`](index.md#directlyoverriddensymbols)
 - [`fakeOverrideOriginal`](index.md#fakeoverrideoriginal)



</div>

</div>
### containingDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="index.html#containingdeclaration">containingDeclaration</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`KaDeclarationSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.md) which contains this symbol, or `null` if there is no containing declaration:

 - For top-level declarations, a containing [`KaScriptSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-script-symbol/index.md), or `null` for non-script declarations.


 - For class members, the containing class symbol.


 - For property members, the corresponding property.


 - For local declarations, the symbol of the containing declaration.



</div>

</div>
### containingFile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="index.html#containingfile">containingFile</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`KaFileSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md) which contains this symbol, or `null` if this symbol is already a [`KaFileSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md), since it has no containing file. Also `null` for Java and library declarations.


</div>

</div>
### containingModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="index.html#containingmodule">containingModule</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaModule`](../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md) which contains this symbol.


</div>

</div>
### containingSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="index.html#containingsymbol">containingSymbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`KaSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md) which contains this symbol, or `null` if there is no containing declaration:

 - For top-level declarations, a [`KaFileSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md), or a [`KaScriptSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-script-symbol/index.md) if the file is a script file.


 - For [`KaScriptSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-script-symbol/index.md)s, a [`KaFileSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md).


 - For class members, the containing class symbol.


 - For local declarations, the symbol of the containing declaration.



</div>

</div>
### directlyOverriddenSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="index.html#directlyoverriddensymbols">directlyOverriddenSymbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Explicitly declared (non-fake) callable symbols that are directly overridden by this callable symbol.

The sequence implicitly unwraps substituted and intersection override symbols (see [`INTERSECTION_OVERRIDE`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-origin/-i-n-t-e-r-s-e-c-t-i-o-n_-o-v-e-r-r-i-d-e/index.md) and [`SUBSTITUTION_OVERRIDE`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-origin/-s-u-b-s-t-i-t-u-t-i-o-n_-o-v-e-r-r-i-d-e/index.md)).

The sequence doesn't include the original overridden declaration of a delegated symbol (for that, use [`fakeOverrideOriginal`](index.md#fakeoverrideoriginal)).

Symbol kinds follow the same mapping as [`allOverriddenSymbols`](index.md#alloverriddensymbols). In particular, property accessor symbols and Java accessor methods of synthetic Java properties are represented by property symbols rather than accessor or Java method symbols. Setters include only mutable properties whose setters are directly overridden.

**Example**

```kotlin
abstract class C {
    open fun foo() { ... }
}

abstract class B : C() {
    override fun foo() { ... }
}

class A : B() {
    override fun foo() { ... }
}
```

For `A.foo`, [`directlyOverriddenSymbols`](index.md#directlyoverriddensymbols) contains only the directly overridden super-declaration, `B.foo`.

**See also**



 - [`allOverriddenSymbols`](index.md#alloverriddensymbols)
 - [`fakeOverrideOriginal`](index.md#fakeoverrideoriginal)



</div>

</div>
### fakeOverrideOriginal

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="index.html#fakeoverrideoriginal">fakeOverrideOriginal</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

The original declared symbol for this callable symbol, after unwrapping fake override [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md)s if needed.

In a class scope, a symbol may be derived from symbols declared in super classes. For example, consider the following:

```
public interface A<T> {
  public fun foo(t: T)
}

public interface B : A<String> {
}
```

In the class scope of `B`, there is a callable symbol `foo` that takes a `String`. This symbol is derived from the original symbol in `A` that takes the type parameter `T` (fake override). Given such a fake override symbol, [`fakeOverrideOriginal`](index.md#fakeoverrideoriginal) is the original declared symbol.

Such a situation can also happen for intersection symbols (in case of multiple supertypes containing symbols with an identical signature after specialization) and delegation.

**See also**



 - [`KaSymbolOrigin.INTERSECTION_OVERRIDE`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-origin/-i-n-t-e-r-s-e-c-t-i-o-n_-o-v-e-r-r-i-d-e/index.md)
 - [`KaSymbolOrigin.SUBSTITUTION_OVERRIDE`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-origin/-s-u-b-s-t-i-t-u-t-i-o-n_-o-v-e-r-r-i-d-e/index.md)
 - [`KaSymbolOrigin.DELEGATED`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-origin/-d-e-l-e-g-a-t-e-d/index.md)



</div>

</div>
### functionalInterface

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-sam-constructor-symbol/index.html">KaSamConstructorSymbol</a><span class="p">.</span><a href="index.html#functionalinterface">functionalInterface</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaClassLikeSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.md) of the corresponding [functional (SAM) interface](https://kotlinlang.org/docs/fun-interfaces.html).

**Example**

```kotlin
fun interface MyPredicate {
    fun test(value: Int): Boolean
}

val p = MyPredicate { it > 0 }  // MyPredicate is a SAM constructor call
```

For the `MyPredicate` SAM constructor symbol, [`functionalInterface`](index.md#functionalinterface) is the symbol for the `MyPredicate` interface.


</div>

</div>
### functionalInterfaceFunction

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">.</span><a href="index.html#functionalinterfacefunction">functionalInterfaceFunction</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The single abstract function of a [functional interface](https://kotlinlang.org/docs/fun-interfaces.html), or `null` if this class is not a functional interface.

A functional interface has exactly one abstract function. In Kotlin, it must be declared with the `fun` modifier. The function may be inherited from a parent interface.

**Example**

```kotlin
fun interface MyPredicate {
    fun test(value: Int): Boolean
}
```

For `MyPredicate`, [`functionalInterfaceFunction`](index.md#functionalinterfacefunction) is the symbol for the `test` function.

**See also**



 - [`KaNamedClassSymbol.isFun`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.md#isfun)
 - [`samConstructor`](index.md#samconstructor)



</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-sam-constructor-symbol/index.html">KaSamConstructorSymbol</a><span class="p">.</span><a href="index.html#functionalinterfacefunction">functionalInterfaceFunction</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/index.html">KaNamedFunctionSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

The single abstract function of the [`functional interface`](index.md#functionalinterface) that this SAM constructor creates.

**Example**

```kotlin
fun interface MyPredicate {
    fun test(value: Int): Boolean
}

val p = MyPredicate { it > 0 }  // MyPredicate is a SAM constructor call
```

For the `MyPredicate` SAM constructor symbol, [`functionalInterfaceFunction`](index.md#functionalinterfacefunction) is the symbol for the `test` function.

**See also**



 - [`KaClassLikeSymbol.functionalInterfaceFunction`](index.md#functionalinterfacefunction)
 - [`functionalInterface`](index.md#functionalinterface)



</div>

</div>
### intersectionOverriddenSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="index.html#intersectionoverriddensymbols">intersectionOverriddenSymbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

All callable symbols overridden by this callable symbol if it is an intersection override, or an empty list otherwise.

Symbol kinds follow the same mapping as [`allOverriddenSymbols`](index.md#alloverriddensymbols). In particular, property accessor symbols and Java accessor methods of synthetic Java properties are represented by property symbols rather than accessor or Java method symbols. Setters include only mutable properties whose setters are overridden by the intersection override.

**Example**

```kotlin
interface Foo<T> {
    fun foo(value: T)
}

interface Bar {
    fun foo(value: String)
}

interface Both : Foo<String>, Bar
```

The `Both` interface contains an automatically generated intersection override for `foo()`. For it, [`intersectionOverriddenSymbols`](index.md#intersectionoverriddensymbols) is a list of two unsubstituted symbols: `Foo.foo(T)` and `Bar.foo(String)`.

**See also**



 - [`KaSymbolOrigin.INTERSECTION_OVERRIDE`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-origin/-i-n-t-e-r-s-e-c-t-i-o-n_-o-v-e-r-r-i-d-e/index.md)



</div>

</div>
### originalConstructorIfTypeAliased

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="p">.</span><a href="index.html#originalconstructoriftypealiased">originalConstructorIfTypeAliased</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.html">KaConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The original [`KaConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md) for a [`type-aliased constructor`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-origin/-t-y-p-e-a-l-i-a-s-e-d_-c-o-n-s-t-r-u-c-t-o-r/index.md), or `null` otherwise.

Currently, this property is marked as experimental because it might be joined with [`fakeOverrideOriginal`](index.md#fakeoverrideoriginal) in the future.


</div>

</div>
### samConstructor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="p">.</span><a href="index.html#samconstructor">samConstructor</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-sam-constructor-symbol/index.html">KaSamConstructorSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The associated [`KaSamConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-sam-constructor-symbol/index.md) if this [`KaClassLikeSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/index.md) is a [functional interface type (SAM)](https://kotlinlang.org/docs/fun-interfaces.html).

**Example**

```kotlin
fun interface MyPredicate {
    fun test(value: Int): Boolean
}

val p = MyPredicate { it > 0 }  // MyPredicate is a SAM constructor call
```

For `MyPredicate`, [`samConstructor`](index.md#samconstructor) is the symbol for the synthetic SAM constructor that enables the `MyPredicate { ... }` lambda syntax.


</div>

</div>
### sealedClassInheritors

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="p">.</span><a href="index.html#sealedclassinheritors">sealedClassInheritors</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The inheritors of the given sealed class.

The list is limited to class symbols which are [`analyzable`](../-ka-analysis-scope-provider/index.md#analysisscope) in the use-site [`KaModule`](../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md). While sealed class inheritors can usually only be defined in the same module, there are more complex [rules](https://kotlinlang.org/docs/sealed-classes.html#inheritance-in-multiplatform-projects) around multiplatform projects. If the use-site module is a common source set and additional sealed inheritors are declared in a platform source set, [`sealedClassInheritors`](index.md#sealedclassinheritors) will not include those additional platform sealed inheritors.

**Throws**



[`IllegalArgumentException`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html)

:   if the given class is not a sealed class.





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
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### getExpectsForActual

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="index.html#getexpectsforactual"><span class="nf">getExpectsForActual</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an `expect` symbol for the given `actual` symbol, if it is available. The function may return multiple `expect` symbols in case of ambiguity errors.


</div>

</div>
### hasConflictingSignatureWith

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="p">.</span><a href="index.html#hasconflictingsignaturewith"><span class="nf">hasConflictingSignatureWith</span></a><span class="p">(</span>other<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="p">, </span>targetPlatform<span class="o">: </span>TargetPlatform<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns whether [`this`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md) declaration has a conflicting signature with [`other`](index.md#hasconflictingsignaturewith) based on platform-specific checks from [`targetPlatform`](index.md#hasconflictingsignaturewith).

Note that it doesn't consider function names or their visibility, only their signatures. In other words, it calculates whether two functions would conflict with each other when named equally and positioned in the same scope.

Example for JVM platform:

```kotlin
fun foo(vararg x: Int) {}

fun bar(x: IntArray) {}
```

Two functions `foo` and `bar` have the same JVM signature (as vararg parameter is transformed into a regular `IntArray` parameter). However, these two functions can coexist on non-JVM platforms.

``kotlin fun foo() {}

fun main() {      fun bar() {} }

```
These two functions `foo` and `bar` have signatures, which are conflicting on every platform.
```


</div>

</div>
### implementationState

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="index.html#implementationstate"><span class="nf">implementationState</span></a><span class="p">(</span>implementerClassSymbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="../-ka-callable-implementation-state/index.html">KaCallableImplementationState</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KaCallableImplementationState`](../-ka-callable-implementation-state/index.md) of the given [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) in the context of [`implementerClassSymbol`](index.md#implementationstate).

Returns `null` if:

 - The symbol is a top-level callable;


 - The symbol is declared in a class or interface that is not a supertype of [`implementerClassSymbol`](index.md#implementationstate);


 - If the symbol is non-implementable (for example, it is a [`KaConstructorSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md), or a [`KaValueParameterSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/index.md)).


The implementation state describes whether a callable is already implemented, has an inherited implementation, can be overridden, or must be explicitly overridden in the given class.

**See also**



 - [`KaCallableImplementationState`](../-ka-callable-implementation-state/index.md)



</div>

</div>
### isDirectSubClassOf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">.</span><a href="index.html#isdirectsubclassof"><span class="nf">isDirectSubClassOf</span></a><span class="p">(</span>superClass<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks if [`this`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) class has [`superClass`](index.md#isdirectsubclassof) listed as its direct superclass.

The class is not considered to be a direct subclass of itself, so `myClass.isDirectSubClassOf(myClass)` is always `false`.


</div>

</div>
### isSubClassOf

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">.</span><a href="index.html#issubclassof"><span class="nf">isSubClassOf</span></a><span class="p">(</span>superClass<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks if [`this`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) class has [`superClass`](index.md#issubclassof) as its superclass somewhere in the inheritance hierarchy.

The class is not considered to be a subclass of itself, so `myClass.isSubClassOf(myClass)` is always `false`.


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
