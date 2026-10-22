---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.resolve.extensions"
---

# org.jetbrains.kotlin.analysis.api.resolve.extensions
## Types
### [`KaResolveExtension`](-ka-resolve-extension/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-ka-resolve-extension/index.html">KaResolveExtension</a> : Disposable
</span></code></pre></div>
</div>


<div markdown>

A resolve extension provides additional Kotlin files containing generated declarations, which will be included in the resolution as if they were regular source files in the module.


</div>

</div>
### [`KaResolveExtensionFile`](-ka-resolve-extension-file/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-ka-resolve-extension-file/index.html">KaResolveExtensionFile</a>
</span></code></pre></div>
</div>


<div markdown>

Represents a Kotlin file that contains generated declarations. It is provided by its [`resolve extension`](-ka-resolve-extension/index.md).


</div>

</div>
### [`KaResolveExtensionNavigationTargetsProvider`](-ka-resolve-extension-navigation-targets-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-ka-resolve-extension-navigation-targets-provider/index.html">KaResolveExtensionNavigationTargetsProvider</a>
</span></code></pre></div>
</div>

</div>
### [`KaResolveExtensionProvider`](-ka-resolve-extension-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="-ka-resolve-extension-provider/index.html">KaResolveExtensionProvider</a>
</span></code></pre></div>
</div>


<div markdown>

Provides [`resolve extensions`](-ka-resolve-extension/index.md) for [`KaModule`](../org.jetbrains.kotlin.analysis.api.projectStructure/-ka-module/index.md)s. Resolve extensions provide additional Kotlin files containing generated declarations, which will be included in the resolution as if they were regular source files in the module.


</div>

</div>
## Properties
### [`isFromResolveExtension`](is-from-resolve-extension.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="is-from-resolve-extension.html">isFromResolveExtension</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the given [`KtElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md) is provided by a [`KaResolveExtension`](-ka-resolve-extension/index.md).


</div>

</div>
### [`isResolveExtensionFile`](is-resolve-extension-file.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span>VirtualFile<span class="p">.</span><a href="is-resolve-extension-file.html">isResolveExtensionFile</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the given VirtualFile is provided by a [`KaResolveExtension`](-ka-resolve-extension/index.md).


</div>

</div>
### [`resolveExtensionNavigationElements`](resolve-extension-navigation-elements.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a><span class="p">.</span><a href="resolve-extension-navigation-elements.html">resolveExtensionNavigationElements</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span>PsiElement<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of PsiElements which are used as navigation targets in place of this [`KtElement`](../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md) provided by a [`KaResolveExtension`](-ka-resolve-extension/index.md).


</div>

</div>
### [`resolveExtensionScopeWithTopLevelDeclarations`](resolve-extension-scope-with-top-level-declarations.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">val </span><a href="resolve-extension-scope-with-top-level-declarations.html">resolveExtensionScopeWithTopLevelDeclarations</a><span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.html">KaScope</a>
</span></code></pre></div>
</div>


<div markdown>

The [`KaScope`](../org.jetbrains.kotlin.analysis.api.scopes/-ka-scope/index.md) containing top-level callable declarations generated by [`KaResolveExtension`](-ka-resolve-extension/index.md)s.


</div>

</div>
