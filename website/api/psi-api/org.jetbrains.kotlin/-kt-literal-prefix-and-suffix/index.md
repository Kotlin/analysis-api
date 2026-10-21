---
tags:
 - jvm
title: "KtLiteralPrefixAndSuffix"
---

# KtLiteralPrefixAndSuffix

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">KtLiteralPrefixAndSuffix</a>
</span></code></pre></div>The rule that a literal may not be glued to the token next to it, as in `a foo"bar"` or `1in a`.

The rule is checked once per tree shape: `FirPrefixAndSuffixSyntaxChecker` walks the PSI, while for the light tree the check rides along with the walk `KotlinLightParser` already makes over the freshly parsed tree. Only the walk differs between the two, so what a literal is and which neighbours are prohibited is kept here.


</div>

## Properties
### relevantLiteralTypes

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#relevantliteraltypes">relevantLiteralTypes</a><span class="o">: </span>TokenSet
</span></code></pre></div>
</div>


<div markdown>

The literal expressions the rule applies to.


</div>

</div>
## Functions
### isProhibitedPrefixOrSuffix

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="index.html#isprohibitedprefixorsuffix"><span class="nf">isProhibitedPrefixOrSuffix</span></a><span class="p">(</span>tokenType<span class="o">: </span>IElementType<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether a token of type [`tokenType`](index.md#isprohibitedprefixorsuffix) may not directly touch a literal. Any other token, whitespace and comments included, separates the two.


</div>

</div>
