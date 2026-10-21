---
tags:
 - jvm
title: "KaInternalsScopeProvider"
---

# KaInternalsScopeProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-subclass-opt-in-required/index.html"><span class="se">SubclassOptInRequired</span></a><span class="p">(</span>markerClass<span class="o"> = </span><span class="p">[</span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-implementation-detail/index.html">KaImplementationDetail::class</a><span class="p">]</span><span class="p">)</span>
<span class="kd">interface </span><a href="index.html">KaInternalsScopeProvider</a>
</span></code></pre></div>
</div>

## Functions
### asCompositeScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#ascompositescope"><span class="nf">asCompositeScope</span></a><span class="p">(</span>scopes<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a><span class="o">></span><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>

</div>
### combinedDeclaredMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#combineddeclaredmemberscope"><span class="nf">combinedDeclaredMemberScope</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>

</div>
### combinedMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#combinedmemberscope"><span class="nf">combinedMemberScope</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>

</div>
### compositeScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#compositescope"><span class="nf">compositeScope</span></a><span class="p">(</span>scopeContext<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-context/index.html">KaScopeContext</a><span class="p">, </span>filter<span class="o">: </span><span class="p">(</span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-kind/index.html">KaScopeKind</a><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>

</div>
### declarationScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#declarationscope"><span class="nf">declarationScope</span></a><span class="p">(</span>typeScope<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.html">KaTypeScope</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>

</div>
### declaredMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#declaredmemberscope"><span class="nf">declaredMemberScope</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>

</div>
### delegatedMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#delegatedmemberscope"><span class="nf">delegatedMemberScope</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>

</div>
### fileScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#filescope"><span class="nf">fileScope</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-file-symbol/index.html">KaFileSymbol</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>

</div>
### importingScopeContext

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#importingscopecontext"><span class="nf">importingScopeContext</span></a><span class="p">(</span>file<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-context/index.html">KaScopeContext</a>
</span></code></pre></div>
</div>

</div>
### memberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#memberscope"><span class="nf">memberScope</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>

</div>
### packageScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#packagescope"><span class="nf">packageScope</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-package-symbol/index.html">KaPackageSymbol</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>

</div>
### scope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#scope"><span class="nf">scope</span></a><span class="p">(</span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.html">KaTypeScope</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### scopeContext

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#scopecontext"><span class="nf">scopeContext</span></a><span class="p">(</span>file<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>position<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.components/-ka-scope-context/index.html">KaScopeContext</a>
</span></code></pre></div>
</div>

</div>
### staticDeclaredMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#staticdeclaredmemberscope"><span class="nf">staticDeclaredMemberScope</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>

</div>
### staticMemberScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#staticmemberscope"><span class="nf">staticMemberScope</span></a><span class="p">(</span>symbol<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols.markers/-ka-declaration-container-symbol/index.html">KaDeclarationContainerSymbol</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>

</div>
### syntheticJavaPropertiesScope

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#syntheticjavapropertiesscope"><span class="nf">syntheticJavaPropertiesScope</span></a><span class="p">(</span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.scopes/-ka-type-scope/index.html">KaTypeScope</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
