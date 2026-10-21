---
tags:
 - jvm
title: "Builder"
---

# Builder

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">Builder</a>
</span></code></pre></div>
</div>

## Constructors
### Builder

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### keywordsRenderer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">lateinit </span><span class="kd">var </span><a href="index.html#keywordsrenderer">keywordsRenderer</a><span class="o">: </span><a href="../../../org.jetbrains.kotlin.analysis.api.renderer.base/-ka-keywords-renderer/index.html">KaKeywordsRenderer</a>
</span></code></pre></div>
</div>

</div>
### modalityProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">lateinit </span><span class="kd">var </span><a href="index.html#modalityprovider">modalityProvider</a><span class="o">: </span><a href="../../../org.jetbrains.kotlin.analysis.api.renderer.declarations.modifiers.renderers/-ka-renderer-modality-modifier-provider/index.html">KaRendererModalityModifierProvider</a>
</span></code></pre></div>
</div>

</div>
### modifierListRenderer

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">lateinit </span><span class="kd">var </span><a href="index.html#modifierlistrenderer">modifierListRenderer</a><span class="o">: </span><a href="../../../org.jetbrains.kotlin.analysis.api.renderer.declarations.modifiers.renderers/-ka-modifier-list-renderer/index.html">KaModifierListRenderer</a>
</span></code></pre></div>
</div>

</div>
### modifiersSorter

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">lateinit </span><span class="kd">var </span><a href="index.html#modifierssorter">modifiersSorter</a><span class="o">: </span><a href="../../../org.jetbrains.kotlin.analysis.api.renderer.declarations.modifiers.renderers/-ka-modifiers-sorter/index.html">KaModifiersSorter</a>
</span></code></pre></div>
</div>

</div>
### otherModifiersProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">lateinit </span><span class="kd">var </span><a href="index.html#othermodifiersprovider">otherModifiersProvider</a><span class="o">: </span><a href="../../../org.jetbrains.kotlin.analysis.api.renderer.declarations.modifiers.renderers/-ka-renderer-other-modifiers-provider/index.html">KaRendererOtherModifiersProvider</a>
</span></code></pre></div>
</div>

</div>
### visibilityProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">lateinit </span><span class="kd">var </span><a href="index.html#visibilityprovider">visibilityProvider</a><span class="o">: </span><a href="../../../org.jetbrains.kotlin.analysis.api.renderer.declarations.modifiers.renderers/-ka-renderer-visibility-modifier-provider/index.html">KaRendererVisibilityModifierProvider</a>
</span></code></pre></div>
</div>

</div>
## Functions
### build

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#build"><span class="nf">build</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../index.html">KaDeclarationModifiersRenderer</a>
</span></code></pre></div>
</div>

</div>
