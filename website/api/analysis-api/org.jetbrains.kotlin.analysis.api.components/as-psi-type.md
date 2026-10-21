---
tags:
 - jvm
title: "asPsiType"
---

# asPsiType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">.</span><a href="as-psi-type.html"><span class="nf">asPsiType</span></a><span class="p">(</span>
    useSitePosition<span class="o">: </span>PsiElement<span class="p">, </span>
    allowErrorTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    mode<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.types/-ka-type-mapping-mode/index.html">KaTypeMappingMode</a><span class="o"> = </span>KaTypeMappingMode.DEFAULT<span class="p">, </span>
    isAnnotationMethod<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span>
    suppressWildcards<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">?</span><span class="o"> = </span>null<span class="p">, </span>
    preserveAnnotations<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">true</span><span class="p">, </span>
    allowNonJvmPlatforms<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span>
<span class="p">)</span><span class="o">: </span>PsiType<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Converts the given [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to a PsiType in the context of the [`useSitePosition`](as-psi-type.md).

PsiType is JVM conception, so this method will return `null` for non-JVM platforms, unless [`allowNonJvmPlatforms`](as-psi-type.md) is set.

#### Receiver
The [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) to convert.

#### Parameters


 - useSitePosition: Determines whether the given [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) needs to be approximated. For instance, if the given type is local but the use site is in the same local scope, we do not need to approximate the local type. However, when exposed to the public as a return type, the resulting type must be approximated accordingly.


 - allowErrorTypes: Determines whether the [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) should still be converted if it contains an error type. When this option is `false`, the result will be `null` if the [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) contains an error type. When `true`, erroneous types will be replaced with the `error.NonExistentClass` type.


 - suppressWildcards: Indicates whether wildcards in type arguments should be suppressed. This option works similar to adding a [`JvmSuppressWildcards`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html) annotation to the containing declaration.

 - `true` means they should be suppressed.


 - `false` means they should appear.


 - `null` means that the default applies, where wildcard suppression/appearance is determined by type annotations.



 - preserveAnnotations: Whether annotations from the original [`KaType`](../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md) should be included in the resulting PsiType with an appropriate conversion.


 - allowNonJvmPlatforms: Whether the PsiType should be computed even for non-JVM modules. The flag provides no validity guarantees – the returned type may be unresolvable from Java, or `null`.





</div>

</div>
