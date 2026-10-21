---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.utils.printer"
---

# org.jetbrains.kotlin.analysis.utils.printer
## Types
### [`PrettyPrinter`](-pretty-printer/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-pretty-printer/index.html">PrettyPrinter</a><span class="p">(</span><span class="kd">val </span>indentSize<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="o"> = </span><span class="nb">2</span><span class="p">)</span> : <a href="https://docs.oracle.com/javase/8/docs/api/java/lang/Appendable.html">Appendable</a>
</span></code></pre></div>
</div>

</div>
## Functions
### [`prettyPrint`](pretty-print.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="pretty-print.html"><span class="nf">prettyPrint</span></a><span class="p">(</span>body<span class="o">: </span><a href="-pretty-printer/index.html">PrettyPrinter</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`prettyPrintWithSettingsFrom`](pretty-print-with-settings-from.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="pretty-print-with-settings-from.html"><span class="nf">prettyPrintWithSettingsFrom</span></a><span class="p">(</span>other<span class="o">: </span><a href="-pretty-printer/index.html">PrettyPrinter</a><span class="p">, </span>body<span class="o">: </span><a href="-pretty-printer/index.html">PrettyPrinter</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
