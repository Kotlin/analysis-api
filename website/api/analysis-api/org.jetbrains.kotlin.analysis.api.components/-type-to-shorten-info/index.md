---
tags:
 - jvm
title: "TypeToShortenInfo"
---

# TypeToShortenInfo

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">class </span><a href="index.html">TypeToShortenInfo</a><span class="p">(</span><span class="kd">val </span>typeToShorten<span class="o">: </span>SmartPsiElementPointer<span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-user-type/index.html">KtUserType</a><span class="o">></span><span class="p">, </span><span class="kd">val </span>shortenedReference<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">)</span>
</span></code></pre></div>A class to keep a [`KtUserType`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-user-type/index.md) to shorten and what shape the shortened result has to be. [`shortenedReference`](index.md#shortenedreference) is the expected result of shortening in a string form. If [`shortenedReference`](index.md#shortenedreference) is null, it means the shortening will simply delete the qualifier. Note that currently the only usage of [`shortenedReference`](index.md#shortenedreference) is the case we have the import-alias. For example, [`shortenedReference`](index.md#shortenedreference) will be "AliasType" when we shorten:

```
import my.package.NewType as AliasType
... my.package.Ne<caret>wType ... // -> we can replace this with `AliasType`.
```


</div>

## Constructors
### TypeToShortenInfo

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>typeToShorten<span class="o">: </span>SmartPsiElementPointer<span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-user-type/index.html">KtUserType</a><span class="o">></span><span class="p">, </span>shortenedReference<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Properties
### shortenedReference

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#shortenedreference">shortenedReference</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>

</div>
### typeToShorten

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#typetoshorten">typeToShorten</a><span class="o">: </span>SmartPsiElementPointer<span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-user-type/index.html">KtUserType</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
