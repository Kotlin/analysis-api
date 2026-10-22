---
tags:
 - jvm
title: "KaSymbolProvider"
---

# KaSymbolProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-session-component-implementation-detail/index.html">KaSessionComponentImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaSymbolProvider</a> : <a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-session-component/index.html">KaSessionComponent</a>
</span></code></pre></div>[`KaSymbolProvider`](index.md) provides [`KaSymbol`](../-ka-symbol/index.md)s for given PSI elements.

<strong>Important</strong>: Symbols can be created only for elements which are a part of the current [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md).

#### See also


 - [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)


#### Inheritors


 - [`KaSession`](../../org.jetbrains.kotlin.analysis.api/-ka-session/index.md)



</div>

## Properties
### classSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">.</span><a href="index.html#classsymbol">classSymbol</a><span class="o">: </span><a href="../-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaClassSymbol`](../-ka-class-symbol/index.md) for the given [`KtClassOrObject`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.md), or `null` for [`KtEnumEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry/index.md) declarations.

To retrieve a [`KaEnumEntrySymbol`](../-ka-enum-entry-symbol/index.md), please refer to [`KtEnumEntry.symbol`](index.md#symbol).


</div>

</div>
### namedClassSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="p">.</span><a href="index.html#namedclasssymbol">namedClassSymbol</a><span class="o">: </span><a href="../-ka-named-class-symbol/index.html">KaNamedClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A [`KaNamedClassSymbol`](../-ka-named-class-symbol/index.md) for the given named [`KtClassOrObject`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.md), or `null` for [`KtEnumEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry/index.md) declarations and object literals.


</div>

</div>
### rootPackageSymbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#rootpackagesymbol">rootPackageSymbol</a><span class="o">: </span><a href="../-ka-package-symbol/index.html">KaPackageSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaPackageSymbol`](../-ka-package-symbol/index.md) for the root package, which is the special package with an empty fully-qualified name.


</div>

</div>
### symbol

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.html">KtDeclaration</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-declaration-symbol/index.html">KaDeclarationSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaDeclarationSymbol`](../-ka-declaration-symbol/index.md) for the given [`KtDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md).

There are more specific `symbol` endpoints, such as [`KtNamedFunction.symbol`](index.md#symbol) and [`KtClassOrObject.classSymbol`](index.md#classsymbol), which can be used when more specific PSI elements are available.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-parameter/index.html">KtParameter</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaVariableSymbol`](../-ka-variable-symbol/index.md) for the given [`KtParameter`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-parameter/index.md).

Unfortunately, [`KtParameter`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-parameter/index.md) in PSI stands for many things, and not all of them are represented by a single type of symbol, so this function does not work for all possible [`KtParameter`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-parameter/index.md)s.

If [`KtParameter.isFunctionTypeParameter`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-parameter/is-function-type-parameter.md) is `true`, i.e. if the given [`KtParameter`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-parameter/index.md) is used as a function type parameter, it is not possible to create [`KaValueParameterSymbol`](../-ka-value-parameter-symbol/index.md), hence an error will be raised.

If [`KtParameter.isLoopParameter`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-parameter/is-loop-parameter.md) is `true`, i.e. if the given [`KtParameter`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-parameter/index.md) is a loop variable in `for` expression, then the symbol is [`KaLocalVariableSymbol`](../-ka-local-variable-symbol/index.md).

If [`KtParameter.isContextParameter`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-parameter/is-context-parameter.md) is `true`, i.e. if the given [`KtParameter`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-parameter/index.md) is used as a context parameter, then the symbol is [`KaContextParameterSymbol`](../-ka-context-parameter-symbol/index.md).

Otherwise, the symbol is [`KaValueParameterSymbol`](../-ka-value-parameter-symbol/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-named-function/index.html">KtNamedFunction</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-function-symbol/index.html">KaFunctionSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaFunctionSymbol`](../-ka-function-symbol/index.md) for the given [`KtNamedFunction`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-named-function/index.md).

If [`KtNamedFunction.getName`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-named-function/get-name.md) is `null`, the symbol is a [`KaAnonymousFunctionSymbol`](../-ka-anonymous-function-symbol/index.md), and otherwise a [`KaNamedFunctionSymbol`](../-ka-named-function-symbol/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor/index.html">KtConstructor</a><span class="o"><</span><span class="o">*</span><span class="o">></span><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-constructor-symbol/index.html">KaConstructorSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaConstructorSymbol`](../-ka-constructor-symbol/index.md) for the given [`KtConstructor`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-constructor/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-parameter/index.html">KtTypeParameter</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-type-parameter-symbol/index.html">KaTypeParameterSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeParameterSymbol`](../-ka-type-parameter-symbol/index.md) for the given [`KtTypeParameter`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-parameter/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-alias/index.html">KtTypeAlias</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-type-alias-symbol/index.html">KaTypeAliasSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaTypeAliasSymbol`](../-ka-type-alias-symbol/index.md) for the given [`KtTypeAlias`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-alias/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry/index.html">KtEnumEntry</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-enum-entry-symbol/index.html">KaEnumEntrySymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaEnumEntrySymbol`](../-ka-enum-entry-symbol/index.md) for the given [`KtEnumEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-enum-entry/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-function-literal/index.html">KtFunctionLiteral</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-anonymous-function-symbol/index.html">KaAnonymousFunctionSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaAnonymousFunctionSymbol`](../-ka-anonymous-function-symbol/index.md) for the given [`KtFunctionLiteral`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-function-literal/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-property/index.html">KtProperty</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaVariableSymbol`](../-ka-variable-symbol/index.md) for the given [`KtProperty`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-property/index.md).

The symbol is a [`KaKotlinPropertySymbol`](../-ka-kotlin-property-symbol/index.md) for non-local properties, and a [`KaLocalVariableSymbol`](../-ka-local-variable-symbol/index.md) for local ones.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-backing-field/index.html">KtBackingField</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-backing-field-symbol/index.html">KaBackingFieldSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaBackingFieldSymbol`](../-ka-backing-field-symbol/index.md) for the given [`KtBackingField`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-backing-field/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-object-literal-expression/index.html">KtObjectLiteralExpression</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-anonymous-object-symbol/index.html">KaAnonymousObjectSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaAnonymousObjectSymbol`](../-ka-anonymous-object-symbol/index.md) for the given [`KtObjectLiteralExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-object-literal-expression/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-object-declaration/index.html">KtObjectDeclaration</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-class-symbol/index.html">KaClassSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaClassSymbol`](../-ka-class-symbol/index.md) for the given [`KtObjectDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-object-declaration/index.md).

The symbol may either be a [`KaAnonymousObjectSymbol`](../-ka-anonymous-object-symbol/index.md) if the given declaration is an [object expression](https://kotlinlang.org/docs/object-declarations.html#object-expressions), or a [`KaNamedClassSymbol`](../-ka-named-class-symbol/index.md) if it is a named object declaration.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-accessor/index.html">KtPropertyAccessor</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-property-accessor-symbol/index.html">KaPropertyAccessorSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaPropertyAccessorSymbol`](../-ka-property-accessor-symbol/index.md) for the given [`KtPropertyAccessor`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-property-accessor/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-initializer/index.html">KtClassInitializer</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-class-initializer-symbol/index.html">KaClassInitializerSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaClassInitializerSymbol`](../-ka-class-initializer-symbol/index.md) for the given [`KtClassInitializer`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-initializer/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.html">KtDestructuringDeclarationEntry</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-variable-symbol/index.html">KaVariableSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaVariableSymbol`](../-ka-variable-symbol/index.md) that corresponds to the local variable introduced by the given [`KtDestructuringDeclarationEntry`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration-entry/index.md).

