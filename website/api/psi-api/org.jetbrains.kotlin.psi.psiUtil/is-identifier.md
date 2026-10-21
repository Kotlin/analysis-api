---
tags:
 - jvm
title: "isIdentifier"
---

# isIdentifier

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">?</span><span class="p">.</span><a href="is-identifier.html"><span class="nf">isIdentifier</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Checks if this string is a valid Kotlin identifier.

A regular identifier (without backticks) must:

 - Start with a letter (including Unicode letters) or underscore;


 - Contain only letters, digits, or underscores;


 - Not be a hard keyword.


Escaped identifiers (strings starting with a backtick) are also supported: the function returns `true` for strings such as `` `class` `` or `` `with spaces` ``.

The function performs only basic, platform-agnostic validation. Individual build targets may impose additional restrictions; for example, the JVM target also applies Java bytecode and Dalvik restrictions. See `org.jetbrains.kotlin.resolve.jvm.checkers.DalvikIdentifierUtils.isValidDalvikCharacter`.

#### See also


 - [`quoteIfNeeded`](quote-if-needed.md)



</div>

</div>
