---
tags:
 - jvm
title: "KtImportInfo"
---

# KtImportInfo

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KtImportInfo</a>
</span></code></pre></div>A representation-agnostic view of a single import statement.

The same information is available whether the import is backed by a full [`KtImportDirective`](../-kt-import-directive/index.md) PSI element or by a lightweight stub, so consumers that only need the imported name, alias, or all-under flag can work uniformly against either representation.

### Example:
```kotlin
import kotlin.collections.List as KList  // importedFqName = kotlin.collections.List, aliasName = "KList"
import kotlin.collections.*              // isAllUnder = true
```

#### Inheritors


 - [`KtImportDirective`](../-kt-import-directive/index.md)



</div>

## Types
### [`ImportContent`](-import-content/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-import-content/index.html">ImportContent</a>
</span></code></pre></div>
</div>


<div markdown>

The imported reference, either as a resolved fully qualified name or as the raw reference expression.


</div>

</div>
## Properties
### aliasName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#aliasname">aliasName</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The alias assigned with `as`, or `null` if the import has no alias.


</div>

</div>
### importContent

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#importcontent">importContent</a><span class="o">: </span><a href="-import-content/index.html">KtImportInfo.ImportContent</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The imported reference, or `null` if it is missing in incomplete code.


</div>

</div>
### importedFqName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#importedfqname">importedFqName</a><span class="o">: </span>FqName<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The fully qualified name being imported, or `null` if it cannot be determined.


</div>

</div>
### importedName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">val </span><a href="index.html#importedname">importedName</a><span class="o">: </span>Name<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

The name under which the imported declaration becomes visible: the [`alias`](index.md#aliasname) if present, otherwise the short name of the imported reference. `null` for an all-under import or when the name cannot be determined.


</div>

</div>
### isAllUnder

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#isallunder">isAllUnder</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

`true` for an all-under import (`import foo.*`), which imports all members of the given scope.


</div>

</div>
