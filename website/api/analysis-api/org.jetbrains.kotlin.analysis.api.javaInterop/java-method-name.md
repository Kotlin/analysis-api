---
tags:
 - jvm
title: "javaMethodName"
---

# javaMethodName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="p">.</span><a href="java-method-name.html">javaMethodName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The visible Java method name for the given [`KaFunctionSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.md). The behavior is unspecified for modules other than the JVM.

The endpoint supports:

 - Mangling due to [`KaSymbolVisibility.INTERNAL`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-visibility/-i-n-t-e-r-n-a-l/index.md) modifier


 - [`JvmName`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-name/index.html)


The name is `null` when the symbol has no method that can be referenced from Java:

 - [`KaConstructorSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/index.md): constructors are neither renamed by [`JvmName`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-name/index.html) nor mangled, so there is no name to compute


 - [`KaSamConstructorSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-sam-constructor-symbol/index.md) and [`KaAnonymousFunctionSymbol`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-anonymous-function-symbol/index.md): there is no addressable JVM method


 - [`KaSymbolLocation.LOCAL`](../org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol-location/-l-o-c-a-l/index.md) declarations: their JVM names are invented during lowering and cannot be reconstructed from a symbol


 - Property accessors of a property without a name, of a `const` property, or of a property with a [`JvmField`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html) backing field, as no accessor method is generated in these cases


 - The computed name is not a valid Java identifier, such as for an escaped Kotlin name like `a b c`, as such a method cannot be referenced from Java code


 - The name is mangled because of value classes: the suffix is either a hash of the signature, as in `classFunInParameter-5lyY9Q4`, or `impl` for a member of a value class, as in `funWithoutParameters-impl`, and the endpoint computes neither



</div>

</div>
