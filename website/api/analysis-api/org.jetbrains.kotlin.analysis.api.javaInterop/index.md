---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.javaInterop"
---

# org.jetbrains.kotlin.analysis.api.javaInterop
## Types
### [`KaElementJavaView`](-ka-element-java-view/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-element-java-view/index.html">KaElementJavaView</a>
</span></code></pre></div>
</div>


<div markdown>

A view on Kotlin [`KtElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md)s from Java perspective.


</div>

</div>
### [`KaSymbolJavaView`](-ka-symbol-java-view/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="-ka-symbol-java-view/index.html">KaSymbolJavaView</a><span class="o"><</span><span class="kd">out </span><a href="-ka-symbol-java-view/index.html">T</a><span class="o"> : </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.html">KaSymbol</a><span class="o">></span> : <a href="-ka-element-java-view/index.html">KaElementJavaView</a>
</span></code></pre></div>
</div>


<div markdown>

A view on Kotlin [`KaSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md)s from Java perspective.


</div>

</div>
## Properties
### [`callableSymbol`](callable-symbol.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span>PsiMember<span class="p">.</span><a href="callable-symbol.html">callableSymbol</a><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaCallableSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md) for the given PsiMember method or field, or `null` for local declarations and Kotlin light classes.


</div>

</div>
### [`containingJvmClassName`](containing-jvm-class-name.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">.</span><a href="containing-jvm-class-name.html">containingJvmClassName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The containing JVM class name for the given [`KaCallableSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.md).


</div>

</div>
### [`isPrimitiveBacked`](is-primitive-backed.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="is-primitive-backed.html">isPrimitiveBacked</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the given [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) is backed by a single JVM primitive type.


</div>

</div>
### [`javaMethodName`](java-method-name.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="p">.</span><a href="java-method-name.html">javaMethodName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The visible Java method name for the given [`KaFunctionSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md). The behavior is unspecified for modules other than the JVM.


</div>

</div>
### [`namedClassSymbol`](named-class-symbol.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span>PsiClass<span class="p">.</span><a href="named-class-symbol.html">namedClassSymbol</a><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaNamedClassSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.md) for the given PsiClass, or `null` for anonymous classes, local classes, type parameters (which are also PsiClasses), and Kotlin light classes.


</div>

</div>
## Functions
### [`asFacadePsiClass`](as-facade-psi-class.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="p">.</span><a href="as-facade-psi-class.html"><span class="nf">asFacadePsiClass</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiClass<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaFileSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.md) to Java facade PsiClass in the context of the [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md).


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


</div>

</div>
### [`asKaType`](as-ka-type.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span>PsiType<span class="p">.</span><a href="as-ka-type.html"><span class="nf">asKaType</span></a><span class="p">(</span>useSitePosition<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given PsiType to a [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) in the context of the [`useSitePosition`](as-ka-type.md).


</div>

</div>
### [`asPsiClass`](as-psi-class.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">.</span><a href="as-psi-class.html"><span class="nf">asPsiClass</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiClass<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaClassSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.md) to Java PsiClass in the context of the [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md).


</div>

</div>
### [`asPsiField`](as-psi-field.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-backing-field-symbol/index.html">KaBackingFieldSymbol</a><span class="p">.</span><a href="as-psi-field.html"><span class="nf">asPsiField</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>PsiField<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaBackingFieldSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-backing-field-symbol/index.md) to Java PsiField in the context of the [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md).


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


</div>

</div>
### [`asPsiMethods`](as-psi-methods.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="p">.</span><a href="as-psi-methods.html"><span class="nf">asPsiMethods</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>PsiMethod<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaFunctionSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md) to Java PsiMethods in the context of the [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md).


</div>

</div>
### [`asPsiParameters`](as-psi-parameters.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-parameter-symbol/index.html">KaParameterSymbol</a><span class="p">.</span><a href="as-psi-parameters.html"><span class="nf">asPsiParameters</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>PsiParameter<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaParameterSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-parameter-symbol/index.md) to Java PsiParameters in the context of the [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md).


</div>

</div>
### [`asPsiTypeParameters`](as-psi-type-parameters.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">.</span><a href="as-psi-type-parameters.html"><span class="nf">asPsiTypeParameters</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>PsiTypeParameter<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaTypeParameterSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.md) to Java PsiTypeParameters in the context of the [`useSiteModule`](../../analysis-api/org.jetbrains.kotlin.analysis.api/index.md).


</div>

</div>
### [`mapToJvmTypeDescriptor`](map-to-jvm-type-descriptor.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="map-to-jvm-type-descriptor.html"><span class="nf">mapToJvmTypeDescriptor</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Convert the given [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a JVM type descriptor with the [`KaTypeMappingMode.DEFAULT`](../org.jetbrains.kotlin.analysis.api.types/-ka-type-mapping-mode/-d-e-f-a-u-l-t/index.md). To learn more about JVM descriptors, check out the [JVM specification](https://docs.oracle.com/javase/specs/jvms/se24/html/jvms-4.html#jvms-4.3).


</div>

</div>
