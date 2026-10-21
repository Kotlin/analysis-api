---
tags:
 - jvm
title: "KaAdditionalKDocResolutionProvider"
---

# KaAdditionalKDocResolutionProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KaAdditionalKDocResolutionProvider</a>
</span></code></pre></div>An extension point to provide additional symbols for a KDoc reference. KDoc link resolution will use symbols returned by this extension point only if the real resolution was unsuccessful.

#### Example
Let's assume that you want to return symbol `fun foo() = 3` for the following KDoc resolution:

```
package com.example

fun foo() = 3

/**
 * [this.is.not.com.example.fo<caret>o] is not the above `com.example.foo`, but you want to resolve it to the above `com.example.foo`.
*/
fun bar() = 7
```

You can create the following provider:

```kotlin
class KaAdditionalKDocResolutionProviderBasedOnNameMatch : KaAdditionalKDocResolutionProvider {
  override fun resolveKdocFqName(analysisSession: KaSession, fqName: FqName, contextElement: KtElement): Collection<KaSymbol> =
    contextElement.containingKtFile.declarations.filter { it.name == fqName.shortName().asString() }.map { it.getSymbol() }
}
```

The extension point name is `org.jetbrains.kotlin.kaAdditionalKDocResolutionProvider`.


</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Functions
### resolveKdocFqName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#resolvekdocfqname"><span class="nf">resolveKdocFqName</span></a><span class="p">(</span>
    analysisSession<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">, </span>
    fqName<span class="o">: </span>FqName<span class="p">, </span>
    contextElement<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-element/index.html">KtElement</a>
<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html">Collection</a><span class="o"><</span><a href="../-ka-symbol/index.html">KaSymbol</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns additional symbols for the given [`contextElement`](index.md#resolvekdocfqname) in KDoc.


</div>

</div>