The symbol is usually a [`KaLocalVariableSymbol`](../-ka-local-variable-symbol/index.md). However, for a top-level destructuring declaration in a script, the symbol is a [`KaKotlinPropertySymbol`](../-ka-kotlin-property-symbol/index.md).

**Example**

```kotlin
val (x, y) = p
```

The destructuring declaration above has two entries, one corresponding to `x` and another to `y`. For both of these entries, we can retrieve a [`KaVariableSymbol`](../-ka-variable-symbol/index.md) which describes the entry.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration/index.html">KtDestructuringDeclaration</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-destructuring-declaration-symbol/index.html">KaDestructuringDeclarationSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaDestructuringDeclarationSymbol`](../-ka-destructuring-declaration-symbol/index.md) for the given [`KtDestructuringDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-destructuring-declaration/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-file-symbol/index.html">KaFileSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaFileSymbol`](../-ka-file-symbol/index.md) for a [`KtFile`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-script/index.html">KtScript</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-script-symbol/index.html">KaScriptSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

A [`KaScriptSymbol`](../-ka-script-symbol/index.md) for a [`KtScript`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-script/index.md).


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-context-receiver/index.html">KtContextReceiver</a><span class="p">.</span><a href="index.html#symbol">symbol</a><span class="o">: </span><a href="../-ka-context-parameter-symbol/index.html">KaContextParameterSymbol</a>
</span></code></pre></div>
</div>


<div markdown>

Represents [`KtContextReceiver`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-context-receiver/index.md) as a [`KaContextParameterSymbol`](../-ka-context-parameter-symbol/index.md).

This is a temporary API for simplicity during the transition from context receivers to context parameters.

<strong>Note</strong>: context receivers inside [`KtFunctionType`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-function-type/index.md) are not supported.


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
### findClass

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#findclass"><span class="nf">findClass</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="../-ka-class-symbol/index.html">KaClassSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaClassSymbol`](../-ka-class-symbol/index.md) for the specified ClassId, or `null` if such a symbol cannot be found.


</div>

</div>
### findClassLike

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#findclasslike"><span class="nf">findClassLike</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="../-ka-class-like-symbol/index.html">KaClassLikeSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaClassLikeSymbol`](../-ka-class-like-symbol/index.md) for the specified ClassId, or `null` if such a symbol cannot be found.

The function combines both class search (see [`findClass`](index.md#findclass)) and type alias search (see [`findTypeAlias`](index.md#findtypealias)).


</div>

</div>
### findPackage

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#findpackage"><span class="nf">findPackage</span></a><span class="p">(</span>fqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="../-ka-package-symbol/index.html">KaPackageSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaPackageSymbol`](../-ka-package-symbol/index.md) corresponding to the given [`fqName`](index.md#findpackage) if that package exists and is visible from the current use site, or `null` otherwise.


</div>

</div>
### findTopLevelCallables

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#findtoplevelcallables"><span class="nf">findTopLevelCallables</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">, </span>name<span class="o">: </span>Name<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence/index.html">Sequence</a><span class="o"><</span><a href="../-ka-callable-symbol/index.html">KaCallableSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Finds top-level functions and properties called [`name`](index.md#findtoplevelcallables) in the package called [`packageFqName`](index.md#findtoplevelcallables). Returns only symbols that are visible from the current use-site module.


</div>

</div>
### findTypeAlias

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#findtypealias"><span class="nf">findTypeAlias</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="../-ka-type-alias-symbol/index.html">KaTypeAliasSymbol</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KaTypeAliasSymbol`](../-ka-type-alias-symbol/index.md) for the specified ClassId, or `null` if such a symbol cannot be found.


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
