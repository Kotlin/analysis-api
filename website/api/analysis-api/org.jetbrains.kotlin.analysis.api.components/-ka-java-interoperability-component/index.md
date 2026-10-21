---
tags:
 - jvm
title: "KaJavaInteroperabilityComponent"
---

# KaJavaInteroperabilityComponent

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaJavaInteroperabilityComponent</a> : <a href="../-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>#### Inheritors


 - [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)



</div>

## Properties
### callableSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span>PsiMember<span class="p">.</span><a href="index.html#callablesymbol">callableSymbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) for the given PsiMember method or field, or `null` for local declarations and Kotlin light classes.


</div>

</div>
### containingJvmClassName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="index.html#containingjvmclassname">containingJvmClassName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The containing JVM class name for the given [`KaCallableSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md).

The property works for both source and library declarations. The JVM class name is a fully qualified name separated by dots, such as `foo.bar.Baz.Companion`.

Applicable only to JVM modules, and common modules with JVM targets. [`containingJvmClassName`](index.md#containingjvmclassname) is always `null` all other kinds of modules.


</div>

</div>
### isPrimitiveBacked

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#isprimitivebacked">isPrimitiveBacked</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is backed by a single JVM primitive type.

This is `true` for non-nullable primitive types and for non-nullable inline value class types whose single underlying property is primitive-backed, recursively. It is `false` for nullable types, regular reference types, and types without a single primitive-backed representation.

Only the inline representation counts. A full value class is compiled as a regular class on the JVM, so it is never primitive-backed, even with exactly one primary property; see [`org.jetbrains.kotlin.analysis.api.symbols.KaNamedClassSymbol.isInline`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.md#isinline).

This property describes the type's underlying representation. It does not imply that every use of the type is emitted as a JVM primitive, as boxing can still be required by the use-site context.

For non-JVM modules, the result describes the equivalent JVM representation inferred from the Kotlin declaration.


</div>

</div>
### namedClassSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span>PsiClass<span class="p">.</span><a href="index.html#namedclasssymbol">namedClassSymbol</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaNamedClassSymbol`](../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.md) for the given PsiClass, or `null` for anonymous classes, local classes, type parameters (which are also PsiClasses), and Kotlin light classes.


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
### asKaType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span>PsiType<span class="p">.</span><a href="index.html#askatype"><span class="nf">asKaType</span></a><span class="p">(</span>useSitePosition<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given PsiType to a [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) in the context of the [`useSitePosition`](index.md#askatype).

[`useSitePosition`](index.md#askatype) clarifies how to resolve some parts of the PsiType. For instance, it can be used to collect type parameters and apply them during the conversion.

**Receiver**

The PsiType to be converted.

**Return**

The converted [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md), or `null` if conversion is not possible. For example, PsiType might not be resolvable.


</div>

</div>
### asPsiType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#aspsitype"><span class="nf">asPsiType</span></a><span class="p">(</span>
    useSitePosition<span class="o">: </span>PsiElement<span class="p">, </span>
    allowErrorTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    mode<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-mapping-mode/index.html">KaTypeMappingMode</a><span class="o"> = </span>KaTypeMappingMode.DEFAULT<span class="p">, </span>
    isAnnotationMethod<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span>
    suppressWildcards<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">?</span><span class="o"> = </span>null<span class="p">, </span>
    preserveAnnotations<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">, </span>
    allowNonJvmPlatforms<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span>
<span class="p">)</span><span class="o">: </span>PsiType<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a PsiType in the context of the [`useSitePosition`](index.md#aspsitype).

PsiType is JVM conception, so this method will return `null` for non-JVM platforms, unless [`allowNonJvmPlatforms`](index.md#aspsitype) is set.

**Receiver**

The [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to convert.

**Parameters**



 - useSitePosition: Determines whether the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) needs to be approximated. For instance, if the given type is local but the use site is in the same local scope, we do not need to approximate the local type. However, when exposed to the public as a return type, the resulting type must be approximated accordingly.


 - allowErrorTypes: Determines whether the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) should still be converted if it contains an error type. When this option is `false`, the result will be `null` if the [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) contains an error type. When `true`, erroneous types will be replaced with the `error.NonExistentClass` type.


 - suppressWildcards: Indicates whether wildcards in type arguments should be suppressed. This option works similar to adding a [`JvmSuppressWildcards`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html) annotation to the containing declaration.

 - `true` means they should be suppressed.


 - `false` means they should appear.


 - `null` means that the default applies, where wildcard suppression/appearance is determined by type annotations.



 - preserveAnnotations: Whether annotations from the original [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) should be included in the resulting PsiType with an appropriate conversion.


 - allowNonJvmPlatforms: Whether the PsiType should be computed even for non-JVM modules. The flag provides no validity guarantees – the returned type may be unresolvable from Java, or `null`.





</div>

</div>
### [`assertIsValidAndAccessible`](../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.md#assertisvalidandaccessible)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.lifetime/-ka-lifetime-owner/index.html">KaLifetimeOwner</a><span class="p">.</span><a href="../../org.jetbrains.kotlin.analysis.api.visibility/-ka-use-site-visibility-checker/index.html#assertisvalidandaccessible"><span class="nf">assertIsValidAndAccessible</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
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
### mapToJvmTypeDescriptor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="index.html#maptojvmtypedescriptor"><span class="nf">mapToJvmTypeDescriptor</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Convert the given [`KaType`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a JVM type descriptor with the [`KaTypeMappingMode.DEFAULT`](../../org.jetbrains.kotlin.analysis.api.types/-ka-type-mapping-mode/-d-e-f-a-u-l-t/index.md). To learn more about JVM descriptors, check out the [JVM specification](https://docs.oracle.com/javase/specs/jvms/se24/html/jvms-4.html#jvms-4.3).


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
