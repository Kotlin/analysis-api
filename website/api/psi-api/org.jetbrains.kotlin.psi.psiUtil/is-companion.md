---
tags:
 - jvm
title: "isCompanion"
---

# isCompanion

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../org.jetbrains.kotlin.psi/-kt-declaration-with-return-type/index.html">KtDeclarationWithReturnType</a><span class="p">.</span><a href="is-companion.html">isCompanion</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the callable is a [companion extension](https://github.com/Kotlin/KEEP/blob/main/proposals/KEEP-0449-companions-block-extension.md#companion-extensions) or comes from a [companion block](https://github.com/Kotlin/KEEP/blob/main/proposals/KEEP-0449-companions-block-extension.md#companion-blocks).

<strong>Note:</strong> according to the KEEP, [`KtEnumEntry`](../org.jetbrains.kotlin.psi/-kt-enum-entry/index.md)s are also considered implicitly declared in a companion block.


</div>

</div>
