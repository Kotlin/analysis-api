---
tags:
 - jvm
title: "KaLocalVariableSymbol"
---

# KaLocalVariableSymbol

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KaLocalVariableSymbol</a> : <a href="../-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>[`KaLocalVariableSymbol`](index.md) represents a local variable.


</div>

## Constructors
### KaLocalVariableSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### allOverriddenSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../-ka-receiver-parameter-symbol/index.html#alloverriddensymbols">allOverriddenSymbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

All explicitly declared (non-fake) callable symbols overridden by this callable symbol.

The sequence implicitly unwraps substituted and intersection override symbols (see [`INTERSECTION_OVERRIDE`](../-ka-symbol-origin/-i-n-t-e-r-s-e-c-t-i-o-n_-o-v-e-r-r-i-d-e/index.md) and [`SUBSTITUTION_OVERRIDE`](../-ka-symbol-origin/-s-u-b-s-t-i-t-u-t-i-o-n_-o-v-e-r-r-i-d-e/index.md)).

The sequence doesn't include the original overridden declaration of a delegated symbol (for that, use [`fakeOverrideOriginal`](../-ka-receiver-parameter-symbol/index.md#fakeoverrideoriginal)).

Depending on this callable symbol, the sequence contains:

 - Regular [`KaNamedFunctionSymbol`](../-ka-named-function-symbol/index.md) that is not a Java accessor method of a synthetic Java property: overridden function symbols.


 - Java [`KaNamedFunctionSymbol`](../-ka-named-function-symbol/index.md) that corresponds to the getter or setter of a [`KaSyntheticJavaPropertySymbol`](../-ka-synthetic-java-property-symbol/index.md): the same property symbols as the corresponding synthetic property accessor, not Java accessor methods.


 - [`KaPropertySymbol`](../-ka-property-symbol/index.md), including [`KaSyntheticJavaPropertySymbol`](../-ka-synthetic-java-property-symbol/index.md): overridden property symbols.


 - [`KaPropertyGetterSymbol`](../-ka-property-getter-symbol/index.md): overridden properties of the containing property, not getter symbols.


 - [`KaPropertySetterSymbol`](../-ka-property-setter-symbol/index.md): overridden mutable properties whose setters are overridden by this setter.


 - [`KaValueParameterSymbol`](../-ka-value-parameter-symbol/index.md) with [`KaValueParameterSymbol.primaryConstructorProperty`](../-ka-value-parameter-symbol/index.md#primaryconstructorproperty): overridden symbols of that generated property.


 - Other callable kinds: an empty sequence.


The sequence may include [`KaSyntheticJavaPropertySymbol`](../-ka-synthetic-java-property-symbol/index.md)s in Java/Kotlin hierarchies.

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

For `A.foo`, [`allOverriddenSymbols`](../-ka-receiver-parameter-symbol/index.md#alloverriddensymbols) contains both overridden super-declarations, `B.foo` and `C.foo`.

**See also**



 - [`directlyOverriddenSymbols`](../-ka-receiver-parameter-symbol/index.md#directlyoverriddensymbols)
 - [`fakeOverrideOriginal`](../-ka-receiver-parameter-symbol/index.md#fakeoverrideoriginal)



</div>

</div>
### anchorPsi

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#anchorpsi">anchorPsi</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A PsiElement associated with the symbol. Usually, it is the best PsiElement representation for a particular [`KaSymbol`](../-ka-symbol/index.md).

It reuses [`realPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#realpsi), but can also provide a value for other [`origin`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#origin)s.

While [`anchorPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#anchorpsi) aims to be the most related element, it is still an approximation, and there are no strict guarantees that it is a particular element.

**Examples:**

```kotlin
class MyClass
```

For this code, [`KaNamedClassSymbol`](../-ka-named-class-symbol/index.md) represents the class, while [`KaConstructorSymbol`](../-ka-constructor-symbol/index.md) represents the implicit constructor. The class is present in the code as a [`KtClassOrObject`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.md), so that element is used. In contrast, the constructor is not present in the code, but can be obtained from the class, so [`anchorPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#anchorpsi) for it is the same [`KtClassOrObject`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.md).

For declarations generated by compiler plugins, it usually points to the declaration from which the symbol was generated, but the behavior is effectively defined by the compiler plugin itself, and the Analysis API use it unchanged.

An alternative can be getting [`realPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#realpsi) or the containing declaration instead for more predictable behavior.

**See also**



 - [`realPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#realpsi)



</div>

</div>
### [`annotations`](../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.md#annotations)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/index.html#annotations">annotations</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-list/index.html">KaAnnotationList</a>
</span></code></pre></div>
</div>


<div markdown>

A list of annotations applied to the annotated entity.


</div>

</div>
### callableId

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">override </span><span class="kd">val </span><a href="index.html#callableid">callableId</a><span class="o">: </span>CallableId<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The callable's CallableId if it exists, or `null` if the declaration is local.


</div>

</div>
### containingDeclaration

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#containingdeclaration">containingDeclaration</a><span class="o">: </span><a href="../-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`KaDeclarationSymbol`](../-ka-declaration-symbol/index.md) which contains this symbol, or `null` if there is no containing declaration:

 - For top-level declarations, a containing [`KaScriptSymbol`](../-ka-script-symbol/index.md), or `null` for non-script declarations.


 - For class members, the containing class symbol.


 - For property members, the corresponding property.


 - For local declarations, the symbol of the containing declaration.



</div>

</div>
### containingFile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#containingfile">containingFile</a><span class="o">: </span><a href="../-ka-file-symbol/index.html">KaFileSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`KaFileSymbol`](../-ka-file-symbol/index.md) which contains this symbol, or `null` if this symbol is already a [`KaFileSymbol`](../-ka-file-symbol/index.md), since it has no containing file. Also `null` for Java and library declarations.


</div>

</div>
### containingFileAnnotations

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="../-ka-receiver-parameter-symbol/index.html#containingfileannotations">containingFileAnnotations</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-list/index.html">KaAnnotationList</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

File-level annotations (`@file:SomeAnnotation`) of the source file this top-level [`KaDeclarationSymbol`](../-ka-declaration-symbol/index.md) was defined in, or `null` for a nested declaration.

This API is only intended to be used by the TypeScript export utility.


</div>

</div>
### [`containingJvmClassName`](../../org.jetbrains.kotlin.analysis.api.javaInterop/containing-jvm-class-name.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.javaInterop/containing-jvm-class-name.html">containingJvmClassName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The containing JVM class name for the given [`KaCallableSymbol`](../-ka-callable-symbol/index.md).


</div>

</div>
### containingModule

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#containingmodule">containingModule</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.html">KaModule</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaModule`](../../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md) which contains this symbol.


</div>

</div>
### containingSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#containingsymbol">containingSymbol</a><span class="o">: </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`KaSymbol`](../-ka-symbol/index.md) which contains this symbol, or `null` if there is no containing declaration:

 - For top-level declarations, a [`KaFileSymbol`](../-ka-file-symbol/index.md), or a [`KaScriptSymbol`](../-ka-script-symbol/index.md) if the file is a script file.


 - For [`KaScriptSymbol`](../-ka-script-symbol/index.md)s, a [`KaFileSymbol`](../-ka-file-symbol/index.md).


 - For class members, the containing class symbol.


 - For local declarations, the symbol of the containing declaration.



</div>

</div>
### contextParameters

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">override </span><span class="kd">val </span><a href="index.html#contextparameters">contextParameters</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-context-parameter-symbol/index.html">KaContextParameterSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of [`KaContextParameterSymbol`](../-ka-context-parameter-symbol/index.md)s directly declared in the symbol.


</div>

</div>
### contextReceivers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">override </span><span class="kd">val </span><a href="index.html#contextreceivers">contextReceivers</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.base/-ka-context-receiver/index.html">KaContextReceiver</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

List of [`KaContextReceiver`](../../org.jetbrains.kotlin.analysis.api.base/-ka-context-receiver/index.md) directly declared in the source code


</div>

</div>
### defaultAnnotationTargets

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#defaultannotationtargets">defaultAnnotationTargets</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-target/index.html">KaAnnotationTarget</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A set of annotation targets matching for the given symbol, or `null` if the symbol cannot be annotated. Annotations with one of targets from the returned set can be placed on the [`KaSymbol`](../-ka-symbol/index.md) without an explicit use-site target.

Such as, annotations with [`KaAnnotationTarget.PROPERTY`](../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-target/-companion/index.md#property) or [`KaAnnotationTarget.VALUE_PARAMETER`](../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-target/-companion/index.md#value_parameter) can be directly placed on a 'val' value parameter, while annotations for [`KaAnnotationTarget.PROPERTY_GETTER`](../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-target/-companion/index.md#property_getter) and [`KaAnnotationTarget.PROPERTY_SETTER`](../../org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-target/-companion/index.md#property_setter) can only be applied using the `@set:AnnotationName` syntax.

Check the [Annotation use-site targets](https://kotlinlang.org/docs/annotations.html#annotation-use-site-targets) documentation for additional information.


</div>

</div>
### deprecation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#deprecation">deprecation</a><span class="o">: </span><a href="../-ka-deprecation/index.html">KaDeprecation</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The deprecation status of the given symbol, or `null` if the symbol is not deprecated.

This considers deprecation annotations applied to the symbol itself and, for property-related symbols, deprecation annotations with appropriate use-site targets.


</div>

</div>
### directlyOverriddenSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../-ka-receiver-parameter-symbol/index.html#directlyoverriddensymbols">directlyOverriddenSymbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Explicitly declared (non-fake) callable symbols that are directly overridden by this callable symbol.

The sequence implicitly unwraps substituted and intersection override symbols (see [`INTERSECTION_OVERRIDE`](../-ka-symbol-origin/-i-n-t-e-r-s-e-c-t-i-o-n_-o-v-e-r-r-i-d-e/index.md) and [`SUBSTITUTION_OVERRIDE`](../-ka-symbol-origin/-s-u-b-s-t-i-t-u-t-i-o-n_-o-v-e-r-r-i-d-e/index.md)).

The sequence doesn't include the original overridden declaration of a delegated symbol (for that, use [`fakeOverrideOriginal`](../-ka-receiver-parameter-symbol/index.md#fakeoverrideoriginal)).

Symbol kinds follow the same mapping as [`allOverriddenSymbols`](../-ka-receiver-parameter-symbol/index.md#alloverriddensymbols). In particular, property accessor symbols and Java accessor methods of synthetic Java properties are represented by property symbols rather than accessor or Java method symbols. Setters include only mutable properties whose setters are directly overridden.

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

For `A.foo`, [`directlyOverriddenSymbols`](../-ka-receiver-parameter-symbol/index.md#directlyoverriddensymbols) contains only the directly overridden super-declaration, `B.foo`.

**See also**



 - [`allOverriddenSymbols`](../-ka-receiver-parameter-symbol/index.md#alloverriddensymbols)
 - [`fakeOverrideOriginal`](../-ka-receiver-parameter-symbol/index.md#fakeoverrideoriginal)



</div>

</div>
### fakeOverrideOriginal

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../-ka-receiver-parameter-symbol/index.html#fakeoverrideoriginal">fakeOverrideOriginal</a><span class="o">: </span><a href="../-ka-callable-symbol/index.html">KaCallableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

The original declared symbol for this callable symbol, after unwrapping fake override [`KaCallableSymbol`](../-ka-callable-symbol/index.md)s if needed.

In a class scope, a symbol may be derived from symbols declared in super classes. For example, consider the following:

```
public interface A<T> {
  public fun foo(t: T)
}

public interface B : A<String> {
}
```

In the class scope of `B`, there is a callable symbol `foo` that takes a `String`. This symbol is derived from the original symbol in `A` that takes the type parameter `T` (fake override). Given such a fake override symbol, [`fakeOverrideOriginal`](../-ka-receiver-parameter-symbol/index.md#fakeoverrideoriginal) is the original declared symbol.

Such a situation can also happen for intersection symbols (in case of multiple supertypes containing symbols with an identical signature after specialization) and delegation.

**See also**



 - [`KaSymbolOrigin.INTERSECTION_OVERRIDE`](../-ka-symbol-origin/-i-n-t-e-r-s-e-c-t-i-o-n_-o-v-e-r-r-i-d-e/index.md)
 - [`KaSymbolOrigin.SUBSTITUTION_OVERRIDE`](../-ka-symbol-origin/-s-u-b-s-t-i-t-u-t-i-o-n_-o-v-e-r-r-i-d-e/index.md)
 - [`KaSymbolOrigin.DELEGATED`](../-ka-symbol-origin/-d-e-l-e-g-a-t-e-d/index.md)



</div>

</div>
### importableFqName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#importablefqname">importableFqName</a><span class="o">: </span>FqName<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A FqName which can be used to import the given symbol, or `null` if the symbol cannot be imported.


</div>

</div>
### intersectionOverriddenSymbols

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../-ka-receiver-parameter-symbol/index.html#intersectionoverriddensymbols">intersectionOverriddenSymbols</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

All callable symbols overridden by this callable symbol if it is an intersection override, or an empty list otherwise.

Symbol kinds follow the same mapping as [`allOverriddenSymbols`](../-ka-receiver-parameter-symbol/index.md#alloverriddensymbols). In particular, property accessor symbols and Java accessor methods of synthetic Java properties are represented by property symbols rather than accessor or Java method symbols. Setters include only mutable properties whose setters are overridden by the intersection override.

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

The `Both` interface contains an automatically generated intersection override for `foo()`. For it, [`intersectionOverriddenSymbols`](../-ka-receiver-parameter-symbol/index.md#intersectionoverriddensymbols) is a list of two unsubstituted symbols: `Foo.foo(T)` and `Bar.foo(String)`.

**See also**



 - [`KaSymbolOrigin.INTERSECTION_OVERRIDE`](../-ka-symbol-origin/-i-n-t-e-r-s-e-c-t-i-o-n_-o-v-e-r-r-i-d-e/index.md)



</div>

</div>
### isActual

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">override </span><span class="kd">val </span><a href="index.html#isactual">isActual</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the declaration is an `actual` declaration in a multiplatform project.

See [the official Kotlin documentation](https://kotlinlang.org/docs/multiplatform-connect-to-apis.html) for more details.


</div>

</div>
### isCompanion

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">override </span><span class="kd">val </span><a href="index.html#iscompanion">isCompanion</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the callable is a [companion extension](https://github.com/Kotlin/KEEP/blob/main/proposals/KEEP-0449-companions-block-extension.md#companion-extensions) or comes from a [companion block](https://github.com/Kotlin/KEEP/blob/main/proposals/KEEP-0449-companions-block-extension.md#companion-blocks).

Java statics are also considered as from companion blocks.

<strong>Note</strong>:

 - According to the KEEP, [`KaEnumEntrySymbol`](../-ka-enum-entry-symbol/index.md) (and its generated callables like `valueOf`) are also considered implicitly declared in a companion block.


 - <strong>Callables from companion objects are not considered as from companion blocks!</strong>


**Examples:**

```kotlin
enum class EnumClass {
  Entry; // true

  val entries: EnumEntries<EnumClass> // true
  // ^ auto-generated by the compiler

  fun regular() {} // false
  val regular: Int = 1 // false
}

class Foo {
  fun classMember() {} // false
  val classMember: Int = 1 // false

  companion {
    fun companionBlockMember() {} // true
    val companionBlockMember: Int = 1 // true
  }

  companion object {
    fun companionMember(){} // false

    @JvmStatic
    fun withJvmStatic(){} // false

    @JvmField
    val withJvmFiled: Int = 42 // false

    lateinit var lateinitVariable: String // false
  }
}

object Object {
  fun objectMember() // false
  val objectMember: Int = 1 // false
}

fun topLevel() {} // false
val topLevel: Int = 1 // false

companion fun Foo.companionExtension() {} // true
companion val Foo.companionExtension: Int get() = 1 // true
```


</div>

</div>
### isDelegated

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#isdelegated">isDelegated</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the variable is a [delegated variable](https://kotlinlang.org/docs/delegated-properties.html).


</div>

</div>
### isDeprecated

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#isdeprecated">isDeprecated</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the symbol is deprecated at any level.

This is a convenience property equivalent to `deprecation != null`.


</div>

</div>
### isExpect

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">override </span><span class="kd">val </span><a href="index.html#isexpect">isExpect</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the declaration is an `expect` declaration in a multiplatform project.

See [the official Kotlin documentation](https://kotlinlang.org/docs/multiplatform-connect-to-apis.html) for more details.

**Example**

```kotlin
expect class A {
    class Nested
}
```

In this example, `isExpect` is `true` for both `A` and `A.Nested`.


</div>

</div>
### isExtension

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">override </span><span class="kd">val </span><a href="index.html#isextension">isExtension</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the callable is an [extension function or property](https://kotlinlang.org/docs/extensions.html).


</div>

</div>
### isExternal

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">override </span><span class="kd">val </span><a href="index.html#isexternal">isExternal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Indicates whether this declaration is `external`.

A declaration is considered external if any of the following is true:

 - it is explicitly marked with the `external` modifier (applicable to classes, functions, properties, and property accessors);


 - it is a member of an `external` class;


 - it is a Java `native` method.


External declarations have no Kotlin implementation and are expected to be provided externally — via [JNI](https://kotlinlang.org/docs/java-interop.html#using-jni-with-kotlin) for the JVM target or [JavaScript interop](https://kotlinlang.org/docs/js-interop.html#external-modifier) for the JS target.

Other kinds of declarations (parameters, destructuring declarations, local variables, etc.) are never considered external.

**Example**

```kotlin
external class C {
    fun foo()

    class Nested {
        fun bar()
    }
}

external val baz: Int
```

In this example (which is legal on the JS target), `C`, `Nested`, `foo`, `bar`, and `baz` are all `external`.


</div>

</div>
### isLateInit

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#islateinit">isLateInit</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the variable is a [late-initialized variable](https://kotlinlang.org/docs/properties.html#late-initialized-properties-and-variables).


</div>

</div>
### isLocal

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#islocal">isLocal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Indicates whether a symbol is defined locally within a body.

**See also**



 - [`KaSymbolLocation.LOCAL`](../-ka-symbol-location/-l-o-c-a-l/index.md)



</div>

</div>
### [`isPublicApi`](../../org.jetbrains.kotlin.analysis.api.visibility/is-public-api.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/is-public-api.html">isPublicApi</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the symbol is effectively public, including internal declarations with the [`PublishedApi`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-published-api/index.html) annotation.


</div>

</div>
### isTopLevel

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#istoplevel">isTopLevel</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Indicates whether a [`KaSymbol`](../-ka-symbol/index.md) is at the top level.

A symbol is considered top-level if it is not a part of other symbols.

**See also**



 - [`KaSymbolLocation.TOP_LEVEL`](../-ka-symbol-location/-t-o-p_-l-e-v-e-l/index.md)



</div>

</div>
### isVal

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#isval">isVal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the declaration is read-only.


</div>

</div>
### klibSourceFileName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="../-ka-receiver-parameter-symbol/index.html#klibsourcefilename">klibSourceFileName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The source file name for the given [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md) located in a Kotlin library (klib), or `null` if the declaration is not located in a klib, or when the source file name is not available.


</div>

</div>
### location

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">override </span><span class="kd">val </span><a href="index.html#location">location</a><span class="o">: </span><a href="../-ka-symbol-location/index.html">KaSymbolLocation</a>
</span></code></pre></div>
</div>


<div markdown>

The kind of location where a symbol is declared in code, e.g. [`KaSymbolLocation.TOP_LEVEL`](../-ka-symbol-location/-t-o-p_-l-e-v-e-l/index.md) for top-level declarations.

The [`location`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#location) is not to be confused with the [`origin`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#origin), which is concerned with the kind of data source or generation the symbol originates from.


</div>

</div>
### modality

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">override </span><span class="kd">val </span><a href="index.html#modality">modality</a><span class="o">: </span><a href="../-ka-symbol-modality/index.html">KaSymbolModality</a>
</span></code></pre></div>
</div>


<div markdown>

The declaration's effective [`KaSymbolModality`](../-ka-symbol-modality/index.md) (e.g. `open`). Effective modality is the symbol's modality after all language rules and compiler plugins have been taken into account, in contrast to the syntactic modality.


</div>

</div>
### [`name`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#name">name</a><span class="o">: </span>Name
</span></code></pre></div>
</div>


<div markdown>

The simple name of this [`KaSymbol`](../-ka-symbol/index.md).


</div>

</div>
### name

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#name">name</a><span class="o">: </span>Name<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The name of the [`KaSymbol`](../-ka-symbol/index.md) if it has one.


</div>

</div>
### origin

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#origin">origin</a><span class="o">: </span><a href="../-ka-symbol-origin/index.html">KaSymbolOrigin</a>
</span></code></pre></div>
</div>


<div markdown>

The kind of data source or generation the symbol originates from (e.g. source files, libraries, compiler plugins).

The [`origin`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#origin) is not to be confused with the [`location`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#location), which is concerned with the symbol's location in code.


</div>

</div>
### psi

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#psi">psi</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

<strong>The API is obsolete and will be deprecated soon. Use </strong>[`<strong>realPsi</strong>`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#realpsi)<strong> or </strong>[`<strong>anchorPsi</strong>`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#anchorpsi)<strong> instead.</strong>

A PsiElement corresponding to this [`KaSymbol`](../-ka-symbol/index.md).

The property is only defined for the following [`origin`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#origin)s:

 - [`KaSymbolOrigin.SOURCE`](../-ka-symbol-origin/-s-o-u-r-c-e/index.md)


 - [`KaSymbolOrigin.JAVA_SOURCE`](../-ka-symbol-origin/-j-a-v-a_-s-o-u-r-c-e/index.md)


 - [`KaSymbolOrigin.JAVA_LIBRARY`](../-ka-symbol-origin/-j-a-v-a_-l-i-b-r-a-r-y/index.md)


 - [`KaSymbolOrigin.LIBRARY`](../-ka-symbol-origin/-l-i-b-r-a-r-y/index.md) (the [`psi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#psi) source element is taken from the generated Kotlin class file)


For other (usually synthetic) origins, the [`psi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#psi) might be `null` or non-null. The Analysis API makes no consistent guarantees about the PSI of such origins.

**See also**



 - [`realPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#realpsi)
 - [`anchorPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#anchorpsi)



</div>

</div>
### realPsi

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#realpsi">realPsi</a><span class="o">: </span>PsiElement<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A PsiElement explicitly present in the code (source or library). This PsiElement is sufficient to restore the symbol via the [`symbol`](../symbol.md) API without any additional information.

It can have a value only for the following [`origin`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#origin)s:

 - [`KaSymbolOrigin.SOURCE`](../-ka-symbol-origin/-s-o-u-r-c-e/index.md)


 - [`KaSymbolOrigin.JAVA_SOURCE`](../-ka-symbol-origin/-j-a-v-a_-s-o-u-r-c-e/index.md)


 - [`KaSymbolOrigin.LIBRARY`](../-ka-symbol-origin/-l-i-b-r-a-r-y/index.md)


 - [`KaSymbolOrigin.JAVA_LIBRARY`](../-ka-symbol-origin/-j-a-v-a_-l-i-b-r-a-r-y/index.md)


For all other [`origin`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#origin)s, the value is `null`.

**Examples:**

```kotlin
class MyClass
```

For this code, [`KaNamedClassSymbol`](../-ka-named-class-symbol/index.md) represents the class, while [`KaConstructorSymbol`](../-ka-constructor-symbol/index.md) represents the implicit constructor. The class is present in the code as a [`KtClassOrObject`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.md), and this is sufficient to obtain the same symbol. In contrast, the constructor is not present in the code and can only be obtained via the class, so [`realPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#realpsi) is `null` for it.

**See also**



 - [`anchorPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#anchorpsi)



</div>

</div>
### receiverParameter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">override </span><span class="kd">val </span><a href="index.html#receiverparameter">receiverParameter</a><span class="o">: </span><a href="../-ka-receiver-parameter-symbol/index.html">KaReceiverParameterSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`receiver parameter`](../-ka-receiver-parameter-symbol/index.md) of the callable, or `null` if the callable has no receiver.

The receiver parameter is present both for regular [`extensions`](../-ka-synthetic-java-property-symbol/index.md#isextension) and for [`companion extensions`](../-ka-synthetic-java-property-symbol/index.md#iscompanion).

**Example**

```kotlin
fun String.foo() {} // the receiver parameter is 'String'
companion fun String.bar() {} // the receiver parameter is also 'String'
```

<strong>Note</strong>: a companion extension is called on the class itself (`String.bar()`) and not on an instance of it, so its receiver parameter never gets an actual value.


</div>

</div>
### receiverType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../-ka-receiver-parameter-symbol/index.html#receivertype">receiverType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The [`receiver parameter`](../-ka-synthetic-java-property-symbol/index.md#receiverparameter)'s type, or `null` if the callable has no receiver.

**See also**



 - [`KaCallableSymbol.receiverParameter`](../-ka-synthetic-java-property-symbol/index.md#receiverparameter)



</div>

</div>
### returnType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../-ka-receiver-parameter-symbol/index.html#returntype">returnType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a>
</span></code></pre></div>
</div>


<div markdown>

The callable's return type. For variables, [`returnType`](../-ka-receiver-parameter-symbol/index.md#returntype) is the type of the variable.

Note: For a `vararg foo: T` parameter, the resulting type is the vararg element `T` type (unlike [`KtDeclaration.returnType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.md#returntype) from [`KaExpressionTypeProvider`](../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.md#returntype), which is the full `Array<out T>` type).

The reasoning behind this is that [`KaCallableSymbol.returnType`](../-ka-receiver-parameter-symbol/index.md#returntype) sees the parameter from the declaration's semantic perspective, representing the signature of the parameter, which contains just the element type. In this paradigm, `vararg` arrays are constructed separately under the hood.

At the same time [`KtDeclaration.returnType`](../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.md#returntype) from [`KaExpressionTypeProvider`](../../org.jetbrains.kotlin.analysis.api.components/-ka-expression-type-provider/index.md#returntype) represents a use-site perspective, which has to desugar `vararg` parameters because they are consumed as array types.


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
### typeParameters

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#typeparameters">typeParameters</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The declaration's type parameters.

See [Generics](https://kotlinlang.org/docs/generics.html)


</div>

</div>
### typeParameters

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="../-ka-receiver-parameter-symbol/index.html#typeparameters">typeParameters</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The declaration's type parameters provided it can have them. Otherwise, an empty list.

See [Generics](https://kotlinlang.org/docs/generics.html)


</div>

</div>
### visibility

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">override </span><span class="kd">val </span><a href="index.html#visibility">visibility</a><span class="o">: </span><a href="../-ka-symbol-visibility/index.html">KaSymbolVisibility</a>
</span></code></pre></div>
</div>


<div markdown>

The declaration's own [`KaSymbolVisibility`](../-ka-symbol-visibility/index.md) (e.g. `public`).

This is the visibility declared directly on the symbol itself, after applying all language rules and compiler plugins, <strong>but not</strong> taking into account the visibility of any containing declarations.

For example, a `public` function declared inside an `internal` class will still have [`KaSymbolVisibility.PUBLIC`](../-ka-symbol-visibility/-p-u-b-l-i-c/index.md) as its own visibility, even though it is not accessible from outside the module due to its containing class being `internal`.

**Example**

```kotlin
internal class InternalClass {
    fun implicitlyPublicFun() {}
    public fun explicitlyPublicFun() {}
}
```

In this example, both `implicitlyPublicFun` and `explicitlyPublicFun` have [`KaSymbolVisibility.PUBLIC`](../-ka-symbol-visibility/-p-u-b-l-i-c/index.md) as their own visibility (the default visibility in Kotlin), even though they are effectively only accessible within the same module because their containing class is `internal`.

To check whether a declaration is actually visible from a specific use-site (taking into account the visibility of all containing declarations), see [`KaUseSiteVisibilityChecker.isVisible`](../../org.jetbrains.kotlin.analysis.api.components/-ka-use-site-visibility-checker/index.md#isvisible).


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
### createPointer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#createpointer"><span class="nf">createPointer</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.pointers/-ka-symbol-pointer/index.html">KaSymbolPointer</a><span class="o"><</span><a href="index.html">KaLocalVariableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaSymbolPointer`](../../org.jetbrains.kotlin.analysis.api.symbols.pointers/-ka-symbol-pointer/index.md) which can be used to retrieve the symbol in a different [`analyze`](../../org.jetbrains.kotlin.analysis.api.session/analyze.md) block (i.e. a different [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)).


</div>

</div>
### [`findKDoc`](../../org.jetbrains.kotlin.analysis.api.kdoc/find-k-doc.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.kdoc/find-k-doc.html"><span class="nf">findKDoc</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.kdoc.psi.api/-k-doc-comment-descriptor/index.html">KDocCommentDescriptor</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Resolves KDoc for this [`KaDeclarationSymbol`](../-ka-declaration-symbol/index.md).


</div>

</div>
### getExpectsForActual

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="../-ka-receiver-parameter-symbol/index.html#getexpectsforactual"><span class="nf">getExpectsForActual</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns an `expect` symbol for the given `actual` symbol, if it is available. The function may return multiple `expect` symbols in case of ambiguity errors.


</div>

</div>
### implementationState

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../-ka-receiver-parameter-symbol/index.html#implementationstate"><span class="nf">implementationState</span></a><span class="p">(</span>implementerClassSymbol<span class="o">: </span><a href="../-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="../-ka-callable-implementation-state/index.html">KaCallableImplementationState</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the [`KaCallableImplementationState`](../-ka-callable-implementation-state/index.md) of the given [`KaCallableSymbol`](../-ka-callable-symbol/index.md) in the context of [`implementerClassSymbol`](../-ka-receiver-parameter-symbol/index.md#implementationstate).

Returns `null` if:

 - The symbol is a top-level callable;


 - The symbol is declared in a class or interface that is not a supertype of [`implementerClassSymbol`](../-ka-receiver-parameter-symbol/index.md#implementationstate);


 - If the symbol is non-implementable (for example, it is a [`KaConstructorSymbol`](../-ka-constructor-symbol/index.md), or a [`KaValueParameterSymbol`](../-ka-value-parameter-symbol/index.md)).


The implementation state describes whether a callable is already implemented, has an inherited implementation, can be overridden, or must be explicitly overridden in the given class.

**See also**



 - [`KaCallableImplementationState`](../-ka-callable-implementation-state/index.md)



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
### [`isVisibleInClass`](../../org.jetbrains.kotlin.analysis.api.visibility/is-visible-in-class.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/is-visible-in-class.html"><span class="nf">isVisibleInClass</span></a><span class="p">(</span>classSymbol<span class="o">: </span><a href="../-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks whether the given [`KaCallableSymbol`](../-ka-callable-symbol/index.md) (possibly inherited from a superclass) is visible in the given [`classSymbol`](../../org.jetbrains.kotlin.analysis.api.visibility/is-visible-in-class.md).


</div>

</div>
### psi

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#psi">PSI</a><span class="o"> : </span>PsiElement<span class="o">> </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#psi"><span class="nf">psi</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#psi">PSI</a>
</span></code></pre></div>
</div>


<div markdown>

<strong>The API is obsolete and will be deprecated soon. Use </strong>[`<strong>realPsi</strong>`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#realpsi)<strong> or </strong>[`<strong>anchorPsi</strong>`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#anchorpsi)<strong> instead.</strong>

Returns the symbol's PsiElement if its type is [`PSI`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#psi), and otherwise throws a [`ClassCastException`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-class-cast-exception/index.html).

**See also**



 - [`realPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#realpsi)
 - [`anchorPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#anchorpsi)



</div>

</div>
### psiSafe

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#psisafe">PSI</a><span class="o"> : </span>PsiElement<span class="o">> </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#psisafe"><span class="nf">psiSafe</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#psisafe">PSI</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

<strong>The API is obsolete and will be deprecated soon. Use </strong>[`<strong>realPsi</strong>`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#realpsi)<strong> or </strong>[`<strong>anchorPsi</strong>`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#anchorpsi)<strong> instead.</strong>

Returns the symbol's PsiElement if its type is [`PSI`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#psisafe), or `null` otherwise.

**See also**



 - [`realPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#realpsi)
 - [`anchorPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#anchorpsi)



</div>

</div>
### [`render`](../../org.jetbrains.kotlin.analysis.api.renderer/render.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.renderer/render.html"><span class="nf">render</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Renders the given [`KaDeclarationSymbol`](../-ka-declaration-symbol/index.md) to a string using the default rendering strategy ([`KaDeclarationRendererForSource.WITH_QUALIFIED_NAMES`](../../org.jetbrains.kotlin.analysis.api.renderer.declarations.impl/-ka-declaration-renderer-for-source/index.md#with_qualified_names)).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../-ka-declaration-symbol/index.html">KaDeclarationSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.renderer/render.html"><span class="nf">render</span></a><span class="p">(</span>renderer<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.renderer.declarations/-ka-declaration-renderer/index.html">KaDeclarationRenderer</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Renders the given [`KaDeclarationSymbol`](../-ka-declaration-symbol/index.md) to a string. The particular rendering strategy is defined by the [`renderer`](../../org.jetbrains.kotlin.analysis.api.renderer/render.md).


</div>

</div>
### sourcePsi

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#sourcepsi">PSI</a><span class="o"> : </span>PsiElement<span class="o">> </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#sourcepsi"><span class="nf">sourcePsi</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#sourcepsi">PSI</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

<strong>The API is obsolete and will be deprecated soon. Use </strong>[`<strong>realPsi</strong>`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#realpsi)<strong> or </strong>[`<strong>anchorPsi</strong>`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#anchorpsi)<strong> instead.</strong>

Returns the symbol's PsiElement. Returns `null` if its [`KaSymbol.origin`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#origin) is not [`KaSymbolOrigin.SOURCE`](../-ka-symbol-origin/-s-o-u-r-c-e/index.md). Throws a [`ClassCastException`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-class-cast-exception/index.html) if its type is not [`PSI`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#sourcepsi).

**See also**



 - [`realPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#realpsi)
 - [`anchorPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#anchorpsi)



</div>

</div>
### sourcePsiSafe

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><span class="kd">reified </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#sourcepsisafe">PSI</a><span class="o"> : </span>PsiElement<span class="o">> </span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#sourcepsisafe"><span class="nf">sourcePsiSafe</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.html#sourcepsisafe">PSI</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

<strong>The API is obsolete and will be deprecated soon. Use </strong>[`<strong>realPsi</strong>`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#realpsi)<strong> or </strong>[`<strong>anchorPsi</strong>`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#anchorpsi)<strong> instead.</strong>

Returns the symbol's PsiElement if its type is [`PSI`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#sourcepsisafe) and [`KaSymbol.origin`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#origin) is [`KaSymbolOrigin.SOURCE`](../-ka-symbol-origin/-s-o-u-r-c-e/index.md) or [`KaSymbolOrigin.JAVA_SOURCE`](../-ka-symbol-origin/-j-a-v-a_-s-o-u-r-c-e/index.md), and `null` otherwise.

**See also**



 - [`realPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#realpsi)
 - [`anchorPsi`](../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-named-symbol/index.md#anchorpsi)



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
