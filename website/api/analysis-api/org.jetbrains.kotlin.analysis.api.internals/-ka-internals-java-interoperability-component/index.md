---
tags:
 - jvm
title: "KaInternalsJavaInteroperabilityComponent"
---

# KaInternalsJavaInteroperabilityComponent

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaInternalsJavaInteroperabilityComponent</a>
</span></code></pre></div>
</div>

## Functions
### asFacadePsiClass

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#asfacadepsiclass"><span class="nf">asFacadePsiClass</span></a><span class="p">(</span>fileSymbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="p">)</span><span class="o">: </span>PsiClass<span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#asfacadepsiclass"><span class="nf">asFacadePsiClass</span></a><span class="p">(</span>scriptSymbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-script-symbol/index.html">KaScriptSymbol</a><span class="p">)</span><span class="o">: </span>PsiClass<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### asKaType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#askatype"><span class="nf">asKaType</span></a><span class="p">(</span>psiType<span class="o">: </span>PsiType<span class="p">, </span>useSitePosition<span class="o">: </span>PsiElement<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### asPsiClass

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#aspsiclass"><span class="nf">asPsiClass</span></a><span class="p">(</span>classSymbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span>PsiClass<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### asPsiField

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#aspsifield"><span class="nf">asPsiField</span></a><span class="p">(</span>backingFieldSymbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-backing-field-symbol/index.html">KaBackingFieldSymbol</a><span class="p">)</span><span class="o">: </span>PsiField<span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#aspsifield"><span class="nf">asPsiField</span></a><span class="p">(</span>classSymbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/index.html">KaClassSymbol</a><span class="p">)</span><span class="o">: </span>PsiField<span class="o">?</span>
</span></code></pre></div>
</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#aspsifield"><span class="nf">asPsiField</span></a><span class="p">(</span>enumEntrySymbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-enum-entry-symbol/index.html">KaEnumEntrySymbol</a><span class="p">)</span><span class="o">: </span>PsiEnumConstant<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### asPsiMethods

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#aspsimethods"><span class="nf">asPsiMethods</span></a><span class="p">(</span>functionSymbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>PsiMethod<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### asPsiParameters

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#aspsiparameters"><span class="nf">asPsiParameters</span></a><span class="p">(</span>parameterSymbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-parameter-symbol/index.html">KaParameterSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>PsiParameter<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### asPsiType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#aspsitype"><span class="nf">asPsiType</span></a><span class="p">(</span>
    type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">, </span>
    useSitePosition<span class="o">: </span>PsiElement<span class="p">, </span>
    allowErrorTypes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    mode<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type-mapping-mode/index.html">KaTypeMappingMode</a><span class="p">, </span>
    isAnnotationMethod<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    suppressWildcards<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o">?</span><span class="p">, </span>
    preserveAnnotations<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    allowNonJvmPlatforms<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
<span class="p">)</span><span class="o">: </span>PsiType<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### asPsiTypeParameters

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#aspsitypeparameters"><span class="nf">asPsiTypeParameters</span></a><span class="p">(</span>typeParameterSymbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span>PsiTypeParameter<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### callableSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#callablesymbol"><span class="nf">callableSymbol</span></a><span class="p">(</span>psiMember<span class="o">: </span>PsiMember<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### containingJvmClassName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#containingjvmclassname"><span class="nf">containingJvmClassName</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### isPrimitiveBacked

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#isprimitivebacked"><span class="nf">isPrimitiveBacked</span></a><span class="p">(</span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>

</div>
### javaGetterName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#javagettername"><span class="nf">javaGetterName</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-property-symbol/index.html">KaPropertySymbol</a><span class="p">)</span><span class="o">: </span>Name
</span></code></pre></div>
</div>

</div>
### javaMethodName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#javamethodname"><span class="nf">javaMethodName</span></a><span class="p">(</span>function<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/index.html">KaFunctionSymbol</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### javaSetterName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#javasettername"><span class="nf">javaSetterName</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-property-symbol/index.html">KaPropertySymbol</a><span class="p">)</span><span class="o">: </span>Name<span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### mapToJvmTypeDescriptor

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#maptojvmtypedescriptor"><span class="nf">mapToJvmTypeDescriptor</span></a><span class="p">(</span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### namedClassSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#namedclasssymbol"><span class="nf">namedClassSymbol</span></a><span class="p">(</span>psiClass<span class="o">: </span>PsiClass<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
