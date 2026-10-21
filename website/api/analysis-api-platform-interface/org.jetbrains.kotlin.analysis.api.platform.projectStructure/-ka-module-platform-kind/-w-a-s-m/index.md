---
tags:
 - jvm
title: "WASM"
---

# WASM

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><a href="index.html">WASM</a>

</span></code></pre></div>Represents a Wasm module.

All component platforms of the underlying TargetPlatform are WasmPlatforms.

This module platform kind covers both Wasm targets (JS and Wasi). While it could be argued that WasmJs and WasmWasi are totally different platforms since they behave like different targets (e.g. different default imports and checkers), the current structure of WasmPlatform treats the Wasm target as a second-layer abstraction. The platform kind follows that and currently has this single value for Wasm regardless of the target.


</div>

## Properties
### [`name`](../../-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.md#name)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.html#name">name</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>

</div>
### [`ordinal`](../../-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.md#ordinal)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="../../-kotlin-compiler-plugins-provider/-compiler-plugin-type/-a-s-s-i-g-n-m-e-n-t/index.html#ordinal">ordinal</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>
</span></code></pre></div>
</div>

</div>
